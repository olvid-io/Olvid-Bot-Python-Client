from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from typing import Optional, Coroutine, AsyncIterator

	# for compatibility with python 3.10
	from typing import TypeVar
	# noinspection PyTypeHints
	Self = TypeVar("OlvidClient")

import grpc
import asyncio
import signal
import os
import dotenv
from asyncio import Task

from . import errors
from .logger import core_logger, command_logger, notification_logger
from ..internal import commands, notifications
from .. import datatypes
from ..listeners.ClientListenerHolder import ClientListenerHolder
from ..listeners.Command import Command, CommandHolder
from ..listeners.GenericNotificationListener import GenericNotificationListener
from ..listeners import ListenersImplementation as listeners
from .StubHolder import StubHolder
from .GrpcTlsConfiguration import GrpcTlsConfiguration, GrpcSimpleTlsConfiguration, GrpcMutualAuthTlsConfiguration, GrpcSslConfiguration
from ..listeners.Notifications import NOTIFICATIONS

# noinspection PyProtectedMember,PyShadowingBuiltins
class OlvidClient(CommandHolder):
	"""
	OlvidClient: basic class to interact with Olvid daemon.

	OlvidClient needs a client key to authenticate on daemon:
	- you can set OLVID_CLIENT_KEY env variable
	- you can use client_key constructor parameter (not recommended)

	Client connects to "http://localhost:50051" by default, you can change this behavior:
	- by setting OLVID_DAEMON_URL env variable
	- by using daemon_url parameter

	On creation OlvidClient will also check `.env` files and can load environment variable from there if there is
	configuration variable were not set in environment.

	See [GrpcTlsConfiguration.py](./GrpcTlsConfiguration.py) and GrpcTlsConfiguration class to see how to set up TLS
	and secure exchanges with daemon.

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

	If you create your own implementation of OlvidClient class you can override any method named `on_something`.
	There is one method for each gRPC notification method.
	Overwritten methods will add listeners for associated notification when you create a client instance.
	For example:

	class ChatBot(OlvidClient)
		async def on_message_received(self, message: datatypes.Message):
			await message.reply("Hello 👋")
	client = ChatBot()

	Every time ChatBot class is instantiated it will add a listener to message_received notification with the method as handler.

	You can also add Command objects with add_listener method. Command are specific listeners.
	They subclass listeners.MessageReceivedListener, and they are created with a regexp filter that will filter notifications.
	Only messages that match the regexp will raise a notification.
	Commands can be added using OlvidClient.command decorator:
	For example:

	class Bot(OlvidClient)
		@OlvidClient.command(regexp_filter="^!help")
		async def on_message_received(self, message: datatypes.Message):
			await message.reply("Help message")
	"""
	_KEY_VARIABLE_NAME: str = "OLVID_CLIENT_KEY"

	_DAEMON_URL_VARIABLE_NAME: str = "OLVID_DAEMON_URL"
	_DAEMON_URL_DEFAULT_VALUE: str = "localhost:50051"

	_CHUNK_LENGTH_VARIABLE_NAME = "OLVID_CHUNK_LENGTH"
	_CHUNK_LENGTH_DEFAULT_VALUE = "1_000_000"

	# we store running clients to notify them if we receive a stop signal
	_running_clients: list["OlvidClient"] = []

	GrpcSslConfiguration: type[GrpcSslConfiguration] = GrpcSslConfiguration
	GrpcSimpleTlsConfiguration: type[GrpcSimpleTlsConfiguration] = GrpcSimpleTlsConfiguration
	GrpcMutualAuthTlsConfiguration: type[GrpcMutualAuthTlsConfiguration] = GrpcMutualAuthTlsConfiguration

	def __init__(self, client_key: Optional[str] = None, daemon_url: Optional[str] = None, parent_client: Optional[Self] = None, tls_configuration: GrpcTlsConfiguration = None):
		self._stopped = False

		config: dict[str, str] = {
			**{  # default values
				self._DAEMON_URL_VARIABLE_NAME: self._DAEMON_URL_DEFAULT_VALUE,
				self._CHUNK_LENGTH_VARIABLE_NAME: self._CHUNK_LENGTH_DEFAULT_VALUE,
			},
			# usecwd=True: fix to use program path to look for a .env file and not `olvid-bot` module installation path
			**dotenv.dotenv_values(dotenv.find_dotenv(usecwd=True)),  # .env file values
			**os.environ  # env values
		}

		# determine the client key to use (argument > parent > env > file)
		if client_key:
			self._client_key: str = client_key
		elif parent_client:
			self._client_key: str = parent_client.client_key
		elif config.get(self._KEY_VARIABLE_NAME):
			self._client_key: str = config.get(self._KEY_VARIABLE_NAME)
		else:
			raise ValueError("Client key not found")

		# determine url (argument > parent > env > file > default)
		if daemon_url:
			self._daemon_url: str = daemon_url
		elif parent_client:
			self._daemon_url: str = parent_client.daemon_url
		else:
			self._daemon_url: str = config.get(self._DAEMON_URL_VARIABLE_NAME)

		# determine chunk length
		self._CHUNK_LENGTH: int = int(config.get(self._CHUNK_LENGTH_VARIABLE_NAME))

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
			self._channel: grpc.aio.Channel = self._parent_client._channel
			core_logger.debug(f"{self.__class__.__name__}: re-used parent configuration")
		# normal case
		else:
			# if tls configuration was not passed, try to load one
			if tls_configuration is not None:
				channel_credential: Optional[grpc.ChannelCredentials] = tls_configuration.get_channel_credentials()
				core_logger.debug(f"{self.__class__.__name__}: using {type(tls_configuration).__name__} parameter")
			elif GrpcMutualAuthTlsConfiguration.load_implicit_configuration() is not None:
				channel_credential: Optional[grpc.ChannelCredentials] = GrpcMutualAuthTlsConfiguration.load_implicit_configuration().get_channel_credentials()
				core_logger.debug(f"{self.__class__.__name__}: using {GrpcMutualAuthTlsConfiguration.__name__}")
			elif GrpcSimpleTlsConfiguration.load_implicit_configuration() is not None:
				channel_credential: Optional[grpc.ChannelCredentials] = GrpcSimpleTlsConfiguration.load_implicit_configuration().get_channel_credentials()
				core_logger.debug(f"{self.__class__.__name__}: using {GrpcSimpleTlsConfiguration.__name__}")
			else:
				channel_credential: Optional[grpc.ChannelCredentials] = None
				core_logger.debug(f"{self.__class__.__name__}: tls disabled")

			# handle http:// and https:// prefix in server url
			# http: just remove prefix
			if self._daemon_url.startswith("http://"):
				target: str = self._daemon_url.removeprefix("http://")
			# https: add ssl channel credentials
			elif self._daemon_url.startswith("https://"):
				target: str = self._daemon_url.removeprefix("https://")
				if not tls_configuration:
					# if there is no tls configuration, we create a simple channel credentials to connect to serer using ssl
					channel_credential = grpc.ssl_channel_credentials()
			else:
				target: str = self._daemon_url

			if channel_credential is None:
				self._channel: grpc.aio.Channel = grpc.aio.insecure_channel(target=target)
			else:
				self._channel: grpc.aio.Channel = grpc.aio.secure_channel(target=target, credentials=channel_credential)

		# create or re-use grpc stubs
		self._stubs = StubHolder(client=self, channel=self._channel, parent=self._parent_client)

		# store any future child client to bind their lifecycle to this one
		self._registered_child: Optional[list[Self]] = []
		# every client keep a list of own registered listeners because listener holder might contain other listeners from parent / son clients
		self._listeners_set: set[GenericNotificationListener] = set()
		# initialize listener holder: warning: this will set up an asyncio loop and cause issues with asyncio.run method that will create its own event loop
		self._listener_holder = ClientListenerHolder(self) if self._parent_client is None else self._parent_client._listener_holder

		# keep a set with pending tasks to keep a strong reference on it (each task might remove itself from the task set when finished)
		self._task_set = set()

		# register this client to stop it if a SIGTERM signal is received (signal sent when you docker container stops)
		if not self._parent_client:
			if len(self._running_clients) == 0:
				# if this is the first running client, register the signal handler
				for s in (signal.SIGTERM, ):
					# noinspection PyTypeChecker
					asyncio.get_event_loop().add_signal_handler(s, self.__stop_signal_handler)
			self._running_clients.append(self)

		# add listeners from overwritten "on_..." methods
		[self.add_listener(listener) for listener in self._get_listeners_to_add()]

		# add commands
		CommandHolder.__init__(self)

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

		if not self._parent_client and self in self._running_clients:
			self._running_clients.remove(self)

		self._stopped = True

		core_logger.debug(f"{self.__class__.__name__}: stopped")

	def _register_child(self, child_client: OlvidClient):
		self._registered_child.append(child_client)

	def are_listeners_finished(self) -> bool:
		# actualize registered listeners (remove listeners that were removed in holder but not removed here)
		self._listeners_set = set([listener for listener in self._listeners_set if listener in self._listener_holder._registered_listeners[listener.listener_key]])
		return len(self._listeners_set) == 0

	async def wait_for_listeners_end(self):
		# if bot was stopped or is not running, there is nothing to wait
		if self._stopped:
			return
		# wait for listeners' end
		while not self.are_listeners_finished():
			await self._listener_holder.wait_for_listener_removed_event()

	async def run_forever(self):
		state = self._channel.get_state(try_to_connect=True)
		while state not in [grpc.ChannelConnectivity.READY, grpc.ChannelConnectivity.TRANSIENT_FAILURE,
							grpc.ChannelConnectivity.SHUTDOWN]:
			await self._channel.wait_for_state_change(state)
			state = self._channel.get_state()
		if state in [grpc.ChannelConnectivity.TRANSIENT_FAILURE, grpc.ChannelConnectivity.SHUTDOWN]:
			raise errors.UnavailableError(details=f"{self.__class__.__name__}: run_forever: Failed to connect to server: {self.daemon_url}")

		await self.wait_for_listeners_end()
		has_listeners = len(self._listeners_set) > 0
		while self._channel.get_state() == grpc.ChannelConnectivity.READY:
			has_listeners = len(self._listeners_set) > 0
			await asyncio.sleep(1)
		# if there were no listeners add a logging message, else ClientListenerHolder probably already logged an error
		if not has_listeners:
			raise errors.UnavailableError(details=f"{self.__class__.__name__}: run_forever: Lost server connection: {self.daemon_url}")

	#####
	# read only properties
	#####
	@property
	def client_key(self) -> str:
		return self._client_key

	@property
	def daemon_url(self) -> str:
		return self._daemon_url

	@staticmethod
	def __stop_signal_handler():
		core_logger.info("Received a stop signal, stopping every running clients")
		# noinspection PyTypeChecker
		for client in OlvidClient._running_clients:
			client.add_background_task(client.stop(), f"force-stop-client")

	#####
	# Background tasks api
	#####
	# this api keeps a reference on created task for you (necessary when running an async task)
	def add_background_task(self, coroutine: Coroutine, name: str = "") -> Task:
		task = asyncio.get_event_loop().create_task(coroutine, name=name if name else None)
		self._task_set.add(task)

		def end_callback(t):
			self._task_set.remove(t)
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
			self.remove_listener(listener)

		# log
		core_logger.debug(f"{self.__class__.__name__}: removed all listeners")

	#####
	# CommandHolder interface implementation
	#####
	def is_message_body_a_valid_command(self, body: str) -> bool:
		return any([isinstance(listener, Command) and listener.match_str(body) for listener in self._listeners_set])

	####
	# NotificationHandler method
	####
	def _get_listeners_to_add(self) -> list[GenericNotificationListener]:
		listeners_list: list = list()
		for notification in NOTIFICATIONS:
			if not self._was_notification_listener_method_overwritten(notification):
				continue
			camel_case_notification_name = "".join(s.title() for s in notification.name.split("_"))
			listener = getattr(listeners, f"{camel_case_notification_name}Listener")(handler=getattr(self, f"on_{notification.name.lower()}"))
			listeners_list.append(listener)
		return listeners_list

	# check if a method was overwritten
	def _was_notification_listener_method_overwritten(self, notification: NOTIFICATIONS) -> bool:
		method_name = f"on_{notification.name.lower()}"
		# check method exists
		if not hasattr(self, method_name):
			return False
		# if listener method is different from original OlvidClient method, return it
		if getattr(type(self), method_name) != getattr(OlvidClient, method_name, None):
			return True
		# listener was not overwritten
		return False

	#####
	# GrpcMetadata property
	####
	def get_grpc_metadata(self) -> list[tuple[str, str]]:
		return [("daemon-client-key", self._client_key)]

	#####
	# other method: manually implemented
	#####
	async def enable_auto_invitation(self, accept_all: bool = False, auto_accept_introduction: bool = False, auto_accept_group: bool = False, auto_accept_one_to_one: bool = False, auto_accept_invitation: bool = False):
		auto_accept: datatypes.IdentitySettings.AutoAcceptInvitation
		if accept_all:
			auto_accept = datatypes.IdentitySettings.AutoAcceptInvitation(True, True, True, True)
		else:
			auto_accept = datatypes.IdentitySettings.AutoAcceptInvitation(auto_accept_introduction=auto_accept_introduction, auto_accept_group=auto_accept_group, auto_accept_invitation=auto_accept_invitation, auto_accept_one_to_one=auto_accept_one_to_one)
		settings: datatypes.IdentitySettings = await self.settings_identity_get()
		if settings.invitation != auto_accept:
			settings.invitation = auto_accept
			await self.settings_identity_set(settings)

	async def enable_keycloak_auto_invite(self, auto_invite_new_members: bool):
		keycloak_auto_invite: datatypes.IdentitySettings.Keycloak = datatypes.IdentitySettings.Keycloak(
			auto_invite_new_members=auto_invite_new_members
		)
		settings: datatypes.IdentitySettings = await self.settings_identity_get()
		if settings.keycloak != keycloak_auto_invite:
			settings.keycloak = keycloak_auto_invite
			await self.settings_identity_set(settings)

	async def set_message_retention_policy(self, existence_duration: int = 0, discussion_count: int = 0, global_count: int = 0, clean_locked_discussions: bool = False, preserve_is_sharing_location_messages: bool = False):
		retention_policy: datatypes.IdentitySettings.MessageRetention = datatypes.IdentitySettings.MessageRetention(
			existence_duration=existence_duration,
			discussion_count=discussion_count,
			global_count=global_count,
			clean_locked_discussions=clean_locked_discussions,
			preserve_is_sharing_location_messages=preserve_is_sharing_location_messages
		)
		settings: datatypes.IdentitySettings = await self.settings_identity_get()
		if settings.message_retention != retention_policy:
			settings.message_retention = retention_policy
			await self.settings_identity_set(settings)

	def attachment_message_list(self, message_id: datatypes.MessageId) -> AsyncIterator[datatypes.Attachment]:
		command_logger.info(f'{self.__class__.__name__}: command: AttachmentMessageList')

		async def iterator(message_iterator: AsyncIterator[commands.AttachmentListResponse]) -> AsyncIterator[
			datatypes.Attachment]:
			async for message in message_iterator:
				for element in message.attachments:
					yield element

		return iterator(self._stubs.attachmentCommandStub.attachment_list(
			commands.AttachmentListRequest(filter=datatypes.AttachmentFilter(message_id=message_id))))

	#####
	# request stream api (manually implemented)
	#####

	# IdentityCommandService
	async def identity_set_photo_file(self, file_path: str) -> commands.IdentitySetPhotoResponse:
		if not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
			raise IOError(f"Cannot open: {file_path}")

		async def identity_set_photo_iterator() -> AsyncIterator:
			with open(file_path, "rb") as fd:
				yield commands.IdentitySetPhotoRequest(
					metadata=commands.IdentitySetPhotoRequestMetadata(filename=os.path.basename(file_path),
																file_size=os.path.getsize(file_path)))
				buffer = fd.read(self._CHUNK_LENGTH)
				while len(buffer) > 0:
					yield commands.IdentitySetPhotoRequest(payload=buffer)
					buffer = fd.read(self._CHUNK_LENGTH)
		command_logger.info(f'{self.__class__.__name__}: command: IdentitySetPhoto')
		return await self._stubs.identityCommandStub.identity_set_photo(identity_set_photo_iterator())

	async def identity_set_photo(self, filename: str, payload: bytes) -> commands.IdentitySetPhotoResponse:
		async def identity_set_photo_iterator(buffer: bytes) -> AsyncIterator:
			yield commands.IdentitySetPhotoRequest(
				metadata=commands.IdentitySetPhotoRequestMetadata(filename=filename,
															file_size=len(payload)))
			while len(buffer) > 0:
				yield commands.IdentitySetPhotoRequest(payload=buffer)
				buffer = buffer[self._CHUNK_LENGTH:]
		command_logger.info(f'{self.__class__.__name__}: command: IdentitySetPhoto')
		return await self._stubs.identityCommandStub.identity_set_photo(identity_set_photo_iterator(payload))

	# GroupCommandService
	async def group_set_photo_file(self, group_id: int, file_path: str) -> datatypes.Group:
		if not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
			raise IOError(f"Cannot open: {file_path}")

		async def group_set_photo_iterator() -> AsyncIterator:
			fd = open(file_path, "rb")
			yield commands.GroupSetPhotoRequest(
				metadata=commands.GroupSetPhotoRequestMetadata(group_id=group_id, filename=os.path.basename(file_path),
															file_size=os.path.getsize(file_path)))
			buffer = fd.read(self._CHUNK_LENGTH)
			while len(buffer) > 0:
				yield commands.GroupSetPhotoRequest(payload=buffer)
				buffer = fd.read(self._CHUNK_LENGTH)
			fd.close()
		command_logger.info(f'{self.__class__.__name__}: command: GroupSetPhoto')
		return (await self._stubs.groupCommandStub.group_set_photo(group_set_photo_iterator())).group

	async def group_set_photo(self, group_id: int, filename: str, payload: bytes) -> datatypes.Group:
		async def group_set_photo_iterator(buffer: bytes) -> AsyncIterator:
			yield commands.GroupSetPhotoRequest(
				metadata=commands.GroupSetPhotoRequestMetadata(group_id=group_id, filename=filename, file_size=len(payload)))
			while len(buffer) > 0:
				yield commands.MessageSendWithAttachmentsRequest(payload=buffer[0:self._CHUNK_LENGTH])
				buffer = buffer[self._CHUNK_LENGTH:]
		command_logger.info(f'{self.__class__.__name__}: command: GroupSetPhoto')
		return (await self._stubs.groupCommandStub.group_set_photo(group_set_photo_iterator(payload))).group

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
					buffer = fd.read(self._CHUNK_LENGTH)
					while len(buffer) > 0:
						yield commands.MessageSendWithAttachmentsRequest(payload=buffer)
						buffer = fd.read(self._CHUNK_LENGTH)
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
	# WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_olvid_client_code.py
	####################################################################################################################
	# ToolCommandService
	async def ping(self) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: Ping')
		await self._stubs.toolCommandStub.ping(commands.PingRequest())
	
	async def daemon_version(self) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: DaemonVersion')
		response: commands.DaemonVersionResponse = await self._stubs.toolCommandStub.daemon_version(commands.DaemonVersionRequest())
		return response.version
	
	async def authentication_test(self) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: AuthenticationTest')
		await self._stubs.toolCommandStub.authentication_test(commands.AuthenticationTestRequest())
	
	async def authentication_admin_test(self) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: AuthenticationAdminTest')
		await self._stubs.toolCommandStub.authentication_admin_test(commands.AuthenticationAdminTestRequest())
	
	# IdentityCommandService
	async def identity_get(self) -> datatypes.Identity:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityGet')
		response: commands.IdentityGetResponse = await self._stubs.identityCommandStub.identity_get(commands.IdentityGetRequest())
		return response.identity
	
	async def identity_get_bytes_identifier(self) -> bytes:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityGetBytesIdentifier')
		response: commands.IdentityGetBytesIdentifierResponse = await self._stubs.identityCommandStub.identity_get_bytes_identifier(commands.IdentityGetBytesIdentifierRequest())
		return response.identifier
	
	async def identity_get_invitation_link(self) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityGetInvitationLink')
		response: commands.IdentityGetInvitationLinkResponse = await self._stubs.identityCommandStub.identity_get_invitation_link(commands.IdentityGetInvitationLinkRequest())
		return response.invitation_link
	
	async def identity_update_details(self, new_details: datatypes.IdentityDetails) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityUpdateDetails')
		await self._stubs.identityCommandStub.identity_update_details(commands.IdentityUpdateDetailsRequest(new_details=new_details))
	
	async def identity_remove_photo(self) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityRemovePhoto')
		await self._stubs.identityCommandStub.identity_remove_photo(commands.IdentityRemovePhotoRequest())
	
	# identity_set_photo: cannot generate request stream rpc code
	
	async def identity_download_photo(self) -> bytes:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityDownloadPhoto')
		response: commands.IdentityDownloadPhotoResponse = await self._stubs.identityCommandStub.identity_download_photo(commands.IdentityDownloadPhotoRequest())
		return response.photo
	
	async def identity_get_api_key_status(self) -> datatypes.Identity.ApiKey:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityGetApiKeyStatus')
		response: commands.IdentityGetApiKeyStatusResponse = await self._stubs.identityCommandStub.identity_get_api_key_status(commands.IdentityGetApiKeyStatusRequest())
		return response.api_key
	
	async def identity_set_api_key(self, api_key: str) -> datatypes.Identity.ApiKey:
		command_logger.info(f'{self.__class__.__name__}: command: IdentitySetApiKey')
		response: commands.IdentitySetApiKeyResponse = await self._stubs.identityCommandStub.identity_set_api_key(commands.IdentitySetApiKeyRequest(api_key=api_key))
		return response.api_key
	
	async def identity_set_configuration_link(self, configuration_link: str) -> datatypes.Identity.ApiKey:
		command_logger.info(f'{self.__class__.__name__}: command: IdentitySetConfigurationLink')
		response: commands.IdentitySetConfigurationLinkResponse = await self._stubs.identityCommandStub.identity_set_configuration_link(commands.IdentitySetConfigurationLinkRequest(configuration_link=configuration_link))
		return response.api_key
	
	# InvitationCommandService
	def invitation_list(self, filter: datatypes.InvitationFilter = None) -> AsyncIterator[datatypes.Invitation]:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationList')
	
		async def iterator(message_iterator: AsyncIterator[commands.InvitationListResponse]) -> AsyncIterator[datatypes.Invitation]:
			async for message in message_iterator:
				for element in message.invitations:
					yield element
		return iterator(self._stubs.invitationCommandStub.invitation_list(commands.InvitationListRequest(filter=filter)))
	
	async def invitation_get(self, invitation_id: int) -> datatypes.Invitation:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationGet')
		response: commands.InvitationGetResponse = await self._stubs.invitationCommandStub.invitation_get(commands.InvitationGetRequest(invitation_id=invitation_id))
		return response.invitation
	
	async def invitation_new(self, invitation_url: str) -> datatypes.Invitation:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationNew')
		response: commands.InvitationNewResponse = await self._stubs.invitationCommandStub.invitation_new(commands.InvitationNewRequest(invitation_url=invitation_url))
		return response.invitation
	
	async def invitation_accept(self, invitation_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationAccept')
		await self._stubs.invitationCommandStub.invitation_accept(commands.InvitationAcceptRequest(invitation_id=invitation_id))
	
	async def invitation_decline(self, invitation_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationDecline')
		await self._stubs.invitationCommandStub.invitation_decline(commands.InvitationDeclineRequest(invitation_id=invitation_id))
	
	async def invitation_sas(self, invitation_id: int, sas: str) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationSas')
		await self._stubs.invitationCommandStub.invitation_sas(commands.InvitationSasRequest(invitation_id=invitation_id, sas=sas))
	
	async def invitation_delete(self, invitation_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: InvitationDelete')
		await self._stubs.invitationCommandStub.invitation_delete(commands.InvitationDeleteRequest(invitation_id=invitation_id))
	
	# ContactCommandService
	def contact_list(self, filter: datatypes.ContactFilter = None) -> AsyncIterator[datatypes.Contact]:
		command_logger.info(f'{self.__class__.__name__}: command: ContactList')
	
		async def iterator(message_iterator: AsyncIterator[commands.ContactListResponse]) -> AsyncIterator[datatypes.Contact]:
			async for message in message_iterator:
				for element in message.contacts:
					yield element
		return iterator(self._stubs.contactCommandStub.contact_list(commands.ContactListRequest(filter=filter)))
	
	async def contact_get(self, contact_id: int) -> datatypes.Contact:
		command_logger.info(f'{self.__class__.__name__}: command: ContactGet')
		response: commands.ContactGetResponse = await self._stubs.contactCommandStub.contact_get(commands.ContactGetRequest(contact_id=contact_id))
		return response.contact
	
	async def contact_get_bytes_identifier(self, contact_id: int) -> bytes:
		command_logger.info(f'{self.__class__.__name__}: command: ContactGetBytesIdentifier')
		response: commands.ContactGetBytesIdentifierResponse = await self._stubs.contactCommandStub.contact_get_bytes_identifier(commands.ContactGetBytesIdentifierRequest(contact_id=contact_id))
		return response.identifier
	
	async def contact_get_invitation_link(self, contact_id: int) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: ContactGetInvitationLink')
		response: commands.ContactGetInvitationLinkResponse = await self._stubs.contactCommandStub.contact_get_invitation_link(commands.ContactGetInvitationLinkRequest(contact_id=contact_id))
		return response.invitation_link
	
	async def contact_delete(self, contact_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: ContactDelete')
		await self._stubs.contactCommandStub.contact_delete(commands.ContactDeleteRequest(contact_id=contact_id))
	
	async def contact_introduction(self, first_contact_id: int, second_contact_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: ContactIntroduction')
		await self._stubs.contactCommandStub.contact_introduction(commands.ContactIntroductionRequest(first_contact_id=first_contact_id, second_contact_id=second_contact_id))
	
	async def contact_download_photo(self, contact_id: int) -> bytes:
		command_logger.info(f'{self.__class__.__name__}: command: ContactDownloadPhoto')
		response: commands.ContactDownloadPhotoResponse = await self._stubs.contactCommandStub.contact_download_photo(commands.ContactDownloadPhotoRequest(contact_id=contact_id))
		return response.photo
	
	async def contact_recreate_channels(self, contact_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: ContactRecreateChannels')
		await self._stubs.contactCommandStub.contact_recreate_channels(commands.ContactRecreateChannelsRequest(contact_id=contact_id))
	
	async def contact_invite_to_one_to_one_discussion(self, contact_id: int) -> datatypes.Invitation:
		command_logger.info(f'{self.__class__.__name__}: command: ContactInviteToOneToOneDiscussion')
		response: commands.ContactInviteToOneToOneDiscussionResponse = await self._stubs.contactCommandStub.contact_invite_to_one_to_one_discussion(commands.ContactInviteToOneToOneDiscussionRequest(contact_id=contact_id))
		return response.invitation
	
	async def contact_downgrade_one_to_one_discussion(self, contact_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: ContactDowngradeOneToOneDiscussion')
		await self._stubs.contactCommandStub.contact_downgrade_one_to_one_discussion(commands.ContactDowngradeOneToOneDiscussionRequest(contact_id=contact_id))
	
	# KeycloakCommandService
	async def keycloak_bind_identity(self, configuration_link: str) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: KeycloakBindIdentity')
		await self._stubs.keycloakCommandStub.keycloak_bind_identity(commands.KeycloakBindIdentityRequest(configuration_link=configuration_link))
	
	async def keycloak_unbind_identity(self) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: KeycloakUnbindIdentity')
		await self._stubs.keycloakCommandStub.keycloak_unbind_identity(commands.KeycloakUnbindIdentityRequest())
	
	def keycloak_user_list(self, filter: datatypes.KeycloakUserFilter = None, last_list_timestamp: int = 0) -> AsyncIterator[tuple[list[datatypes.KeycloakUser], int]]:
		command_logger.info(f'{self.__class__.__name__}: command: KeycloakUserList')
	
		async def iterator(message_iterator: AsyncIterator[commands.KeycloakUserListResponse]) -> AsyncIterator[tuple[list[datatypes.KeycloakUser], int]]:
			async for message in message_iterator:
				yield message.users, message.last_list_timestamp
		return iterator(self._stubs.keycloakCommandStub.keycloak_user_list(commands.KeycloakUserListRequest(filter=filter, last_list_timestamp=last_list_timestamp)))
	
	async def keycloak_add_user_as_contact(self, keycloak_id: str) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: KeycloakAddUserAsContact')
		await self._stubs.keycloakCommandStub.keycloak_add_user_as_contact(commands.KeycloakAddUserAsContactRequest(keycloak_id=keycloak_id))
	
	# GroupCommandService
	def group_list(self, filter: datatypes.GroupFilter = None) -> AsyncIterator[datatypes.Group]:
		command_logger.info(f'{self.__class__.__name__}: command: GroupList')
	
		async def iterator(message_iterator: AsyncIterator[commands.GroupListResponse]) -> AsyncIterator[datatypes.Group]:
			async for message in message_iterator:
				for element in message.groups:
					yield element
		return iterator(self._stubs.groupCommandStub.group_list(commands.GroupListRequest(filter=filter)))
	
	async def group_get(self, group_id: int) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupGet')
		response: commands.GroupGetResponse = await self._stubs.groupCommandStub.group_get(commands.GroupGetRequest(group_id=group_id))
		return response.group
	
	async def group_get_bytes_identifier(self, group_id: int) -> bytes:
		command_logger.info(f'{self.__class__.__name__}: command: GroupGetBytesIdentifier')
		response: commands.GroupGetBytesIdentifierResponse = await self._stubs.groupCommandStub.group_get_bytes_identifier(commands.GroupGetBytesIdentifierRequest(group_id=group_id))
		return response.identifier
	
	async def group_new_standard_group(self, name: str = "", description: str = "", admin_contact_ids: list[int] = ()) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupNewStandardGroup')
		response: commands.GroupNewStandardGroupResponse = await self._stubs.groupCommandStub.group_new_standard_group(commands.GroupNewStandardGroupRequest(name=name, description=description, admin_contact_ids=admin_contact_ids))
		return response.group
	
	async def group_new_controlled_group(self, name: str = "", description: str = "", admin_contact_ids: list[int] = (), contact_ids: list[int] = ()) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupNewControlledGroup')
		response: commands.GroupNewControlledGroupResponse = await self._stubs.groupCommandStub.group_new_controlled_group(commands.GroupNewControlledGroupRequest(name=name, description=description, admin_contact_ids=admin_contact_ids, contact_ids=contact_ids))
		return response.group
	
	async def group_new_read_only_group(self, name: str = "", description: str = "", admin_contact_ids: list[int] = (), contact_ids: list[int] = ()) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupNewReadOnlyGroup')
		response: commands.GroupNewReadOnlyGroupResponse = await self._stubs.groupCommandStub.group_new_read_only_group(commands.GroupNewReadOnlyGroupRequest(name=name, description=description, admin_contact_ids=admin_contact_ids, contact_ids=contact_ids))
		return response.group
	
	async def group_new_advanced_group(self, name: str = "", description: str = "", advanced_configuration: datatypes.Group.AdvancedConfiguration = None, members: list[datatypes.GroupMember] = None) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupNewAdvancedGroup')
		response: commands.GroupNewAdvancedGroupResponse = await self._stubs.groupCommandStub.group_new_advanced_group(commands.GroupNewAdvancedGroupRequest(name=name, description=description, advanced_configuration=advanced_configuration, members=members))
		return response.group
	
	async def group_disband(self, group_id: int) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupDisband')
		response: commands.GroupDisbandResponse = await self._stubs.groupCommandStub.group_disband(commands.GroupDisbandRequest(group_id=group_id))
		return response.group
	
	async def group_leave(self, group_id: int) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupLeave')
		response: commands.GroupLeaveResponse = await self._stubs.groupCommandStub.group_leave(commands.GroupLeaveRequest(group_id=group_id))
		return response.group
	
	async def group_update(self, group: datatypes.Group) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupUpdate')
		response: commands.GroupUpdateResponse = await self._stubs.groupCommandStub.group_update(commands.GroupUpdateRequest(group=group))
		return response.group
	
	async def group_unset_photo(self, group_id: int) -> datatypes.Group:
		command_logger.info(f'{self.__class__.__name__}: command: GroupUnsetPhoto')
		response: commands.GroupUnsetPhotoResponse = await self._stubs.groupCommandStub.group_unset_photo(commands.GroupUnsetPhotoRequest(group_id=group_id))
		return response.group
	
	# group_set_photo: cannot generate request stream rpc code
	
	async def group_download_photo(self, group_id: int) -> bytes:
		command_logger.info(f'{self.__class__.__name__}: command: GroupDownloadPhoto')
		response: commands.GroupDownloadPhotoResponse = await self._stubs.groupCommandStub.group_download_photo(commands.GroupDownloadPhotoRequest(group_id=group_id))
		return response.photo
	
	# DiscussionCommandService
	def discussion_list(self, filter: datatypes.DiscussionFilter = None) -> AsyncIterator[datatypes.Discussion]:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionList')
	
		async def iterator(message_iterator: AsyncIterator[commands.DiscussionListResponse]) -> AsyncIterator[datatypes.Discussion]:
			async for message in message_iterator:
				for element in message.discussions:
					yield element
		return iterator(self._stubs.discussionCommandStub.discussion_list(commands.DiscussionListRequest(filter=filter)))
	
	async def discussion_get(self, discussion_id: int) -> datatypes.Discussion:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionGet')
		response: commands.DiscussionGetResponse = await self._stubs.discussionCommandStub.discussion_get(commands.DiscussionGetRequest(discussion_id=discussion_id))
		return response.discussion
	
	async def discussion_get_bytes_identifier(self, discussion_id: int) -> bytes:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionGetBytesIdentifier')
		response: commands.DiscussionGetBytesIdentifierResponse = await self._stubs.discussionCommandStub.discussion_get_bytes_identifier(commands.DiscussionGetBytesIdentifierRequest(discussion_id=discussion_id))
		return response.identifier
	
	async def discussion_get_by_contact(self, contact_id: int) -> datatypes.Discussion:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionGetByContact')
		response: commands.DiscussionGetByContactResponse = await self._stubs.discussionCommandStub.discussion_get_by_contact(commands.DiscussionGetByContactRequest(contact_id=contact_id))
		return response.discussion
	
	async def discussion_get_by_group(self, group_id: int) -> datatypes.Discussion:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionGetByGroup')
		response: commands.DiscussionGetByGroupResponse = await self._stubs.discussionCommandStub.discussion_get_by_group(commands.DiscussionGetByGroupRequest(group_id=group_id))
		return response.discussion
	
	async def discussion_empty(self, discussion_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionEmpty')
		await self._stubs.discussionCommandStub.discussion_empty(commands.DiscussionEmptyRequest(discussion_id=discussion_id))
	
	async def discussion_download_photo(self, discussion_id: int) -> bytes:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionDownloadPhoto')
		response: commands.DiscussionDownloadPhotoResponse = await self._stubs.discussionCommandStub.discussion_download_photo(commands.DiscussionDownloadPhotoRequest(discussion_id=discussion_id))
		return response.photo
	
	def discussion_locked_list(self) -> AsyncIterator[datatypes.Discussion]:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionLockedList')
	
		async def iterator(message_iterator: AsyncIterator[commands.DiscussionLockedListResponse]) -> AsyncIterator[datatypes.Discussion]:
			async for message in message_iterator:
				for element in message.discussions:
					yield element
		return iterator(self._stubs.discussionCommandStub.discussion_locked_list(commands.DiscussionLockedListRequest()))
	
	async def discussion_locked_delete(self, discussion_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionLockedDelete')
		await self._stubs.discussionCommandStub.discussion_locked_delete(commands.DiscussionLockedDeleteRequest(discussion_id=discussion_id))
	
	# MessageCommandService
	def message_list(self, filter: datatypes.MessageFilter = None, unread: bool = False) -> AsyncIterator[datatypes.Message]:
		command_logger.info(f'{self.__class__.__name__}: command: MessageList')
	
		async def iterator(message_iterator: AsyncIterator[commands.MessageListResponse]) -> AsyncIterator[datatypes.Message]:
			async for message in message_iterator:
				for element in message.messages:
					yield element
		return iterator(self._stubs.messageCommandStub.message_list(commands.MessageListRequest(filter=filter, unread=unread)))
	
	async def message_get(self, message_id: datatypes.MessageId) -> datatypes.Message:
		command_logger.info(f'{self.__class__.__name__}: command: MessageGet')
		response: commands.MessageGetResponse = await self._stubs.messageCommandStub.message_get(commands.MessageGetRequest(message_id=message_id))
		return response.message
	
	async def message_refresh(self) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: MessageRefresh')
		await self._stubs.messageCommandStub.message_refresh(commands.MessageRefreshRequest())
	
	async def message_delete(self, message_id: datatypes.MessageId, delete_everywhere: bool = False) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: MessageDelete')
		await self._stubs.messageCommandStub.message_delete(commands.MessageDeleteRequest(message_id=message_id, delete_everywhere=delete_everywhere))
	
	async def message_send(self, discussion_id: int, body: str, reply_id: datatypes.MessageId = None, ephemerality: datatypes.MessageEphemerality = None, disable_link_preview: bool = False) -> datatypes.Message:
		command_logger.info(f'{self.__class__.__name__}: command: MessageSend')
		response: commands.MessageSendResponse = await self._stubs.messageCommandStub.message_send(commands.MessageSendRequest(discussion_id=discussion_id, body=body, reply_id=reply_id, ephemerality=ephemerality, disable_link_preview=disable_link_preview))
		return response.message
	
	# message_send_with_attachments: cannot generate request stream rpc code
	
	async def message_send_location(self, discussion_id: int, latitude: float, longitude: float, altitude: float = 0.0, precision: float = 0.0, address: str = "", preview_filename: str = "", preview_payload: bytes = b"", ephemerality: datatypes.MessageEphemerality = None) -> datatypes.Message:
		command_logger.info(f'{self.__class__.__name__}: command: MessageSendLocation')
		response: commands.MessageSendLocationResponse = await self._stubs.messageCommandStub.message_send_location(commands.MessageSendLocationRequest(discussion_id=discussion_id, latitude=latitude, longitude=longitude, altitude=altitude, precision=precision, address=address, preview_filename=preview_filename, preview_payload=preview_payload, ephemerality=ephemerality))
		return response.message
	
	async def message_start_location_sharing(self, discussion_id: int, latitude: float, longitude: float, altitude: float = 0.0, precision: float = 0.0) -> datatypes.Message:
		command_logger.info(f'{self.__class__.__name__}: command: MessageStartLocationSharing')
		response: commands.MessageStartLocationSharingResponse = await self._stubs.messageCommandStub.message_start_location_sharing(commands.MessageStartLocationSharingRequest(discussion_id=discussion_id, latitude=latitude, longitude=longitude, altitude=altitude, precision=precision))
		return response.message
	
	async def message_update_location_sharing(self, message_id: datatypes.MessageId, latitude: float, longitude: float, altitude: float = 0.0, precision: float = 0.0) -> datatypes.Message:
		command_logger.info(f'{self.__class__.__name__}: command: MessageUpdateLocationSharing')
		response: commands.MessageUpdateLocationSharingResponse = await self._stubs.messageCommandStub.message_update_location_sharing(commands.MessageUpdateLocationSharingRequest(message_id=message_id, latitude=latitude, longitude=longitude, altitude=altitude, precision=precision))
		return response.message
	
	async def message_end_location_sharing(self, message_id: datatypes.MessageId) -> datatypes.Message:
		command_logger.info(f'{self.__class__.__name__}: command: MessageEndLocationSharing')
		response: commands.MessageEndLocationSharingResponse = await self._stubs.messageCommandStub.message_end_location_sharing(commands.MessageEndLocationSharingRequest(message_id=message_id))
		return response.message
	
	async def message_react(self, message_id: datatypes.MessageId, reaction: str = "") -> None:
		command_logger.info(f'{self.__class__.__name__}: command: MessageReact')
		await self._stubs.messageCommandStub.message_react(commands.MessageReactRequest(message_id=message_id, reaction=reaction))
	
	async def message_update_body(self, message_id: datatypes.MessageId, updated_body: str) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: MessageUpdateBody')
		await self._stubs.messageCommandStub.message_update_body(commands.MessageUpdateBodyRequest(message_id=message_id, updated_body=updated_body))
	
	# AttachmentCommandService
	def attachment_list(self, filter: datatypes.AttachmentFilter = None) -> AsyncIterator[datatypes.Attachment]:
		command_logger.info(f'{self.__class__.__name__}: command: AttachmentList')
	
		async def iterator(message_iterator: AsyncIterator[commands.AttachmentListResponse]) -> AsyncIterator[datatypes.Attachment]:
			async for message in message_iterator:
				for element in message.attachments:
					yield element
		return iterator(self._stubs.attachmentCommandStub.attachment_list(commands.AttachmentListRequest(filter=filter)))
	
	async def attachment_get(self, attachment_id: datatypes.AttachmentId) -> datatypes.Attachment:
		command_logger.info(f'{self.__class__.__name__}: command: AttachmentGet')
		response: commands.AttachmentGetResponse = await self._stubs.attachmentCommandStub.attachment_get(commands.AttachmentGetRequest(attachment_id=attachment_id))
		return response.attachment
	
	async def attachment_delete(self, attachment_id: datatypes.AttachmentId, delete_everywhere: bool = False) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: AttachmentDelete')
		await self._stubs.attachmentCommandStub.attachment_delete(commands.AttachmentDeleteRequest(attachment_id=attachment_id, delete_everywhere=delete_everywhere))
	
	def attachment_download(self, attachment_id: datatypes.AttachmentId) -> AsyncIterator[bytes]:
		command_logger.info(f'{self.__class__.__name__}: command: AttachmentDownload')
	
		async def iterator(message_iterator: AsyncIterator[commands.AttachmentDownloadResponse]) -> AsyncIterator[bytes]:
			async for message in message_iterator:
				yield message.chunk
		return iterator(self._stubs.attachmentCommandStub.attachment_download(commands.AttachmentDownloadRequest(attachment_id=attachment_id)))
	
	# StorageCommandService
	def storage_list(self, filter: datatypes.StorageElementFilter = None) -> AsyncIterator[datatypes.StorageElement]:
		command_logger.info(f'{self.__class__.__name__}: command: StorageList')
	
		async def iterator(message_iterator: AsyncIterator[commands.StorageListResponse]) -> AsyncIterator[datatypes.StorageElement]:
			async for message in message_iterator:
				for element in message.elements:
					yield element
		return iterator(self._stubs.storageCommandStub.storage_list(commands.StorageListRequest(filter=filter)))
	
	async def storage_get(self, key: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: StorageGet')
		response: commands.StorageGetResponse = await self._stubs.storageCommandStub.storage_get(commands.StorageGetRequest(key=key))
		return response.value
	
	async def storage_set(self, key: str, value: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: StorageSet')
		response: commands.StorageSetResponse = await self._stubs.storageCommandStub.storage_set(commands.StorageSetRequest(key=key, value=value))
		return response.previous_value
	
	async def storage_unset(self, key: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: StorageUnset')
		response: commands.StorageUnsetResponse = await self._stubs.storageCommandStub.storage_unset(commands.StorageUnsetRequest(key=key))
		return response.previous_value
	
	# DiscussionStorageCommandService
	def discussion_storage_list(self, discussion_id: int, filter: datatypes.StorageElementFilter = None) -> AsyncIterator[datatypes.StorageElement]:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionStorageList')
	
		async def iterator(message_iterator: AsyncIterator[commands.DiscussionStorageListResponse]) -> AsyncIterator[datatypes.StorageElement]:
			async for message in message_iterator:
				for element in message.elements:
					yield element
		return iterator(self._stubs.discussionStorageCommandStub.discussion_storage_list(commands.DiscussionStorageListRequest(discussion_id=discussion_id, filter=filter)))
	
	async def discussion_storage_get(self, discussion_id: int, key: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionStorageGet')
		response: commands.DiscussionStorageGetResponse = await self._stubs.discussionStorageCommandStub.discussion_storage_get(commands.DiscussionStorageGetRequest(discussion_id=discussion_id, key=key))
		return response.value
	
	async def discussion_storage_set(self, discussion_id: int, key: str, value: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionStorageSet')
		response: commands.DiscussionStorageSetResponse = await self._stubs.discussionStorageCommandStub.discussion_storage_set(commands.DiscussionStorageSetRequest(discussion_id=discussion_id, key=key, value=value))
		return response.previous_value
	
	async def discussion_storage_unset(self, discussion_id: int, key: str) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: DiscussionStorageUnset')
		response: commands.DiscussionStorageUnsetResponse = await self._stubs.discussionStorageCommandStub.discussion_storage_unset(commands.DiscussionStorageUnsetRequest(discussion_id=discussion_id, key=key))
		return response.previous_value
	
	# CallCommandService
	async def call_start_discussion_call(self, discussion_id: int) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: CallStartDiscussionCall')
		response: commands.CallStartDiscussionCallResponse = await self._stubs.callCommandStub.call_start_discussion_call(commands.CallStartDiscussionCallRequest(discussion_id=discussion_id))
		return response.call_identifier
	
	async def call_start_custom_call(self, contact_ids: list[int] = (), discussion_id: int = 0) -> str:
		command_logger.info(f'{self.__class__.__name__}: command: CallStartCustomCall')
		response: commands.CallStartCustomCallResponse = await self._stubs.callCommandStub.call_start_custom_call(commands.CallStartCustomCallRequest(contact_ids=contact_ids, discussion_id=discussion_id))
		return response.call_identifier
	
	# SettingsCommandService
	async def settings_identity_get(self) -> datatypes.IdentitySettings:
		command_logger.info(f'{self.__class__.__name__}: command: SettingsIdentityGet')
		response: commands.SettingsIdentityGetResponse = await self._stubs.settingsCommandStub.settings_identity_get(commands.SettingsIdentityGetRequest())
		return response.identity_settings
	
	async def settings_identity_set(self, identity_settings: datatypes.IdentitySettings) -> datatypes.IdentitySettings:
		command_logger.info(f'{self.__class__.__name__}: command: SettingsIdentitySet')
		response: commands.SettingsIdentitySetResponse = await self._stubs.settingsCommandStub.settings_identity_set(commands.SettingsIdentitySetRequest(identity_settings=identity_settings))
		return response.identity_settings
	
	async def settings_discussion_get(self, discussion_id: int) -> datatypes.DiscussionSettings:
		command_logger.info(f'{self.__class__.__name__}: command: SettingsDiscussionGet')
		response: commands.SettingsDiscussionGetResponse = await self._stubs.settingsCommandStub.settings_discussion_get(commands.SettingsDiscussionGetRequest(discussion_id=discussion_id))
		return response.discussion_settings
	
	async def settings_discussion_set(self, discussion_settings: datatypes.DiscussionSettings) -> datatypes.DiscussionSettings:
		command_logger.info(f'{self.__class__.__name__}: command: SettingsDiscussionSet')
		response: commands.SettingsDiscussionSetResponse = await self._stubs.settingsCommandStub.settings_discussion_set(commands.SettingsDiscussionSetRequest(discussion_settings=discussion_settings))
		return response.discussion_settings
	
	# InvitationNotificationService
	def _notif_invitation_received(self, count: int = 0, filter: datatypes.InvitationFilter = None) -> AsyncIterator[notifications.InvitationReceivedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: InvitationReceived')
		return self._stubs.invitationNotificationStub.invitation_received(notifications.SubscribeToInvitationReceivedNotification(count=count, filter=filter))
	
	def _notif_invitation_sent(self, count: int = 0, filter: datatypes.InvitationFilter = None) -> AsyncIterator[notifications.InvitationSentNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: InvitationSent')
		return self._stubs.invitationNotificationStub.invitation_sent(notifications.SubscribeToInvitationSentNotification(count=count, filter=filter))
	
	def _notif_invitation_deleted(self, count: int = 0, filter: datatypes.InvitationFilter = None, invitation_ids: list[int] = ()) -> AsyncIterator[notifications.InvitationDeletedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: InvitationDeleted')
		return self._stubs.invitationNotificationStub.invitation_deleted(notifications.SubscribeToInvitationDeletedNotification(count=count, filter=filter, invitation_ids=invitation_ids))
	
	def _notif_invitation_updated(self, count: int = 0, filter: datatypes.InvitationFilter = None, invitation_ids: list[int] = ()) -> AsyncIterator[notifications.InvitationUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: InvitationUpdated')
		return self._stubs.invitationNotificationStub.invitation_updated(notifications.SubscribeToInvitationUpdatedNotification(count=count, filter=filter, invitation_ids=invitation_ids))
	
	# ContactNotificationService
	def _notif_contact_new(self, count: int = 0, filter: datatypes.ContactFilter = None) -> AsyncIterator[notifications.ContactNewNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: ContactNew')
		return self._stubs.contactNotificationStub.contact_new(notifications.SubscribeToContactNewNotification(count=count, filter=filter))
	
	def _notif_contact_deleted(self, count: int = 0, filter: datatypes.ContactFilter = None, contact_ids: list[int] = ()) -> AsyncIterator[notifications.ContactDeletedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: ContactDeleted')
		return self._stubs.contactNotificationStub.contact_deleted(notifications.SubscribeToContactDeletedNotification(count=count, filter=filter, contact_ids=contact_ids))
	
	def _notif_contact_details_updated(self, count: int = 0, filter: datatypes.ContactFilter = None, contact_ids: list[int] = ()) -> AsyncIterator[notifications.ContactDetailsUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: ContactDetailsUpdated')
		return self._stubs.contactNotificationStub.contact_details_updated(notifications.SubscribeToContactDetailsUpdatedNotification(count=count, filter=filter, contact_ids=contact_ids))
	
	def _notif_contact_photo_updated(self, count: int = 0, filter: datatypes.ContactFilter = None, contact_ids: list[int] = ()) -> AsyncIterator[notifications.ContactPhotoUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: ContactPhotoUpdated')
		return self._stubs.contactNotificationStub.contact_photo_updated(notifications.SubscribeToContactPhotoUpdatedNotification(count=count, filter=filter, contact_ids=contact_ids))
	
	# GroupNotificationService
	def _notif_group_new(self, count: int = 0, group_filter: datatypes.GroupFilter = None) -> AsyncIterator[notifications.GroupNewNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupNew')
		return self._stubs.groupNotificationStub.group_new(notifications.SubscribeToGroupNewNotification(count=count, group_filter=group_filter))
	
	def _notif_group_deleted(self, count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None) -> AsyncIterator[notifications.GroupDeletedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupDeleted')
		return self._stubs.groupNotificationStub.group_deleted(notifications.SubscribeToGroupDeletedNotification(count=count, group_ids=group_ids, group_filter=group_filter))
	
	def _notif_group_name_updated(self, count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, previous_name_search: str = "") -> AsyncIterator[notifications.GroupNameUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupNameUpdated')
		return self._stubs.groupNotificationStub.group_name_updated(notifications.SubscribeToGroupNameUpdatedNotification(count=count, group_ids=group_ids, group_filter=group_filter, previous_name_search=previous_name_search))
	
	def _notif_group_photo_updated(self, count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None) -> AsyncIterator[notifications.GroupPhotoUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupPhotoUpdated')
		return self._stubs.groupNotificationStub.group_photo_updated(notifications.SubscribeToGroupPhotoUpdatedNotification(count=count, group_ids=group_ids, group_filter=group_filter))
	
	def _notif_group_description_updated(self, count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, previous_description_search: str = "") -> AsyncIterator[notifications.GroupDescriptionUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupDescriptionUpdated')
		return self._stubs.groupNotificationStub.group_description_updated(notifications.SubscribeToGroupDescriptionUpdatedNotification(count=count, group_ids=group_ids, group_filter=group_filter, previous_description_search=previous_description_search))
	
	def _notif_group_pending_member_added(self, count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, pending_member_filter: datatypes.PendingGroupMemberFilter = None) -> AsyncIterator[notifications.GroupPendingMemberAddedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupPendingMemberAdded')
		return self._stubs.groupNotificationStub.group_pending_member_added(notifications.SubscribeToGroupPendingMemberAddedNotification(count=count, group_ids=group_ids, group_filter=group_filter, pending_member_filter=pending_member_filter))
	
	def _notif_group_pending_member_removed(self, count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, pending_member_filter: datatypes.PendingGroupMemberFilter = None) -> AsyncIterator[notifications.GroupPendingMemberRemovedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupPendingMemberRemoved')
		return self._stubs.groupNotificationStub.group_pending_member_removed(notifications.SubscribeToGroupPendingMemberRemovedNotification(count=count, group_ids=group_ids, group_filter=group_filter, pending_member_filter=pending_member_filter))
	
	def _notif_group_member_joined(self, count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, member_filter: datatypes.GroupMemberFilter = None) -> AsyncIterator[notifications.GroupMemberJoinedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupMemberJoined')
		return self._stubs.groupNotificationStub.group_member_joined(notifications.SubscribeToGroupMemberJoinedNotification(count=count, group_ids=group_ids, group_filter=group_filter, member_filter=member_filter))
	
	def _notif_group_member_left(self, count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, member_filter: datatypes.GroupMemberFilter = None) -> AsyncIterator[notifications.GroupMemberLeftNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupMemberLeft')
		return self._stubs.groupNotificationStub.group_member_left(notifications.SubscribeToGroupMemberLeftNotification(count=count, group_ids=group_ids, group_filter=group_filter, member_filter=member_filter))
	
	def _notif_group_own_permissions_updated(self, count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, permissions_filter: datatypes.GroupPermissionFilter = None, previous_permissions_filter: datatypes.GroupPermissionFilter = None) -> AsyncIterator[notifications.GroupOwnPermissionsUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupOwnPermissionsUpdated')
		return self._stubs.groupNotificationStub.group_own_permissions_updated(notifications.SubscribeToGroupOwnPermissionsUpdatedNotification(count=count, group_ids=group_ids, group_filter=group_filter, permissions_filter=permissions_filter, previous_permissions_filter=previous_permissions_filter))
	
	def _notif_group_member_permissions_updated(self, count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, member_filter: datatypes.GroupMemberFilter = None, previous_permission_filter: datatypes.GroupMemberFilter = None) -> AsyncIterator[notifications.GroupMemberPermissionsUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: GroupMemberPermissionsUpdated')
		return self._stubs.groupNotificationStub.group_member_permissions_updated(notifications.SubscribeToGroupMemberPermissionsUpdatedNotification(count=count, group_ids=group_ids, group_filter=group_filter, member_filter=member_filter, previous_permission_filter=previous_permission_filter))
	
	# DiscussionNotificationService
	def _notif_discussion_new(self, count: int = 0, filter: datatypes.DiscussionFilter = None) -> AsyncIterator[notifications.DiscussionNewNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: DiscussionNew')
		return self._stubs.discussionNotificationStub.discussion_new(notifications.SubscribeToDiscussionNewNotification(count=count, filter=filter))
	
	def _notif_discussion_locked(self, count: int = 0, filter: datatypes.DiscussionFilter = None, discussion_ids: list[int] = ()) -> AsyncIterator[notifications.DiscussionLockedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: DiscussionLocked')
		return self._stubs.discussionNotificationStub.discussion_locked(notifications.SubscribeToDiscussionLockedNotification(count=count, filter=filter, discussion_ids=discussion_ids))
	
	def _notif_discussion_title_updated(self, count: int = 0, filter: datatypes.DiscussionFilter = None, discussion_ids: list[int] = ()) -> AsyncIterator[notifications.DiscussionTitleUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: DiscussionTitleUpdated')
		return self._stubs.discussionNotificationStub.discussion_title_updated(notifications.SubscribeToDiscussionTitleUpdatedNotification(count=count, filter=filter, discussion_ids=discussion_ids))
	
	def _notif_discussion_settings_updated(self, count: int = 0, filter: datatypes.DiscussionFilter = None, discussion_ids: list[int] = ()) -> AsyncIterator[notifications.DiscussionSettingsUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: DiscussionSettingsUpdated')
		return self._stubs.discussionNotificationStub.discussion_settings_updated(notifications.SubscribeToDiscussionSettingsUpdatedNotification(count=count, filter=filter, discussion_ids=discussion_ids))
	
	# MessageNotificationService
	def _notif_message_received(self, count: int = 0, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageReceivedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageReceived')
		return self._stubs.messageNotificationStub.message_received(notifications.SubscribeToMessageReceivedNotification(count=count, filter=filter))
	
	def _notif_message_sent(self, count: int = 0, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageSentNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageSent')
		return self._stubs.messageNotificationStub.message_sent(notifications.SubscribeToMessageSentNotification(count=count, filter=filter))
	
	def _notif_message_deleted(self, count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageDeletedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageDeleted')
		return self._stubs.messageNotificationStub.message_deleted(notifications.SubscribeToMessageDeletedNotification(count=count, message_ids=message_ids, filter=filter))
	
	def _notif_message_body_updated(self, count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageBodyUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageBodyUpdated')
		return self._stubs.messageNotificationStub.message_body_updated(notifications.SubscribeToMessageBodyUpdatedNotification(count=count, message_ids=message_ids, filter=filter))
	
	def _notif_message_uploaded(self, count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageUploadedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageUploaded')
		return self._stubs.messageNotificationStub.message_uploaded(notifications.SubscribeToMessageUploadedNotification(count=count, message_ids=message_ids, filter=filter))
	
	def _notif_message_delivered(self, count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageDeliveredNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageDelivered')
		return self._stubs.messageNotificationStub.message_delivered(notifications.SubscribeToMessageDeliveredNotification(count=count, message_ids=message_ids, filter=filter))
	
	def _notif_message_read(self, count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageReadNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageRead')
		return self._stubs.messageNotificationStub.message_read(notifications.SubscribeToMessageReadNotification(count=count, message_ids=message_ids, filter=filter))
	
	def _notif_message_location_received(self, count: int = 0, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageLocationReceivedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageLocationReceived')
		return self._stubs.messageNotificationStub.message_location_received(notifications.SubscribeToMessageLocationReceivedNotification(count=count, filter=filter))
	
	def _notif_message_location_sent(self, count: int = 0, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageLocationSentNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageLocationSent')
		return self._stubs.messageNotificationStub.message_location_sent(notifications.SubscribeToMessageLocationSentNotification(count=count, filter=filter))
	
	def _notif_message_location_sharing_start(self, count: int = 0, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageLocationSharingStartNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageLocationSharingStart')
		return self._stubs.messageNotificationStub.message_location_sharing_start(notifications.SubscribeToMessageLocationSharingStartNotification(count=count, filter=filter))
	
	def _notif_message_location_sharing_update(self, count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageLocationSharingUpdateNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageLocationSharingUpdate')
		return self._stubs.messageNotificationStub.message_location_sharing_update(notifications.SubscribeToMessageLocationSharingUpdateNotification(count=count, message_ids=message_ids, filter=filter))
	
	def _notif_message_location_sharing_end(self, count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None) -> AsyncIterator[notifications.MessageLocationSharingEndNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageLocationSharingEnd')
		return self._stubs.messageNotificationStub.message_location_sharing_end(notifications.SubscribeToMessageLocationSharingEndNotification(count=count, message_ids=message_ids, filter=filter))
	
	def _notif_message_reaction_added(self, count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None, reaction_filter: datatypes.ReactionFilter = None) -> AsyncIterator[notifications.MessageReactionAddedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageReactionAdded')
		return self._stubs.messageNotificationStub.message_reaction_added(notifications.SubscribeToMessageReactionAddedNotification(count=count, message_ids=message_ids, filter=filter, reaction_filter=reaction_filter))
	
	def _notif_message_reaction_updated(self, count: int = 0, message_ids: list[datatypes.MessageId] = None, message_filter: datatypes.MessageFilter = None, reaction_filter: datatypes.ReactionFilter = None, previous_reaction_filter: datatypes.ReactionFilter = None) -> AsyncIterator[notifications.MessageReactionUpdatedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageReactionUpdated')
		return self._stubs.messageNotificationStub.message_reaction_updated(notifications.SubscribeToMessageReactionUpdatedNotification(count=count, message_ids=message_ids, message_filter=message_filter, reaction_filter=reaction_filter, previous_reaction_filter=previous_reaction_filter))
	
	def _notif_message_reaction_removed(self, count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None, reaction_filter: datatypes.ReactionFilter = None) -> AsyncIterator[notifications.MessageReactionRemovedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: MessageReactionRemoved')
		return self._stubs.messageNotificationStub.message_reaction_removed(notifications.SubscribeToMessageReactionRemovedNotification(count=count, message_ids=message_ids, filter=filter, reaction_filter=reaction_filter))
	
	# AttachmentNotificationService
	def _notif_attachment_received(self, count: int = 0, filter: datatypes.AttachmentFilter = None) -> AsyncIterator[notifications.AttachmentReceivedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: AttachmentReceived')
		return self._stubs.attachmentNotificationStub.attachment_received(notifications.SubscribeToAttachmentReceivedNotification(count=count, filter=filter))
	
	def _notif_attachment_uploaded(self, count: int = 0, filter: datatypes.AttachmentFilter = None, message_ids: list[datatypes.MessageId] = None, attachment_ids: list[datatypes.AttachmentId] = None) -> AsyncIterator[notifications.AttachmentUploadedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: AttachmentUploaded')
		return self._stubs.attachmentNotificationStub.attachment_uploaded(notifications.SubscribeToAttachmentUploadedNotification(count=count, filter=filter, message_ids=message_ids, attachment_ids=attachment_ids))
	
	# CallNotificationService
	def _notif_call_incoming_call(self, count: int = 0) -> AsyncIterator[notifications.CallIncomingCallNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: CallIncomingCall')
		return self._stubs.callNotificationStub.call_incoming_call(notifications.SubscribeToCallIncomingCallNotification(count=count))
	
	def _notif_call_ringing(self, count: int = 0) -> AsyncIterator[notifications.CallRingingNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: CallRinging')
		return self._stubs.callNotificationStub.call_ringing(notifications.SubscribeToCallRingingNotification(count=count))
	
	def _notif_call_accepted(self, count: int = 0) -> AsyncIterator[notifications.CallAcceptedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: CallAccepted')
		return self._stubs.callNotificationStub.call_accepted(notifications.SubscribeToCallAcceptedNotification(count=count))
	
	def _notif_call_declined(self, count: int = 0) -> AsyncIterator[notifications.CallDeclinedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: CallDeclined')
		return self._stubs.callNotificationStub.call_declined(notifications.SubscribeToCallDeclinedNotification(count=count))
	
	def _notif_call_busy(self, count: int = 0) -> AsyncIterator[notifications.CallBusyNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: CallBusy')
		return self._stubs.callNotificationStub.call_busy(notifications.SubscribeToCallBusyNotification(count=count))
	
	def _notif_call_ended(self, count: int = 0) -> AsyncIterator[notifications.CallEndedNotification]:
		notification_logger.debug(f'{self.__class__.__name__}: subscribed to: CallEnded')
		return self._stubs.callNotificationStub.call_ended(notifications.SubscribeToCallEndedNotification(count=count))

	# InvitationNotificationService
	async def on_invitation_received(self, invitation: datatypes.Invitation):
		pass

	async def on_invitation_sent(self, invitation: datatypes.Invitation):
		pass

	async def on_invitation_deleted(self, invitation: datatypes.Invitation):
		pass

	async def on_invitation_updated(self, invitation: datatypes.Invitation, previous_invitation_status: datatypes.Invitation.Status):
		pass

	# ContactNotificationService
	async def on_contact_new(self, contact: datatypes.Contact):
		pass

	async def on_contact_deleted(self, contact: datatypes.Contact):
		pass

	async def on_contact_details_updated(self, contact: datatypes.Contact, previous_details: datatypes.IdentityDetails):
		pass

	async def on_contact_photo_updated(self, contact: datatypes.Contact):
		pass

	# GroupNotificationService
	async def on_group_new(self, group: datatypes.Group):
		pass

	async def on_group_deleted(self, group: datatypes.Group):
		pass

	async def on_group_name_updated(self, group: datatypes.Group, previous_name: str):
		pass

	async def on_group_photo_updated(self, group: datatypes.Group):
		pass

	async def on_group_description_updated(self, group: datatypes.Group, previous_description: str):
		pass

	async def on_group_pending_member_added(self, group: datatypes.Group, pending_member: datatypes.PendingGroupMember):
		pass

	async def on_group_pending_member_removed(self, group: datatypes.Group, pending_member: datatypes.PendingGroupMember):
		pass

	async def on_group_member_joined(self, group: datatypes.Group, member: datatypes.GroupMember):
		pass

	async def on_group_member_left(self, group: datatypes.Group, member: datatypes.GroupMember):
		pass

	async def on_group_own_permissions_updated(self, group: datatypes.Group, permissions: datatypes.GroupMemberPermissions, previous_permissions: datatypes.GroupMemberPermissions):
		pass

	async def on_group_member_permissions_updated(self, group: datatypes.Group, member: datatypes.GroupMember, previous_permissions: datatypes.GroupMemberPermissions):
		pass

	# DiscussionNotificationService
	async def on_discussion_new(self, discussion: datatypes.Discussion):
		pass

	async def on_discussion_locked(self, discussion: datatypes.Discussion):
		pass

	async def on_discussion_title_updated(self, discussion: datatypes.Discussion, previous_title: str):
		pass

	async def on_discussion_settings_updated(self, discussion: datatypes.Discussion, new_settings: datatypes.DiscussionSettings, previous_settings: datatypes.DiscussionSettings):
		pass

	# MessageNotificationService
	async def on_message_received(self, message: datatypes.Message):
		pass

	async def on_message_sent(self, message: datatypes.Message):
		pass

	async def on_message_deleted(self, message: datatypes.Message):
		pass

	async def on_message_body_updated(self, message: datatypes.Message, previous_body: str):
		pass

	async def on_message_uploaded(self, message: datatypes.Message):
		pass

	async def on_message_delivered(self, message: datatypes.Message):
		pass

	async def on_message_read(self, message: datatypes.Message):
		pass

	async def on_message_location_received(self, message: datatypes.Message):
		pass

	async def on_message_location_sent(self, message: datatypes.Message):
		pass

	async def on_message_location_sharing_start(self, message: datatypes.Message):
		pass

	async def on_message_location_sharing_update(self, message: datatypes.Message, previous_location: datatypes.MessageLocation):
		pass

	async def on_message_location_sharing_end(self, message: datatypes.Message):
		pass

	async def on_message_reaction_added(self, message: datatypes.Message, reaction: datatypes.MessageReaction):
		pass

	async def on_message_reaction_updated(self, message: datatypes.Message, reaction: datatypes.MessageReaction, previous_reaction: datatypes.MessageReaction):
		pass

	async def on_message_reaction_removed(self, message: datatypes.Message, reaction: datatypes.MessageReaction):
		pass

	# AttachmentNotificationService
	async def on_attachment_received(self, attachment: datatypes.Attachment):
		pass

	async def on_attachment_uploaded(self, attachment: datatypes.Attachment):
		pass

	# CallNotificationService
	async def on_call_incoming_call(self, call_identifier: str, discussion_id: int, participant_id: datatypes.CallParticipantId, caller_display_name: str, participant_count: int):
		pass

	async def on_call_ringing(self, call_identifier: str, participant_id: datatypes.CallParticipantId):
		pass

	async def on_call_accepted(self, call_identifier: str, participant_id: datatypes.CallParticipantId):
		pass

	async def on_call_declined(self, call_identifier: str, participant_id: datatypes.CallParticipantId):
		pass

	async def on_call_busy(self, call_identifier: str, participant_id: datatypes.CallParticipantId):
		pass

	async def on_call_ended(self, call_identifier: str):
		pass
