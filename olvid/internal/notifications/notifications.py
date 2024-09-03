####
# WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_protobuf_overlay
####

from __future__ import annotations  # this block is necessary for compilation
from typing import TYPE_CHECKING  # this block is necessary for compilation
if TYPE_CHECKING:  # this block is necessary for compilation
	from ...core.OlvidClient import OlvidClient  # this block is necessary for compilation
import grpc
from typing import Coroutine, Any, AsyncIterator
from ...protobuf import olvid

from ...datatypes import *


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToAttachmentReceivedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_attachment_received_notification: SubscribeToAttachmentReceivedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToAttachmentReceivedNotification":
		return SubscribeToAttachmentReceivedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.attachment_notifications_pb2.SubscribeToAttachmentReceivedNotification, client: OlvidClient = None) -> "SubscribeToAttachmentReceivedNotification":
		return SubscribeToAttachmentReceivedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.attachment_notifications_pb2.SubscribeToAttachmentReceivedNotification], client: OlvidClient = None) -> list["SubscribeToAttachmentReceivedNotification"]:
		return [SubscribeToAttachmentReceivedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.attachment_notifications_pb2.SubscribeToAttachmentReceivedNotification], client: OlvidClient = None) -> "SubscribeToAttachmentReceivedNotification":
		native_message = await promise
		return SubscribeToAttachmentReceivedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToAttachmentReceivedNotification"]):
		if messages is None:
			return []
		return [SubscribeToAttachmentReceivedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToAttachmentReceivedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.attachment_notifications_pb2.SubscribeToAttachmentReceivedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToAttachmentReceivedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToAttachmentReceivedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentReceivedNotification:
	def __init__(self, client: OlvidClient = None, attachment: "Attachment" = None):
		self._client: OlvidClient = client
		self.attachment: Attachment = attachment

	def _update_content(self, attachment_received_notification: AttachmentReceivedNotification) -> None:
		self.attachment: Attachment = attachment_received_notification.attachment

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentReceivedNotification":
		return AttachmentReceivedNotification(client=self._client, attachment=self.attachment._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.attachment_notifications_pb2.AttachmentReceivedNotification, client: OlvidClient = None) -> "AttachmentReceivedNotification":
		return AttachmentReceivedNotification(client, attachment=Attachment._from_native(native_message.attachment, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.attachment_notifications_pb2.AttachmentReceivedNotification], client: OlvidClient = None) -> list["AttachmentReceivedNotification"]:
		return [AttachmentReceivedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.attachment_notifications_pb2.AttachmentReceivedNotification], client: OlvidClient = None) -> "AttachmentReceivedNotification":
		native_message = await promise
		return AttachmentReceivedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentReceivedNotification"]):
		if messages is None:
			return []
		return [AttachmentReceivedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentReceivedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.attachment_notifications_pb2.AttachmentReceivedNotification(attachment=Attachment._to_native(message.attachment if message.attachment else None))

	def __str__(self):
		s: str = ''
		if self.attachment:
			s += f'attachment: ({self.attachment}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentReceivedNotification):
			return False
		return self.attachment == other.attachment

	def __bool__(self):
		return bool(self.attachment)

	def __hash__(self):
		return hash(self.attachment)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentReceivedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.attachment is None or self.attachment._test_assertion(expected.attachment)
		except AssertionError as e:
			raise AssertionError("attachment: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToAttachmentUploadedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_attachment_uploaded_notification: SubscribeToAttachmentUploadedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToAttachmentUploadedNotification":
		return SubscribeToAttachmentUploadedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.attachment_notifications_pb2.SubscribeToAttachmentUploadedNotification, client: OlvidClient = None) -> "SubscribeToAttachmentUploadedNotification":
		return SubscribeToAttachmentUploadedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.attachment_notifications_pb2.SubscribeToAttachmentUploadedNotification], client: OlvidClient = None) -> list["SubscribeToAttachmentUploadedNotification"]:
		return [SubscribeToAttachmentUploadedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.attachment_notifications_pb2.SubscribeToAttachmentUploadedNotification], client: OlvidClient = None) -> "SubscribeToAttachmentUploadedNotification":
		native_message = await promise
		return SubscribeToAttachmentUploadedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToAttachmentUploadedNotification"]):
		if messages is None:
			return []
		return [SubscribeToAttachmentUploadedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToAttachmentUploadedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.attachment_notifications_pb2.SubscribeToAttachmentUploadedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToAttachmentUploadedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToAttachmentUploadedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentUploadedNotification:
	def __init__(self, client: OlvidClient = None, attachment: "Attachment" = None):
		self._client: OlvidClient = client
		self.attachment: Attachment = attachment

	def _update_content(self, attachment_uploaded_notification: AttachmentUploadedNotification) -> None:
		self.attachment: Attachment = attachment_uploaded_notification.attachment

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentUploadedNotification":
		return AttachmentUploadedNotification(client=self._client, attachment=self.attachment._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.attachment_notifications_pb2.AttachmentUploadedNotification, client: OlvidClient = None) -> "AttachmentUploadedNotification":
		return AttachmentUploadedNotification(client, attachment=Attachment._from_native(native_message.attachment, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.attachment_notifications_pb2.AttachmentUploadedNotification], client: OlvidClient = None) -> list["AttachmentUploadedNotification"]:
		return [AttachmentUploadedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.attachment_notifications_pb2.AttachmentUploadedNotification], client: OlvidClient = None) -> "AttachmentUploadedNotification":
		native_message = await promise
		return AttachmentUploadedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentUploadedNotification"]):
		if messages is None:
			return []
		return [AttachmentUploadedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentUploadedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.attachment_notifications_pb2.AttachmentUploadedNotification(attachment=Attachment._to_native(message.attachment if message.attachment else None))

	def __str__(self):
		s: str = ''
		if self.attachment:
			s += f'attachment: ({self.attachment}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentUploadedNotification):
			return False
		return self.attachment == other.attachment

	def __bool__(self):
		return bool(self.attachment)

	def __hash__(self):
		return hash(self.attachment)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentUploadedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.attachment is None or self.attachment._test_assertion(expected.attachment)
		except AssertionError as e:
			raise AssertionError("attachment: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToContactNewNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_contact_new_notification: SubscribeToContactNewNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToContactNewNotification":
		return SubscribeToContactNewNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactNewNotification, client: OlvidClient = None) -> "SubscribeToContactNewNotification":
		return SubscribeToContactNewNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactNewNotification], client: OlvidClient = None) -> list["SubscribeToContactNewNotification"]:
		return [SubscribeToContactNewNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactNewNotification], client: OlvidClient = None) -> "SubscribeToContactNewNotification":
		native_message = await promise
		return SubscribeToContactNewNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToContactNewNotification"]):
		if messages is None:
			return []
		return [SubscribeToContactNewNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToContactNewNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactNewNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToContactNewNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToContactNewNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactNewNotification:
	def __init__(self, client: OlvidClient = None, contact: "Contact" = None):
		self._client: OlvidClient = client
		self.contact: Contact = contact

	def _update_content(self, contact_new_notification: ContactNewNotification) -> None:
		self.contact: Contact = contact_new_notification.contact

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactNewNotification":
		return ContactNewNotification(client=self._client, contact=self.contact._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.contact_notifications_pb2.ContactNewNotification, client: OlvidClient = None) -> "ContactNewNotification":
		return ContactNewNotification(client, contact=Contact._from_native(native_message.contact, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.contact_notifications_pb2.ContactNewNotification], client: OlvidClient = None) -> list["ContactNewNotification"]:
		return [ContactNewNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.contact_notifications_pb2.ContactNewNotification], client: OlvidClient = None) -> "ContactNewNotification":
		native_message = await promise
		return ContactNewNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactNewNotification"]):
		if messages is None:
			return []
		return [ContactNewNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactNewNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.contact_notifications_pb2.ContactNewNotification(contact=Contact._to_native(message.contact if message.contact else None))

	def __str__(self):
		s: str = ''
		if self.contact:
			s += f'contact: ({self.contact}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactNewNotification):
			return False
		return self.contact == other.contact

	def __bool__(self):
		return bool(self.contact)

	def __hash__(self):
		return hash(self.contact)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactNewNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.contact is None or self.contact._test_assertion(expected.contact)
		except AssertionError as e:
			raise AssertionError("contact: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToContactDeletedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_contact_deleted_notification: SubscribeToContactDeletedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToContactDeletedNotification":
		return SubscribeToContactDeletedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactDeletedNotification, client: OlvidClient = None) -> "SubscribeToContactDeletedNotification":
		return SubscribeToContactDeletedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactDeletedNotification], client: OlvidClient = None) -> list["SubscribeToContactDeletedNotification"]:
		return [SubscribeToContactDeletedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactDeletedNotification], client: OlvidClient = None) -> "SubscribeToContactDeletedNotification":
		native_message = await promise
		return SubscribeToContactDeletedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToContactDeletedNotification"]):
		if messages is None:
			return []
		return [SubscribeToContactDeletedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToContactDeletedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactDeletedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToContactDeletedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToContactDeletedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactDeletedNotification:
	def __init__(self, client: OlvidClient = None, contact: "Contact" = None):
		self._client: OlvidClient = client
		self.contact: Contact = contact

	def _update_content(self, contact_deleted_notification: ContactDeletedNotification) -> None:
		self.contact: Contact = contact_deleted_notification.contact

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDeletedNotification":
		return ContactDeletedNotification(client=self._client, contact=self.contact._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.contact_notifications_pb2.ContactDeletedNotification, client: OlvidClient = None) -> "ContactDeletedNotification":
		return ContactDeletedNotification(client, contact=Contact._from_native(native_message.contact, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.contact_notifications_pb2.ContactDeletedNotification], client: OlvidClient = None) -> list["ContactDeletedNotification"]:
		return [ContactDeletedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.contact_notifications_pb2.ContactDeletedNotification], client: OlvidClient = None) -> "ContactDeletedNotification":
		native_message = await promise
		return ContactDeletedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactDeletedNotification"]):
		if messages is None:
			return []
		return [ContactDeletedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactDeletedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.contact_notifications_pb2.ContactDeletedNotification(contact=Contact._to_native(message.contact if message.contact else None))

	def __str__(self):
		s: str = ''
		if self.contact:
			s += f'contact: ({self.contact}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactDeletedNotification):
			return False
		return self.contact == other.contact

	def __bool__(self):
		return bool(self.contact)

	def __hash__(self):
		return hash(self.contact)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactDeletedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.contact is None or self.contact._test_assertion(expected.contact)
		except AssertionError as e:
			raise AssertionError("contact: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToContactDetailsUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_contact_details_updated_notification: SubscribeToContactDetailsUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToContactDetailsUpdatedNotification":
		return SubscribeToContactDetailsUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactDetailsUpdatedNotification, client: OlvidClient = None) -> "SubscribeToContactDetailsUpdatedNotification":
		return SubscribeToContactDetailsUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactDetailsUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToContactDetailsUpdatedNotification"]:
		return [SubscribeToContactDetailsUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactDetailsUpdatedNotification], client: OlvidClient = None) -> "SubscribeToContactDetailsUpdatedNotification":
		native_message = await promise
		return SubscribeToContactDetailsUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToContactDetailsUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToContactDetailsUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToContactDetailsUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactDetailsUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToContactDetailsUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToContactDetailsUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactDetailsUpdatedNotification:
	def __init__(self, client: OlvidClient = None, contact: "Contact" = None, previous_details: "IdentityDetails" = None):
		self._client: OlvidClient = client
		self.contact: Contact = contact
		self.previous_details: IdentityDetails = previous_details

	def _update_content(self, contact_details_updated_notification: ContactDetailsUpdatedNotification) -> None:
		self.contact: Contact = contact_details_updated_notification.contact
		self.previous_details: IdentityDetails = contact_details_updated_notification.previous_details

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDetailsUpdatedNotification":
		return ContactDetailsUpdatedNotification(client=self._client, contact=self.contact._clone(), previous_details=self.previous_details._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.contact_notifications_pb2.ContactDetailsUpdatedNotification, client: OlvidClient = None) -> "ContactDetailsUpdatedNotification":
		return ContactDetailsUpdatedNotification(client, contact=Contact._from_native(native_message.contact, client=client), previous_details=IdentityDetails._from_native(native_message.previous_details, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.contact_notifications_pb2.ContactDetailsUpdatedNotification], client: OlvidClient = None) -> list["ContactDetailsUpdatedNotification"]:
		return [ContactDetailsUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.contact_notifications_pb2.ContactDetailsUpdatedNotification], client: OlvidClient = None) -> "ContactDetailsUpdatedNotification":
		native_message = await promise
		return ContactDetailsUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactDetailsUpdatedNotification"]):
		if messages is None:
			return []
		return [ContactDetailsUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactDetailsUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.contact_notifications_pb2.ContactDetailsUpdatedNotification(contact=Contact._to_native(message.contact if message.contact else None), previous_details=IdentityDetails._to_native(message.previous_details if message.previous_details else None))

	def __str__(self):
		s: str = ''
		if self.contact:
			s += f'contact: ({self.contact}), '
		if self.previous_details:
			s += f'previous_details: ({self.previous_details}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactDetailsUpdatedNotification):
			return False
		return self.contact == other.contact and self.previous_details == other.previous_details

	def __bool__(self):
		return bool(self.contact) or bool(self.previous_details)

	def __hash__(self):
		return hash((self.contact, self.previous_details))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactDetailsUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.contact is None or self.contact._test_assertion(expected.contact)
		except AssertionError as e:
			raise AssertionError("contact: " + str(e))
		try:
			assert expected.previous_details is None or self.previous_details._test_assertion(expected.previous_details)
		except AssertionError as e:
			raise AssertionError("previous_details: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToDiscussionNewNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_discussion_new_notification: SubscribeToDiscussionNewNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToDiscussionNewNotification":
		return SubscribeToDiscussionNewNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionNewNotification, client: OlvidClient = None) -> "SubscribeToDiscussionNewNotification":
		return SubscribeToDiscussionNewNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionNewNotification], client: OlvidClient = None) -> list["SubscribeToDiscussionNewNotification"]:
		return [SubscribeToDiscussionNewNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionNewNotification], client: OlvidClient = None) -> "SubscribeToDiscussionNewNotification":
		native_message = await promise
		return SubscribeToDiscussionNewNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToDiscussionNewNotification"]):
		if messages is None:
			return []
		return [SubscribeToDiscussionNewNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToDiscussionNewNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionNewNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToDiscussionNewNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToDiscussionNewNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionNewNotification:
	def __init__(self, client: OlvidClient = None, discussion: "Discussion" = None):
		self._client: OlvidClient = client
		self.discussion: Discussion = discussion

	def _update_content(self, discussion_new_notification: DiscussionNewNotification) -> None:
		self.discussion: Discussion = discussion_new_notification.discussion

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionNewNotification":
		return DiscussionNewNotification(client=self._client, discussion=self.discussion._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionNewNotification, client: OlvidClient = None) -> "DiscussionNewNotification":
		return DiscussionNewNotification(client, discussion=Discussion._from_native(native_message.discussion, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionNewNotification], client: OlvidClient = None) -> list["DiscussionNewNotification"]:
		return [DiscussionNewNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionNewNotification], client: OlvidClient = None) -> "DiscussionNewNotification":
		native_message = await promise
		return DiscussionNewNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionNewNotification"]):
		if messages is None:
			return []
		return [DiscussionNewNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionNewNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionNewNotification(discussion=Discussion._to_native(message.discussion if message.discussion else None))

	def __str__(self):
		s: str = ''
		if self.discussion:
			s += f'discussion: ({self.discussion}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionNewNotification):
			return False
		return self.discussion == other.discussion

	def __bool__(self):
		return bool(self.discussion)

	def __hash__(self):
		return hash(self.discussion)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionNewNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.discussion is None or self.discussion._test_assertion(expected.discussion)
		except AssertionError as e:
			raise AssertionError("discussion: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToDiscussionLockedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_discussion_locked_notification: SubscribeToDiscussionLockedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToDiscussionLockedNotification":
		return SubscribeToDiscussionLockedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionLockedNotification, client: OlvidClient = None) -> "SubscribeToDiscussionLockedNotification":
		return SubscribeToDiscussionLockedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionLockedNotification], client: OlvidClient = None) -> list["SubscribeToDiscussionLockedNotification"]:
		return [SubscribeToDiscussionLockedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionLockedNotification], client: OlvidClient = None) -> "SubscribeToDiscussionLockedNotification":
		native_message = await promise
		return SubscribeToDiscussionLockedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToDiscussionLockedNotification"]):
		if messages is None:
			return []
		return [SubscribeToDiscussionLockedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToDiscussionLockedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionLockedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToDiscussionLockedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToDiscussionLockedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionLockedNotification:
	def __init__(self, client: OlvidClient = None, discussion: "Discussion" = None):
		self._client: OlvidClient = client
		self.discussion: Discussion = discussion

	def _update_content(self, discussion_locked_notification: DiscussionLockedNotification) -> None:
		self.discussion: Discussion = discussion_locked_notification.discussion

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionLockedNotification":
		return DiscussionLockedNotification(client=self._client, discussion=self.discussion._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionLockedNotification, client: OlvidClient = None) -> "DiscussionLockedNotification":
		return DiscussionLockedNotification(client, discussion=Discussion._from_native(native_message.discussion, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionLockedNotification], client: OlvidClient = None) -> list["DiscussionLockedNotification"]:
		return [DiscussionLockedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionLockedNotification], client: OlvidClient = None) -> "DiscussionLockedNotification":
		native_message = await promise
		return DiscussionLockedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionLockedNotification"]):
		if messages is None:
			return []
		return [DiscussionLockedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionLockedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionLockedNotification(discussion=Discussion._to_native(message.discussion if message.discussion else None))

	def __str__(self):
		s: str = ''
		if self.discussion:
			s += f'discussion: ({self.discussion}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionLockedNotification):
			return False
		return self.discussion == other.discussion

	def __bool__(self):
		return bool(self.discussion)

	def __hash__(self):
		return hash(self.discussion)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionLockedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.discussion is None or self.discussion._test_assertion(expected.discussion)
		except AssertionError as e:
			raise AssertionError("discussion: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToDiscussionTitleUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_discussion_title_updated_notification: SubscribeToDiscussionTitleUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToDiscussionTitleUpdatedNotification":
		return SubscribeToDiscussionTitleUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionTitleUpdatedNotification, client: OlvidClient = None) -> "SubscribeToDiscussionTitleUpdatedNotification":
		return SubscribeToDiscussionTitleUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionTitleUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToDiscussionTitleUpdatedNotification"]:
		return [SubscribeToDiscussionTitleUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionTitleUpdatedNotification], client: OlvidClient = None) -> "SubscribeToDiscussionTitleUpdatedNotification":
		native_message = await promise
		return SubscribeToDiscussionTitleUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToDiscussionTitleUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToDiscussionTitleUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToDiscussionTitleUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionTitleUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToDiscussionTitleUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToDiscussionTitleUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionTitleUpdatedNotification:
	def __init__(self, client: OlvidClient = None, discussion: "Discussion" = None, previous_title: str = ""):
		self._client: OlvidClient = client
		self.discussion: Discussion = discussion
		self.previous_title: str = previous_title

	def _update_content(self, discussion_title_updated_notification: DiscussionTitleUpdatedNotification) -> None:
		self.discussion: Discussion = discussion_title_updated_notification.discussion
		self.previous_title: str = discussion_title_updated_notification.previous_title

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionTitleUpdatedNotification":
		return DiscussionTitleUpdatedNotification(client=self._client, discussion=self.discussion._clone(), previous_title=self.previous_title)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionTitleUpdatedNotification, client: OlvidClient = None) -> "DiscussionTitleUpdatedNotification":
		return DiscussionTitleUpdatedNotification(client, discussion=Discussion._from_native(native_message.discussion, client=client), previous_title=native_message.previous_title)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionTitleUpdatedNotification], client: OlvidClient = None) -> list["DiscussionTitleUpdatedNotification"]:
		return [DiscussionTitleUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionTitleUpdatedNotification], client: OlvidClient = None) -> "DiscussionTitleUpdatedNotification":
		native_message = await promise
		return DiscussionTitleUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionTitleUpdatedNotification"]):
		if messages is None:
			return []
		return [DiscussionTitleUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionTitleUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionTitleUpdatedNotification(discussion=Discussion._to_native(message.discussion if message.discussion else None), previous_title=message.previous_title if message.previous_title else None)

	def __str__(self):
		s: str = ''
		if self.discussion:
			s += f'discussion: ({self.discussion}), '
		if self.previous_title:
			s += f'previous_title: {self.previous_title}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionTitleUpdatedNotification):
			return False
		return self.discussion == other.discussion and self.previous_title == other.previous_title

	def __bool__(self):
		return bool(self.discussion) or self.previous_title != ""

	def __hash__(self):
		return hash((self.discussion, self.previous_title))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionTitleUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.discussion is None or self.discussion._test_assertion(expected.discussion)
		except AssertionError as e:
			raise AssertionError("discussion: " + str(e))
		assert expected.previous_title == "" or self.previous_title == expected.previous_title, "Invalid value: previous_title: " + str(expected.previous_title) + " != " + str(self.previous_title)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToDiscussionSettingsUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_discussion_settings_updated_notification: SubscribeToDiscussionSettingsUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToDiscussionSettingsUpdatedNotification":
		return SubscribeToDiscussionSettingsUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionSettingsUpdatedNotification, client: OlvidClient = None) -> "SubscribeToDiscussionSettingsUpdatedNotification":
		return SubscribeToDiscussionSettingsUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionSettingsUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToDiscussionSettingsUpdatedNotification"]:
		return [SubscribeToDiscussionSettingsUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionSettingsUpdatedNotification], client: OlvidClient = None) -> "SubscribeToDiscussionSettingsUpdatedNotification":
		native_message = await promise
		return SubscribeToDiscussionSettingsUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToDiscussionSettingsUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToDiscussionSettingsUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToDiscussionSettingsUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionSettingsUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToDiscussionSettingsUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToDiscussionSettingsUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionSettingsUpdatedNotification:
	def __init__(self, client: OlvidClient = None, new_settings: "DiscussionSettings" = None, previous_settings: "DiscussionSettings" = None):
		self._client: OlvidClient = client
		self.new_settings: DiscussionSettings = new_settings
		self.previous_settings: DiscussionSettings = previous_settings

	def _update_content(self, discussion_settings_updated_notification: DiscussionSettingsUpdatedNotification) -> None:
		self.new_settings: DiscussionSettings = discussion_settings_updated_notification.new_settings
		self.previous_settings: DiscussionSettings = discussion_settings_updated_notification.previous_settings

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionSettingsUpdatedNotification":
		return DiscussionSettingsUpdatedNotification(client=self._client, new_settings=self.new_settings._clone(), previous_settings=self.previous_settings._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionSettingsUpdatedNotification, client: OlvidClient = None) -> "DiscussionSettingsUpdatedNotification":
		return DiscussionSettingsUpdatedNotification(client, new_settings=DiscussionSettings._from_native(native_message.new_settings, client=client), previous_settings=DiscussionSettings._from_native(native_message.previous_settings, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionSettingsUpdatedNotification], client: OlvidClient = None) -> list["DiscussionSettingsUpdatedNotification"]:
		return [DiscussionSettingsUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionSettingsUpdatedNotification], client: OlvidClient = None) -> "DiscussionSettingsUpdatedNotification":
		native_message = await promise
		return DiscussionSettingsUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionSettingsUpdatedNotification"]):
		if messages is None:
			return []
		return [DiscussionSettingsUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionSettingsUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionSettingsUpdatedNotification(new_settings=DiscussionSettings._to_native(message.new_settings if message.new_settings else None), previous_settings=DiscussionSettings._to_native(message.previous_settings if message.previous_settings else None))

	def __str__(self):
		s: str = ''
		if self.new_settings:
			s += f'new_settings: ({self.new_settings}), '
		if self.previous_settings:
			s += f'previous_settings: ({self.previous_settings}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionSettingsUpdatedNotification):
			return False
		return self.new_settings == other.new_settings and self.previous_settings == other.previous_settings

	def __bool__(self):
		return bool(self.new_settings) or bool(self.previous_settings)

	def __hash__(self):
		return hash((self.new_settings, self.previous_settings))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionSettingsUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.new_settings is None or self.new_settings._test_assertion(expected.new_settings)
		except AssertionError as e:
			raise AssertionError("new_settings: " + str(e))
		try:
			assert expected.previous_settings is None or self.previous_settings._test_assertion(expected.previous_settings)
		except AssertionError as e:
			raise AssertionError("previous_settings: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupNewNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_new_notification: SubscribeToGroupNewNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupNewNotification":
		return SubscribeToGroupNewNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupNewNotification, client: OlvidClient = None) -> "SubscribeToGroupNewNotification":
		return SubscribeToGroupNewNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupNewNotification], client: OlvidClient = None) -> list["SubscribeToGroupNewNotification"]:
		return [SubscribeToGroupNewNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupNewNotification], client: OlvidClient = None) -> "SubscribeToGroupNewNotification":
		native_message = await promise
		return SubscribeToGroupNewNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupNewNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupNewNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupNewNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupNewNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupNewNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupNewNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNewNotification:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_new_notification: GroupNewNotification) -> None:
		self.group: Group = group_new_notification.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewNotification":
		return GroupNewNotification(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupNewNotification, client: OlvidClient = None) -> "GroupNewNotification":
		return GroupNewNotification(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupNewNotification], client: OlvidClient = None) -> list["GroupNewNotification"]:
		return [GroupNewNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupNewNotification], client: OlvidClient = None) -> "GroupNewNotification":
		native_message = await promise
		return GroupNewNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupNewNotification"]):
		if messages is None:
			return []
		return [GroupNewNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupNewNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupNewNotification(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupNewNotification):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupNewNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupDeletedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_deleted_notification: SubscribeToGroupDeletedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupDeletedNotification":
		return SubscribeToGroupDeletedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupDeletedNotification, client: OlvidClient = None) -> "SubscribeToGroupDeletedNotification":
		return SubscribeToGroupDeletedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupDeletedNotification], client: OlvidClient = None) -> list["SubscribeToGroupDeletedNotification"]:
		return [SubscribeToGroupDeletedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupDeletedNotification], client: OlvidClient = None) -> "SubscribeToGroupDeletedNotification":
		native_message = await promise
		return SubscribeToGroupDeletedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupDeletedNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupDeletedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupDeletedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupDeletedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupDeletedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupDeletedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupDeletedNotification:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_deleted_notification: GroupDeletedNotification) -> None:
		self.group: Group = group_deleted_notification.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupDeletedNotification":
		return GroupDeletedNotification(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupDeletedNotification, client: OlvidClient = None) -> "GroupDeletedNotification":
		return GroupDeletedNotification(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupDeletedNotification], client: OlvidClient = None) -> list["GroupDeletedNotification"]:
		return [GroupDeletedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupDeletedNotification], client: OlvidClient = None) -> "GroupDeletedNotification":
		native_message = await promise
		return GroupDeletedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupDeletedNotification"]):
		if messages is None:
			return []
		return [GroupDeletedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupDeletedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupDeletedNotification(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupDeletedNotification):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupDeletedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupNameUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_name_updated_notification: SubscribeToGroupNameUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupNameUpdatedNotification":
		return SubscribeToGroupNameUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupNameUpdatedNotification, client: OlvidClient = None) -> "SubscribeToGroupNameUpdatedNotification":
		return SubscribeToGroupNameUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupNameUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToGroupNameUpdatedNotification"]:
		return [SubscribeToGroupNameUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupNameUpdatedNotification], client: OlvidClient = None) -> "SubscribeToGroupNameUpdatedNotification":
		native_message = await promise
		return SubscribeToGroupNameUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupNameUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupNameUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupNameUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupNameUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupNameUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupNameUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNameUpdatedNotification:
	def __init__(self, client: OlvidClient = None, group: "Group" = None, previous_name: str = ""):
		self._client: OlvidClient = client
		self.group: Group = group
		self.previous_name: str = previous_name

	def _update_content(self, group_name_updated_notification: GroupNameUpdatedNotification) -> None:
		self.group: Group = group_name_updated_notification.group
		self.previous_name: str = group_name_updated_notification.previous_name

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNameUpdatedNotification":
		return GroupNameUpdatedNotification(client=self._client, group=self.group._clone(), previous_name=self.previous_name)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupNameUpdatedNotification, client: OlvidClient = None) -> "GroupNameUpdatedNotification":
		return GroupNameUpdatedNotification(client, group=Group._from_native(native_message.group, client=client), previous_name=native_message.previous_name)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupNameUpdatedNotification], client: OlvidClient = None) -> list["GroupNameUpdatedNotification"]:
		return [GroupNameUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupNameUpdatedNotification], client: OlvidClient = None) -> "GroupNameUpdatedNotification":
		native_message = await promise
		return GroupNameUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupNameUpdatedNotification"]):
		if messages is None:
			return []
		return [GroupNameUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupNameUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupNameUpdatedNotification(group=Group._to_native(message.group if message.group else None), previous_name=message.previous_name if message.previous_name else None)

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		if self.previous_name:
			s += f'previous_name: {self.previous_name}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupNameUpdatedNotification):
			return False
		return self.group == other.group and self.previous_name == other.previous_name

	def __bool__(self):
		return bool(self.group) or self.previous_name != ""

	def __hash__(self):
		return hash((self.group, self.previous_name))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupNameUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		assert expected.previous_name == "" or self.previous_name == expected.previous_name, "Invalid value: previous_name: " + str(expected.previous_name) + " != " + str(self.previous_name)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupDescriptionUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_description_updated_notification: SubscribeToGroupDescriptionUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupDescriptionUpdatedNotification":
		return SubscribeToGroupDescriptionUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupDescriptionUpdatedNotification, client: OlvidClient = None) -> "SubscribeToGroupDescriptionUpdatedNotification":
		return SubscribeToGroupDescriptionUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupDescriptionUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToGroupDescriptionUpdatedNotification"]:
		return [SubscribeToGroupDescriptionUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupDescriptionUpdatedNotification], client: OlvidClient = None) -> "SubscribeToGroupDescriptionUpdatedNotification":
		native_message = await promise
		return SubscribeToGroupDescriptionUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupDescriptionUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupDescriptionUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupDescriptionUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupDescriptionUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupDescriptionUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupDescriptionUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupDescriptionUpdatedNotification:
	def __init__(self, client: OlvidClient = None, group: "Group" = None, previous_description: str = ""):
		self._client: OlvidClient = client
		self.group: Group = group
		self.previous_description: str = previous_description

	def _update_content(self, group_description_updated_notification: GroupDescriptionUpdatedNotification) -> None:
		self.group: Group = group_description_updated_notification.group
		self.previous_description: str = group_description_updated_notification.previous_description

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupDescriptionUpdatedNotification":
		return GroupDescriptionUpdatedNotification(client=self._client, group=self.group._clone(), previous_description=self.previous_description)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupDescriptionUpdatedNotification, client: OlvidClient = None) -> "GroupDescriptionUpdatedNotification":
		return GroupDescriptionUpdatedNotification(client, group=Group._from_native(native_message.group, client=client), previous_description=native_message.previous_description)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupDescriptionUpdatedNotification], client: OlvidClient = None) -> list["GroupDescriptionUpdatedNotification"]:
		return [GroupDescriptionUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupDescriptionUpdatedNotification], client: OlvidClient = None) -> "GroupDescriptionUpdatedNotification":
		native_message = await promise
		return GroupDescriptionUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupDescriptionUpdatedNotification"]):
		if messages is None:
			return []
		return [GroupDescriptionUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupDescriptionUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupDescriptionUpdatedNotification(group=Group._to_native(message.group if message.group else None), previous_description=message.previous_description if message.previous_description else None)

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		if self.previous_description:
			s += f'previous_description: {self.previous_description}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupDescriptionUpdatedNotification):
			return False
		return self.group == other.group and self.previous_description == other.previous_description

	def __bool__(self):
		return bool(self.group) or self.previous_description != ""

	def __hash__(self):
		return hash((self.group, self.previous_description))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupDescriptionUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		assert expected.previous_description == "" or self.previous_description == expected.previous_description, "Invalid value: previous_description: " + str(expected.previous_description) + " != " + str(self.previous_description)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupPendingMemberAddedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_pending_member_added_notification: SubscribeToGroupPendingMemberAddedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupPendingMemberAddedNotification":
		return SubscribeToGroupPendingMemberAddedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupPendingMemberAddedNotification, client: OlvidClient = None) -> "SubscribeToGroupPendingMemberAddedNotification":
		return SubscribeToGroupPendingMemberAddedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupPendingMemberAddedNotification], client: OlvidClient = None) -> list["SubscribeToGroupPendingMemberAddedNotification"]:
		return [SubscribeToGroupPendingMemberAddedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupPendingMemberAddedNotification], client: OlvidClient = None) -> "SubscribeToGroupPendingMemberAddedNotification":
		native_message = await promise
		return SubscribeToGroupPendingMemberAddedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupPendingMemberAddedNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupPendingMemberAddedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupPendingMemberAddedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupPendingMemberAddedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupPendingMemberAddedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupPendingMemberAddedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupPendingMemberAddedNotification:
	def __init__(self, client: OlvidClient = None, group: "Group" = None, pending_member: "PendingGroupMember" = None):
		self._client: OlvidClient = client
		self.group: Group = group
		self.pending_member: PendingGroupMember = pending_member

	def _update_content(self, group_pending_member_added_notification: GroupPendingMemberAddedNotification) -> None:
		self.group: Group = group_pending_member_added_notification.group
		self.pending_member: PendingGroupMember = group_pending_member_added_notification.pending_member

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupPendingMemberAddedNotification":
		return GroupPendingMemberAddedNotification(client=self._client, group=self.group._clone(), pending_member=self.pending_member._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupPendingMemberAddedNotification, client: OlvidClient = None) -> "GroupPendingMemberAddedNotification":
		return GroupPendingMemberAddedNotification(client, group=Group._from_native(native_message.group, client=client), pending_member=PendingGroupMember._from_native(native_message.pending_member, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupPendingMemberAddedNotification], client: OlvidClient = None) -> list["GroupPendingMemberAddedNotification"]:
		return [GroupPendingMemberAddedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupPendingMemberAddedNotification], client: OlvidClient = None) -> "GroupPendingMemberAddedNotification":
		native_message = await promise
		return GroupPendingMemberAddedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupPendingMemberAddedNotification"]):
		if messages is None:
			return []
		return [GroupPendingMemberAddedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupPendingMemberAddedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupPendingMemberAddedNotification(group=Group._to_native(message.group if message.group else None), pending_member=PendingGroupMember._to_native(message.pending_member if message.pending_member else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		if self.pending_member:
			s += f'pending_member: ({self.pending_member}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupPendingMemberAddedNotification):
			return False
		return self.group == other.group and self.pending_member == other.pending_member

	def __bool__(self):
		return bool(self.group) or bool(self.pending_member)

	def __hash__(self):
		return hash((self.group, self.pending_member))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupPendingMemberAddedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		try:
			assert expected.pending_member is None or self.pending_member._test_assertion(expected.pending_member)
		except AssertionError as e:
			raise AssertionError("pending_member: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupPendingMemberRemovedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_pending_member_removed_notification: SubscribeToGroupPendingMemberRemovedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupPendingMemberRemovedNotification":
		return SubscribeToGroupPendingMemberRemovedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupPendingMemberRemovedNotification, client: OlvidClient = None) -> "SubscribeToGroupPendingMemberRemovedNotification":
		return SubscribeToGroupPendingMemberRemovedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupPendingMemberRemovedNotification], client: OlvidClient = None) -> list["SubscribeToGroupPendingMemberRemovedNotification"]:
		return [SubscribeToGroupPendingMemberRemovedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupPendingMemberRemovedNotification], client: OlvidClient = None) -> "SubscribeToGroupPendingMemberRemovedNotification":
		native_message = await promise
		return SubscribeToGroupPendingMemberRemovedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupPendingMemberRemovedNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupPendingMemberRemovedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupPendingMemberRemovedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupPendingMemberRemovedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupPendingMemberRemovedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupPendingMemberRemovedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupPendingMemberRemovedNotification:
	def __init__(self, client: OlvidClient = None, group: "Group" = None, pending_member: "PendingGroupMember" = None):
		self._client: OlvidClient = client
		self.group: Group = group
		self.pending_member: PendingGroupMember = pending_member

	def _update_content(self, group_pending_member_removed_notification: GroupPendingMemberRemovedNotification) -> None:
		self.group: Group = group_pending_member_removed_notification.group
		self.pending_member: PendingGroupMember = group_pending_member_removed_notification.pending_member

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupPendingMemberRemovedNotification":
		return GroupPendingMemberRemovedNotification(client=self._client, group=self.group._clone(), pending_member=self.pending_member._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupPendingMemberRemovedNotification, client: OlvidClient = None) -> "GroupPendingMemberRemovedNotification":
		return GroupPendingMemberRemovedNotification(client, group=Group._from_native(native_message.group, client=client), pending_member=PendingGroupMember._from_native(native_message.pending_member, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupPendingMemberRemovedNotification], client: OlvidClient = None) -> list["GroupPendingMemberRemovedNotification"]:
		return [GroupPendingMemberRemovedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupPendingMemberRemovedNotification], client: OlvidClient = None) -> "GroupPendingMemberRemovedNotification":
		native_message = await promise
		return GroupPendingMemberRemovedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupPendingMemberRemovedNotification"]):
		if messages is None:
			return []
		return [GroupPendingMemberRemovedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupPendingMemberRemovedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupPendingMemberRemovedNotification(group=Group._to_native(message.group if message.group else None), pending_member=PendingGroupMember._to_native(message.pending_member if message.pending_member else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		if self.pending_member:
			s += f'pending_member: ({self.pending_member}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupPendingMemberRemovedNotification):
			return False
		return self.group == other.group and self.pending_member == other.pending_member

	def __bool__(self):
		return bool(self.group) or bool(self.pending_member)

	def __hash__(self):
		return hash((self.group, self.pending_member))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupPendingMemberRemovedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		try:
			assert expected.pending_member is None or self.pending_member._test_assertion(expected.pending_member)
		except AssertionError as e:
			raise AssertionError("pending_member: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupMemberJoinedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_member_joined_notification: SubscribeToGroupMemberJoinedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupMemberJoinedNotification":
		return SubscribeToGroupMemberJoinedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberJoinedNotification, client: OlvidClient = None) -> "SubscribeToGroupMemberJoinedNotification":
		return SubscribeToGroupMemberJoinedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberJoinedNotification], client: OlvidClient = None) -> list["SubscribeToGroupMemberJoinedNotification"]:
		return [SubscribeToGroupMemberJoinedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberJoinedNotification], client: OlvidClient = None) -> "SubscribeToGroupMemberJoinedNotification":
		native_message = await promise
		return SubscribeToGroupMemberJoinedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupMemberJoinedNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupMemberJoinedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupMemberJoinedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberJoinedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupMemberJoinedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupMemberJoinedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupMemberJoinedNotification:
	def __init__(self, client: OlvidClient = None, group: "Group" = None, member: "GroupMember" = None):
		self._client: OlvidClient = client
		self.group: Group = group
		self.member: GroupMember = member

	def _update_content(self, group_member_joined_notification: GroupMemberJoinedNotification) -> None:
		self.group: Group = group_member_joined_notification.group
		self.member: GroupMember = group_member_joined_notification.member

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupMemberJoinedNotification":
		return GroupMemberJoinedNotification(client=self._client, group=self.group._clone(), member=self.member._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberJoinedNotification, client: OlvidClient = None) -> "GroupMemberJoinedNotification":
		return GroupMemberJoinedNotification(client, group=Group._from_native(native_message.group, client=client), member=GroupMember._from_native(native_message.member, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberJoinedNotification], client: OlvidClient = None) -> list["GroupMemberJoinedNotification"]:
		return [GroupMemberJoinedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberJoinedNotification], client: OlvidClient = None) -> "GroupMemberJoinedNotification":
		native_message = await promise
		return GroupMemberJoinedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupMemberJoinedNotification"]):
		if messages is None:
			return []
		return [GroupMemberJoinedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupMemberJoinedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberJoinedNotification(group=Group._to_native(message.group if message.group else None), member=GroupMember._to_native(message.member if message.member else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		if self.member:
			s += f'member: ({self.member}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupMemberJoinedNotification):
			return False
		return self.group == other.group and self.member == other.member

	def __bool__(self):
		return bool(self.group) or bool(self.member)

	def __hash__(self):
		return hash((self.group, self.member))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupMemberJoinedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		try:
			assert expected.member is None or self.member._test_assertion(expected.member)
		except AssertionError as e:
			raise AssertionError("member: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupMemberLeftNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_member_left_notification: SubscribeToGroupMemberLeftNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupMemberLeftNotification":
		return SubscribeToGroupMemberLeftNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberLeftNotification, client: OlvidClient = None) -> "SubscribeToGroupMemberLeftNotification":
		return SubscribeToGroupMemberLeftNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberLeftNotification], client: OlvidClient = None) -> list["SubscribeToGroupMemberLeftNotification"]:
		return [SubscribeToGroupMemberLeftNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberLeftNotification], client: OlvidClient = None) -> "SubscribeToGroupMemberLeftNotification":
		native_message = await promise
		return SubscribeToGroupMemberLeftNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupMemberLeftNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupMemberLeftNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupMemberLeftNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberLeftNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupMemberLeftNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupMemberLeftNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupMemberLeftNotification:
	def __init__(self, client: OlvidClient = None, group: "Group" = None, member: "GroupMember" = None):
		self._client: OlvidClient = client
		self.group: Group = group
		self.member: GroupMember = member

	def _update_content(self, group_member_left_notification: GroupMemberLeftNotification) -> None:
		self.group: Group = group_member_left_notification.group
		self.member: GroupMember = group_member_left_notification.member

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupMemberLeftNotification":
		return GroupMemberLeftNotification(client=self._client, group=self.group._clone(), member=self.member._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberLeftNotification, client: OlvidClient = None) -> "GroupMemberLeftNotification":
		return GroupMemberLeftNotification(client, group=Group._from_native(native_message.group, client=client), member=GroupMember._from_native(native_message.member, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberLeftNotification], client: OlvidClient = None) -> list["GroupMemberLeftNotification"]:
		return [GroupMemberLeftNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberLeftNotification], client: OlvidClient = None) -> "GroupMemberLeftNotification":
		native_message = await promise
		return GroupMemberLeftNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupMemberLeftNotification"]):
		if messages is None:
			return []
		return [GroupMemberLeftNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupMemberLeftNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberLeftNotification(group=Group._to_native(message.group if message.group else None), member=GroupMember._to_native(message.member if message.member else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		if self.member:
			s += f'member: ({self.member}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupMemberLeftNotification):
			return False
		return self.group == other.group and self.member == other.member

	def __bool__(self):
		return bool(self.group) or bool(self.member)

	def __hash__(self):
		return hash((self.group, self.member))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupMemberLeftNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		try:
			assert expected.member is None or self.member._test_assertion(expected.member)
		except AssertionError as e:
			raise AssertionError("member: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupOwnPermissionsUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_own_permissions_updated_notification: SubscribeToGroupOwnPermissionsUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupOwnPermissionsUpdatedNotification":
		return SubscribeToGroupOwnPermissionsUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupOwnPermissionsUpdatedNotification, client: OlvidClient = None) -> "SubscribeToGroupOwnPermissionsUpdatedNotification":
		return SubscribeToGroupOwnPermissionsUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupOwnPermissionsUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToGroupOwnPermissionsUpdatedNotification"]:
		return [SubscribeToGroupOwnPermissionsUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupOwnPermissionsUpdatedNotification], client: OlvidClient = None) -> "SubscribeToGroupOwnPermissionsUpdatedNotification":
		native_message = await promise
		return SubscribeToGroupOwnPermissionsUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupOwnPermissionsUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupOwnPermissionsUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupOwnPermissionsUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupOwnPermissionsUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupOwnPermissionsUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupOwnPermissionsUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupOwnPermissionsUpdatedNotification:
	def __init__(self, client: OlvidClient = None, group: "Group" = None, permissions: "GroupMemberPermissions" = None, previous_permissions: "GroupMemberPermissions" = None):
		self._client: OlvidClient = client
		self.group: Group = group
		self.permissions: GroupMemberPermissions = permissions
		self.previous_permissions: GroupMemberPermissions = previous_permissions

	def _update_content(self, group_own_permissions_updated_notification: GroupOwnPermissionsUpdatedNotification) -> None:
		self.group: Group = group_own_permissions_updated_notification.group
		self.permissions: GroupMemberPermissions = group_own_permissions_updated_notification.permissions
		self.previous_permissions: GroupMemberPermissions = group_own_permissions_updated_notification.previous_permissions

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupOwnPermissionsUpdatedNotification":
		return GroupOwnPermissionsUpdatedNotification(client=self._client, group=self.group._clone(), permissions=self.permissions._clone(), previous_permissions=self.previous_permissions._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupOwnPermissionsUpdatedNotification, client: OlvidClient = None) -> "GroupOwnPermissionsUpdatedNotification":
		return GroupOwnPermissionsUpdatedNotification(client, group=Group._from_native(native_message.group, client=client), permissions=GroupMemberPermissions._from_native(native_message.permissions, client=client), previous_permissions=GroupMemberPermissions._from_native(native_message.previous_permissions, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupOwnPermissionsUpdatedNotification], client: OlvidClient = None) -> list["GroupOwnPermissionsUpdatedNotification"]:
		return [GroupOwnPermissionsUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupOwnPermissionsUpdatedNotification], client: OlvidClient = None) -> "GroupOwnPermissionsUpdatedNotification":
		native_message = await promise
		return GroupOwnPermissionsUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupOwnPermissionsUpdatedNotification"]):
		if messages is None:
			return []
		return [GroupOwnPermissionsUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupOwnPermissionsUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupOwnPermissionsUpdatedNotification(group=Group._to_native(message.group if message.group else None), permissions=GroupMemberPermissions._to_native(message.permissions if message.permissions else None), previous_permissions=GroupMemberPermissions._to_native(message.previous_permissions if message.previous_permissions else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		if self.permissions:
			s += f'permissions: ({self.permissions}), '
		if self.previous_permissions:
			s += f'previous_permissions: ({self.previous_permissions}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupOwnPermissionsUpdatedNotification):
			return False
		return self.group == other.group and self.permissions == other.permissions and self.previous_permissions == other.previous_permissions

	def __bool__(self):
		return bool(self.group) or bool(self.permissions) or bool(self.previous_permissions)

	def __hash__(self):
		return hash((self.group, self.permissions, self.previous_permissions))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupOwnPermissionsUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		try:
			assert expected.permissions is None or self.permissions._test_assertion(expected.permissions)
		except AssertionError as e:
			raise AssertionError("permissions: " + str(e))
		try:
			assert expected.previous_permissions is None or self.previous_permissions._test_assertion(expected.previous_permissions)
		except AssertionError as e:
			raise AssertionError("previous_permissions: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupMemberPermissionsUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_member_permissions_updated_notification: SubscribeToGroupMemberPermissionsUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupMemberPermissionsUpdatedNotification":
		return SubscribeToGroupMemberPermissionsUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberPermissionsUpdatedNotification, client: OlvidClient = None) -> "SubscribeToGroupMemberPermissionsUpdatedNotification":
		return SubscribeToGroupMemberPermissionsUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberPermissionsUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToGroupMemberPermissionsUpdatedNotification"]:
		return [SubscribeToGroupMemberPermissionsUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberPermissionsUpdatedNotification], client: OlvidClient = None) -> "SubscribeToGroupMemberPermissionsUpdatedNotification":
		native_message = await promise
		return SubscribeToGroupMemberPermissionsUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupMemberPermissionsUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupMemberPermissionsUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupMemberPermissionsUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberPermissionsUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupMemberPermissionsUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupMemberPermissionsUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupMemberPermissionsUpdatedNotification:
	def __init__(self, client: OlvidClient = None, group: "Group" = None, member: "GroupMember" = None, previous_permissions: "GroupMemberPermissions" = None):
		self._client: OlvidClient = client
		self.group: Group = group
		self.member: GroupMember = member
		self.previous_permissions: GroupMemberPermissions = previous_permissions

	def _update_content(self, group_member_permissions_updated_notification: GroupMemberPermissionsUpdatedNotification) -> None:
		self.group: Group = group_member_permissions_updated_notification.group
		self.member: GroupMember = group_member_permissions_updated_notification.member
		self.previous_permissions: GroupMemberPermissions = group_member_permissions_updated_notification.previous_permissions

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupMemberPermissionsUpdatedNotification":
		return GroupMemberPermissionsUpdatedNotification(client=self._client, group=self.group._clone(), member=self.member._clone(), previous_permissions=self.previous_permissions._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberPermissionsUpdatedNotification, client: OlvidClient = None) -> "GroupMemberPermissionsUpdatedNotification":
		return GroupMemberPermissionsUpdatedNotification(client, group=Group._from_native(native_message.group, client=client), member=GroupMember._from_native(native_message.member, client=client), previous_permissions=GroupMemberPermissions._from_native(native_message.previous_permissions, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberPermissionsUpdatedNotification], client: OlvidClient = None) -> list["GroupMemberPermissionsUpdatedNotification"]:
		return [GroupMemberPermissionsUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberPermissionsUpdatedNotification], client: OlvidClient = None) -> "GroupMemberPermissionsUpdatedNotification":
		native_message = await promise
		return GroupMemberPermissionsUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupMemberPermissionsUpdatedNotification"]):
		if messages is None:
			return []
		return [GroupMemberPermissionsUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupMemberPermissionsUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberPermissionsUpdatedNotification(group=Group._to_native(message.group if message.group else None), member=GroupMember._to_native(message.member if message.member else None), previous_permissions=GroupMemberPermissions._to_native(message.previous_permissions if message.previous_permissions else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		if self.member:
			s += f'member: ({self.member}), '
		if self.previous_permissions:
			s += f'previous_permissions: ({self.previous_permissions}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupMemberPermissionsUpdatedNotification):
			return False
		return self.group == other.group and self.member == other.member and self.previous_permissions == other.previous_permissions

	def __bool__(self):
		return bool(self.group) or bool(self.member) or bool(self.previous_permissions)

	def __hash__(self):
		return hash((self.group, self.member, self.previous_permissions))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupMemberPermissionsUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		try:
			assert expected.member is None or self.member._test_assertion(expected.member)
		except AssertionError as e:
			raise AssertionError("member: " + str(e))
		try:
			assert expected.previous_permissions is None or self.previous_permissions._test_assertion(expected.previous_permissions)
		except AssertionError as e:
			raise AssertionError("previous_permissions: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupUpdateInProgressNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_update_in_progress_notification: SubscribeToGroupUpdateInProgressNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupUpdateInProgressNotification":
		return SubscribeToGroupUpdateInProgressNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupUpdateInProgressNotification, client: OlvidClient = None) -> "SubscribeToGroupUpdateInProgressNotification":
		return SubscribeToGroupUpdateInProgressNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupUpdateInProgressNotification], client: OlvidClient = None) -> list["SubscribeToGroupUpdateInProgressNotification"]:
		return [SubscribeToGroupUpdateInProgressNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupUpdateInProgressNotification], client: OlvidClient = None) -> "SubscribeToGroupUpdateInProgressNotification":
		native_message = await promise
		return SubscribeToGroupUpdateInProgressNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupUpdateInProgressNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupUpdateInProgressNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupUpdateInProgressNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupUpdateInProgressNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupUpdateInProgressNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupUpdateInProgressNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupUpdateInProgressNotification:
	def __init__(self, client: OlvidClient = None, group_id: int = 0):
		self._client: OlvidClient = client
		self.group_id: int = group_id

	def _update_content(self, group_update_in_progress_notification: GroupUpdateInProgressNotification) -> None:
		self.group_id: int = group_update_in_progress_notification.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupUpdateInProgressNotification":
		return GroupUpdateInProgressNotification(client=self._client, group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupUpdateInProgressNotification, client: OlvidClient = None) -> "GroupUpdateInProgressNotification":
		return GroupUpdateInProgressNotification(client, group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupUpdateInProgressNotification], client: OlvidClient = None) -> list["GroupUpdateInProgressNotification"]:
		return [GroupUpdateInProgressNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupUpdateInProgressNotification], client: OlvidClient = None) -> "GroupUpdateInProgressNotification":
		native_message = await promise
		return GroupUpdateInProgressNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupUpdateInProgressNotification"]):
		if messages is None:
			return []
		return [GroupUpdateInProgressNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupUpdateInProgressNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupUpdateInProgressNotification(group_id=message.group_id if message.group_id else None)

	def __str__(self):
		s: str = ''
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupUpdateInProgressNotification):
			return False
		return self.group_id == other.group_id

	def __bool__(self):
		return self.group_id != 0

	def __hash__(self):
		return hash(self.group_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupUpdateInProgressNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.group_id == 0 or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToGroupUpdateFinishedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_group_update_finished_notification: SubscribeToGroupUpdateFinishedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToGroupUpdateFinishedNotification":
		return SubscribeToGroupUpdateFinishedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupUpdateFinishedNotification, client: OlvidClient = None) -> "SubscribeToGroupUpdateFinishedNotification":
		return SubscribeToGroupUpdateFinishedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupUpdateFinishedNotification], client: OlvidClient = None) -> list["SubscribeToGroupUpdateFinishedNotification"]:
		return [SubscribeToGroupUpdateFinishedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupUpdateFinishedNotification], client: OlvidClient = None) -> "SubscribeToGroupUpdateFinishedNotification":
		native_message = await promise
		return SubscribeToGroupUpdateFinishedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToGroupUpdateFinishedNotification"]):
		if messages is None:
			return []
		return [SubscribeToGroupUpdateFinishedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToGroupUpdateFinishedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupUpdateFinishedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToGroupUpdateFinishedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToGroupUpdateFinishedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupUpdateFinishedNotification:
	def __init__(self, client: OlvidClient = None, group_id: int = 0):
		self._client: OlvidClient = client
		self.group_id: int = group_id

	def _update_content(self, group_update_finished_notification: GroupUpdateFinishedNotification) -> None:
		self.group_id: int = group_update_finished_notification.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupUpdateFinishedNotification":
		return GroupUpdateFinishedNotification(client=self._client, group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.group_notifications_pb2.GroupUpdateFinishedNotification, client: OlvidClient = None) -> "GroupUpdateFinishedNotification":
		return GroupUpdateFinishedNotification(client, group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.group_notifications_pb2.GroupUpdateFinishedNotification], client: OlvidClient = None) -> list["GroupUpdateFinishedNotification"]:
		return [GroupUpdateFinishedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.group_notifications_pb2.GroupUpdateFinishedNotification], client: OlvidClient = None) -> "GroupUpdateFinishedNotification":
		native_message = await promise
		return GroupUpdateFinishedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupUpdateFinishedNotification"]):
		if messages is None:
			return []
		return [GroupUpdateFinishedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupUpdateFinishedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.group_notifications_pb2.GroupUpdateFinishedNotification(group_id=message.group_id if message.group_id else None)

	def __str__(self):
		s: str = ''
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupUpdateFinishedNotification):
			return False
		return self.group_id == other.group_id

	def __bool__(self):
		return self.group_id != 0

	def __hash__(self):
		return hash(self.group_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupUpdateFinishedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.group_id == 0 or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToIdentityCreatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_identity_created_notification: SubscribeToIdentityCreatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToIdentityCreatedNotification":
		return SubscribeToIdentityCreatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityCreatedNotification, client: OlvidClient = None) -> "SubscribeToIdentityCreatedNotification":
		return SubscribeToIdentityCreatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityCreatedNotification], client: OlvidClient = None) -> list["SubscribeToIdentityCreatedNotification"]:
		return [SubscribeToIdentityCreatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityCreatedNotification], client: OlvidClient = None) -> "SubscribeToIdentityCreatedNotification":
		native_message = await promise
		return SubscribeToIdentityCreatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToIdentityCreatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToIdentityCreatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToIdentityCreatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityCreatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToIdentityCreatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToIdentityCreatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityCreatedNotification:
	def __init__(self, client: OlvidClient = None, identity: "Identity" = None):
		self._client: OlvidClient = client
		self.identity: Identity = identity

	def _update_content(self, identity_created_notification: IdentityCreatedNotification) -> None:
		self.identity: Identity = identity_created_notification.identity

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityCreatedNotification":
		return IdentityCreatedNotification(client=self._client, identity=self.identity._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.identity_notifications_pb2.IdentityCreatedNotification, client: OlvidClient = None) -> "IdentityCreatedNotification":
		return IdentityCreatedNotification(client, identity=Identity._from_native(native_message.identity, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.identity_notifications_pb2.IdentityCreatedNotification], client: OlvidClient = None) -> list["IdentityCreatedNotification"]:
		return [IdentityCreatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.identity_notifications_pb2.IdentityCreatedNotification], client: OlvidClient = None) -> "IdentityCreatedNotification":
		native_message = await promise
		return IdentityCreatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityCreatedNotification"]):
		if messages is None:
			return []
		return [IdentityCreatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityCreatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.identity_notifications_pb2.IdentityCreatedNotification(identity=Identity._to_native(message.identity if message.identity else None))

	def __str__(self):
		s: str = ''
		if self.identity:
			s += f'identity: ({self.identity}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityCreatedNotification):
			return False
		return self.identity == other.identity

	def __bool__(self):
		return bool(self.identity)

	def __hash__(self):
		return hash(self.identity)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityCreatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity is None or self.identity._test_assertion(expected.identity)
		except AssertionError as e:
			raise AssertionError("identity: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToIdentityDeletedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_identity_deleted_notification: SubscribeToIdentityDeletedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToIdentityDeletedNotification":
		return SubscribeToIdentityDeletedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityDeletedNotification, client: OlvidClient = None) -> "SubscribeToIdentityDeletedNotification":
		return SubscribeToIdentityDeletedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityDeletedNotification], client: OlvidClient = None) -> list["SubscribeToIdentityDeletedNotification"]:
		return [SubscribeToIdentityDeletedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityDeletedNotification], client: OlvidClient = None) -> "SubscribeToIdentityDeletedNotification":
		native_message = await promise
		return SubscribeToIdentityDeletedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToIdentityDeletedNotification"]):
		if messages is None:
			return []
		return [SubscribeToIdentityDeletedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToIdentityDeletedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityDeletedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToIdentityDeletedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToIdentityDeletedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityDeletedNotification:
	def __init__(self, client: OlvidClient = None, identity: "Identity" = None):
		self._client: OlvidClient = client
		self.identity: Identity = identity

	def _update_content(self, identity_deleted_notification: IdentityDeletedNotification) -> None:
		self.identity: Identity = identity_deleted_notification.identity

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityDeletedNotification":
		return IdentityDeletedNotification(client=self._client, identity=self.identity._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.identity_notifications_pb2.IdentityDeletedNotification, client: OlvidClient = None) -> "IdentityDeletedNotification":
		return IdentityDeletedNotification(client, identity=Identity._from_native(native_message.identity, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.identity_notifications_pb2.IdentityDeletedNotification], client: OlvidClient = None) -> list["IdentityDeletedNotification"]:
		return [IdentityDeletedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.identity_notifications_pb2.IdentityDeletedNotification], client: OlvidClient = None) -> "IdentityDeletedNotification":
		native_message = await promise
		return IdentityDeletedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityDeletedNotification"]):
		if messages is None:
			return []
		return [IdentityDeletedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityDeletedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.identity_notifications_pb2.IdentityDeletedNotification(identity=Identity._to_native(message.identity if message.identity else None))

	def __str__(self):
		s: str = ''
		if self.identity:
			s += f'identity: ({self.identity}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityDeletedNotification):
			return False
		return self.identity == other.identity

	def __bool__(self):
		return bool(self.identity)

	def __hash__(self):
		return hash(self.identity)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityDeletedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity is None or self.identity._test_assertion(expected.identity)
		except AssertionError as e:
			raise AssertionError("identity: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToIdentityUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_identity_updated_notification: SubscribeToIdentityUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToIdentityUpdatedNotification":
		return SubscribeToIdentityUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityUpdatedNotification, client: OlvidClient = None) -> "SubscribeToIdentityUpdatedNotification":
		return SubscribeToIdentityUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToIdentityUpdatedNotification"]:
		return [SubscribeToIdentityUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityUpdatedNotification], client: OlvidClient = None) -> "SubscribeToIdentityUpdatedNotification":
		native_message = await promise
		return SubscribeToIdentityUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToIdentityUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToIdentityUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToIdentityUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.identity_notifications_pb2.SubscribeToIdentityUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToIdentityUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToIdentityUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityDetailsUpdatedNotification:
	def __init__(self, client: OlvidClient = None, identity: "Identity" = None, previous_details: "IdentityDetails" = None):
		self._client: OlvidClient = client
		self.identity: Identity = identity
		self.previous_details: IdentityDetails = previous_details

	def _update_content(self, identity_details_updated_notification: IdentityDetailsUpdatedNotification) -> None:
		self.identity: Identity = identity_details_updated_notification.identity
		self.previous_details: IdentityDetails = identity_details_updated_notification.previous_details

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityDetailsUpdatedNotification":
		return IdentityDetailsUpdatedNotification(client=self._client, identity=self.identity._clone(), previous_details=self.previous_details._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.identity_notifications_pb2.IdentityDetailsUpdatedNotification, client: OlvidClient = None) -> "IdentityDetailsUpdatedNotification":
		return IdentityDetailsUpdatedNotification(client, identity=Identity._from_native(native_message.identity, client=client), previous_details=IdentityDetails._from_native(native_message.previous_details, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.identity_notifications_pb2.IdentityDetailsUpdatedNotification], client: OlvidClient = None) -> list["IdentityDetailsUpdatedNotification"]:
		return [IdentityDetailsUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.identity_notifications_pb2.IdentityDetailsUpdatedNotification], client: OlvidClient = None) -> "IdentityDetailsUpdatedNotification":
		native_message = await promise
		return IdentityDetailsUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityDetailsUpdatedNotification"]):
		if messages is None:
			return []
		return [IdentityDetailsUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityDetailsUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.identity_notifications_pb2.IdentityDetailsUpdatedNotification(identity=Identity._to_native(message.identity if message.identity else None), previous_details=IdentityDetails._to_native(message.previous_details if message.previous_details else None))

	def __str__(self):
		s: str = ''
		if self.identity:
			s += f'identity: ({self.identity}), '
		if self.previous_details:
			s += f'previous_details: ({self.previous_details}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityDetailsUpdatedNotification):
			return False
		return self.identity == other.identity and self.previous_details == other.previous_details

	def __bool__(self):
		return bool(self.identity) or bool(self.previous_details)

	def __hash__(self):
		return hash((self.identity, self.previous_details))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityDetailsUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity is None or self.identity._test_assertion(expected.identity)
		except AssertionError as e:
			raise AssertionError("identity: " + str(e))
		try:
			assert expected.previous_details is None or self.previous_details._test_assertion(expected.previous_details)
		except AssertionError as e:
			raise AssertionError("previous_details: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToInvitationReceivedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_invitation_received_notification: SubscribeToInvitationReceivedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToInvitationReceivedNotification":
		return SubscribeToInvitationReceivedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationReceivedNotification, client: OlvidClient = None) -> "SubscribeToInvitationReceivedNotification":
		return SubscribeToInvitationReceivedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationReceivedNotification], client: OlvidClient = None) -> list["SubscribeToInvitationReceivedNotification"]:
		return [SubscribeToInvitationReceivedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationReceivedNotification], client: OlvidClient = None) -> "SubscribeToInvitationReceivedNotification":
		native_message = await promise
		return SubscribeToInvitationReceivedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToInvitationReceivedNotification"]):
		if messages is None:
			return []
		return [SubscribeToInvitationReceivedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToInvitationReceivedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationReceivedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToInvitationReceivedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToInvitationReceivedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationReceivedNotification:
	def __init__(self, client: OlvidClient = None, invitation: "Invitation" = None):
		self._client: OlvidClient = client
		self.invitation: Invitation = invitation

	def _update_content(self, invitation_received_notification: InvitationReceivedNotification) -> None:
		self.invitation: Invitation = invitation_received_notification.invitation

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationReceivedNotification":
		return InvitationReceivedNotification(client=self._client, invitation=self.invitation._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationReceivedNotification, client: OlvidClient = None) -> "InvitationReceivedNotification":
		return InvitationReceivedNotification(client, invitation=Invitation._from_native(native_message.invitation, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationReceivedNotification], client: OlvidClient = None) -> list["InvitationReceivedNotification"]:
		return [InvitationReceivedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationReceivedNotification], client: OlvidClient = None) -> "InvitationReceivedNotification":
		native_message = await promise
		return InvitationReceivedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationReceivedNotification"]):
		if messages is None:
			return []
		return [InvitationReceivedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationReceivedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationReceivedNotification(invitation=Invitation._to_native(message.invitation if message.invitation else None))

	def __str__(self):
		s: str = ''
		if self.invitation:
			s += f'invitation: ({self.invitation}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationReceivedNotification):
			return False
		return self.invitation == other.invitation

	def __bool__(self):
		return bool(self.invitation)

	def __hash__(self):
		return hash(self.invitation)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationReceivedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.invitation is None or self.invitation._test_assertion(expected.invitation)
		except AssertionError as e:
			raise AssertionError("invitation: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToInvitationSentNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_invitation_sent_notification: SubscribeToInvitationSentNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToInvitationSentNotification":
		return SubscribeToInvitationSentNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationSentNotification, client: OlvidClient = None) -> "SubscribeToInvitationSentNotification":
		return SubscribeToInvitationSentNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationSentNotification], client: OlvidClient = None) -> list["SubscribeToInvitationSentNotification"]:
		return [SubscribeToInvitationSentNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationSentNotification], client: OlvidClient = None) -> "SubscribeToInvitationSentNotification":
		native_message = await promise
		return SubscribeToInvitationSentNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToInvitationSentNotification"]):
		if messages is None:
			return []
		return [SubscribeToInvitationSentNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToInvitationSentNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationSentNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToInvitationSentNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToInvitationSentNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationSentNotification:
	def __init__(self, client: OlvidClient = None, invitation: "Invitation" = None):
		self._client: OlvidClient = client
		self.invitation: Invitation = invitation

	def _update_content(self, invitation_sent_notification: InvitationSentNotification) -> None:
		self.invitation: Invitation = invitation_sent_notification.invitation

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationSentNotification":
		return InvitationSentNotification(client=self._client, invitation=self.invitation._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationSentNotification, client: OlvidClient = None) -> "InvitationSentNotification":
		return InvitationSentNotification(client, invitation=Invitation._from_native(native_message.invitation, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationSentNotification], client: OlvidClient = None) -> list["InvitationSentNotification"]:
		return [InvitationSentNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationSentNotification], client: OlvidClient = None) -> "InvitationSentNotification":
		native_message = await promise
		return InvitationSentNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationSentNotification"]):
		if messages is None:
			return []
		return [InvitationSentNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationSentNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationSentNotification(invitation=Invitation._to_native(message.invitation if message.invitation else None))

	def __str__(self):
		s: str = ''
		if self.invitation:
			s += f'invitation: ({self.invitation}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationSentNotification):
			return False
		return self.invitation == other.invitation

	def __bool__(self):
		return bool(self.invitation)

	def __hash__(self):
		return hash(self.invitation)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationSentNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.invitation is None or self.invitation._test_assertion(expected.invitation)
		except AssertionError as e:
			raise AssertionError("invitation: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToInvitationDeletedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_invitation_deleted_notification: SubscribeToInvitationDeletedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToInvitationDeletedNotification":
		return SubscribeToInvitationDeletedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationDeletedNotification, client: OlvidClient = None) -> "SubscribeToInvitationDeletedNotification":
		return SubscribeToInvitationDeletedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationDeletedNotification], client: OlvidClient = None) -> list["SubscribeToInvitationDeletedNotification"]:
		return [SubscribeToInvitationDeletedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationDeletedNotification], client: OlvidClient = None) -> "SubscribeToInvitationDeletedNotification":
		native_message = await promise
		return SubscribeToInvitationDeletedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToInvitationDeletedNotification"]):
		if messages is None:
			return []
		return [SubscribeToInvitationDeletedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToInvitationDeletedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationDeletedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToInvitationDeletedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToInvitationDeletedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationDeletedNotification:
	def __init__(self, client: OlvidClient = None, invitation: "Invitation" = None):
		self._client: OlvidClient = client
		self.invitation: Invitation = invitation

	def _update_content(self, invitation_deleted_notification: InvitationDeletedNotification) -> None:
		self.invitation: Invitation = invitation_deleted_notification.invitation

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationDeletedNotification":
		return InvitationDeletedNotification(client=self._client, invitation=self.invitation._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationDeletedNotification, client: OlvidClient = None) -> "InvitationDeletedNotification":
		return InvitationDeletedNotification(client, invitation=Invitation._from_native(native_message.invitation, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationDeletedNotification], client: OlvidClient = None) -> list["InvitationDeletedNotification"]:
		return [InvitationDeletedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationDeletedNotification], client: OlvidClient = None) -> "InvitationDeletedNotification":
		native_message = await promise
		return InvitationDeletedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationDeletedNotification"]):
		if messages is None:
			return []
		return [InvitationDeletedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationDeletedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationDeletedNotification(invitation=Invitation._to_native(message.invitation if message.invitation else None))

	def __str__(self):
		s: str = ''
		if self.invitation:
			s += f'invitation: ({self.invitation}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationDeletedNotification):
			return False
		return self.invitation == other.invitation

	def __bool__(self):
		return bool(self.invitation)

	def __hash__(self):
		return hash(self.invitation)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationDeletedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.invitation is None or self.invitation._test_assertion(expected.invitation)
		except AssertionError as e:
			raise AssertionError("invitation: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToInvitationUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_invitation_updated_notification: SubscribeToInvitationUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToInvitationUpdatedNotification":
		return SubscribeToInvitationUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationUpdatedNotification, client: OlvidClient = None) -> "SubscribeToInvitationUpdatedNotification":
		return SubscribeToInvitationUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToInvitationUpdatedNotification"]:
		return [SubscribeToInvitationUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationUpdatedNotification], client: OlvidClient = None) -> "SubscribeToInvitationUpdatedNotification":
		native_message = await promise
		return SubscribeToInvitationUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToInvitationUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToInvitationUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToInvitationUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToInvitationUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToInvitationUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationUpdatedNotification:
	def __init__(self, client: OlvidClient = None, invitation: "Invitation" = None, previous_invitation_status: "Invitation.Status" = 0):
		self._client: OlvidClient = client
		self.invitation: Invitation = invitation
		self.previous_invitation_status: Invitation.Status = previous_invitation_status

	def _update_content(self, invitation_updated_notification: InvitationUpdatedNotification) -> None:
		self.invitation: Invitation = invitation_updated_notification.invitation
		self.previous_invitation_status: Invitation.Status = invitation_updated_notification.previous_invitation_status

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationUpdatedNotification":
		return InvitationUpdatedNotification(client=self._client, invitation=self.invitation._clone(), previous_invitation_status=self.previous_invitation_status)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationUpdatedNotification, client: OlvidClient = None) -> "InvitationUpdatedNotification":
		return InvitationUpdatedNotification(client, invitation=Invitation._from_native(native_message.invitation, client=client), previous_invitation_status=Invitation.Status(native_message.previous_invitation_status))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationUpdatedNotification], client: OlvidClient = None) -> list["InvitationUpdatedNotification"]:
		return [InvitationUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationUpdatedNotification], client: OlvidClient = None) -> "InvitationUpdatedNotification":
		native_message = await promise
		return InvitationUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationUpdatedNotification"]):
		if messages is None:
			return []
		return [InvitationUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationUpdatedNotification(invitation=Invitation._to_native(message.invitation if message.invitation else None), previous_invitation_status=message.previous_invitation_status.value if message.previous_invitation_status else None)

	def __str__(self):
		s: str = ''
		if self.invitation:
			s += f'invitation: ({self.invitation}), '
		if self.previous_invitation_status:
			s += f'previous_invitation_status: {self.previous_invitation_status}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationUpdatedNotification):
			return False
		return self.invitation == other.invitation and self.previous_invitation_status == other.previous_invitation_status

	def __bool__(self):
		return bool(self.invitation) or bool(self.previous_invitation_status)

	def __hash__(self):
		return hash((self.invitation, self.previous_invitation_status))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.invitation is None or self.invitation._test_assertion(expected.invitation)
		except AssertionError as e:
			raise AssertionError("invitation: " + str(e))
		assert expected.previous_invitation_status == 0 or self.previous_invitation_status == expected.previous_invitation_status, "Invalid value: previous_invitation_status: " + str(expected.previous_invitation_status) + " != " + str(self.previous_invitation_status)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageReceivedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_received_notification: SubscribeToMessageReceivedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageReceivedNotification":
		return SubscribeToMessageReceivedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReceivedNotification, client: OlvidClient = None) -> "SubscribeToMessageReceivedNotification":
		return SubscribeToMessageReceivedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReceivedNotification], client: OlvidClient = None) -> list["SubscribeToMessageReceivedNotification"]:
		return [SubscribeToMessageReceivedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReceivedNotification], client: OlvidClient = None) -> "SubscribeToMessageReceivedNotification":
		native_message = await promise
		return SubscribeToMessageReceivedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageReceivedNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageReceivedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageReceivedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReceivedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageReceivedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageReceivedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageReceivedNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_received_notification: MessageReceivedNotification) -> None:
		self.message: Message = message_received_notification.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageReceivedNotification":
		return MessageReceivedNotification(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageReceivedNotification, client: OlvidClient = None) -> "MessageReceivedNotification":
		return MessageReceivedNotification(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageReceivedNotification], client: OlvidClient = None) -> list["MessageReceivedNotification"]:
		return [MessageReceivedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageReceivedNotification], client: OlvidClient = None) -> "MessageReceivedNotification":
		native_message = await promise
		return MessageReceivedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageReceivedNotification"]):
		if messages is None:
			return []
		return [MessageReceivedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageReceivedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageReceivedNotification(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageReceivedNotification):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageReceivedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageSentNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_sent_notification: SubscribeToMessageSentNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageSentNotification":
		return SubscribeToMessageSentNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageSentNotification, client: OlvidClient = None) -> "SubscribeToMessageSentNotification":
		return SubscribeToMessageSentNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageSentNotification], client: OlvidClient = None) -> list["SubscribeToMessageSentNotification"]:
		return [SubscribeToMessageSentNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageSentNotification], client: OlvidClient = None) -> "SubscribeToMessageSentNotification":
		native_message = await promise
		return SubscribeToMessageSentNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageSentNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageSentNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageSentNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageSentNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageSentNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageSentNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageSentNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_sent_notification: MessageSentNotification) -> None:
		self.message: Message = message_sent_notification.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSentNotification":
		return MessageSentNotification(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageSentNotification, client: OlvidClient = None) -> "MessageSentNotification":
		return MessageSentNotification(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageSentNotification], client: OlvidClient = None) -> list["MessageSentNotification"]:
		return [MessageSentNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageSentNotification], client: OlvidClient = None) -> "MessageSentNotification":
		native_message = await promise
		return MessageSentNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageSentNotification"]):
		if messages is None:
			return []
		return [MessageSentNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageSentNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageSentNotification(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageSentNotification):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageSentNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageDeletedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_deleted_notification: SubscribeToMessageDeletedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageDeletedNotification":
		return SubscribeToMessageDeletedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageDeletedNotification, client: OlvidClient = None) -> "SubscribeToMessageDeletedNotification":
		return SubscribeToMessageDeletedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageDeletedNotification], client: OlvidClient = None) -> list["SubscribeToMessageDeletedNotification"]:
		return [SubscribeToMessageDeletedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageDeletedNotification], client: OlvidClient = None) -> "SubscribeToMessageDeletedNotification":
		native_message = await promise
		return SubscribeToMessageDeletedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageDeletedNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageDeletedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageDeletedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageDeletedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageDeletedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageDeletedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageDeletedNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_deleted_notification: MessageDeletedNotification) -> None:
		self.message: Message = message_deleted_notification.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageDeletedNotification":
		return MessageDeletedNotification(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageDeletedNotification, client: OlvidClient = None) -> "MessageDeletedNotification":
		return MessageDeletedNotification(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageDeletedNotification], client: OlvidClient = None) -> list["MessageDeletedNotification"]:
		return [MessageDeletedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageDeletedNotification], client: OlvidClient = None) -> "MessageDeletedNotification":
		native_message = await promise
		return MessageDeletedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageDeletedNotification"]):
		if messages is None:
			return []
		return [MessageDeletedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageDeletedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageDeletedNotification(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageDeletedNotification):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageDeletedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageBodyUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_body_updated_notification: SubscribeToMessageBodyUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageBodyUpdatedNotification":
		return SubscribeToMessageBodyUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageBodyUpdatedNotification, client: OlvidClient = None) -> "SubscribeToMessageBodyUpdatedNotification":
		return SubscribeToMessageBodyUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageBodyUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToMessageBodyUpdatedNotification"]:
		return [SubscribeToMessageBodyUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageBodyUpdatedNotification], client: OlvidClient = None) -> "SubscribeToMessageBodyUpdatedNotification":
		native_message = await promise
		return SubscribeToMessageBodyUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageBodyUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageBodyUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageBodyUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageBodyUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageBodyUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageBodyUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageBodyUpdatedNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None, previous_body: str = ""):
		self._client: OlvidClient = client
		self.message: Message = message
		self.previous_body: str = previous_body

	def _update_content(self, message_body_updated_notification: MessageBodyUpdatedNotification) -> None:
		self.message: Message = message_body_updated_notification.message
		self.previous_body: str = message_body_updated_notification.previous_body

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageBodyUpdatedNotification":
		return MessageBodyUpdatedNotification(client=self._client, message=self.message._clone(), previous_body=self.previous_body)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageBodyUpdatedNotification, client: OlvidClient = None) -> "MessageBodyUpdatedNotification":
		return MessageBodyUpdatedNotification(client, message=Message._from_native(native_message.message, client=client), previous_body=native_message.previous_body)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageBodyUpdatedNotification], client: OlvidClient = None) -> list["MessageBodyUpdatedNotification"]:
		return [MessageBodyUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageBodyUpdatedNotification], client: OlvidClient = None) -> "MessageBodyUpdatedNotification":
		native_message = await promise
		return MessageBodyUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageBodyUpdatedNotification"]):
		if messages is None:
			return []
		return [MessageBodyUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageBodyUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageBodyUpdatedNotification(message=Message._to_native(message.message if message.message else None), previous_body=message.previous_body if message.previous_body else None)

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		if self.previous_body:
			s += f'previous_body: {self.previous_body}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageBodyUpdatedNotification):
			return False
		return self.message == other.message and self.previous_body == other.previous_body

	def __bool__(self):
		return bool(self.message) or self.previous_body != ""

	def __hash__(self):
		return hash((self.message, self.previous_body))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageBodyUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		assert expected.previous_body == "" or self.previous_body == expected.previous_body, "Invalid value: previous_body: " + str(expected.previous_body) + " != " + str(self.previous_body)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageUploadedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_uploaded_notification: SubscribeToMessageUploadedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageUploadedNotification":
		return SubscribeToMessageUploadedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageUploadedNotification, client: OlvidClient = None) -> "SubscribeToMessageUploadedNotification":
		return SubscribeToMessageUploadedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageUploadedNotification], client: OlvidClient = None) -> list["SubscribeToMessageUploadedNotification"]:
		return [SubscribeToMessageUploadedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageUploadedNotification], client: OlvidClient = None) -> "SubscribeToMessageUploadedNotification":
		native_message = await promise
		return SubscribeToMessageUploadedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageUploadedNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageUploadedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageUploadedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageUploadedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageUploadedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageUploadedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageUploadedNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_uploaded_notification: MessageUploadedNotification) -> None:
		self.message: Message = message_uploaded_notification.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageUploadedNotification":
		return MessageUploadedNotification(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageUploadedNotification, client: OlvidClient = None) -> "MessageUploadedNotification":
		return MessageUploadedNotification(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageUploadedNotification], client: OlvidClient = None) -> list["MessageUploadedNotification"]:
		return [MessageUploadedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageUploadedNotification], client: OlvidClient = None) -> "MessageUploadedNotification":
		native_message = await promise
		return MessageUploadedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageUploadedNotification"]):
		if messages is None:
			return []
		return [MessageUploadedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageUploadedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageUploadedNotification(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageUploadedNotification):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageUploadedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageDeliveredNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_delivered_notification: SubscribeToMessageDeliveredNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageDeliveredNotification":
		return SubscribeToMessageDeliveredNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageDeliveredNotification, client: OlvidClient = None) -> "SubscribeToMessageDeliveredNotification":
		return SubscribeToMessageDeliveredNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageDeliveredNotification], client: OlvidClient = None) -> list["SubscribeToMessageDeliveredNotification"]:
		return [SubscribeToMessageDeliveredNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageDeliveredNotification], client: OlvidClient = None) -> "SubscribeToMessageDeliveredNotification":
		native_message = await promise
		return SubscribeToMessageDeliveredNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageDeliveredNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageDeliveredNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageDeliveredNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageDeliveredNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageDeliveredNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageDeliveredNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageDeliveredNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_delivered_notification: MessageDeliveredNotification) -> None:
		self.message: Message = message_delivered_notification.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageDeliveredNotification":
		return MessageDeliveredNotification(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageDeliveredNotification, client: OlvidClient = None) -> "MessageDeliveredNotification":
		return MessageDeliveredNotification(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageDeliveredNotification], client: OlvidClient = None) -> list["MessageDeliveredNotification"]:
		return [MessageDeliveredNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageDeliveredNotification], client: OlvidClient = None) -> "MessageDeliveredNotification":
		native_message = await promise
		return MessageDeliveredNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageDeliveredNotification"]):
		if messages is None:
			return []
		return [MessageDeliveredNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageDeliveredNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageDeliveredNotification(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageDeliveredNotification):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageDeliveredNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageReadNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_read_notification: SubscribeToMessageReadNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageReadNotification":
		return SubscribeToMessageReadNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReadNotification, client: OlvidClient = None) -> "SubscribeToMessageReadNotification":
		return SubscribeToMessageReadNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReadNotification], client: OlvidClient = None) -> list["SubscribeToMessageReadNotification"]:
		return [SubscribeToMessageReadNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReadNotification], client: OlvidClient = None) -> "SubscribeToMessageReadNotification":
		native_message = await promise
		return SubscribeToMessageReadNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageReadNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageReadNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageReadNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReadNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageReadNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageReadNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageReadNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_read_notification: MessageReadNotification) -> None:
		self.message: Message = message_read_notification.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageReadNotification":
		return MessageReadNotification(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageReadNotification, client: OlvidClient = None) -> "MessageReadNotification":
		return MessageReadNotification(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageReadNotification], client: OlvidClient = None) -> list["MessageReadNotification"]:
		return [MessageReadNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageReadNotification], client: OlvidClient = None) -> "MessageReadNotification":
		native_message = await promise
		return MessageReadNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageReadNotification"]):
		if messages is None:
			return []
		return [MessageReadNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageReadNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageReadNotification(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageReadNotification):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageReadNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageLocationReceivedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_location_received_notification: SubscribeToMessageLocationReceivedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageLocationReceivedNotification":
		return SubscribeToMessageLocationReceivedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationReceivedNotification, client: OlvidClient = None) -> "SubscribeToMessageLocationReceivedNotification":
		return SubscribeToMessageLocationReceivedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationReceivedNotification], client: OlvidClient = None) -> list["SubscribeToMessageLocationReceivedNotification"]:
		return [SubscribeToMessageLocationReceivedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationReceivedNotification], client: OlvidClient = None) -> "SubscribeToMessageLocationReceivedNotification":
		native_message = await promise
		return SubscribeToMessageLocationReceivedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageLocationReceivedNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageLocationReceivedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageLocationReceivedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationReceivedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageLocationReceivedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageLocationReceivedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageLocationReceivedNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_location_received_notification: MessageLocationReceivedNotification) -> None:
		self.message: Message = message_location_received_notification.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageLocationReceivedNotification":
		return MessageLocationReceivedNotification(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationReceivedNotification, client: OlvidClient = None) -> "MessageLocationReceivedNotification":
		return MessageLocationReceivedNotification(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationReceivedNotification], client: OlvidClient = None) -> list["MessageLocationReceivedNotification"]:
		return [MessageLocationReceivedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationReceivedNotification], client: OlvidClient = None) -> "MessageLocationReceivedNotification":
		native_message = await promise
		return MessageLocationReceivedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageLocationReceivedNotification"]):
		if messages is None:
			return []
		return [MessageLocationReceivedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageLocationReceivedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationReceivedNotification(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageLocationReceivedNotification):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageLocationReceivedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageLocationSharingStartNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_location_sharing_start_notification: SubscribeToMessageLocationSharingStartNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageLocationSharingStartNotification":
		return SubscribeToMessageLocationSharingStartNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingStartNotification, client: OlvidClient = None) -> "SubscribeToMessageLocationSharingStartNotification":
		return SubscribeToMessageLocationSharingStartNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingStartNotification], client: OlvidClient = None) -> list["SubscribeToMessageLocationSharingStartNotification"]:
		return [SubscribeToMessageLocationSharingStartNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingStartNotification], client: OlvidClient = None) -> "SubscribeToMessageLocationSharingStartNotification":
		native_message = await promise
		return SubscribeToMessageLocationSharingStartNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageLocationSharingStartNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageLocationSharingStartNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageLocationSharingStartNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingStartNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageLocationSharingStartNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageLocationSharingStartNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageLocationSharingStartNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_location_sharing_start_notification: MessageLocationSharingStartNotification) -> None:
		self.message: Message = message_location_sharing_start_notification.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageLocationSharingStartNotification":
		return MessageLocationSharingStartNotification(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingStartNotification, client: OlvidClient = None) -> "MessageLocationSharingStartNotification":
		return MessageLocationSharingStartNotification(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingStartNotification], client: OlvidClient = None) -> list["MessageLocationSharingStartNotification"]:
		return [MessageLocationSharingStartNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingStartNotification], client: OlvidClient = None) -> "MessageLocationSharingStartNotification":
		native_message = await promise
		return MessageLocationSharingStartNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageLocationSharingStartNotification"]):
		if messages is None:
			return []
		return [MessageLocationSharingStartNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageLocationSharingStartNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingStartNotification(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageLocationSharingStartNotification):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageLocationSharingStartNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageLocationSharingUpdateNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_location_sharing_update_notification: SubscribeToMessageLocationSharingUpdateNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageLocationSharingUpdateNotification":
		return SubscribeToMessageLocationSharingUpdateNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingUpdateNotification, client: OlvidClient = None) -> "SubscribeToMessageLocationSharingUpdateNotification":
		return SubscribeToMessageLocationSharingUpdateNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingUpdateNotification], client: OlvidClient = None) -> list["SubscribeToMessageLocationSharingUpdateNotification"]:
		return [SubscribeToMessageLocationSharingUpdateNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingUpdateNotification], client: OlvidClient = None) -> "SubscribeToMessageLocationSharingUpdateNotification":
		native_message = await promise
		return SubscribeToMessageLocationSharingUpdateNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageLocationSharingUpdateNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageLocationSharingUpdateNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageLocationSharingUpdateNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingUpdateNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageLocationSharingUpdateNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageLocationSharingUpdateNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageLocationSharingUpdateNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None, previous_location: "MessageLocation" = None):
		self._client: OlvidClient = client
		self.message: Message = message
		self.previous_location: MessageLocation = previous_location

	def _update_content(self, message_location_sharing_update_notification: MessageLocationSharingUpdateNotification) -> None:
		self.message: Message = message_location_sharing_update_notification.message
		self.previous_location: MessageLocation = message_location_sharing_update_notification.previous_location

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageLocationSharingUpdateNotification":
		return MessageLocationSharingUpdateNotification(client=self._client, message=self.message._clone(), previous_location=self.previous_location._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingUpdateNotification, client: OlvidClient = None) -> "MessageLocationSharingUpdateNotification":
		return MessageLocationSharingUpdateNotification(client, message=Message._from_native(native_message.message, client=client), previous_location=MessageLocation._from_native(native_message.previous_location, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingUpdateNotification], client: OlvidClient = None) -> list["MessageLocationSharingUpdateNotification"]:
		return [MessageLocationSharingUpdateNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingUpdateNotification], client: OlvidClient = None) -> "MessageLocationSharingUpdateNotification":
		native_message = await promise
		return MessageLocationSharingUpdateNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageLocationSharingUpdateNotification"]):
		if messages is None:
			return []
		return [MessageLocationSharingUpdateNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageLocationSharingUpdateNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingUpdateNotification(message=Message._to_native(message.message if message.message else None), previous_location=MessageLocation._to_native(message.previous_location if message.previous_location else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		if self.previous_location:
			s += f'previous_location: ({self.previous_location}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageLocationSharingUpdateNotification):
			return False
		return self.message == other.message and self.previous_location == other.previous_location

	def __bool__(self):
		return bool(self.message) or bool(self.previous_location)

	def __hash__(self):
		return hash((self.message, self.previous_location))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageLocationSharingUpdateNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		try:
			assert expected.previous_location is None or self.previous_location._test_assertion(expected.previous_location)
		except AssertionError as e:
			raise AssertionError("previous_location: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageLocationSharingEndNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_location_sharing_end_notification: SubscribeToMessageLocationSharingEndNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageLocationSharingEndNotification":
		return SubscribeToMessageLocationSharingEndNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingEndNotification, client: OlvidClient = None) -> "SubscribeToMessageLocationSharingEndNotification":
		return SubscribeToMessageLocationSharingEndNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingEndNotification], client: OlvidClient = None) -> list["SubscribeToMessageLocationSharingEndNotification"]:
		return [SubscribeToMessageLocationSharingEndNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingEndNotification], client: OlvidClient = None) -> "SubscribeToMessageLocationSharingEndNotification":
		native_message = await promise
		return SubscribeToMessageLocationSharingEndNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageLocationSharingEndNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageLocationSharingEndNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageLocationSharingEndNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingEndNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageLocationSharingEndNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageLocationSharingEndNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageLocationSharingEndNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_location_sharing_end_notification: MessageLocationSharingEndNotification) -> None:
		self.message: Message = message_location_sharing_end_notification.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageLocationSharingEndNotification":
		return MessageLocationSharingEndNotification(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingEndNotification, client: OlvidClient = None) -> "MessageLocationSharingEndNotification":
		return MessageLocationSharingEndNotification(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingEndNotification], client: OlvidClient = None) -> list["MessageLocationSharingEndNotification"]:
		return [MessageLocationSharingEndNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingEndNotification], client: OlvidClient = None) -> "MessageLocationSharingEndNotification":
		native_message = await promise
		return MessageLocationSharingEndNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageLocationSharingEndNotification"]):
		if messages is None:
			return []
		return [MessageLocationSharingEndNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageLocationSharingEndNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingEndNotification(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageLocationSharingEndNotification):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageLocationSharingEndNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageReactionAddedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_reaction_added_notification: SubscribeToMessageReactionAddedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageReactionAddedNotification":
		return SubscribeToMessageReactionAddedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionAddedNotification, client: OlvidClient = None) -> "SubscribeToMessageReactionAddedNotification":
		return SubscribeToMessageReactionAddedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionAddedNotification], client: OlvidClient = None) -> list["SubscribeToMessageReactionAddedNotification"]:
		return [SubscribeToMessageReactionAddedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionAddedNotification], client: OlvidClient = None) -> "SubscribeToMessageReactionAddedNotification":
		native_message = await promise
		return SubscribeToMessageReactionAddedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageReactionAddedNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageReactionAddedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageReactionAddedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionAddedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageReactionAddedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageReactionAddedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageReactionAddedNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None, reaction: "MessageReaction" = None):
		self._client: OlvidClient = client
		self.message: Message = message
		self.reaction: MessageReaction = reaction

	def _update_content(self, message_reaction_added_notification: MessageReactionAddedNotification) -> None:
		self.message: Message = message_reaction_added_notification.message
		self.reaction: MessageReaction = message_reaction_added_notification.reaction

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageReactionAddedNotification":
		return MessageReactionAddedNotification(client=self._client, message=self.message._clone(), reaction=self.reaction._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionAddedNotification, client: OlvidClient = None) -> "MessageReactionAddedNotification":
		return MessageReactionAddedNotification(client, message=Message._from_native(native_message.message, client=client), reaction=MessageReaction._from_native(native_message.reaction, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionAddedNotification], client: OlvidClient = None) -> list["MessageReactionAddedNotification"]:
		return [MessageReactionAddedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionAddedNotification], client: OlvidClient = None) -> "MessageReactionAddedNotification":
		native_message = await promise
		return MessageReactionAddedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageReactionAddedNotification"]):
		if messages is None:
			return []
		return [MessageReactionAddedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageReactionAddedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionAddedNotification(message=Message._to_native(message.message if message.message else None), reaction=MessageReaction._to_native(message.reaction if message.reaction else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		if self.reaction:
			s += f'reaction: ({self.reaction}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageReactionAddedNotification):
			return False
		return self.message == other.message and self.reaction == other.reaction

	def __bool__(self):
		return bool(self.message) or bool(self.reaction)

	def __hash__(self):
		return hash((self.message, self.reaction))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageReactionAddedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		try:
			assert expected.reaction is None or self.reaction._test_assertion(expected.reaction)
		except AssertionError as e:
			raise AssertionError("reaction: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageReactionUpdatedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_reaction_updated_notification: SubscribeToMessageReactionUpdatedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageReactionUpdatedNotification":
		return SubscribeToMessageReactionUpdatedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionUpdatedNotification, client: OlvidClient = None) -> "SubscribeToMessageReactionUpdatedNotification":
		return SubscribeToMessageReactionUpdatedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionUpdatedNotification], client: OlvidClient = None) -> list["SubscribeToMessageReactionUpdatedNotification"]:
		return [SubscribeToMessageReactionUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionUpdatedNotification], client: OlvidClient = None) -> "SubscribeToMessageReactionUpdatedNotification":
		native_message = await promise
		return SubscribeToMessageReactionUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageReactionUpdatedNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageReactionUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageReactionUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionUpdatedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageReactionUpdatedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageReactionUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageReactionUpdatedNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None, reaction: "MessageReaction" = None, previous_reaction: "MessageReaction" = None):
		self._client: OlvidClient = client
		self.message: Message = message
		self.reaction: MessageReaction = reaction
		self.previous_reaction: MessageReaction = previous_reaction

	def _update_content(self, message_reaction_updated_notification: MessageReactionUpdatedNotification) -> None:
		self.message: Message = message_reaction_updated_notification.message
		self.reaction: MessageReaction = message_reaction_updated_notification.reaction
		self.previous_reaction: MessageReaction = message_reaction_updated_notification.previous_reaction

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageReactionUpdatedNotification":
		return MessageReactionUpdatedNotification(client=self._client, message=self.message._clone(), reaction=self.reaction._clone(), previous_reaction=self.previous_reaction._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionUpdatedNotification, client: OlvidClient = None) -> "MessageReactionUpdatedNotification":
		return MessageReactionUpdatedNotification(client, message=Message._from_native(native_message.message, client=client), reaction=MessageReaction._from_native(native_message.reaction, client=client), previous_reaction=MessageReaction._from_native(native_message.previous_reaction, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionUpdatedNotification], client: OlvidClient = None) -> list["MessageReactionUpdatedNotification"]:
		return [MessageReactionUpdatedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionUpdatedNotification], client: OlvidClient = None) -> "MessageReactionUpdatedNotification":
		native_message = await promise
		return MessageReactionUpdatedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageReactionUpdatedNotification"]):
		if messages is None:
			return []
		return [MessageReactionUpdatedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageReactionUpdatedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionUpdatedNotification(message=Message._to_native(message.message if message.message else None), reaction=MessageReaction._to_native(message.reaction if message.reaction else None), previous_reaction=MessageReaction._to_native(message.previous_reaction if message.previous_reaction else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		if self.reaction:
			s += f'reaction: ({self.reaction}), '
		if self.previous_reaction:
			s += f'previous_reaction: ({self.previous_reaction}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageReactionUpdatedNotification):
			return False
		return self.message == other.message and self.reaction == other.reaction and self.previous_reaction == other.previous_reaction

	def __bool__(self):
		return bool(self.message) or bool(self.reaction) or bool(self.previous_reaction)

	def __hash__(self):
		return hash((self.message, self.reaction, self.previous_reaction))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageReactionUpdatedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		try:
			assert expected.reaction is None or self.reaction._test_assertion(expected.reaction)
		except AssertionError as e:
			raise AssertionError("reaction: " + str(e))
		try:
			assert expected.previous_reaction is None or self.previous_reaction._test_assertion(expected.previous_reaction)
		except AssertionError as e:
			raise AssertionError("previous_reaction: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SubscribeToMessageReactionRemovedNotification:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, subscribe_to_message_reaction_removed_notification: SubscribeToMessageReactionRemovedNotification) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SubscribeToMessageReactionRemovedNotification":
		return SubscribeToMessageReactionRemovedNotification(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionRemovedNotification, client: OlvidClient = None) -> "SubscribeToMessageReactionRemovedNotification":
		return SubscribeToMessageReactionRemovedNotification(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionRemovedNotification], client: OlvidClient = None) -> list["SubscribeToMessageReactionRemovedNotification"]:
		return [SubscribeToMessageReactionRemovedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionRemovedNotification], client: OlvidClient = None) -> "SubscribeToMessageReactionRemovedNotification":
		native_message = await promise
		return SubscribeToMessageReactionRemovedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SubscribeToMessageReactionRemovedNotification"]):
		if messages is None:
			return []
		return [SubscribeToMessageReactionRemovedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SubscribeToMessageReactionRemovedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionRemovedNotification()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SubscribeToMessageReactionRemovedNotification):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SubscribeToMessageReactionRemovedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageReactionRemovedNotification:
	def __init__(self, client: OlvidClient = None, message: "Message" = None, reaction: "MessageReaction" = None):
		self._client: OlvidClient = client
		self.message: Message = message
		self.reaction: MessageReaction = reaction

	def _update_content(self, message_reaction_removed_notification: MessageReactionRemovedNotification) -> None:
		self.message: Message = message_reaction_removed_notification.message
		self.reaction: MessageReaction = message_reaction_removed_notification.reaction

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageReactionRemovedNotification":
		return MessageReactionRemovedNotification(client=self._client, message=self.message._clone(), reaction=self.reaction._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionRemovedNotification, client: OlvidClient = None) -> "MessageReactionRemovedNotification":
		return MessageReactionRemovedNotification(client, message=Message._from_native(native_message.message, client=client), reaction=MessageReaction._from_native(native_message.reaction, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionRemovedNotification], client: OlvidClient = None) -> list["MessageReactionRemovedNotification"]:
		return [MessageReactionRemovedNotification._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionRemovedNotification], client: OlvidClient = None) -> "MessageReactionRemovedNotification":
		native_message = await promise
		return MessageReactionRemovedNotification._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageReactionRemovedNotification"]):
		if messages is None:
			return []
		return [MessageReactionRemovedNotification._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageReactionRemovedNotification"]):
		if message is None:
			return None
		return olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionRemovedNotification(message=Message._to_native(message.message if message.message else None), reaction=MessageReaction._to_native(message.reaction if message.reaction else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		if self.reaction:
			s += f'reaction: ({self.reaction}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageReactionRemovedNotification):
			return False
		return self.message == other.message and self.reaction == other.reaction

	def __bool__(self):
		return bool(self.message) or bool(self.reaction)

	def __hash__(self):
		return hash((self.message, self.reaction))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageReactionRemovedNotification):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		try:
			assert expected.reaction is None or self.reaction._test_assertion(expected.reaction)
		except AssertionError as e:
			raise AssertionError("reaction: " + str(e))
		return True


class InvitationNotificationServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.notification_service_pb2_grpc.InvitationNotificationServiceStub = olvid.daemon.services.v1.notification_service_pb2_grpc.InvitationNotificationServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_received(self, subscribe_to_invitation_received_notification: SubscribeToInvitationReceivedNotification) -> AsyncIterator[InvitationReceivedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationReceivedNotification]) -> AsyncIterator[InvitationReceivedNotification]:
			async for native_message in iterator.__aiter__():
				yield InvitationReceivedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_invitation_received_notification
		return response_iterator(self.__stub.InvitationReceived(olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationReceivedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_sent(self, subscribe_to_invitation_sent_notification: SubscribeToInvitationSentNotification) -> AsyncIterator[InvitationSentNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationSentNotification]) -> AsyncIterator[InvitationSentNotification]:
			async for native_message in iterator.__aiter__():
				yield InvitationSentNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_invitation_sent_notification
		return response_iterator(self.__stub.InvitationSent(olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationSentNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_deleted(self, subscribe_to_invitation_deleted_notification: SubscribeToInvitationDeletedNotification) -> AsyncIterator[InvitationDeletedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationDeletedNotification]) -> AsyncIterator[InvitationDeletedNotification]:
			async for native_message in iterator.__aiter__():
				yield InvitationDeletedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_invitation_deleted_notification
		return response_iterator(self.__stub.InvitationDeleted(olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationDeletedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_updated(self, subscribe_to_invitation_updated_notification: SubscribeToInvitationUpdatedNotification) -> AsyncIterator[InvitationUpdatedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.invitation_notifications_pb2.InvitationUpdatedNotification]) -> AsyncIterator[InvitationUpdatedNotification]:
			async for native_message in iterator.__aiter__():
				yield InvitationUpdatedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_invitation_updated_notification
		return response_iterator(self.__stub.InvitationUpdated(olvid.daemon.notification.v1.invitation_notifications_pb2.SubscribeToInvitationUpdatedNotification(), metadata=self._client.grpc_metadata))


class ContactNotificationServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.notification_service_pb2_grpc.ContactNotificationServiceStub = olvid.daemon.services.v1.notification_service_pb2_grpc.ContactNotificationServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_new(self, subscribe_to_contact_new_notification: SubscribeToContactNewNotification) -> AsyncIterator[ContactNewNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.contact_notifications_pb2.ContactNewNotification]) -> AsyncIterator[ContactNewNotification]:
			async for native_message in iterator.__aiter__():
				yield ContactNewNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_contact_new_notification
		return response_iterator(self.__stub.ContactNew(olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactNewNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_deleted(self, subscribe_to_contact_deleted_notification: SubscribeToContactDeletedNotification) -> AsyncIterator[ContactDeletedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.contact_notifications_pb2.ContactDeletedNotification]) -> AsyncIterator[ContactDeletedNotification]:
			async for native_message in iterator.__aiter__():
				yield ContactDeletedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_contact_deleted_notification
		return response_iterator(self.__stub.ContactDeleted(olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactDeletedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_details_updated(self, subscribe_to_contact_details_updated_notification: SubscribeToContactDetailsUpdatedNotification) -> AsyncIterator[ContactDetailsUpdatedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.contact_notifications_pb2.ContactDetailsUpdatedNotification]) -> AsyncIterator[ContactDetailsUpdatedNotification]:
			async for native_message in iterator.__aiter__():
				yield ContactDetailsUpdatedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_contact_details_updated_notification
		return response_iterator(self.__stub.ContactDetailsUpdated(olvid.daemon.notification.v1.contact_notifications_pb2.SubscribeToContactDetailsUpdatedNotification(), metadata=self._client.grpc_metadata))


class GroupNotificationServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.notification_service_pb2_grpc.GroupNotificationServiceStub = olvid.daemon.services.v1.notification_service_pb2_grpc.GroupNotificationServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_new(self, subscribe_to_group_new_notification: SubscribeToGroupNewNotification) -> AsyncIterator[GroupNewNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupNewNotification]) -> AsyncIterator[GroupNewNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupNewNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_new_notification
		return response_iterator(self.__stub.GroupNew(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupNewNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_deleted(self, subscribe_to_group_deleted_notification: SubscribeToGroupDeletedNotification) -> AsyncIterator[GroupDeletedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupDeletedNotification]) -> AsyncIterator[GroupDeletedNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupDeletedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_deleted_notification
		return response_iterator(self.__stub.GroupDeleted(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupDeletedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_name_updated(self, subscribe_to_group_name_updated_notification: SubscribeToGroupNameUpdatedNotification) -> AsyncIterator[GroupNameUpdatedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupNameUpdatedNotification]) -> AsyncIterator[GroupNameUpdatedNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupNameUpdatedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_name_updated_notification
		return response_iterator(self.__stub.GroupNameUpdated(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupNameUpdatedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_description_updated(self, subscribe_to_group_description_updated_notification: SubscribeToGroupDescriptionUpdatedNotification) -> AsyncIterator[GroupDescriptionUpdatedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupDescriptionUpdatedNotification]) -> AsyncIterator[GroupDescriptionUpdatedNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupDescriptionUpdatedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_description_updated_notification
		return response_iterator(self.__stub.GroupDescriptionUpdated(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupDescriptionUpdatedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_pending_member_added(self, subscribe_to_group_pending_member_added_notification: SubscribeToGroupPendingMemberAddedNotification) -> AsyncIterator[GroupPendingMemberAddedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupPendingMemberAddedNotification]) -> AsyncIterator[GroupPendingMemberAddedNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupPendingMemberAddedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_pending_member_added_notification
		return response_iterator(self.__stub.GroupPendingMemberAdded(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupPendingMemberAddedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_pending_member_removed(self, subscribe_to_group_pending_member_removed_notification: SubscribeToGroupPendingMemberRemovedNotification) -> AsyncIterator[GroupPendingMemberRemovedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupPendingMemberRemovedNotification]) -> AsyncIterator[GroupPendingMemberRemovedNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupPendingMemberRemovedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_pending_member_removed_notification
		return response_iterator(self.__stub.GroupPendingMemberRemoved(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupPendingMemberRemovedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_member_joined(self, subscribe_to_group_member_joined_notification: SubscribeToGroupMemberJoinedNotification) -> AsyncIterator[GroupMemberJoinedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberJoinedNotification]) -> AsyncIterator[GroupMemberJoinedNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupMemberJoinedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_member_joined_notification
		return response_iterator(self.__stub.GroupMemberJoined(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberJoinedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_member_left(self, subscribe_to_group_member_left_notification: SubscribeToGroupMemberLeftNotification) -> AsyncIterator[GroupMemberLeftNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberLeftNotification]) -> AsyncIterator[GroupMemberLeftNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupMemberLeftNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_member_left_notification
		return response_iterator(self.__stub.GroupMemberLeft(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberLeftNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_own_permissions_updated(self, subscribe_to_group_own_permissions_updated_notification: SubscribeToGroupOwnPermissionsUpdatedNotification) -> AsyncIterator[GroupOwnPermissionsUpdatedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupOwnPermissionsUpdatedNotification]) -> AsyncIterator[GroupOwnPermissionsUpdatedNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupOwnPermissionsUpdatedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_own_permissions_updated_notification
		return response_iterator(self.__stub.GroupOwnPermissionsUpdated(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupOwnPermissionsUpdatedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_member_permissions_updated(self, subscribe_to_group_member_permissions_updated_notification: SubscribeToGroupMemberPermissionsUpdatedNotification) -> AsyncIterator[GroupMemberPermissionsUpdatedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupMemberPermissionsUpdatedNotification]) -> AsyncIterator[GroupMemberPermissionsUpdatedNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupMemberPermissionsUpdatedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_member_permissions_updated_notification
		return response_iterator(self.__stub.GroupMemberPermissionsUpdated(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupMemberPermissionsUpdatedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_update_in_progress(self, subscribe_to_group_update_in_progress_notification: SubscribeToGroupUpdateInProgressNotification) -> AsyncIterator[GroupUpdateInProgressNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupUpdateInProgressNotification]) -> AsyncIterator[GroupUpdateInProgressNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupUpdateInProgressNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_update_in_progress_notification
		return response_iterator(self.__stub.GroupUpdateInProgress(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupUpdateInProgressNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_update_finished(self, subscribe_to_group_update_finished_notification: SubscribeToGroupUpdateFinishedNotification) -> AsyncIterator[GroupUpdateFinishedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.group_notifications_pb2.GroupUpdateFinishedNotification]) -> AsyncIterator[GroupUpdateFinishedNotification]:
			async for native_message in iterator.__aiter__():
				yield GroupUpdateFinishedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_group_update_finished_notification
		return response_iterator(self.__stub.GroupUpdateFinished(olvid.daemon.notification.v1.group_notifications_pb2.SubscribeToGroupUpdateFinishedNotification(), metadata=self._client.grpc_metadata))


class DiscussionNotificationServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.notification_service_pb2_grpc.DiscussionNotificationServiceStub = olvid.daemon.services.v1.notification_service_pb2_grpc.DiscussionNotificationServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_new(self, subscribe_to_discussion_new_notification: SubscribeToDiscussionNewNotification) -> AsyncIterator[DiscussionNewNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionNewNotification]) -> AsyncIterator[DiscussionNewNotification]:
			async for native_message in iterator.__aiter__():
				yield DiscussionNewNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_discussion_new_notification
		return response_iterator(self.__stub.DiscussionNew(olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionNewNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_locked(self, subscribe_to_discussion_locked_notification: SubscribeToDiscussionLockedNotification) -> AsyncIterator[DiscussionLockedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionLockedNotification]) -> AsyncIterator[DiscussionLockedNotification]:
			async for native_message in iterator.__aiter__():
				yield DiscussionLockedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_discussion_locked_notification
		return response_iterator(self.__stub.DiscussionLocked(olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionLockedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_title_updated(self, subscribe_to_discussion_title_updated_notification: SubscribeToDiscussionTitleUpdatedNotification) -> AsyncIterator[DiscussionTitleUpdatedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionTitleUpdatedNotification]) -> AsyncIterator[DiscussionTitleUpdatedNotification]:
			async for native_message in iterator.__aiter__():
				yield DiscussionTitleUpdatedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_discussion_title_updated_notification
		return response_iterator(self.__stub.DiscussionTitleUpdated(olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionTitleUpdatedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_settings_updated(self, subscribe_to_discussion_settings_updated_notification: SubscribeToDiscussionSettingsUpdatedNotification) -> AsyncIterator[DiscussionSettingsUpdatedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.discussion_notifications_pb2.DiscussionSettingsUpdatedNotification]) -> AsyncIterator[DiscussionSettingsUpdatedNotification]:
			async for native_message in iterator.__aiter__():
				yield DiscussionSettingsUpdatedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_discussion_settings_updated_notification
		return response_iterator(self.__stub.DiscussionSettingsUpdated(olvid.daemon.notification.v1.discussion_notifications_pb2.SubscribeToDiscussionSettingsUpdatedNotification(), metadata=self._client.grpc_metadata))


class MessageNotificationServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.notification_service_pb2_grpc.MessageNotificationServiceStub = olvid.daemon.services.v1.notification_service_pb2_grpc.MessageNotificationServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_received(self, subscribe_to_message_received_notification: SubscribeToMessageReceivedNotification) -> AsyncIterator[MessageReceivedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageReceivedNotification]) -> AsyncIterator[MessageReceivedNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageReceivedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_received_notification
		return response_iterator(self.__stub.MessageReceived(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReceivedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_sent(self, subscribe_to_message_sent_notification: SubscribeToMessageSentNotification) -> AsyncIterator[MessageSentNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageSentNotification]) -> AsyncIterator[MessageSentNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageSentNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_sent_notification
		return response_iterator(self.__stub.MessageSent(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageSentNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_deleted(self, subscribe_to_message_deleted_notification: SubscribeToMessageDeletedNotification) -> AsyncIterator[MessageDeletedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageDeletedNotification]) -> AsyncIterator[MessageDeletedNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageDeletedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_deleted_notification
		return response_iterator(self.__stub.MessageDeleted(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageDeletedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_body_updated(self, subscribe_to_message_body_updated_notification: SubscribeToMessageBodyUpdatedNotification) -> AsyncIterator[MessageBodyUpdatedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageBodyUpdatedNotification]) -> AsyncIterator[MessageBodyUpdatedNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageBodyUpdatedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_body_updated_notification
		return response_iterator(self.__stub.MessageBodyUpdated(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageBodyUpdatedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_uploaded(self, subscribe_to_message_uploaded_notification: SubscribeToMessageUploadedNotification) -> AsyncIterator[MessageUploadedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageUploadedNotification]) -> AsyncIterator[MessageUploadedNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageUploadedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_uploaded_notification
		return response_iterator(self.__stub.MessageUploaded(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageUploadedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_delivered(self, subscribe_to_message_delivered_notification: SubscribeToMessageDeliveredNotification) -> AsyncIterator[MessageDeliveredNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageDeliveredNotification]) -> AsyncIterator[MessageDeliveredNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageDeliveredNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_delivered_notification
		return response_iterator(self.__stub.MessageDelivered(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageDeliveredNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_read(self, subscribe_to_message_read_notification: SubscribeToMessageReadNotification) -> AsyncIterator[MessageReadNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageReadNotification]) -> AsyncIterator[MessageReadNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageReadNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_read_notification
		return response_iterator(self.__stub.MessageRead(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReadNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_location_received(self, subscribe_to_message_location_received_notification: SubscribeToMessageLocationReceivedNotification) -> AsyncIterator[MessageLocationReceivedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationReceivedNotification]) -> AsyncIterator[MessageLocationReceivedNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageLocationReceivedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_location_received_notification
		return response_iterator(self.__stub.MessageLocationReceived(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationReceivedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_location_sharing_start(self, subscribe_to_message_location_sharing_start_notification: SubscribeToMessageLocationSharingStartNotification) -> AsyncIterator[MessageLocationSharingStartNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingStartNotification]) -> AsyncIterator[MessageLocationSharingStartNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageLocationSharingStartNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_location_sharing_start_notification
		return response_iterator(self.__stub.MessageLocationSharingStart(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingStartNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_location_sharing_update(self, subscribe_to_message_location_sharing_update_notification: SubscribeToMessageLocationSharingUpdateNotification) -> AsyncIterator[MessageLocationSharingUpdateNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingUpdateNotification]) -> AsyncIterator[MessageLocationSharingUpdateNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageLocationSharingUpdateNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_location_sharing_update_notification
		return response_iterator(self.__stub.MessageLocationSharingUpdate(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingUpdateNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_location_sharing_end(self, subscribe_to_message_location_sharing_end_notification: SubscribeToMessageLocationSharingEndNotification) -> AsyncIterator[MessageLocationSharingEndNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageLocationSharingEndNotification]) -> AsyncIterator[MessageLocationSharingEndNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageLocationSharingEndNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_location_sharing_end_notification
		return response_iterator(self.__stub.MessageLocationSharingEnd(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageLocationSharingEndNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_reaction_added(self, subscribe_to_message_reaction_added_notification: SubscribeToMessageReactionAddedNotification) -> AsyncIterator[MessageReactionAddedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionAddedNotification]) -> AsyncIterator[MessageReactionAddedNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageReactionAddedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_reaction_added_notification
		return response_iterator(self.__stub.MessageReactionAdded(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionAddedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_reaction_updated(self, subscribe_to_message_reaction_updated_notification: SubscribeToMessageReactionUpdatedNotification) -> AsyncIterator[MessageReactionUpdatedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionUpdatedNotification]) -> AsyncIterator[MessageReactionUpdatedNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageReactionUpdatedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_reaction_updated_notification
		return response_iterator(self.__stub.MessageReactionUpdated(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionUpdatedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_reaction_removed(self, subscribe_to_message_reaction_removed_notification: SubscribeToMessageReactionRemovedNotification) -> AsyncIterator[MessageReactionRemovedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.message_notifications_pb2.MessageReactionRemovedNotification]) -> AsyncIterator[MessageReactionRemovedNotification]:
			async for native_message in iterator.__aiter__():
				yield MessageReactionRemovedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_message_reaction_removed_notification
		return response_iterator(self.__stub.MessageReactionRemoved(olvid.daemon.notification.v1.message_notifications_pb2.SubscribeToMessageReactionRemovedNotification(), metadata=self._client.grpc_metadata))


class AttachmentNotificationServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.notification_service_pb2_grpc.AttachmentNotificationServiceStub = olvid.daemon.services.v1.notification_service_pb2_grpc.AttachmentNotificationServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def attachment_received(self, subscribe_to_attachment_received_notification: SubscribeToAttachmentReceivedNotification) -> AsyncIterator[AttachmentReceivedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.attachment_notifications_pb2.AttachmentReceivedNotification]) -> AsyncIterator[AttachmentReceivedNotification]:
			async for native_message in iterator.__aiter__():
				yield AttachmentReceivedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_attachment_received_notification
		return response_iterator(self.__stub.AttachmentReceived(olvid.daemon.notification.v1.attachment_notifications_pb2.SubscribeToAttachmentReceivedNotification(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def attachment_uploaded(self, subscribe_to_attachment_uploaded_notification: SubscribeToAttachmentUploadedNotification) -> AsyncIterator[AttachmentUploadedNotification]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.notification.v1.attachment_notifications_pb2.AttachmentUploadedNotification]) -> AsyncIterator[AttachmentUploadedNotification]:
			async for native_message in iterator.__aiter__():
				yield AttachmentUploadedNotification._from_native(native_message, client=self._client)
		overlay_object = subscribe_to_attachment_uploaded_notification
		return response_iterator(self.__stub.AttachmentUploaded(olvid.daemon.notification.v1.attachment_notifications_pb2.SubscribeToAttachmentUploadedNotification(), metadata=self._client.grpc_metadata))
