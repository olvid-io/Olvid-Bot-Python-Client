####
# WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_listeners_module.py
####

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .. import datatypes
	from typing import Optional, Callable, Coroutine, Any, Union

from ..listeners.GenericNotificationListener import GenericNotificationListener
from .Notifications import NOTIFICATIONS


# InvitationNotificationService
# noinspection DuplicatedCode
class InvitationReceivedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Invitation], Optional[Coroutine]], checkers: list[Callable[[datatypes.Invitation], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.InvitationFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.invitation) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.INVITATION_RECEIVED,
			handler=lambda n: handler(n.invitation),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Invitation], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.invitation))


# noinspection DuplicatedCode
class InvitationSentListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Invitation], Optional[Coroutine]], checkers: list[Callable[[datatypes.Invitation], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.InvitationFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.invitation) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.INVITATION_SENT,
			handler=lambda n: handler(n.invitation),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Invitation], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.invitation))


# noinspection DuplicatedCode
class InvitationDeletedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Invitation], Optional[Coroutine]], checkers: list[Callable[[datatypes.Invitation], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.InvitationFilter = None, invitation_ids: list[int] = ()):
		if checkers:
			checkers = [lambda n: checker(n.invitation) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.INVITATION_DELETED,
			handler=lambda n: handler(n.invitation),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter, "invitation_ids": invitation_ids}
	
	def add_checker(self, checker: Callable[[datatypes.Invitation], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.invitation))


# noinspection DuplicatedCode
class InvitationUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Invitation, datatypes.Invitation.Status], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Invitation, datatypes.Invitation.Status], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.InvitationFilter = None, invitation_ids: list[int] = ()):
		if checkers:
			checkers = [lambda n: checker(n.invitation, n.previous_invitation_status) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.INVITATION_UPDATED,
			handler=lambda n: handler(n.invitation, n.previous_invitation_status),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter, "invitation_ids": invitation_ids}

	def add_checker(self, checker: Callable[[datatypes.Invitation, datatypes.Invitation.Status], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.invitation, n.previous_invitation_status))


# ContactNotificationService
# noinspection DuplicatedCode
class ContactNewListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Contact], Optional[Coroutine]], checkers: list[Callable[[datatypes.Contact], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.ContactFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.contact) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.CONTACT_NEW,
			handler=lambda n: handler(n.contact),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Contact], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.contact))


# noinspection DuplicatedCode
class ContactDeletedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Contact], Optional[Coroutine]], checkers: list[Callable[[datatypes.Contact], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.ContactFilter = None, contact_ids: list[int] = ()):
		if checkers:
			checkers = [lambda n: checker(n.contact) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.CONTACT_DELETED,
			handler=lambda n: handler(n.contact),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter, "contact_ids": contact_ids}
	
	def add_checker(self, checker: Callable[[datatypes.Contact], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.contact))


# noinspection DuplicatedCode
class ContactDetailsUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Contact, datatypes.IdentityDetails], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Contact, datatypes.IdentityDetails], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.ContactFilter = None, contact_ids: list[int] = ()):
		if checkers:
			checkers = [lambda n: checker(n.contact, n.previous_details) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.CONTACT_DETAILS_UPDATED,
			handler=lambda n: handler(n.contact, n.previous_details),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter, "contact_ids": contact_ids}

	def add_checker(self, checker: Callable[[datatypes.Contact, datatypes.IdentityDetails], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.contact, n.previous_details))


# noinspection DuplicatedCode
class ContactPhotoUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Contact], Optional[Coroutine]], checkers: list[Callable[[datatypes.Contact], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.ContactFilter = None, contact_ids: list[int] = ()):
		if checkers:
			checkers = [lambda n: checker(n.contact) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.CONTACT_PHOTO_UPDATED,
			handler=lambda n: handler(n.contact),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter, "contact_ids": contact_ids}
	
	def add_checker(self, checker: Callable[[datatypes.Contact], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.contact))


# GroupNotificationService
# noinspection DuplicatedCode
class GroupNewListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group], Optional[Coroutine]], checkers: list[Callable[[datatypes.Group], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_filter: datatypes.GroupFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.group) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_NEW,
			handler=lambda n: handler(n.group),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_filter": group_filter}
	
	def add_checker(self, checker: Callable[[datatypes.Group], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group))


# noinspection DuplicatedCode
class GroupDeletedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group], Optional[Coroutine]], checkers: list[Callable[[datatypes.Group], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.group) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_DELETED,
			handler=lambda n: handler(n.group),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids, "group_filter": group_filter}
	
	def add_checker(self, checker: Callable[[datatypes.Group], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group))


# noinspection DuplicatedCode
class GroupNameUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, str], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Group, str], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, previous_name_search: str = ""):
		if checkers:
			checkers = [lambda n: checker(n.group, n.previous_name) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_NAME_UPDATED,
			handler=lambda n: handler(n.group, n.previous_name),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids, "group_filter": group_filter, "previous_name_search": previous_name_search}

	def add_checker(self, checker: Callable[[datatypes.Group, str], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group, n.previous_name))


# noinspection DuplicatedCode
class GroupPhotoUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group], Optional[Coroutine]], checkers: list[Callable[[datatypes.Group], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.group) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_PHOTO_UPDATED,
			handler=lambda n: handler(n.group),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids, "group_filter": group_filter}
	
	def add_checker(self, checker: Callable[[datatypes.Group], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group))


# noinspection DuplicatedCode
class GroupDescriptionUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, str], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Group, str], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, previous_description_search: str = ""):
		if checkers:
			checkers = [lambda n: checker(n.group, n.previous_description) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_DESCRIPTION_UPDATED,
			handler=lambda n: handler(n.group, n.previous_description),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids, "group_filter": group_filter, "previous_description_search": previous_description_search}

	def add_checker(self, checker: Callable[[datatypes.Group, str], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group, n.previous_description))


# noinspection DuplicatedCode
class GroupPendingMemberAddedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.PendingGroupMember], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Group, datatypes.PendingGroupMember], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, pending_member_filter: datatypes.PendingGroupMemberFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.group, n.pending_member) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_PENDING_MEMBER_ADDED,
			handler=lambda n: handler(n.group, n.pending_member),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids, "group_filter": group_filter, "pending_member_filter": pending_member_filter}

	def add_checker(self, checker: Callable[[datatypes.Group, datatypes.PendingGroupMember], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group, n.pending_member))


# noinspection DuplicatedCode
class GroupPendingMemberRemovedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.PendingGroupMember], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Group, datatypes.PendingGroupMember], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, pending_member_filter: datatypes.PendingGroupMemberFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.group, n.pending_member) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_PENDING_MEMBER_REMOVED,
			handler=lambda n: handler(n.group, n.pending_member),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids, "group_filter": group_filter, "pending_member_filter": pending_member_filter}

	def add_checker(self, checker: Callable[[datatypes.Group, datatypes.PendingGroupMember], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group, n.pending_member))


# noinspection DuplicatedCode
class GroupMemberJoinedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.GroupMember], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Group, datatypes.GroupMember], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, member_filter: datatypes.GroupMemberFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.group, n.member) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_MEMBER_JOINED,
			handler=lambda n: handler(n.group, n.member),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids, "group_filter": group_filter, "member_filter": member_filter}

	def add_checker(self, checker: Callable[[datatypes.Group, datatypes.GroupMember], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group, n.member))


# noinspection DuplicatedCode
class GroupMemberLeftListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.GroupMember], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Group, datatypes.GroupMember], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, member_filter: datatypes.GroupMemberFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.group, n.member) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_MEMBER_LEFT,
			handler=lambda n: handler(n.group, n.member),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids, "group_filter": group_filter, "member_filter": member_filter}

	def add_checker(self, checker: Callable[[datatypes.Group, datatypes.GroupMember], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group, n.member))


# noinspection DuplicatedCode
class GroupOwnPermissionsUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.GroupMemberPermissions, datatypes.GroupMemberPermissions], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Group, datatypes.GroupMemberPermissions, datatypes.GroupMemberPermissions], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, permissions_filter: datatypes.GroupPermissionFilter = None, previous_permissions_filter: datatypes.GroupPermissionFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.group, n.permissions, n.previous_permissions) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_OWN_PERMISSIONS_UPDATED,
			handler=lambda n: handler(n.group, n.permissions, n.previous_permissions),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids, "group_filter": group_filter, "permissions_filter": permissions_filter, "previous_permissions_filter": previous_permissions_filter}

	def add_checker(self, checker: Callable[[datatypes.Group, datatypes.GroupMemberPermissions, datatypes.GroupMemberPermissions], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group, n.permissions, n.previous_permissions))


# noinspection DuplicatedCode
class GroupMemberPermissionsUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Group, datatypes.GroupMember, datatypes.GroupMemberPermissions], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Group, datatypes.GroupMember, datatypes.GroupMemberPermissions], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = (), group_filter: datatypes.GroupFilter = None, member_filter: datatypes.GroupMemberFilter = None, previous_permission_filter: datatypes.GroupMemberFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.group, n.member, n.previous_permissions) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_MEMBER_PERMISSIONS_UPDATED,
			handler=lambda n: handler(n.group, n.member, n.previous_permissions),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids, "group_filter": group_filter, "member_filter": member_filter, "previous_permission_filter": previous_permission_filter}

	def add_checker(self, checker: Callable[[datatypes.Group, datatypes.GroupMember, datatypes.GroupMemberPermissions], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group, n.member, n.previous_permissions))


# noinspection DuplicatedCode
class GroupUpdateInProgressListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[int], Optional[Coroutine]], checkers: list[Callable[[int], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = ()):
		if checkers:
			checkers = [lambda n: checker(n.group_id) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_UPDATE_IN_PROGRESS,
			handler=lambda n: handler(n.group_id),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids}
	
	def add_checker(self, checker: Callable[[int], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group_id))


# noinspection DuplicatedCode
class GroupUpdateFinishedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[int], Optional[Coroutine]], checkers: list[Callable[[int], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, group_ids: list[int] = ()):
		if checkers:
			checkers = [lambda n: checker(n.group_id) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.GROUP_UPDATE_FINISHED,
			handler=lambda n: handler(n.group_id),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "group_ids": group_ids}
	
	def add_checker(self, checker: Callable[[int], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.group_id))


# DiscussionNotificationService
# noinspection DuplicatedCode
class DiscussionNewListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Discussion], Optional[Coroutine]], checkers: list[Callable[[datatypes.Discussion], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.DiscussionFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.discussion) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.DISCUSSION_NEW,
			handler=lambda n: handler(n.discussion),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Discussion], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.discussion))


# noinspection DuplicatedCode
class DiscussionLockedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Discussion], Optional[Coroutine]], checkers: list[Callable[[datatypes.Discussion], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.DiscussionFilter = None, discussion_ids: list[int] = ()):
		if checkers:
			checkers = [lambda n: checker(n.discussion) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.DISCUSSION_LOCKED,
			handler=lambda n: handler(n.discussion),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter, "discussion_ids": discussion_ids}
	
	def add_checker(self, checker: Callable[[datatypes.Discussion], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.discussion))


# noinspection DuplicatedCode
class DiscussionTitleUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Discussion, str], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Discussion, str], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.DiscussionFilter = None, discussion_ids: list[int] = ()):
		if checkers:
			checkers = [lambda n: checker(n.discussion, n.previous_title) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.DISCUSSION_TITLE_UPDATED,
			handler=lambda n: handler(n.discussion, n.previous_title),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter, "discussion_ids": discussion_ids}

	def add_checker(self, checker: Callable[[datatypes.Discussion, str], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.discussion, n.previous_title))


# noinspection DuplicatedCode
class DiscussionSettingsUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Discussion, datatypes.DiscussionSettings, datatypes.DiscussionSettings], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Discussion, datatypes.DiscussionSettings, datatypes.DiscussionSettings], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.DiscussionFilter = None, discussion_ids: list[int] = ()):
		if checkers:
			checkers = [lambda n: checker(n.discussion, n.new_settings, n.previous_settings) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.DISCUSSION_SETTINGS_UPDATED,
			handler=lambda n: handler(n.discussion, n.new_settings, n.previous_settings),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter, "discussion_ids": discussion_ids}

	def add_checker(self, checker: Callable[[datatypes.Discussion, datatypes.DiscussionSettings, datatypes.DiscussionSettings], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.discussion, n.new_settings, n.previous_settings))


# MessageNotificationService
# noinspection DuplicatedCode
class MessageReceivedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], checkers: list[Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_RECEIVED,
			handler=lambda n: handler(n.message),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message))


# noinspection DuplicatedCode
class MessageSentListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], checkers: list[Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_SENT,
			handler=lambda n: handler(n.message),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message))


# noinspection DuplicatedCode
class MessageDeletedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], checkers: list[Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_DELETED,
			handler=lambda n: handler(n.message),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "message_ids": message_ids, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message))


# noinspection DuplicatedCode
class MessageBodyUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message, str], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Message, str], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message, n.previous_body) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_BODY_UPDATED,
			handler=lambda n: handler(n.message, n.previous_body),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "message_ids": message_ids, "filter": filter}

	def add_checker(self, checker: Callable[[datatypes.Message, str], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message, n.previous_body))


# noinspection DuplicatedCode
class MessageUploadedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], checkers: list[Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_UPLOADED,
			handler=lambda n: handler(n.message),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "message_ids": message_ids, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message))


# noinspection DuplicatedCode
class MessageDeliveredListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], checkers: list[Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_DELIVERED,
			handler=lambda n: handler(n.message),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "message_ids": message_ids, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message))


# noinspection DuplicatedCode
class MessageReadListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], checkers: list[Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_READ,
			handler=lambda n: handler(n.message),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "message_ids": message_ids, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message))


# noinspection DuplicatedCode
class MessageLocationReceivedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], checkers: list[Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_LOCATION_RECEIVED,
			handler=lambda n: handler(n.message),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message))


# noinspection DuplicatedCode
class MessageLocationSentListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], checkers: list[Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_LOCATION_SENT,
			handler=lambda n: handler(n.message),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message))


# noinspection DuplicatedCode
class MessageLocationSharingStartListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], checkers: list[Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_LOCATION_SHARING_START,
			handler=lambda n: handler(n.message),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message))


# noinspection DuplicatedCode
class MessageLocationSharingUpdateListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message, datatypes.MessageLocation], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Message, datatypes.MessageLocation], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message, n.previous_location) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_LOCATION_SHARING_UPDATE,
			handler=lambda n: handler(n.message, n.previous_location),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "message_ids": message_ids, "filter": filter}

	def add_checker(self, checker: Callable[[datatypes.Message, datatypes.MessageLocation], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message, n.previous_location))


# noinspection DuplicatedCode
class MessageLocationSharingEndListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message], Optional[Coroutine]], checkers: list[Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_LOCATION_SHARING_END,
			handler=lambda n: handler(n.message),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "message_ids": message_ids, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message))


# noinspection DuplicatedCode
class MessageReactionAddedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message, datatypes.MessageReaction], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Message, datatypes.MessageReaction], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None, reaction_filter: datatypes.ReactionFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message, n.reaction) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_REACTION_ADDED,
			handler=lambda n: handler(n.message, n.reaction),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "message_ids": message_ids, "filter": filter, "reaction_filter": reaction_filter}

	def add_checker(self, checker: Callable[[datatypes.Message, datatypes.MessageReaction], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message, n.reaction))


# noinspection DuplicatedCode
class MessageReactionUpdatedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message, datatypes.MessageReaction, datatypes.MessageReaction], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Message, datatypes.MessageReaction, datatypes.MessageReaction], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, message_ids: list[datatypes.MessageId] = None, message_filter: datatypes.MessageFilter = None, reaction_filter: datatypes.ReactionFilter = None, previous_reaction_filter: datatypes.ReactionFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message, n.reaction, n.previous_reaction) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_REACTION_UPDATED,
			handler=lambda n: handler(n.message, n.reaction, n.previous_reaction),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "message_ids": message_ids, "message_filter": message_filter, "reaction_filter": reaction_filter, "previous_reaction_filter": previous_reaction_filter}

	def add_checker(self, checker: Callable[[datatypes.Message, datatypes.MessageReaction, datatypes.MessageReaction], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message, n.reaction, n.previous_reaction))


# noinspection DuplicatedCode
class MessageReactionRemovedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Message, datatypes.MessageReaction], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[datatypes.Message, datatypes.MessageReaction], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, message_ids: list[datatypes.MessageId] = None, filter: datatypes.MessageFilter = None, reaction_filter: datatypes.ReactionFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.message, n.reaction) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.MESSAGE_REACTION_REMOVED,
			handler=lambda n: handler(n.message, n.reaction),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "message_ids": message_ids, "filter": filter, "reaction_filter": reaction_filter}

	def add_checker(self, checker: Callable[[datatypes.Message, datatypes.MessageReaction], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.message, n.reaction))


# AttachmentNotificationService
# noinspection DuplicatedCode
class AttachmentReceivedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Attachment], Optional[Coroutine]], checkers: list[Callable[[datatypes.Attachment], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.AttachmentFilter = None):
		if checkers:
			checkers = [lambda n: checker(n.attachment) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.ATTACHMENT_RECEIVED,
			handler=lambda n: handler(n.attachment),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter}
	
	def add_checker(self, checker: Callable[[datatypes.Attachment], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.attachment))


# noinspection DuplicatedCode
class AttachmentUploadedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[datatypes.Attachment], Optional[Coroutine]], checkers: list[Callable[[datatypes.Attachment], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0, filter: datatypes.AttachmentFilter = None, message_ids: list[datatypes.MessageId] = None, attachment_ids: list[datatypes.AttachmentId] = None):
		if checkers:
			checkers = [lambda n: checker(n.attachment) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.ATTACHMENT_UPLOADED,
			handler=lambda n: handler(n.attachment),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count, "filter": filter, "message_ids": message_ids, "attachment_ids": attachment_ids}
	
	def add_checker(self, checker: Callable[[datatypes.Attachment], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.attachment))


# CallNotificationService
# noinspection DuplicatedCode
class CallIncomingCallListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str, int, datatypes.CallParticipantId, str, int], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[str, int, datatypes.CallParticipantId, str, int], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0):
		if checkers:
			checkers = [lambda n: checker(n.call_identifier, n.discussion_id, n.participant_id, n.caller_display_name, n.participant_count) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_INCOMING_CALL,
			handler=lambda n: handler(n.call_identifier, n.discussion_id, n.participant_id, n.caller_display_name, n.participant_count),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count}

	def add_checker(self, checker: Callable[[str, int, datatypes.CallParticipantId, str, int], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.call_identifier, n.discussion_id, n.participant_id, n.caller_display_name, n.participant_count))


# noinspection DuplicatedCode
class CallRingingListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str, datatypes.CallParticipantId], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[str, datatypes.CallParticipantId], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0):
		if checkers:
			checkers = [lambda n: checker(n.call_identifier, n.participant_id) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_RINGING,
			handler=lambda n: handler(n.call_identifier, n.participant_id),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count}

	def add_checker(self, checker: Callable[[str, datatypes.CallParticipantId], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.call_identifier, n.participant_id))


# noinspection DuplicatedCode
class CallAcceptedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str, datatypes.CallParticipantId], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[str, datatypes.CallParticipantId], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0):
		if checkers:
			checkers = [lambda n: checker(n.call_identifier, n.participant_id) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_ACCEPTED,
			handler=lambda n: handler(n.call_identifier, n.participant_id),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count}

	def add_checker(self, checker: Callable[[str, datatypes.CallParticipantId], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.call_identifier, n.participant_id))


# noinspection DuplicatedCode
class CallDeclinedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str, datatypes.CallParticipantId], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[str, datatypes.CallParticipantId], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0):
		if checkers:
			checkers = [lambda n: checker(n.call_identifier, n.participant_id) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_DECLINED,
			handler=lambda n: handler(n.call_identifier, n.participant_id),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count}

	def add_checker(self, checker: Callable[[str, datatypes.CallParticipantId], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.call_identifier, n.participant_id))


# noinspection DuplicatedCode
class CallBusyListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str, datatypes.CallParticipantId], Optional[Coroutine[Any, Any, None]]], checkers: list[Callable[[str, datatypes.CallParticipantId], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0):
		if checkers:
			checkers = [lambda n: checker(n.call_identifier, n.participant_id) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_BUSY,
			handler=lambda n: handler(n.call_identifier, n.participant_id),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count}

	def add_checker(self, checker: Callable[[str, datatypes.CallParticipantId], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.call_identifier, n.participant_id))


# noinspection DuplicatedCode
class CallEndedListener(GenericNotificationListener):
	def __init__(self, handler: Callable[[str], Optional[Coroutine]], checkers: list[Callable[[str], Union[bool, Coroutine[Any, Any, bool]]]] = None, count: int = -1, priority: int = 0, filter_count: int = 0):
		if checkers:
			checkers = [lambda n: checker(n.call_identifier) for checker in checkers]
		super().__init__(
			notification_type=NOTIFICATIONS.CALL_ENDED,
			handler=lambda n: handler(n.call_identifier),
			checkers=checkers,
			count=-1 if count == 0 else count,
			priority=priority
		)
		self._iterator_args = {"count": filter_count}
	
	def add_checker(self, checker: Callable[[str], Union[bool, Coroutine[Any, Any, bool]]]):
		super().add_checker(lambda n: checker(n.call_identifier))


del annotations
del TYPE_CHECKING
