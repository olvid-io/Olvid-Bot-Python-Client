####
# WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_listeners_module.py
####

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .. import datatypes
	from typing import Optional, Callable, Coroutine, Any

from ..listeners.GenericNotificationListener import GenericNotificationListener
from .Notifications import NOTIFICATIONS


# InvitationNotificationService
# noinspection DuplicatedCode,PyShadowingBuiltins
class InvitationReceivedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Invitation], Optional[Coroutine]], count: int = 0, filter: datatypes.InvitationFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.INVITATION_RECEIVED,
			handler=lambda n: handler(n.invitation)
		)
		self._iterator_args = {"count": count, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class InvitationSentListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Invitation], Optional[Coroutine]], count: int = 0, filter: datatypes.InvitationFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.INVITATION_SENT,
			handler=lambda n: handler(n.invitation)
		)
		self._iterator_args = {"count": count, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class InvitationDeletedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Invitation], Optional[Coroutine]], count: int = 0, filter: datatypes.InvitationFilter = None, invitation_ids: list[int] = ()):
		super().__init__(
			notification_type=NOTIFICATIONS.INVITATION_DELETED,
			handler=lambda n: handler(n.invitation)
		)
		self._iterator_args = {"count": count, "filter": filter, "invitation_ids": invitation_ids}


# noinspection DuplicatedCode,PyShadowingBuiltins
class InvitationUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Invitation, datatypes.Invitation.Status], Optional[Coroutine[Any, Any, None]]], count: int = 0, filter: datatypes.InvitationFilter = None, invitation_ids: list[int] = ()):
		super().__init__(
			notification_type=NOTIFICATIONS.INVITATION_UPDATED,
			handler=lambda n: handler(n.invitation, n.previous_invitation_status)
		)
		self._iterator_args = {"count": count, "filter": filter, "invitation_ids": invitation_ids}


# ContactNotificationService
# noinspection DuplicatedCode,PyShadowingBuiltins
class ContactNewListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Contact], Optional[Coroutine]], count: int = 0, filter: datatypes.ContactFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.CONTACT_NEW,
			handler=lambda n: handler(n.contact)
		)
		self._iterator_args = {"count": count, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class ContactDeletedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Contact], Optional[Coroutine]], count: int = 0, filter: datatypes.ContactFilter = None, contact_ids: list[int] = ()):
		super().__init__(
			notification_type=NOTIFICATIONS.CONTACT_DELETED,
			handler=lambda n: handler(n.contact)
		)
		self._iterator_args = {"count": count, "filter": filter, "contact_ids": contact_ids}


# noinspection DuplicatedCode,PyShadowingBuiltins
class ContactDetailsUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Contact, datatypes.IdentityDetails], Optional[Coroutine[Any, Any, None]]], count: int = 0, filter: datatypes.ContactFilter = None, contact_ids: list[int] = ()):
		super().__init__(
			notification_type=NOTIFICATIONS.CONTACT_DETAILS_UPDATED,
			handler=lambda n: handler(n.contact, n.previous_details)
		)
		self._iterator_args = {"count": count, "filter": filter, "contact_ids": contact_ids}


# noinspection DuplicatedCode,PyShadowingBuiltins
class ContactPhotoUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Contact], Optional[Coroutine]], count: int = 0, filter: datatypes.ContactFilter = None, contact_ids: list[int] = ()):
		super().__init__(
			notification_type=NOTIFICATIONS.CONTACT_PHOTO_UPDATED,
			handler=lambda n: handler(n.contact)
		)
		self._iterator_args = {"count": count, "filter": filter, "contact_ids": contact_ids}


# GroupNotificationService
# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupNewListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group], Optional[Coroutine]], count: int = 0, group_filter: datatypes.GroupFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_NEW,
			handler=lambda n: handler(n.group)
		)
		self._iterator_args = {"count": count, "group_filter": group_filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupDeletedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group], Optional[Coroutine]], count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_DELETED,
			handler=lambda n: handler(n.group)
		)
		self._iterator_args = {"count": count, "group_ids": group_ids, "group_filter": group_filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupNameUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, str], Optional[Coroutine[Any, Any, None]]], count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, previous_name_search: str = ""):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_NAME_UPDATED,
			handler=lambda n: handler(n.group, n.previous_name)
		)
		self._iterator_args = {"count": count, "group_ids": group_ids, "group_filter": group_filter, "previous_name_search": previous_name_search}


# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupPhotoUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group], Optional[Coroutine]], count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_PHOTO_UPDATED,
			handler=lambda n: handler(n.group)
		)
		self._iterator_args = {"count": count, "group_ids": group_ids, "group_filter": group_filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupDescriptionUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, str], Optional[Coroutine[Any, Any, None]]], count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, previous_description_search: str = ""):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_DESCRIPTION_UPDATED,
			handler=lambda n: handler(n.group, n.previous_description)
		)
		self._iterator_args = {"count": count, "group_ids": group_ids, "group_filter": group_filter, "previous_description_search": previous_description_search}


# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupPendingMemberAddedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.PendingGroupMember], Optional[Coroutine[Any, Any, None]]], count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, pending_member_filter: datatypes.PendingGroupMemberFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_PENDING_MEMBER_ADDED,
			handler=lambda n: handler(n.group, n.pending_member)
		)
		self._iterator_args = {"count": count, "group_ids": group_ids, "group_filter": group_filter, "pending_member_filter": pending_member_filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupPendingMemberRemovedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.PendingGroupMember], Optional[Coroutine[Any, Any, None]]], count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, pending_member_filter: datatypes.PendingGroupMemberFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_PENDING_MEMBER_REMOVED,
			handler=lambda n: handler(n.group, n.pending_member)
		)
		self._iterator_args = {"count": count, "group_ids": group_ids, "group_filter": group_filter, "pending_member_filter": pending_member_filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupMemberJoinedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.GroupMember], Optional[Coroutine[Any, Any, None]]], count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, member_filter: datatypes.GroupMemberFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_MEMBER_JOINED,
			handler=lambda n: handler(n.group, n.member)
		)
		self._iterator_args = {"count": count, "group_ids": group_ids, "group_filter": group_filter, "member_filter": member_filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupMemberLeftListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.GroupMember], Optional[Coroutine[Any, Any, None]]], count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, member_filter: datatypes.GroupMemberFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_MEMBER_LEFT,
			handler=lambda n: handler(n.group, n.member)
		)
		self._iterator_args = {"count": count, "group_ids": group_ids, "group_filter": group_filter, "member_filter": member_filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupOwnPermissionsUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.GroupMemberPermissions, datatypes.GroupMemberPermissions], Optional[Coroutine[Any, Any, None]]], count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, permissions_filter: datatypes.GroupPermissionFilter = None, previous_permissions_filter: datatypes.GroupPermissionFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_OWN_PERMISSIONS_UPDATED,
			handler=lambda n: handler(n.group, n.permissions, n.previous_permissions)
		)
		self._iterator_args = {"count": count, "group_ids": group_ids, "group_filter": group_filter, "permissions_filter": permissions_filter, "previous_permissions_filter": previous_permissions_filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class GroupMemberPermissionsUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.GroupMember, datatypes.GroupMemberPermissions], Optional[Coroutine[Any, Any, None]]], count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, member_filter: datatypes.GroupMemberFilter = None, previous_permission_filter: datatypes.GroupMemberFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_MEMBER_PERMISSIONS_UPDATED,
			handler=lambda n: handler(n.group, n.member, n.previous_permissions)
		)
		self._iterator_args = {"count": count, "group_ids": group_ids, "group_filter": group_filter, "member_filter": member_filter, "previous_permission_filter": previous_permission_filter}


# DiscussionNotificationService
# noinspection DuplicatedCode,PyShadowingBuiltins
class DiscussionNewListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Discussion], Optional[Coroutine]], count: int = 0, filter: datatypes.DiscussionFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.DISCUSSION_NEW,
			handler=lambda n: handler(n.discussion)
		)
		self._iterator_args = {"count": count, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class DiscussionLockedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Discussion], Optional[Coroutine]], count: int = 0, filter: datatypes.DiscussionFilter = None, discussion_ids: list[int] = ()):
		super().__init__(
			notification_type=NOTIFICATIONS.DISCUSSION_LOCKED,
			handler=lambda n: handler(n.discussion)
		)
		self._iterator_args = {"count": count, "filter": filter, "discussion_ids": discussion_ids}


# noinspection DuplicatedCode,PyShadowingBuiltins
class DiscussionTitleUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Discussion, str], Optional[Coroutine[Any, Any, None]]], count: int = 0, filter: datatypes.DiscussionFilter = None, discussion_ids: list[int] = ()):
		super().__init__(
			notification_type=NOTIFICATIONS.DISCUSSION_TITLE_UPDATED,
			handler=lambda n: handler(n.discussion, n.previous_title)
		)
		self._iterator_args = {"count": count, "filter": filter, "discussion_ids": discussion_ids}


# noinspection DuplicatedCode,PyShadowingBuiltins
class DiscussionSettingsUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Discussion, datatypes.DiscussionSettings, datatypes.DiscussionSettings], Optional[Coroutine[Any, Any, None]]], count: int = 0, filter: datatypes.DiscussionFilter = None, discussion_ids: list[int] = ()):
		super().__init__(
			notification_type=NOTIFICATIONS.DISCUSSION_SETTINGS_UPDATED,
			handler=lambda n: handler(n.discussion, n.new_settings, n.previous_settings)
		)
		self._iterator_args = {"count": count, "filter": filter, "discussion_ids": discussion_ids}


# MessageNotificationService
# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageReceivedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], count: int = 0, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_RECEIVED,
			handler=lambda n: handler(n.message)
		)
		self._iterator_args = {"count": count, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageSentListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], count: int = 0, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_SENT,
			handler=lambda n: handler(n.message)
		)
		self._iterator_args = {"count": count, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageDeletedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_DELETED,
			handler=lambda n: handler(n.message)
		)
		self._iterator_args = {"count": count, "message_ids": message_ids, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageBodyUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message, str], Optional[Coroutine[Any, Any, None]]], count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_BODY_UPDATED,
			handler=lambda n: handler(n.message, n.previous_body)
		)
		self._iterator_args = {"count": count, "message_ids": message_ids, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageUploadedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_UPLOADED,
			handler=lambda n: handler(n.message)
		)
		self._iterator_args = {"count": count, "message_ids": message_ids, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageDeliveredListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_DELIVERED,
			handler=lambda n: handler(n.message)
		)
		self._iterator_args = {"count": count, "message_ids": message_ids, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageReadListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_READ,
			handler=lambda n: handler(n.message)
		)
		self._iterator_args = {"count": count, "message_ids": message_ids, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageLocationReceivedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], count: int = 0, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_LOCATION_RECEIVED,
			handler=lambda n: handler(n.message)
		)
		self._iterator_args = {"count": count, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageLocationSentListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], count: int = 0, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_LOCATION_SENT,
			handler=lambda n: handler(n.message)
		)
		self._iterator_args = {"count": count, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageLocationSharingStartListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], count: int = 0, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_LOCATION_SHARING_START,
			handler=lambda n: handler(n.message)
		)
		self._iterator_args = {"count": count, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageLocationSharingUpdateListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message, datatypes.MessageLocation], Optional[Coroutine[Any, Any, None]]], count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_LOCATION_SHARING_UPDATE,
			handler=lambda n: handler(n.message, n.previous_location)
		)
		self._iterator_args = {"count": count, "message_ids": message_ids, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageLocationSharingEndListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_LOCATION_SHARING_END,
			handler=lambda n: handler(n.message)
		)
		self._iterator_args = {"count": count, "message_ids": message_ids, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageReactionAddedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message, datatypes.MessageReaction], Optional[Coroutine[Any, Any, None]]], count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None, reaction_filter: datatypes.ReactionFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_REACTION_ADDED,
			handler=lambda n: handler(n.message, n.reaction)
		)
		self._iterator_args = {"count": count, "message_ids": message_ids, "filter": filter, "reaction_filter": reaction_filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageReactionUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message, datatypes.MessageReaction, datatypes.MessageReaction], Optional[Coroutine[Any, Any, None]]], count: int = 0, message_ids: list[datatypes.MessageId] = None, message_filter: datatypes.MessageFilter = None, reaction_filter: datatypes.ReactionFilter = None, previous_reaction_filter: datatypes.ReactionFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_REACTION_UPDATED,
			handler=lambda n: handler(n.message, n.reaction, n.previous_reaction)
		)
		self._iterator_args = {"count": count, "message_ids": message_ids, "message_filter": message_filter, "reaction_filter": reaction_filter, "previous_reaction_filter": previous_reaction_filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class MessageReactionRemovedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message, datatypes.MessageReaction], Optional[Coroutine[Any, Any, None]]], count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None, reaction_filter: datatypes.ReactionFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_REACTION_REMOVED,
			handler=lambda n: handler(n.message, n.reaction)
		)
		self._iterator_args = {"count": count, "message_ids": message_ids, "filter": filter, "reaction_filter": reaction_filter}


# AttachmentNotificationService
# noinspection DuplicatedCode,PyShadowingBuiltins
class AttachmentReceivedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Attachment], Optional[Coroutine]], count: int = 0, filter: datatypes.AttachmentFilter = None):
		super().__init__(
			notification_type=NOTIFICATIONS.ATTACHMENT_RECEIVED,
			handler=lambda n: handler(n.attachment)
		)
		self._iterator_args = {"count": count, "filter": filter}


# noinspection DuplicatedCode,PyShadowingBuiltins
class AttachmentUploadedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Attachment], Optional[Coroutine]], count: int = 0, filter: datatypes.AttachmentFilter = None, message_ids: list[datatypes.MessageId] = None, attachment_ids: list[datatypes.AttachmentId] = None):
		super().__init__(
			notification_type=NOTIFICATIONS.ATTACHMENT_UPLOADED,
			handler=lambda n: handler(n.attachment)
		)
		self._iterator_args = {"count": count, "filter": filter, "message_ids": message_ids, "attachment_ids": attachment_ids}


# CallNotificationService
# noinspection DuplicatedCode,PyShadowingBuiltins
class CallIncomingCallListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str, int, datatypes.CallParticipantId, str, int], Optional[Coroutine[Any, Any, None]]], count: int = 0):
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_INCOMING_CALL,
			handler=lambda n: handler(n.call_identifier, n.discussion_id, n.participant_id, n.caller_display_name, n.participant_count)
		)
		self._iterator_args = {"count": count}


# noinspection DuplicatedCode,PyShadowingBuiltins
class CallRingingListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str, datatypes.CallParticipantId], Optional[Coroutine[Any, Any, None]]], count: int = 0):
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_RINGING,
			handler=lambda n: handler(n.call_identifier, n.participant_id)
		)
		self._iterator_args = {"count": count}


# noinspection DuplicatedCode,PyShadowingBuiltins
class CallAcceptedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str, datatypes.CallParticipantId], Optional[Coroutine[Any, Any, None]]], count: int = 0):
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_ACCEPTED,
			handler=lambda n: handler(n.call_identifier, n.participant_id)
		)
		self._iterator_args = {"count": count}


# noinspection DuplicatedCode,PyShadowingBuiltins
class CallDeclinedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str, datatypes.CallParticipantId], Optional[Coroutine[Any, Any, None]]], count: int = 0):
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_DECLINED,
			handler=lambda n: handler(n.call_identifier, n.participant_id)
		)
		self._iterator_args = {"count": count}


# noinspection DuplicatedCode,PyShadowingBuiltins
class CallBusyListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str, datatypes.CallParticipantId], Optional[Coroutine[Any, Any, None]]], count: int = 0):
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_BUSY,
			handler=lambda n: handler(n.call_identifier, n.participant_id)
		)
		self._iterator_args = {"count": count}


# noinspection DuplicatedCode,PyShadowingBuiltins
class CallEndedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str], Optional[Coroutine]], count: int = 0):
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_ENDED,
			handler=lambda n: handler(n.call_identifier)
		)
		self._iterator_args = {"count": count}


del annotations
del TYPE_CHECKING
