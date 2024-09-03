from __future__ import annotations  # this block is necessary for compilation
from typing import Optional, Callable, Any

from grpc import Channel

from ..internal import commands, notifications, admin

from typing import TYPE_CHECKING  # this block is necessary for compilation
if TYPE_CHECKING:  # this block is necessary for compilation
	from .OlvidClient import OlvidClient


class StubHolder:
	def __init__(self, client: "OlvidClient", channel: Channel, parent: Optional[OlvidClient] = None):
		self._client: OlvidClient = client
		self._parent: Optional[OlvidClient] = parent
		self._channel: Channel = channel

		# create command stubs
		self.identityCommandStub: commands.IdentityCommandServiceStub = self._get_or_create_stub(
			"identityCommandStub", commands.IdentityCommandServiceStub)
		self.invitationCommandStub: commands.InvitationCommandServiceStub = self._get_or_create_stub(
			"invitationCommandStub", commands.InvitationCommandServiceStub)
		self.contactCommandStub: commands.ContactCommandServiceStub = self._get_or_create_stub("contactCommandStub",
																								commands.ContactCommandServiceStub)
		self.groupCommandStub: commands.GroupCommandServiceStub = self._get_or_create_stub("groupCommandStub",
																							commands.GroupCommandServiceStub)
		self.discussionCommandStub: commands.DiscussionCommandServiceStub = self._get_or_create_stub(
			"discussionCommandStub", commands.DiscussionCommandServiceStub)
		self.messageCommandStub: commands.MessageCommandServiceStub = self._get_or_create_stub("messageCommandStub",
																								commands.MessageCommandServiceStub)
		self.attachmentCommandStub: commands.AttachmentCommandServiceStub = self._get_or_create_stub(
			"attachmentCommandStub", commands.AttachmentCommandServiceStub)
		self.storageCommandStub: commands.StorageCommandServiceStub = self._get_or_create_stub("storageCommandStub",
																								commands.StorageCommandServiceStub)
		self.discussionStorageCommandStub: commands.DiscussionStorageCommandServiceStub = self._get_or_create_stub(
			"discussionStorageCommandStub", commands.DiscussionStorageCommandServiceStub)

		# create notification stubs
		self.invitationNotificationStub: notifications.InvitationNotificationServiceStub = self._get_or_create_stub(
			"invitationNotificationStub", notifications.InvitationNotificationServiceStub)
		self.contactNotificationStub: notifications.ContactNotificationServiceStub = self._get_or_create_stub(
			"contactNotificationStub", notifications.ContactNotificationServiceStub)
		self.groupNotificationStub: notifications.GroupNotificationServiceStub = self._get_or_create_stub(
			"groupNotificationStub", notifications.GroupNotificationServiceStub)
		self.discussionNotificationStub: notifications.DiscussionNotificationServiceStub = self._get_or_create_stub(
			"discussionNotificationStub", notifications.DiscussionNotificationServiceStub)
		self.messageNotificationStub: notifications.MessageNotificationServiceStub = self._get_or_create_stub(
			"messageNotificationStub", notifications.MessageNotificationServiceStub)
		self.attachmentNotificationStub: notifications.AttachmentNotificationServiceStub = self._get_or_create_stub(
			"attachmentNotificationStub", notifications.AttachmentNotificationServiceStub)

		# do not create admin stubs
		self.clientKeyAdminStub: Optional[admin.ClientKeyAdminServiceStub] = None
		self.identityAdminStub: Optional[admin.IdentityAdminServiceStub] = None

	def create_admin_stubs(self):
		self.clientKeyAdminStub: admin.ClientKeyAdminServiceStub = self._get_or_create_stub("clientKeyAdminStub", admin.ClientKeyAdminServiceStub)
		self.identityAdminStub: admin.IdentityAdminServiceStub = self._get_or_create_stub("identityAdminStub", admin.IdentityAdminServiceStub)

	def _get_or_create_stub(self, attribute_name: str, stub_factory: Callable[["OlvidClient", Channel], Any]):
		if not self._parent:
			return stub_factory(self._client, self._channel)
		if not hasattr(self._parent._stubs, attribute_name):
			return stub_factory(self._client, self._channel)
		return getattr(self._parent._stubs, attribute_name)
