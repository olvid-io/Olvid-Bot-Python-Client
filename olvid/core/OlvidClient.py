from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from olvid.listeners.GenericNotificationListener import GenericNotificationListener
	from typing import Optional, Coroutine, AsyncIterator

	# for compatibility with python 3.10
	from typing import TypeVar
	# noinspection PyTypeHints
	Self = TypeVar("OlvidClient")

import grpc
import asyncio
import signal
import os
from asyncio import Task

from .logger import core_logger, command_logger, notification_logger
from ..internal import commands, notifications
from .. import datatypes
from ..listeners.ClientListenerHolder import ClientListenerHolder
from ..listeners.Command import Command
from .StubHolder import StubHolder


# noinspection PyProtectedMember,PyShadowingBuiltins
class OlvidClient:
	"""
	OlvidClient: basic class to interact with Olvid daemon.

	OlvidClient needs a client key to authenticate on daemon, you can pass it using:
	- by setting OLVID_CLIENT_KEY env variable
	- by writing it in a .client_key file
	- by passing it as a client_key constructor parameter (to avoid)

	By default, client connects to "localhost:50051" you can change this behavior:
	- set DAEMON_HOSTNAME and/or DAEMON_PORT env variable
	- use server_target parameter. It must be the full server address including hostname/ip and port

	OlvidClient implements every gRPC command methods defined in daemon API.
	You can find methods using the same name as in gRPC but using snake case.
	Request and Response encapsulation layer is fully invisible, you won't need to use Request and Response messages.
	For example for message_send method you can use:
	`client.message_send(discussion_id, body)` and it will return a `datatypes.Message` item.
	you don't use MessageSendRequest and MessageSendResponse.

	OlvidClient also implements a listener mechanism to listen to notification implemented in grpc Notification services.
	Use this code to add a listener to message_received notification:
	`client.add_listener(listeners.MessageReceivedListener(handler=lambda message: print(message)))`
	Again you won't need to use encapsulation messages SubscribeToMessageSendNotification and MessageReceivedNotification.
	"""
	_CHUNK_LENGTH = 1_000_000

	_KEY_ENV_VARIABLE_NAME: str = "OLVID_CLIENT_KEY"
	_KEY_FILE_PATH: str = ".client_key"

	_HOSTNAME_DEFAULT_VALUE: str = "localhost"
	_HOSTNAME_ENV_VARIABLE_NAME: str = "DAEMON_HOSTNAME"

	_PORT_DEFAULT_VALUE: str = "50051"
	_PORT_ENV_VARIABLE_NAME: str = "DAEMON_PORT"

	# we store running clients to notify them if we receive a stop signal
	_running_clients: list[Self] = []

	def __init__(self, client_key: Optional[str] = None, server_target: Optional[str] = None, parent_client: Optional[Self] = None):
		self._stopped = False

		# determine the client key to use (argument > parent > env > file)
		if client_key:
			self._client_key: str = client_key
		elif parent_client:
			self._client_key = parent_client.client_key
		elif os.environ.get(self._KEY_ENV_VARIABLE_NAME):
			self._client_key = os.environ.get(self._KEY_ENV_VARIABLE_NAME).strip()
		elif os.path.isfile(self._KEY_FILE_PATH):
			self._client_key = open(self._KEY_FILE_PATH).read().strip()
		else:
			raise ValueError("Client key not found")

		# determine target (argument > parent > env > default)
		if server_target:
			self._server_target = server_target
		elif parent_client:
			self._server_target = parent_client.server_target
		else:
			self._hostname = os.environ.get(self._HOSTNAME_ENV_VARIABLE_NAME).strip() if os.environ.get(self._HOSTNAME_ENV_VARIABLE_NAME) else self._HOSTNAME_DEFAULT_VALUE
			self._port = os.environ.get(self._PORT_ENV_VARIABLE_NAME).strip() if os.environ.get(self._PORT_ENV_VARIABLE_NAME) else self._PORT_DEFAULT_VALUE
			self._server_target = f"{self._hostname}:{self._port}"

		# store parent client
		self._parent_client: Optional[Self] = parent_client

		# children client case
		if self._parent_client is not None:
			# check parent is running
			if self._parent_client and self._parent_client._stopped:
				raise RuntimeError(f"{self.__class__.__name__}: parent client have been stopped")
			# register as parent's children
			self._parent_client._register_child(self)
			# re-use parent channel
			self._channel: grpc.Channel = self._parent_client._channel
		else:
			self._channel: grpc.Channel = grpc.aio.insecure_channel(target=self._server_target)
		self._registered_child: Optional[list[Self]] = []

		# create or re-use grpc stubs
		self._stubs = StubHolder(client=self, channel=self._channel, parent=self._parent_client)

		# every client keep a list of own registered listeners because listener holder might contain other listeners from parent / son clients
		self._listeners_set: set[GenericNotificationListener] = set()
		# initialize listener holder: warning: this will set up an asyncio loop and cause issues with asyncio.run method that will create its own event loop
		self._listener_holder = ClientListenerHolder(self) if self._parent_client is None else self._parent_client._listener_holder

		# keep a set with pending tasks to keep a strong reference on it (each task might remove itself from the task set when finished)
		self.__task_set = set()

		# register this client to stop it if a SIGTERM signal is received (signal sent when you docker container stops)
		if len(self._running_clients) == 0:
			# if this is the first running client, register the signal handler
			for s in (signal.SIGTERM, ):
				asyncio.get_event_loop().add_signal_handler(s, self.__stop_signal_handler)
		self._running_clients.append(self)

	async def stop(self):
		if self._stopped:
			core_logger.warning(f"{self.__class__.__name__}: trying to stop a stopped instance")
			return

		# stop children
		for child in self._registered_child:
			if not child._stopped:
				await child.stop()

		# remove listeners from holder
		self.remove_all_listeners()

		# if no parent close channels and stop listener_holder
		if self._parent_client is None:
			if self._listener_holder:
				await self._listener_holder.stop()
			if self._channel:
				await self._channel.close()

		self._listener_holder = None

		self._running_clients.remove(self)

		self._stopped = True

		core_logger.debug(f"{self.__class__.__name__}: stopped")

	def _register_child(self, child_client: OlvidClient):
		self._registered_child.append(child_client)

	def are_listeners_finished(self) -> bool:
		self._listeners_set = set([listener for listener in self._listeners_set if not listener.is_finished])
		return len(self._listeners_set) == 0

	async def wait_for_listeners_end(self):
		# if bot was stopped or is not running, there is nothing to wait
		if self._stopped:
			return
		# wait for listeners' end
		while not self.are_listeners_finished():
			await self._listener_holder.wait_for_listener_removed_event()

	#####
	# read only properties
	#####
	@property
	def client_key(self) -> str:
		return self._client_key

	@property
	def server_target(self) -> str:
		return self._server_target

	@staticmethod
	def __stop_signal_handler():
		core_logger.info("Received a stop signal, stopping every running clients")
		for client in OlvidClient._running_clients:
			client.add_background_task(client.stop(), f"force-stop-client")

	#####
	# Background tasks api
	#####
	# this api keeps a reference on created task for you (necessary when running an async task)
	def add_background_task(self, coroutine: Coroutine, name: str = "") -> Task:
		task = asyncio.get_event_loop().create_task(coroutine, name=name if name else None)
		self.__task_set.add(task)

		def end_callback(t):
			self.__task_set.remove(t)
		task.add_done_callback(end_callback)
		return task

	#####
	# Listeners api
	####
	def add_listener(self, listener: GenericNotificationListener):
		if self._stopped:
			raise RuntimeError("Cannot add a listener to a stopped instance")

		if listener not in self._listeners_set:
			self._listeners_set.add(listener)
		self._listener_holder.add_listener(listener)

		# log
		if isinstance(listener, Command):
			core_logger.debug(f"{self.__class__.__name__}: command added: {listener}")
		else:
			core_logger.debug(f"{self.__class__.__name__}: listener added: {listener}")

	def remove_listener(self, listener: GenericNotificationListener):
		if self._stopped:
			core_logger.warning(f"{self.__class__.__name__}: removing a listener on a stopped instance")

		self._listeners_set.discard(listener)
		self._listener_holder.remove_listener(listener)

		# log
		if isinstance(listener, Command):
			core_logger.debug(f"{self.__class__.__name__}: command removed: {listener}")
		else:
			core_logger.debug(f"{self.__class__.__name__}: listener removed: {listener}")

	def remove_all_listeners(self):
		if self._stopped:
			core_logger.warning(f"{self.__class__.__name__}: removing listeners on a stopped instance")

		listeners_copy = self._listeners_set.copy()
		for listener in listeners_copy:
			self._listener_holder.remove_listener(listener)

		# log
		core_logger.debug(f"{self.__class__.__name__}: removed all listeners")

	#####
	# GrpcMetadata property
	####
	@property
	def grpc_metadata(self) -> list[tuple[str, str]]:
		return [("daemon-client-key", self._client_key)]

	#####
	# other method: manually implemented
	#####
	def attachment_message_list(self, message_id: datatypes.MessageId) -> AsyncIterator[datatypes.Attachment]:
		command_logger.info(f'{self.__class__.__name__}: command: AttachmentMessageList')

		async def iterator(message_iterator: AsyncIterator[commands.AttachmentListResponse]) -> AsyncIterator[
			datatypes.Attachment]:
			async for message in message_iterator:
				for element in message.attachments:
					yield element

		return iterator(self._stubs.attachmentCommandStub.attachment_list(
			commands.AttachmentListRequest(client=self, filter=datatypes.AttachmentFilter(message_id=message_id))))

	#####
	# request stream api (manually implemented)
	#####

	# IdentityCommandService
	async def identity_set_photo(self, file_path: str) -> commands.IdentitySetPhotoResponse:
		if not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
			raise IOError(f"Cannot open: {file_path}")

		async def identity_set_photo_iterator() -> AsyncIterator:
			with open(file_path, "rb") as fd:
				yield commands.IdentitySetPhotoRequest(
					metadata=commands.IdentitySetPhotoRequestMetadata(filename=os.path.basename(file_path),
																file_size=os.path.getsize(file_path)))
				buffer = fd.read(OlvidClient._CHUNK_LENGTH)
				while len(buffer) > 0:
					yield commands.IdentitySetPhotoRequest(payload=buffer)
					buffer = fd.read(OlvidClient._CHUNK_LENGTH)
		command_logger.info(f'{self.__class__.__name__}: command: IdentitySetPhoto')
		return await self._stubs.identityCommandStub.identity_set_photo(identity_set_photo_iterator())

	# GroupCommandService
	async def group_set_photo(self, group_id: int, file_path: str) -> datatypes.Group:
		async def group_set_photo_iterator() -> AsyncIterator:
			fd = open(file_path, "rb")
			yield commands.GroupSetPhotoRequest(
				metadata=commands.GroupSetPhotoRequestMetadata(group_id=group_id, filename=os.path.basename(file_path),
															file_size=os.path.getsize(file_path)))
			buffer = fd.read(OlvidClient._CHUNK_LENGTH)
			while len(buffer) > 0:
				yield commands.GroupSetPhotoRequest(payload=buffer)
				buffer = fd.read(OlvidClient._CHUNK_LENGTH)
			fd.close()
		command_logger.info(f'{self.__class__.__name__}: command: GroupSetPhoto')
		return (await self._stubs.groupCommandStub.group_set_photo(group_set_photo_iterator())).group

	# MessageCommandService
	async def message_send_with_attachments_files(self, discussion_id: int, file_paths: list[str], body: str = "", reply_id: datatypes.MessageId = None, ephemerality: datatypes.MessageEphemerality = None, disable_link_preview: bool = False) -> tuple[datatypes.Message, list[datatypes.Attachment]]:
		async def message_send_with_attachments_files_generator():
			# send metadata
			files: list[commands.MessageSendWithAttachmentsRequestMetadata.File] = [commands.MessageSendWithAttachmentsRequestMetadata.File(filename=os.path.basename(file_path), file_size=os.path.getsize(file_path)) for file_path in file_paths]
			m = commands.MessageSendWithAttachmentsRequest(metadata=commands.MessageSendWithAttachmentsRequestMetadata(
				body=body if body else "",
				reply_id=reply_id,
				discussion_id=discussion_id,
				ephemerality=ephemerality,
				files=files,
				disable_link_preview=disable_link_preview
			))
			yield m
			# send files content
			for file_path in file_paths:
				with open(file_path, "rb") as fd:
					buffer = fd.read(OlvidClient._CHUNK_LENGTH)
					while len(buffer) > 0:
						yield commands.MessageSendWithAttachmentsRequest(payload=buffer)
						buffer = fd.read(OlvidClient._CHUNK_LENGTH)
				# send file delimiter
				yield commands.MessageSendWithAttachmentsRequest(file_delimiter=True)
		command_logger.info(f'{self.__class__.__name__}: command: MessageSendWithAttachmentsFiles')
		response = await self._stubs.messageCommandStub.message_send_with_attachments(message_send_with_attachments_request_iterator=message_send_with_attachments_files_generator())
		return response.message, response.attachments

	async def message_send_with_attachments(self, discussion_id: int, attachments_filename_with_payload: list[tuple[str, bytes]], body: str = "", reply_id: datatypes.MessageId = None, ephemerality: datatypes.MessageEphemerality = None, disable_link_preview: bool = False) -> tuple[datatypes.Message, list[datatypes.Attachment]]:
		async def message_send_with_attachments_generator():
			# send metadata
			files: list[commands.MessageSendWithAttachmentsRequestMetadata.File] = [commands.MessageSendWithAttachmentsRequestMetadata.File(filename=filename, file_size=len(file_content)) for filename, file_content in attachments_filename_with_payload]
			m = commands.MessageSendWithAttachmentsRequest(metadata=commands.MessageSendWithAttachmentsRequestMetadata(
				body=body if body else "",
				reply_id=reply_id,
				discussion_id=discussion_id,
				ephemerality=ephemerality,
				files=files,
				disable_link_preview=disable_link_preview
			))
			yield m
			# send files content
			for filename, file_content in attachments_filename_with_payload:
				while len(file_content) > 0:
					yield commands.MessageSendWithAttachmentsRequest(payload=file_content[0:self._CHUNK_LENGTH])
					file_content = file_content[self._CHUNK_LENGTH:]
				# send file delimiter
				yield commands.MessageSendWithAttachmentsRequest(file_delimiter=True)
		command_logger.info(f'{self.__class__.__name__}: command: MessageSendWithAttachments')
		response = await self._stubs.messageCommandStub.message_send_with_attachments(message_send_with_attachments_request_iterator=message_send_with_attachments_generator())
		return response.message, response.attachments

	# response stream and non stream api, generated code
	####################################################################################################################
	##### WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_olvid_client_code.py
	####################################################################################################################
	# IdentityCommandService
	async def identity_get(self) -> datatypes.Identity:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityGet')
		response: commands.IdentityGetResponse = await self._stubs.identityCommandStub.identity_get(commands.IdentityGetRequest(client=self))
		return response.identity
	
	async def identity_update_details(self, new_details: datatypes.IdentityDetails) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityUpdateDetails')
		await self._stubs.identityCommandStub.identity_update_details(commands.IdentityUpdateDetailsRequest(client=self, new_details=new_details))
	
	async def identity_remove_photo(self) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityRemovePhoto')
		await self._stubs.identityCommandStub.identity_remove_photo(commands.IdentityRemovePhotoRequest(client=self))
	
	# identity_set_photo: cannot generate request stream rpc code
	
	async def identity_keycloak_bind(self, configuration_link: str) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityKeycloakBind')
		await self._stubs.identityCommandStub.identity_keycloak_bind(commands.IdentityKeycloakBindRequest(client=self, configuration_link=configuration_link))
	
	async def identity_keycloak_unbind(self) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityKeycloakUnbind')
		await self._stubs.identityCommandStub.identity_keycloak_unbind(commands.IdentityKeycloakUnbindRequest(client=self))
	
	async def identity_set_api_key(self, api_key: str) -> datatypes.Identity.ApiKey:
		command_logger.info(f'{self.__class__.__name__}: command: IdentitySetApiKey')
		response: commands.IdentitySetApiKeyResponse = await self._stubs.identityCommandStub.identity_set_api_key(commands.IdentitySetApiKeyRequest(client=self, api_key=api_key))
		return response.api_key
	
	async def identity_set_configuration_link(self, configuration_link: str) -> datatypes.Identity.ApiKey:
		command_logger.info(f'{self.__class__.__name__}: command: IdentitySetConfigurationLink')
		response: commands.IdentitySetConfigurationLinkResponse = await self._stubs.identityCommandStub.identity_set_configuration_link(commands.IdentitySetConfigurationLinkRequest(client=self, configuration_link=configuration_link))
		return response.api_key
	
	# InvitationCommandService
	def invitation_list(self, filter: datatypes.InvitationFilter = None) -> AsyncIterator[datatypes.Invitation]:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationList')
	
		async def iterator(message_iterator: AsyncIterator[commands.InvitationListResponse]) -> AsyncIterator[datatypes.Invitation]:
			async for message in message_iterator:
				for element in message.invitations:
					yield element
		return iterator(self._stubs.invitationCommandStub.invitation_list(commands.InvitationListRequest(client=self, filter=filter)))
	
	async def invitation_get(self, invitation_id: int) -> datatypes.Invitation:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationGet')
		response: commands.InvitationGetResponse = await self._stubs.invitationCommandStub.invitation_get(commands.InvitationGetRequest(client=self, invitation_id=invitation_id))
		return response.invitation
	
	async def invitation_new(self, invitation_url: str) -> datatypes.Invitation:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationNew')
		response: commands.InvitationNewResponse = await self._stubs.invitationCommandStub.invitation_new(commands.InvitationNewRequest(client=self, invitation_url=invitation_url))
		return response.invitation
	
	async def invitation_accept(self, invitation_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationAccept')
		await self._stubs.invitationCommandStub.invitation_accept(commands.InvitationAcceptRequest(client=self, invitation_id=invitation_id))
	
	async def invitation_decline(self, invitation_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationDecline')
		await self._stubs.invitationCommandStub.invitation_decline(commands.InvitationDeclineRequest(client=self, invitation_id=invitation_id))
	
	async def invitation_sas(self, invitation_id: int, sas: str) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationSas')
		await self._stubs.invitationCommandStub.invitation_sas(commands.InvitationSasRequest(client=self, invitation_id=invitation_id, sas=sas))
	
	async def invitation_delete(self, invitation_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationDelete')
		await self._stubs.invitationCommandStub.invitation_delete(commands.InvitationDeleteRequest(client=self, invitation_id=invitation_id))
	
	# ContactCommandService
	def contact_list(self, filter: datatypes.ContactFilter = None) -> AsyncIterator[datatypes.Contact]:
		command_logger.info(f'{self.__class__.__name__}: command: ContactList')
	
		async def iterator(message_iterator: AsyncIterator[commands.ContactListResponse]) -> AsyncIterator[datatypes.Contact]:
			async for message in message_iterator:
				for element in message.contacts:
					yield element
		return iterator(self._stubs.contactCommandStub.contact_list(commands.ContactListRequest(client=self, filter=filter)))
	
	async def contact_get(self, contact_id: int) -> datatypes.Contact:
		command_logger.info(f'{self.__class__.__name__}: command: ContactGet')
		response: commands.ContactGetResponse = await self._stubs.contactCommandStub.contact_get(commands.ContactGetRequest(client=self, contact_id=contact_id))
		return response.contact
	
	async def contact_delete(self, contact_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: ContactDelete')
		await self._stubs.contactCommandStub.contact_delete(commands.ContactDeleteRequest(client=self, contact_id=contact_id))
	
	async def contact_introduction(self, first_contact_id: int, second_contact_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: ContactIntroduction')
		await self._stubs.contactCommandStub.contact_introduction(commands.ContactIntroductionRequest(client=self, first_contact_id=first_contact_id, second_contact_id=second_contact_id))
	
	async def contact_invite_to_one_to_one_discussion(self, contact_id: int) -> datatypes.Invitation:
		command_logger.info(f'{self.__class__.__name__}: command: ContactInviteToOneToOneDiscussion')
		response: commands.ContactInviteToOneToOneDiscussionResponse = await self._stubs.contactCommandStub.contact_invite_to_one_to_one_discussion(commands.ContactInviteToOneToOneDiscussionRequest(client=self, contact_id=contact_id))
		return response.invitation
	
	async def contact_downgrade_one_to_one_discussion(self, contact_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: ContactDowngradeOneToOneDiscussion')
		await self._stubs.contactCommandStub.contact_downgrade_one_to_one_discussion(commands.ContactDowngradeOneToOneDiscussionRequest(client=self, contact_id=contact_id))
	
	# GroupCommandService
	def group_list(self, filter: datatypes.GroupFilter = None) -> AsyncIterator[datatypes.Group]:
		command_logger.info(f'{self.__class__.__name__}: command: GroupList')
	
		async def iterator(message_iterator: AsyncIterator[commands.GroupListResponse]) -> AsyncIterator[datatypes.Group]:
			async for message in message_iterator:
				for element in message.groups:
					yield element
		return iterator(self._stubs.groupCommandStub.group_list(commands.GroupListRequest(client=self, filter=filter)))
	
	async def group_get(self, group_id: int) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupGet')
		response: commands.GroupGetResponse = await self._stubs.groupCommandStub.group_get(commands.GroupGetRequest(client=self, group_id=group_id))
		return response.group
	
	async def group_new_standard_group(self, name: str = "", description: str = "", admin_contact_ids: list[int] = ()) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupNewStandardGroup')
		response: commands.GroupNewStandardGroupResponse = await self._stubs.groupCommandStub.group_new_standard_group(commands.GroupNewStandardGroupRequest(client=self, name=name, description=description, admin_contact_ids=admin_contact_ids))
		return response.group
	
	async def group_new_controlled_group(self, name: str = "", description: str = "", admin_contact_ids: list[int] = (), contact_ids: list[int] = ()) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupNewControlledGroup')
		response: commands.GroupNewControlledGroupResponse = await self._stubs.groupCommandStub.group_new_controlled_group(commands.GroupNewControlledGroupRequest(client=self, name=name, description=description, admin_contact_ids=admin_contact_ids, contact_ids=contact_ids))
		return response.group
	
	async def group_new_read_only_group(self, name: str = "", description: str = "", admin_contact_ids: list[int] = (), contact_ids: list[int] = ()) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupNewReadOnlyGroup')
		response: commands.GroupNewReadOnlyGroupResponse = await self._stubs.groupCommandStub.group_new_read_only_group(commands.GroupNewReadOnlyGroupRequest(client=self, name=name, description=description, admin_contact_ids=admin_contact_ids, contact_ids=contact_ids))
		return response.group
	
	async def group_new_advanced_group(self, name: str = "", description: str = "", advanced_configuration: datatypes.Group.AdvancedConfiguration = None, members: list[datatypes.GroupMember] = None) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupNewAdvancedGroup')
		response: commands.GroupNewAdvancedGroupResponse = await self._stubs.groupCommandStub.group_new_advanced_group(commands.GroupNewAdvancedGroupRequest(client=self, name=name, description=description, advanced_configuration=advanced_configuration, members=members))
		return response.group
	
	async def group_disband(self, group_id: int) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupDisband')
		response: commands.GroupDisbandResponse = await self._stubs.groupCommandStub.group_disband(commands.GroupDisbandRequest(client=self, group_id=group_id))
		return response.group
	
	async def group_leave(self, group_id: int) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupLeave')
		response: commands.GroupLeaveResponse = await self._stubs.groupCommandStub.group_leave(commands.GroupLeaveRequest(client=self, group_id=group_id))
		return response.group
	
	async def group_update(self, group: datatypes.Group) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupUpdate')
		response: commands.GroupUpdateResponse = await self._stubs.groupCommandStub.group_update(commands.GroupUpdateRequest(client=self, group=group))
		return response.group
	
	async def group_unset_photo(self, group_id: int) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupUnsetPhoto')
		response: commands.GroupUnsetPhotoResponse = await self._stubs.groupCommandStub.group_unset_photo(commands.GroupUnsetPhotoRequest(client=self, group_id=group_id))
		return response.group
	
	# group_set_photo: cannot generate request stream rpc code
	
	# DiscussionCommandService
	def discussion_list(self, filter: datatypes.DiscussionFilter = None) -> AsyncIterator[datatypes.Discussion]:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionList')
	
		async def iterator(message_iterator: AsyncIterator[commands.DiscussionListResponse]) -> AsyncIterator[datatypes.Discussion]:
			async for message in message_iterator:
				for element in message.discussions:
					yield element
		return iterator(self._stubs.discussionCommandStub.discussion_list(commands.DiscussionListRequest(client=self, filter=filter)))
	
	async def discussion_get(self, discussion_id: int) -> datatypes.Discussion:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionGet')
		response: commands.DiscussionGetResponse = await self._stubs.discussionCommandStub.discussion_get(commands.DiscussionGetRequest(client=self, discussion_id=discussion_id))
		return response.discussion
	
	async def discussion_get_by_contact(self, contact_id: int) -> datatypes.Discussion:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionGetByContact')
		response: commands.DiscussionGetByContactResponse = await self._stubs.discussionCommandStub.discussion_get_by_contact(commands.DiscussionGetByContactRequest(client=self, contact_id=contact_id))
		return response.discussion
	
	async def discussion_get_by_group(self, group_id: int) -> datatypes.Discussion:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionGetByGroup')
		response: commands.DiscussionGetByGroupResponse = await self._stubs.discussionCommandStub.discussion_get_by_group(commands.DiscussionGetByGroupRequest(client=self, group_id=group_id))
		return response.discussion
	
	async def discussion_empty(self, discussion_id: int, delete_everywhere: bool = False) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionEmpty')
		await self._stubs.discussionCommandStub.discussion_empty(commands.DiscussionEmptyRequest(client=self, discussion_id=discussion_id, delete_everywhere=delete_everywhere))
	
	async def discussion_settings_get(self, discussion_id: int) -> datatypes.DiscussionSettings:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionSettingsGet')
		response: commands.DiscussionSettingsGetResponse = await self._stubs.discussionCommandStub.discussion_settings_get(commands.DiscussionSettingsGetRequest(client=self, discussion_id=discussion_id))
		return response.settings
	
	async def discussion_settings_set(self, settings: datatypes.DiscussionSettings) -> datatypes.DiscussionSettings:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionSettingsSet')
		response: commands.DiscussionSettingsSetResponse = await self._stubs.discussionCommandStub.discussion_settings_set(commands.DiscussionSettingsSetRequest(client=self, settings=settings))
		return response.new_settings
	
	def discussion_locked_list(self) -> AsyncIterator[datatypes.Discussion]:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionLockedList')
	
		async def iterator(message_iterator: AsyncIterator[commands.DiscussionLockedListResponse]) -> AsyncIterator[datatypes.Discussion]:
			async for message in message_iterator:
				for element in message.discussions:
					yield element
		return iterator(self._stubs.discussionCommandStub.discussion_locked_list(commands.DiscussionLockedListRequest(client=self)))
	
	async def discussion_locked_delete(self, discussion_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionLockedDelete')
		await self._stubs.discussionCommandStub.discussion_locked_delete(commands.DiscussionLockedDeleteRequest(client=self, discussion_id=discussion_id))
	
	# MessageCommandService
	def message_list(self, filter: datatypes.MessageFilter = None, unread: bool = False) -> AsyncIterator[datatypes.Message]:
		command_logger.info(f'{self.__class__.__name__}: command: MessageList')
	
		async def iterator(message_iterator: AsyncIterator[commands.MessageListResponse]) -> AsyncIterator[datatypes.Message]:
			async for message in message_iterator:
				for element in message.messages:
					yield element
		return iterator(self._stubs.messageCommandStub.message_list(commands.MessageListRequest(client=self, filter=filter, unread=unread)))
	
	async def message_get(self, message_id: datatypes.MessageId) -> datatypes.Message:
		command_logger.info(f'{self.__class__.__name__}: command: MessageGet')
		response: commands.MessageGetResponse = await self._stubs.messageCommandStub.message_get(commands.MessageGetRequest(client=self, message_id=message_id))
		return response.message
	
	async def message_refresh(self) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: MessageRefresh')
		await self._stubs.messageCommandStub.message_refresh(commands.MessageRefreshRequest(client=self))
	
	async def message_delete(self, message_id: datatypes.MessageId, delete_everywhere: bool = False) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: MessageDelete')
		await self._stubs.messageCommandStub.message_delete(commands.MessageDeleteRequest(client=self, message_id=message_id, delete_everywhere=delete_everywhere))
	
	async def message_send(self, discussion_id: int, body: str, reply_id: datatypes.MessageId = None, ephemerality: datatypes.MessageEphemerality = None, disable_link_preview: bool = False) -> datatypes.Message:
		command_logger.info(f'{self.__class__.__name__}: command: MessageSend')
		response: commands.MessageSendResponse = await self._stubs.messageCommandStub.message_send(commands.MessageSendRequest(client=self, discussion_id=discussion_id, body=body, reply_id=reply_id, ephemerality=ephemerality, disable_link_preview=disable_link_preview))
		return response.message
	
	# message_send_with_attachments: cannot generate request stream rpc code
	
	async def message_react(self, message_id: datatypes.MessageId, reaction: str) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: MessageReact')
		await self._stubs.messageCommandStub.message_react(commands.MessageReactRequest(client=self, message_id=message_id, reaction=reaction))
	
	async def message_update_body(self, message_id: datatypes.MessageId, updated_body: str) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: MessageUpdateBody')
		await self._stubs.messageCommandStub.message_update_body(commands.MessageUpdateBodyRequest(client=self, message_id=message_id, updated_body=updated_body))
	
	async def message_send_voip(self, discussion_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: MessageSendVoip')
		await self._stubs.messageCommandStub.message_send_voip(commands.MessageSendVoipRequest(client=self, discussion_id=discussion_id))
	
	# AttachmentCommandService
	def attachment_list(self, filter: datatypes.AttachmentFilter = None) -> AsyncIterator[datatypes.Attachment]:
		command_logger.info(f'{self.__class__.__name__}: command: AttachmentList')
	
		async def iterator(message_iterator: AsyncIterator[commands.AttachmentListResponse]) -> AsyncIterator[datatypes.Attachment]:
			async for message in message_iterator:
				for element in message.attachments:
					yield element
		return iterator(self._stubs.attachmentCommandStub.attachment_list(commands.AttachmentListRequest(client=self, filter=filter)))
	
	async def attachment_get(self, attachment_id: datatypes.AttachmentId) -> datatypes.Attachment:
		command_logger.info(f'{self.__class__.__name__}: command: AttachmentGet')
		response: commands.AttachmentGetResponse = await self._stubs.attachmentCommandStub.attachment_get(commands.AttachmentGetRequest(client=self, attachment_id=attachment_id))
		return response.attachment
	
	async def attachment_delete(self, attachment_id: datatypes.AttachmentId, delete_everywhere: bool = False) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: AttachmentDelete')
		await self._stubs.attachmentCommandStub.attachment_delete(commands.AttachmentDeleteRequest(client=self, attachment_id=attachment_id, delete_everywhere=delete_everywhere))
	
	def attachment_download(self, attachment_id: datatypes.AttachmentId) -> AsyncIterator[bytes]:
		command_logger.info(f'{self.__class__.__name__}: command: AttachmentDownload')
	
		async def iterator(message_iterator: AsyncIterator[commands.AttachmentDownloadResponse]) -> AsyncIterator[bytes]:
			async for message in message_iterator:
				yield message.chunk
		return iterator(self._stubs.attachmentCommandStub.attachment_download(commands.AttachmentDownloadRequest(client=self, attachment_id=attachment_id)))
	
	# StorageCommandService
	def storage_list(self, filter: datatypes.StorageElementFilter = None) -> AsyncIterator[datatypes.StorageElement]:
		command_logger.info(f'{self.__class__.__name__}: command: StorageList')
	
		async def iterator(message_iterator: AsyncIterator[commands.StorageListResponse]) -> AsyncIterator[datatypes.StorageElement]:
			async for message in message_iterator:
				for element in message.elements:
					yield element
		return iterator(self._stubs.storageCommandStub.storage_list(commands.StorageListRequest(client=self, filter=filter)))
	
	async def storage_get(self, key: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: StorageGet')
		response: commands.StorageGetResponse = await self._stubs.storageCommandStub.storage_get(commands.StorageGetRequest(client=self, key=key))
		return response.value
	
	async def storage_set(self, key: str, value: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: StorageSet')
		response: commands.StorageSetResponse = await self._stubs.storageCommandStub.storage_set(commands.StorageSetRequest(client=self, key=key, value=value))
		return response.previous_value
	
	async def storage_unset(self, key: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: StorageUnset')
		response: commands.StorageUnsetResponse = await self._stubs.storageCommandStub.storage_unset(commands.StorageUnsetRequest(client=self, key=key))
		return response.previous_value
	
	# DiscussionStorageCommandService
	def discussion_storage_list(self, discussion_id: int, filter: datatypes.StorageElementFilter = None) -> AsyncIterator[datatypes.StorageElement]:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionStorageList')
	
		async def iterator(message_iterator: AsyncIterator[commands.DiscussionStorageListResponse]) -> AsyncIterator[datatypes.StorageElement]:
			async for message in message_iterator:
				for element in message.elements:
					yield element
		return iterator(self._stubs.discussionStorageCommandStub.discussion_storage_list(commands.DiscussionStorageListRequest(client=self, discussion_id=discussion_id, filter=filter)))
	
	async def discussion_storage_get(self, discussion_id: int, key: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionStorageGet')
		response: commands.DiscussionStorageGetResponse = await self._stubs.discussionStorageCommandStub.discussion_storage_get(commands.DiscussionStorageGetRequest(client=self, discussion_id=discussion_id, key=key))
		return response.value
	
	async def discussion_storage_set(self, discussion_id: int, key: str, value: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionStorageSet')
		response: commands.DiscussionStorageSetResponse = await self._stubs.discussionStorageCommandStub.discussion_storage_set(commands.DiscussionStorageSetRequest(client=self, discussion_id=discussion_id, key=key, value=value))
		return response.previous_value
	
	async def discussion_storage_unset(self, discussion_id: int, key: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionStorageUnset')
		response: commands.DiscussionStorageUnsetResponse = await self._stubs.discussionStorageCommandStub.discussion_storage_unset(commands.DiscussionStorageUnsetRequest(client=self, discussion_id=discussion_id, key=key))
		return response.previous_value
	
	# InvitationNotificationService
	def _notif_invitation_received(self) -> AsyncIterator[notifications.InvitationReceivedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: InvitationReceived')
		return self._stubs.invitationNotificationStub.invitation_received(notifications.SubscribeToInvitationReceivedNotification(client=self))
	
	def _notif_invitation_sent(self) -> AsyncIterator[notifications.InvitationSentNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: InvitationSent')
		return self._stubs.invitationNotificationStub.invitation_sent(notifications.SubscribeToInvitationSentNotification(client=self))
	
	def _notif_invitation_deleted(self) -> AsyncIterator[notifications.InvitationDeletedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: InvitationDeleted')
		return self._stubs.invitationNotificationStub.invitation_deleted(notifications.SubscribeToInvitationDeletedNotification(client=self))
	
	def _notif_invitation_updated(self) -> AsyncIterator[notifications.InvitationUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: InvitationUpdated')
		return self._stubs.invitationNotificationStub.invitation_updated(notifications.SubscribeToInvitationUpdatedNotification(client=self))
	
	# ContactNotificationService
	def _notif_contact_new(self) -> AsyncIterator[notifications.ContactNewNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: ContactNew')
		return self._stubs.contactNotificationStub.contact_new(notifications.SubscribeToContactNewNotification(client=self))
	
	def _notif_contact_deleted(self) -> AsyncIterator[notifications.ContactDeletedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: ContactDeleted')
		return self._stubs.contactNotificationStub.contact_deleted(notifications.SubscribeToContactDeletedNotification(client=self))
	
	def _notif_contact_details_updated(self) -> AsyncIterator[notifications.ContactDetailsUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: ContactDetailsUpdated')
		return self._stubs.contactNotificationStub.contact_details_updated(notifications.SubscribeToContactDetailsUpdatedNotification(client=self))
	
	# GroupNotificationService
	def _notif_group_new(self) -> AsyncIterator[notifications.GroupNewNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupNew')
		return self._stubs.groupNotificationStub.group_new(notifications.SubscribeToGroupNewNotification(client=self))
	
	def _notif_group_deleted(self) -> AsyncIterator[notifications.GroupDeletedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupDeleted')
		return self._stubs.groupNotificationStub.group_deleted(notifications.SubscribeToGroupDeletedNotification(client=self))
	
	def _notif_group_name_updated(self) -> AsyncIterator[notifications.GroupNameUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupNameUpdated')
		return self._stubs.groupNotificationStub.group_name_updated(notifications.SubscribeToGroupNameUpdatedNotification(client=self))
	
	def _notif_group_description_updated(self) -> AsyncIterator[notifications.GroupDescriptionUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupDescriptionUpdated')
		return self._stubs.groupNotificationStub.group_description_updated(notifications.SubscribeToGroupDescriptionUpdatedNotification(client=self))
	
	def _notif_group_pending_member_added(self) -> AsyncIterator[notifications.GroupPendingMemberAddedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupPendingMemberAdded')
		return self._stubs.groupNotificationStub.group_pending_member_added(notifications.SubscribeToGroupPendingMemberAddedNotification(client=self))
	
	def _notif_group_pending_member_removed(self) -> AsyncIterator[notifications.GroupPendingMemberRemovedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupPendingMemberRemoved')
		return self._stubs.groupNotificationStub.group_pending_member_removed(notifications.SubscribeToGroupPendingMemberRemovedNotification(client=self))
	
	def _notif_group_member_joined(self) -> AsyncIterator[notifications.GroupMemberJoinedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupMemberJoined')
		return self._stubs.groupNotificationStub.group_member_joined(notifications.SubscribeToGroupMemberJoinedNotification(client=self))
	
	def _notif_group_member_left(self) -> AsyncIterator[notifications.GroupMemberLeftNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupMemberLeft')
		return self._stubs.groupNotificationStub.group_member_left(notifications.SubscribeToGroupMemberLeftNotification(client=self))
	
	def _notif_group_own_permissions_updated(self) -> AsyncIterator[notifications.GroupOwnPermissionsUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupOwnPermissionsUpdated')
		return self._stubs.groupNotificationStub.group_own_permissions_updated(notifications.SubscribeToGroupOwnPermissionsUpdatedNotification(client=self))
	
	def _notif_group_member_permissions_updated(self) -> AsyncIterator[notifications.GroupMemberPermissionsUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupMemberPermissionsUpdated')
		return self._stubs.groupNotificationStub.group_member_permissions_updated(notifications.SubscribeToGroupMemberPermissionsUpdatedNotification(client=self))
	
	def _notif_group_update_in_progress(self) -> AsyncIterator[notifications.GroupUpdateInProgressNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupUpdateInProgress')
		return self._stubs.groupNotificationStub.group_update_in_progress(notifications.SubscribeToGroupUpdateInProgressNotification(client=self))
	
	def _notif_group_update_finished(self) -> AsyncIterator[notifications.GroupUpdateFinishedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupUpdateFinished')
		return self._stubs.groupNotificationStub.group_update_finished(notifications.SubscribeToGroupUpdateFinishedNotification(client=self))
	
	# DiscussionNotificationService
	def _notif_discussion_new(self) -> AsyncIterator[notifications.DiscussionNewNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: DiscussionNew')
		return self._stubs.discussionNotificationStub.discussion_new(notifications.SubscribeToDiscussionNewNotification(client=self))
	
	def _notif_discussion_locked(self) -> AsyncIterator[notifications.DiscussionLockedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: DiscussionLocked')
		return self._stubs.discussionNotificationStub.discussion_locked(notifications.SubscribeToDiscussionLockedNotification(client=self))
	
	def _notif_discussion_title_updated(self) -> AsyncIterator[notifications.DiscussionTitleUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: DiscussionTitleUpdated')
		return self._stubs.discussionNotificationStub.discussion_title_updated(notifications.SubscribeToDiscussionTitleUpdatedNotification(client=self))
	
	def _notif_discussion_settings_updated(self) -> AsyncIterator[notifications.DiscussionSettingsUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: DiscussionSettingsUpdated')
		return self._stubs.discussionNotificationStub.discussion_settings_updated(notifications.SubscribeToDiscussionSettingsUpdatedNotification(client=self))
	
	# MessageNotificationService
	def _notif_message_received(self) -> AsyncIterator[notifications.MessageReceivedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageReceived')
		return self._stubs.messageNotificationStub.message_received(notifications.SubscribeToMessageReceivedNotification(client=self))
	
	def _notif_message_sent(self) -> AsyncIterator[notifications.MessageSentNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageSent')
		return self._stubs.messageNotificationStub.message_sent(notifications.SubscribeToMessageSentNotification(client=self))
	
	def _notif_message_deleted(self) -> AsyncIterator[notifications.MessageDeletedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageDeleted')
		return self._stubs.messageNotificationStub.message_deleted(notifications.SubscribeToMessageDeletedNotification(client=self))
	
	def _notif_message_body_updated(self) -> AsyncIterator[notifications.MessageBodyUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageBodyUpdated')
		return self._stubs.messageNotificationStub.message_body_updated(notifications.SubscribeToMessageBodyUpdatedNotification(client=self))
	
	def _notif_message_uploaded(self) -> AsyncIterator[notifications.MessageUploadedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageUploaded')
		return self._stubs.messageNotificationStub.message_uploaded(notifications.SubscribeToMessageUploadedNotification(client=self))
	
	def _notif_message_delivered(self) -> AsyncIterator[notifications.MessageDeliveredNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageDelivered')
		return self._stubs.messageNotificationStub.message_delivered(notifications.SubscribeToMessageDeliveredNotification(client=self))
	
	def _notif_message_read(self) -> AsyncIterator[notifications.MessageReadNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageRead')
		return self._stubs.messageNotificationStub.message_read(notifications.SubscribeToMessageReadNotification(client=self))
	
	def _notif_message_location_received(self) -> AsyncIterator[notifications.MessageLocationReceivedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageLocationReceived')
		return self._stubs.messageNotificationStub.message_location_received(notifications.SubscribeToMessageLocationReceivedNotification(client=self))
	
	def _notif_message_location_sharing_start(self) -> AsyncIterator[notifications.MessageLocationSharingStartNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageLocationSharingStart')
		return self._stubs.messageNotificationStub.message_location_sharing_start(notifications.SubscribeToMessageLocationSharingStartNotification(client=self))
	
	def _notif_message_location_sharing_update(self) -> AsyncIterator[notifications.MessageLocationSharingUpdateNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageLocationSharingUpdate')
		return self._stubs.messageNotificationStub.message_location_sharing_update(notifications.SubscribeToMessageLocationSharingUpdateNotification(client=self))
	
	def _notif_message_location_sharing_end(self) -> AsyncIterator[notifications.MessageLocationSharingEndNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageLocationSharingEnd')
		return self._stubs.messageNotificationStub.message_location_sharing_end(notifications.SubscribeToMessageLocationSharingEndNotification(client=self))
	
	def _notif_message_reaction_added(self) -> AsyncIterator[notifications.MessageReactionAddedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageReactionAdded')
		return self._stubs.messageNotificationStub.message_reaction_added(notifications.SubscribeToMessageReactionAddedNotification(client=self))
	
	def _notif_message_reaction_updated(self) -> AsyncIterator[notifications.MessageReactionUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageReactionUpdated')
		return self._stubs.messageNotificationStub.message_reaction_updated(notifications.SubscribeToMessageReactionUpdatedNotification(client=self))
	
	def _notif_message_reaction_removed(self) -> AsyncIterator[notifications.MessageReactionRemovedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageReactionRemoved')
		return self._stubs.messageNotificationStub.message_reaction_removed(notifications.SubscribeToMessageReactionRemovedNotification(client=self))
	
	# AttachmentNotificationService
	def _notif_attachment_received(self) -> AsyncIterator[notifications.AttachmentReceivedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: AttachmentReceived')
		return self._stubs.attachmentNotificationStub.attachment_received(notifications.SubscribeToAttachmentReceivedNotification(client=self))
	
	def _notif_attachment_uploaded(self) -> AsyncIterator[notifications.AttachmentUploadedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: AttachmentUploaded')
		return self._stubs.attachmentNotificationStub.attachment_uploaded(notifications.SubscribeToAttachmentUploadedNotification(client=self))
	
	