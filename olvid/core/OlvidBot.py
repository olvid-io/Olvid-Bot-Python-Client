from typing import Optional

from .OlvidClient import OlvidClient
from .. import datatypes
from ..listeners.Command import Command, CommandHolder
from ..listeners.GenericNotificationListener import GenericNotificationListener
from ..listeners.Notifications import NOTIFICATIONS
from ..listeners import ListenersImplementation as listeners


class OlvidBot(OlvidClient, CommandHolder):
	"""
	OlvidBot: OlvidClient extended to add notification handlers.

	As OlvidBot extends OlvidClient it has the same constraints, for example it needs to find a valid client_key to
	connect to a daemon (see OlvidClient for more information).

	OlvidBot implements a set of method named on_something. There is one method for each gRPC notification method.
	On instantiation overwritten methods will automatically be subscribed as notification listener.
	For example:
	```
	class Bot(OlvidBot)
		async def on_message_received(self, message: datatypes.Message):
			print(message)
	```
	Every time Bot class is instantiated it will add a listener to message_received notification with the method as handler.

	OlvidBot can also add Command objects with add_command method. Command are specific listeners.
	They subclass listeners.MessageReceivedListener, and they are created with a regexp filter that will filter notifications.
	Only messages that match the regexp will raise a notification.
	Commands can be added using OlvidBot.command decorator:
	For example:
	```
	class Bot(OlvidBot)
		OlvidBot.command(regexp_filter="^!help")
		async def on_message_received(self, message: datatypes.Message):
			await message.reply("Help message")
	```
	"""
	def __init__(self, bot_name: str = None, client_key: Optional[str] = None, server_target: Optional[str] = None,
				parent_client: Optional['OlvidClient'] = None):
		OlvidClient.__init__(self, client_key=client_key, server_target=server_target, parent_client=parent_client)
		CommandHolder.__init__(self)
		self._name = bot_name if bot_name is not None else self.__class__.__name__

		# add NotificationListener overwritten methods to listeners
		listeners_to_add = self._get_listeners_to_add()
		for listener in listeners_to_add:
			self.add_listener(listener)

	# read only properties
	@property
	def name(self) -> str:
		return self._name

	#####
	# CommandHolder interface implementation
	#####
	def add_command(self, command: Command):
		self.add_listener(command)

	def remove_command(self, command: Command):
		self.remove_listener(command)

	def is_message_body_a_valid_command(self, body: str) -> bool:
		return any([isinstance(listener, Command) and listener.match_str(body) for listener in self._listeners_set])

	#####
	# Common methods
	#####
	def __str__(self) -> str:
		current_listeners = [f"{listener.listener_key}: (finished: {listener.is_finished})" for listener in self._listeners_set]
		return f"{self.name}: {', '.join(current_listeners)}"

	#####
	# tools
	#####
	def print(self, *args, **kwargs):
		print(f"{self._name}:", *args, **kwargs)

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
		# if listener method is different from original OlvidBot method, return it
		if getattr(type(self), method_name) != getattr(OlvidBot, method_name, None):
			return True
		# listener was not overwritten
		return False

	#####
	# Notification handlers: override any of this method to easily add a handler for any type of notification
	#####

	####################################################################################################################
	##### WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_olvid_client_code.py
	####################################################################################################################
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

	# GroupNotificationService
	async def on_group_new(self, group: datatypes.Group):
		pass

	async def on_group_deleted(self, group: datatypes.Group):
		pass

	async def on_group_name_updated(self, group: datatypes.Group, previous_name: str):
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

	async def on_group_update_in_progress(self, group_id: int):
		pass

	async def on_group_update_finished(self, group_id: int):
		pass

	# DiscussionNotificationService
	async def on_discussion_new(self, discussion: datatypes.Discussion):
		pass

	async def on_discussion_locked(self, discussion: datatypes.Discussion):
		pass

	async def on_discussion_title_updated(self, discussion: datatypes.Discussion, previous_title: str):
		pass

	async def on_discussion_settings_updated(self, new_settings: datatypes.DiscussionSettings, previous_settings: datatypes.DiscussionSettings):
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
