####
# WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_protobuf_overlay
####

from __future__ import annotations  # this block is necessary for compilation
from typing import TYPE_CHECKING  # this block is necessary for compilation
import os
if TYPE_CHECKING:  # this block is necessary for compilation
	from ..core.OlvidClient import OlvidClient  # this block is necessary for compilation
	from ..listeners import ListenersImplementation as listeners
from typing import Coroutine, Any, Union, Callable, Optional
from ..protobuf import olvid
from enum import Enum


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentId:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Type(Enum):
		TYPE_UNSPECIFIED = 0
		TYPE_INBOUND = 1
		TYPE_OUTBOUND = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["AttachmentId.Type"]:
			return [AttachmentId.Type(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, type: "AttachmentId.Type" = 0, id: int = 0):
		self._client: OlvidClient = client
		self.type: AttachmentId.Type = type
		self.id: int = id

	def _update_content(self, attachment_id: AttachmentId) -> None:
		self.type: AttachmentId.Type = attachment_id.type
		self.id: int = attachment_id.id

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentId":
		return AttachmentId(client=self._client, type=self.type, id=self.id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.attachment_pb2.AttachmentId, client: OlvidClient = None) -> "AttachmentId":
		return AttachmentId(client, type=AttachmentId.Type(native_message.type), id=native_message.id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.attachment_pb2.AttachmentId], client: OlvidClient = None) -> list["AttachmentId"]:
		return [AttachmentId._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.attachment_pb2.AttachmentId], client: OlvidClient = None) -> "AttachmentId":
		native_message = await promise
		return AttachmentId._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentId"]):
		if messages is None:
			return []
		return [AttachmentId._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentId"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.attachment_pb2.AttachmentId(type=message.type.value if message.type else None, id=message.id if message.id else None)

	def __str__(self):
		s: str = ''
		if self.type:
			s += f'type: {self.type}, '
		if self.id:
			s += f'id: {self.id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentId):
			return False
		return self.type == other.type and self.id == other.id

	def __bool__(self):
		return bool(self.type) or self.id != 0

	def __hash__(self):
		return hash((self.type, self.id))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentId):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.type == 0 or self.type == expected.type, "Invalid value: type: " + str(expected.type) + " != " + str(self.type)
		assert expected.id == 0 or self.id == expected.id, "Invalid value: id: " + str(expected.id) + " != " + str(self.id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class Attachment:
	def __init__(self, client: OlvidClient = None, id: "AttachmentId" = None, discussion_id: int = 0, message_id: "MessageId" = None, file_name: str = "", mime_type: str = "", size: int = 0):
		self._client: OlvidClient = client
		self.id: AttachmentId = id
		self.discussion_id: int = discussion_id
		self.message_id: MessageId = message_id
		self.file_name: str = file_name
		self.mime_type: str = mime_type
		self.size: int = size

	def _update_content(self, attachment: Attachment) -> None:
		self.id: AttachmentId = attachment.id
		self.discussion_id: int = attachment.discussion_id
		self.message_id: MessageId = attachment.message_id
		self.file_name: str = attachment.file_name
		self.mime_type: str = attachment.mime_type
		self.size: int = attachment.size

	# noinspection PyProtectedMember
	def _clone(self) -> "Attachment":
		return Attachment(client=self._client, id=self.id._clone(), discussion_id=self.discussion_id, message_id=self.message_id._clone(), file_name=self.file_name, mime_type=self.mime_type, size=self.size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.attachment_pb2.Attachment, client: OlvidClient = None) -> "Attachment":
		return Attachment(client, id=AttachmentId._from_native(native_message.id, client=client), discussion_id=native_message.discussion_id, message_id=MessageId._from_native(native_message.message_id, client=client), file_name=native_message.file_name, mime_type=native_message.mime_type, size=native_message.size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.attachment_pb2.Attachment], client: OlvidClient = None) -> list["Attachment"]:
		return [Attachment._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.attachment_pb2.Attachment], client: OlvidClient = None) -> "Attachment":
		native_message = await promise
		return Attachment._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["Attachment"]):
		if messages is None:
			return []
		return [Attachment._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["Attachment"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.attachment_pb2.Attachment(id=AttachmentId._to_native(message.id if message.id else None), discussion_id=message.discussion_id if message.discussion_id else None, message_id=MessageId._to_native(message.message_id if message.message_id else None), file_name=message.file_name if message.file_name else None, mime_type=message.mime_type if message.mime_type else None, size=message.size if message.size else None)

	def __str__(self):
		s: str = ''
		if self.id:
			s += f'id: ({self.id}), '
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.message_id:
			s += f'message_id: ({self.message_id}), '
		if self.file_name:
			s += f'file_name: {self.file_name}, '
		if self.mime_type:
			s += f'mime_type: {self.mime_type}, '
		if self.size:
			s += f'size: {self.size}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, Attachment):
			return False
		return self.id == other.id and self.discussion_id == other.discussion_id and self.message_id == other.message_id and self.file_name == other.file_name and self.mime_type == other.mime_type and self.size == other.size

	def __bool__(self):
		return bool(self.id) or self.discussion_id != 0 or bool(self.message_id) or self.file_name != "" or self.mime_type != "" or self.size != 0

	def __hash__(self):
		return hash((self.id, self.discussion_id, self.message_id, self.file_name, self.mime_type, self.size))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, Attachment):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.id is None or self.id._test_assertion(expected.id)
		except AssertionError as e:
			raise AssertionError("id: " + str(e))
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		try:
			assert expected.message_id is None or self.message_id._test_assertion(expected.message_id)
		except AssertionError as e:
			raise AssertionError("message_id: " + str(e))
		assert expected.file_name == "" or self.file_name == expected.file_name, "Invalid value: file_name: " + str(expected.file_name) + " != " + str(self.file_name)
		assert expected.mime_type == "" or self.mime_type == expected.mime_type, "Invalid value: mime_type: " + str(expected.mime_type) + " != " + str(self.mime_type)
		assert expected.size == 0 or self.size == expected.size, "Invalid value: size: " + str(expected.size) + " != " + str(self.size)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentFilter:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class FileType(Enum):
		FILE_TYPE_UNSPECIFIED = 0
		FILE_TYPE_IMAGE = 3
		FILE_TYPE_VIDEO = 4
		FILE_TYPE_IMAGE_VIDEO = 5
		FILE_TYPE_AUDIO = 6
		FILE_TYPE_LINK_PREVIEW = 7
		FILE_TYPE_NOT_LINK_PREVIEW = 8
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["AttachmentFilter.FileType"]:
			return [AttachmentFilter.FileType(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, type: "AttachmentId.Type" = 0, file_type: "AttachmentFilter.FileType" = 0, discussion_id: int = 0, message_id: "MessageId" = None, filename_search: str = "", mime_type_search: str = "", min_size: int = 0, max_size: int = 0):
		self._client: OlvidClient = client
		self.type: AttachmentId.Type = type
		self.file_type: AttachmentFilter.FileType = file_type
		self.discussion_id: int = discussion_id
		self.message_id: MessageId = message_id
		self.filename_search: str = filename_search
		self.mime_type_search: str = mime_type_search
		self.min_size: int = min_size
		self.max_size: int = max_size

	def _update_content(self, attachment_filter: AttachmentFilter) -> None:
		self.type: AttachmentId.Type = attachment_filter.type
		self.file_type: AttachmentFilter.FileType = attachment_filter.file_type
		self.discussion_id: int = attachment_filter.discussion_id
		self.message_id: MessageId = attachment_filter.message_id
		self.filename_search: str = attachment_filter.filename_search
		self.mime_type_search: str = attachment_filter.mime_type_search
		self.min_size: int = attachment_filter.min_size
		self.max_size: int = attachment_filter.max_size

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentFilter":
		return AttachmentFilter(client=self._client, type=self.type, file_type=self.file_type, discussion_id=self.discussion_id, message_id=self.message_id._clone(), filename_search=self.filename_search, mime_type_search=self.mime_type_search, min_size=self.min_size, max_size=self.max_size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.attachment_pb2.AttachmentFilter, client: OlvidClient = None) -> "AttachmentFilter":
		return AttachmentFilter(client, type=AttachmentId.Type(native_message.type), file_type=AttachmentFilter.FileType(native_message.file_type), discussion_id=native_message.discussion_id, message_id=MessageId._from_native(native_message.message_id, client=client), filename_search=native_message.filename_search, mime_type_search=native_message.mime_type_search, min_size=native_message.min_size, max_size=native_message.max_size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.attachment_pb2.AttachmentFilter], client: OlvidClient = None) -> list["AttachmentFilter"]:
		return [AttachmentFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.attachment_pb2.AttachmentFilter], client: OlvidClient = None) -> "AttachmentFilter":
		native_message = await promise
		return AttachmentFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentFilter"]):
		if messages is None:
			return []
		return [AttachmentFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.attachment_pb2.AttachmentFilter(type=message.type.value if message.type else None, file_type=message.file_type.value if message.file_type else None, discussion_id=message.discussion_id if message.discussion_id else None, message_id=MessageId._to_native(message.message_id if message.message_id else None), filename_search=message.filename_search if message.filename_search else None, mime_type_search=message.mime_type_search if message.mime_type_search else None, min_size=message.min_size if message.min_size else None, max_size=message.max_size if message.max_size else None)

	def __str__(self):
		s: str = ''
		if self.type:
			s += f'type: {self.type}, '
		if self.file_type:
			s += f'file_type: {self.file_type}, '
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.message_id:
			s += f'message_id: ({self.message_id}), '
		if self.filename_search:
			s += f'filename_search: {self.filename_search}, '
		if self.mime_type_search:
			s += f'mime_type_search: {self.mime_type_search}, '
		if self.min_size:
			s += f'min_size: {self.min_size}, '
		if self.max_size:
			s += f'max_size: {self.max_size}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentFilter):
			return False
		return self.type == other.type and self.file_type == other.file_type and self.discussion_id == other.discussion_id and self.message_id == other.message_id and self.filename_search == other.filename_search and self.mime_type_search == other.mime_type_search and self.min_size == other.min_size and self.max_size == other.max_size

	def __bool__(self):
		return bool(self.type) or bool(self.file_type) or self.discussion_id != 0 or bool(self.message_id) or self.filename_search != "" or self.mime_type_search != "" or self.min_size != 0 or self.max_size != 0

	def __hash__(self):
		return hash((self.type, self.file_type, self.discussion_id, self.message_id, self.filename_search, self.mime_type_search, self.min_size, self.max_size))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.type == 0 or self.type == expected.type, "Invalid value: type: " + str(expected.type) + " != " + str(self.type)
		assert expected.file_type == 0 or self.file_type == expected.file_type, "Invalid value: file_type: " + str(expected.file_type) + " != " + str(self.file_type)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		try:
			assert expected.message_id is None or self.message_id._test_assertion(expected.message_id)
		except AssertionError as e:
			raise AssertionError("message_id: " + str(e))
		assert expected.filename_search == "" or self.filename_search == expected.filename_search, "Invalid value: filename_search: " + str(expected.filename_search) + " != " + str(self.filename_search)
		assert expected.mime_type_search == "" or self.mime_type_search == expected.mime_type_search, "Invalid value: mime_type_search: " + str(expected.mime_type_search) + " != " + str(self.mime_type_search)
		assert expected.min_size == 0 or self.min_size == expected.min_size, "Invalid value: min_size: " + str(expected.min_size) + " != " + str(self.min_size)
		assert expected.max_size == 0 or self.max_size == expected.max_size, "Invalid value: max_size: " + str(expected.max_size) + " != " + str(self.max_size)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ClientKey:
	def __init__(self, client: OlvidClient = None, name: str = "", key: str = "", identity_id: int = 0):
		self._client: OlvidClient = client
		self.name: str = name
		self.key: str = key
		self.identity_id: int = identity_id

	def _update_content(self, client_key: ClientKey) -> None:
		self.name: str = client_key.name
		self.key: str = client_key.key
		self.identity_id: int = client_key.identity_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKey":
		return ClientKey(client=self._client, name=self.name, key=self.key, identity_id=self.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.client_key_pb2.ClientKey, client: OlvidClient = None) -> "ClientKey":
		return ClientKey(client, name=native_message.name, key=native_message.key, identity_id=native_message.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.client_key_pb2.ClientKey], client: OlvidClient = None) -> list["ClientKey"]:
		return [ClientKey._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.client_key_pb2.ClientKey], client: OlvidClient = None) -> "ClientKey":
		native_message = await promise
		return ClientKey._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ClientKey"]):
		if messages is None:
			return []
		return [ClientKey._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ClientKey"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.client_key_pb2.ClientKey(name=message.name if message.name else None, key=message.key if message.key else None, identity_id=message.identity_id if message.identity_id else None)

	def __str__(self):
		s: str = ''
		if self.name:
			s += f'name: {self.name}, '
		if self.key:
			s += f'key: {self.key}, '
		if self.identity_id:
			s += f'identity_id: {self.identity_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ClientKey):
			return False
		return self.name == other.name and self.key == other.key and self.identity_id == other.identity_id

	def __bool__(self):
		return self.name != "" or self.key != "" or self.identity_id != 0

	def __hash__(self):
		return hash((self.name, self.key, self.identity_id))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ClientKey):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.name == "" or self.name == expected.name, "Invalid value: name: " + str(expected.name) + " != " + str(self.name)
		assert expected.key == "" or self.key == expected.key, "Invalid value: key: " + str(expected.key) + " != " + str(self.key)
		assert expected.identity_id == 0 or self.identity_id == expected.identity_id, "Invalid value: identity_id: " + str(expected.identity_id) + " != " + str(self.identity_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ClientKeyFilter:
	def __init__(self, client: OlvidClient = None, admin_key: bool = None, identity_id: int = None, name_search: str = "", key: str = ""):
		self._client: OlvidClient = client
		self.admin_key: bool = admin_key
		self.identity_id: int = identity_id
		self.name_search: str = name_search
		self.key: str = key

	def _update_content(self, client_key_filter: ClientKeyFilter) -> None:
		self.admin_key: bool = client_key_filter.admin_key
		self.identity_id: int = client_key_filter.identity_id
		self.name_search: str = client_key_filter.name_search
		self.key: str = client_key_filter.key

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyFilter":
		return ClientKeyFilter(client=self._client, admin_key=self.admin_key, identity_id=self.identity_id, name_search=self.name_search, key=self.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.client_key_pb2.ClientKeyFilter, client: OlvidClient = None) -> "ClientKeyFilter":
		return ClientKeyFilter(client, admin_key=native_message.admin_key, identity_id=native_message.identity_id, name_search=native_message.name_search, key=native_message.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.client_key_pb2.ClientKeyFilter], client: OlvidClient = None) -> list["ClientKeyFilter"]:
		return [ClientKeyFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.client_key_pb2.ClientKeyFilter], client: OlvidClient = None) -> "ClientKeyFilter":
		native_message = await promise
		return ClientKeyFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ClientKeyFilter"]):
		if messages is None:
			return []
		return [ClientKeyFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ClientKeyFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.client_key_pb2.ClientKeyFilter(admin_key=message.admin_key if message.admin_key else None, identity_id=message.identity_id if message.identity_id else None, name_search=message.name_search if message.name_search else None, key=message.key if message.key else None)

	def __str__(self):
		s: str = ''
		if self.admin_key:
			s += f'admin_key: {self.admin_key}, '
		if self.identity_id:
			s += f'identity_id: {self.identity_id}, '
		if self.name_search:
			s += f'name_search: {self.name_search}, '
		if self.key:
			s += f'key: {self.key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ClientKeyFilter):
			return False
		return self.admin_key == other.admin_key and self.identity_id == other.identity_id and self.name_search == other.name_search and self.key == other.key

	def __bool__(self):
		return self.admin_key is not None or self.identity_id is not None or self.name_search != "" or self.key != ""

	def __hash__(self):
		return hash((self.admin_key, self.identity_id, self.name_search, self.key))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ClientKeyFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.admin_key is None or self.admin_key == expected.admin_key, "Invalid value: admin_key: " + str(expected.admin_key) + " != " + str(self.admin_key)
		assert expected.identity_id is None or self.identity_id == expected.identity_id, "Invalid value: identity_id: " + str(expected.identity_id) + " != " + str(self.identity_id)
		assert expected.name_search == "" or self.name_search == expected.name_search, "Invalid value: name_search: " + str(expected.name_search) + " != " + str(self.name_search)
		assert expected.key == "" or self.key == expected.key, "Invalid value: key: " + str(expected.key) + " != " + str(self.key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class Contact:
	def __init__(self, client: OlvidClient = None, id: int = 0, display_name: str = "", details: "IdentityDetails" = None, established_channel_count: int = 0, device_count: int = 0, has_one_to_one_discussion: bool = False, has_a_photo: bool = False, keycloak_managed: bool = False):
		self._client: OlvidClient = client
		self.id: int = id
		self.display_name: str = display_name
		self.details: IdentityDetails = details
		self.established_channel_count: int = established_channel_count
		self.device_count: int = device_count
		self.has_one_to_one_discussion: bool = has_one_to_one_discussion
		self.has_a_photo: bool = has_a_photo
		self.keycloak_managed: bool = keycloak_managed

	def _update_content(self, contact: Contact) -> None:
		self.id: int = contact.id
		self.display_name: str = contact.display_name
		self.details: IdentityDetails = contact.details
		self.established_channel_count: int = contact.established_channel_count
		self.device_count: int = contact.device_count
		self.has_one_to_one_discussion: bool = contact.has_one_to_one_discussion
		self.has_a_photo: bool = contact.has_a_photo
		self.keycloak_managed: bool = contact.keycloak_managed

	# noinspection PyProtectedMember
	def _clone(self) -> "Contact":
		return Contact(client=self._client, id=self.id, display_name=self.display_name, details=self.details._clone(), established_channel_count=self.established_channel_count, device_count=self.device_count, has_one_to_one_discussion=self.has_one_to_one_discussion, has_a_photo=self.has_a_photo, keycloak_managed=self.keycloak_managed)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.contact_pb2.Contact, client: OlvidClient = None) -> "Contact":
		return Contact(client, id=native_message.id, display_name=native_message.display_name, details=IdentityDetails._from_native(native_message.details, client=client), established_channel_count=native_message.established_channel_count, device_count=native_message.device_count, has_one_to_one_discussion=native_message.has_one_to_one_discussion, has_a_photo=native_message.has_a_photo, keycloak_managed=native_message.keycloak_managed)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.contact_pb2.Contact], client: OlvidClient = None) -> list["Contact"]:
		return [Contact._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.contact_pb2.Contact], client: OlvidClient = None) -> "Contact":
		native_message = await promise
		return Contact._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["Contact"]):
		if messages is None:
			return []
		return [Contact._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["Contact"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.contact_pb2.Contact(id=message.id if message.id else None, display_name=message.display_name if message.display_name else None, details=IdentityDetails._to_native(message.details if message.details else None), established_channel_count=message.established_channel_count if message.established_channel_count else None, device_count=message.device_count if message.device_count else None, has_one_to_one_discussion=message.has_one_to_one_discussion if message.has_one_to_one_discussion else None, has_a_photo=message.has_a_photo if message.has_a_photo else None, keycloak_managed=message.keycloak_managed if message.keycloak_managed else None)

	def __str__(self):
		s: str = ''
		if self.id:
			s += f'id: {self.id}, '
		if self.display_name:
			s += f'display_name: {self.display_name}, '
		if self.details:
			s += f'details: ({self.details}), '
		if self.established_channel_count:
			s += f'established_channel_count: {self.established_channel_count}, '
		if self.device_count:
			s += f'device_count: {self.device_count}, '
		if self.has_one_to_one_discussion:
			s += f'has_one_to_one_discussion: {self.has_one_to_one_discussion}, '
		if self.has_a_photo:
			s += f'has_a_photo: {self.has_a_photo}, '
		if self.keycloak_managed:
			s += f'keycloak_managed: {self.keycloak_managed}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, Contact):
			return False
		return self.id == other.id and self.display_name == other.display_name and self.details == other.details and self.established_channel_count == other.established_channel_count and self.device_count == other.device_count and self.has_one_to_one_discussion == other.has_one_to_one_discussion and self.has_a_photo == other.has_a_photo and self.keycloak_managed == other.keycloak_managed

	def __bool__(self):
		return self.id != 0 or self.display_name != "" or bool(self.details) or self.established_channel_count != 0 or self.device_count != 0 or self.has_one_to_one_discussion or self.has_a_photo or self.keycloak_managed

	def __hash__(self):
		return hash((self.id, self.display_name, self.details, self.established_channel_count, self.device_count, self.has_one_to_one_discussion, self.has_a_photo, self.keycloak_managed))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, Contact):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.id == 0 or self.id == expected.id, "Invalid value: id: " + str(expected.id) + " != " + str(self.id)
		assert expected.display_name == "" or self.display_name == expected.display_name, "Invalid value: display_name: " + str(expected.display_name) + " != " + str(self.display_name)
		try:
			assert expected.details is None or self.details._test_assertion(expected.details)
		except AssertionError as e:
			raise AssertionError("details: " + str(e))
		assert expected.established_channel_count == 0 or self.established_channel_count == expected.established_channel_count, "Invalid value: established_channel_count: " + str(expected.established_channel_count) + " != " + str(self.established_channel_count)
		assert expected.device_count == 0 or self.device_count == expected.device_count, "Invalid value: device_count: " + str(expected.device_count) + " != " + str(self.device_count)
		assert expected.has_one_to_one_discussion is False or self.has_one_to_one_discussion == expected.has_one_to_one_discussion, "Invalid value: has_one_to_one_discussion: " + str(expected.has_one_to_one_discussion) + " != " + str(self.has_one_to_one_discussion)
		assert expected.has_a_photo is False or self.has_a_photo == expected.has_a_photo, "Invalid value: has_a_photo: " + str(expected.has_a_photo) + " != " + str(self.has_a_photo)
		assert expected.keycloak_managed is False or self.keycloak_managed == expected.keycloak_managed, "Invalid value: keycloak_managed: " + str(expected.keycloak_managed) + " != " + str(self.keycloak_managed)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactFilter:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class OneToOne(Enum):
		ONE_TO_ONE_UNSPECIFIED = 0
		ONE_TO_ONE_IS = 1
		ONE_TO_ONE_IS_NOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["ContactFilter.OneToOne"]:
			return [ContactFilter.OneToOne(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Photo(Enum):
		PHOTO_UNSPECIFIED = 0
		PHOTO_HAS = 1
		PHOTO_HAS_NOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["ContactFilter.Photo"]:
			return [ContactFilter.Photo(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Keycloak(Enum):
		KEYCLOAK_UNSPECIFIED = 0
		KEYCLOAK_MANAGED = 1
		KEYCLOAK_NOT_MANAGED = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["ContactFilter.Keycloak"]:
			return [ContactFilter.Keycloak(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, one_to_one: "ContactFilter.OneToOne" = 0, photo: "ContactFilter.Photo" = 0, keycloak: "ContactFilter.Keycloak" = 0, display_name_search: str = "", details_search: "IdentityDetails" = None):
		self._client: OlvidClient = client
		self.one_to_one: ContactFilter.OneToOne = one_to_one
		self.photo: ContactFilter.Photo = photo
		self.keycloak: ContactFilter.Keycloak = keycloak
		self.display_name_search: str = display_name_search
		self.details_search: IdentityDetails = details_search

	def _update_content(self, contact_filter: ContactFilter) -> None:
		self.one_to_one: ContactFilter.OneToOne = contact_filter.one_to_one
		self.photo: ContactFilter.Photo = contact_filter.photo
		self.keycloak: ContactFilter.Keycloak = contact_filter.keycloak
		self.display_name_search: str = contact_filter.display_name_search
		self.details_search: IdentityDetails = contact_filter.details_search

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactFilter":
		return ContactFilter(client=self._client, one_to_one=self.one_to_one, photo=self.photo, keycloak=self.keycloak, display_name_search=self.display_name_search, details_search=self.details_search._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.contact_pb2.ContactFilter, client: OlvidClient = None) -> "ContactFilter":
		return ContactFilter(client, one_to_one=ContactFilter.OneToOne(native_message.one_to_one), photo=ContactFilter.Photo(native_message.photo), keycloak=ContactFilter.Keycloak(native_message.keycloak), display_name_search=native_message.display_name_search, details_search=IdentityDetails._from_native(native_message.details_search, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.contact_pb2.ContactFilter], client: OlvidClient = None) -> list["ContactFilter"]:
		return [ContactFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.contact_pb2.ContactFilter], client: OlvidClient = None) -> "ContactFilter":
		native_message = await promise
		return ContactFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactFilter"]):
		if messages is None:
			return []
		return [ContactFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.contact_pb2.ContactFilter(one_to_one=message.one_to_one.value if message.one_to_one else None, photo=message.photo.value if message.photo else None, keycloak=message.keycloak.value if message.keycloak else None, display_name_search=message.display_name_search if message.display_name_search else None, details_search=IdentityDetails._to_native(message.details_search if message.details_search else None))

	def __str__(self):
		s: str = ''
		if self.one_to_one:
			s += f'one_to_one: {self.one_to_one}, '
		if self.photo:
			s += f'photo: {self.photo}, '
		if self.keycloak:
			s += f'keycloak: {self.keycloak}, '
		if self.display_name_search:
			s += f'display_name_search: {self.display_name_search}, '
		if self.details_search:
			s += f'details_search: ({self.details_search}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactFilter):
			return False
		return self.one_to_one == other.one_to_one and self.photo == other.photo and self.keycloak == other.keycloak and self.display_name_search == other.display_name_search and self.details_search == other.details_search

	def __bool__(self):
		return bool(self.one_to_one) or bool(self.photo) or bool(self.keycloak) or self.display_name_search != "" or bool(self.details_search)

	def __hash__(self):
		return hash((self.one_to_one, self.photo, self.keycloak, self.display_name_search, self.details_search))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.one_to_one == 0 or self.one_to_one == expected.one_to_one, "Invalid value: one_to_one: " + str(expected.one_to_one) + " != " + str(self.one_to_one)
		assert expected.photo == 0 or self.photo == expected.photo, "Invalid value: photo: " + str(expected.photo) + " != " + str(self.photo)
		assert expected.keycloak == 0 or self.keycloak == expected.keycloak, "Invalid value: keycloak: " + str(expected.keycloak) + " != " + str(self.keycloak)
		assert expected.display_name_search == "" or self.display_name_search == expected.display_name_search, "Invalid value: display_name_search: " + str(expected.display_name_search) + " != " + str(self.display_name_search)
		try:
			assert expected.details_search is None or self.details_search._test_assertion(expected.details_search)
		except AssertionError as e:
			raise AssertionError("details_search: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class Discussion:
	def __init__(self, client: OlvidClient = None, id: int = 0, title: str = "", contact_id: int = None, group_id: int = None):
		self._client: OlvidClient = client
		self.id: int = id
		self.title: str = title
		self.contact_id: int = contact_id
		self.group_id: int = group_id

	def _update_content(self, discussion: Discussion) -> None:
		self.id: int = discussion.id
		self.title: str = discussion.title
		self.contact_id: int = discussion.contact_id
		self.group_id: int = discussion.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "Discussion":
		return Discussion(client=self._client, id=self.id, title=self.title, contact_id=self.contact_id, group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.discussion_pb2.Discussion, client: OlvidClient = None) -> "Discussion":
		return Discussion(client, id=native_message.id, title=native_message.title, contact_id=native_message.contact_id, group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.discussion_pb2.Discussion], client: OlvidClient = None) -> list["Discussion"]:
		return [Discussion._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.discussion_pb2.Discussion], client: OlvidClient = None) -> "Discussion":
		native_message = await promise
		return Discussion._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["Discussion"]):
		if messages is None:
			return []
		return [Discussion._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["Discussion"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.discussion_pb2.Discussion(id=message.id if message.id else None, title=message.title if message.title else None, contact_id=message.contact_id if message.contact_id else None, group_id=message.group_id if message.group_id else None)

	def __str__(self):
		s: str = ''
		if self.id:
			s += f'id: {self.id}, '
		if self.title:
			s += f'title: {self.title}, '
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, Discussion):
			return False
		return self.id == other.id and self.title == other.title and self.contact_id == other.contact_id and self.group_id == other.group_id

	def __bool__(self):
		return self.id != 0 or self.title != "" or self.contact_id is not None or self.group_id is not None

	def __hash__(self):
		return hash((self.id, self.title, self.contact_id, self.group_id))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, Discussion):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.id == 0 or self.id == expected.id, "Invalid value: id: " + str(expected.id) + " != " + str(self.id)
		assert expected.title == "" or self.title == expected.title, "Invalid value: title: " + str(expected.title) + " != " + str(self.title)
		assert expected.contact_id is None or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		assert expected.group_id is None or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionSettings:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0, read_once: bool = False, existence_duration: int = 0, visibility_duration: int = 0):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id
		self.read_once: bool = read_once
		self.existence_duration: int = existence_duration
		self.visibility_duration: int = visibility_duration

	def _update_content(self, discussion_settings: DiscussionSettings) -> None:
		self.discussion_id: int = discussion_settings.discussion_id
		self.read_once: bool = discussion_settings.read_once
		self.existence_duration: int = discussion_settings.existence_duration
		self.visibility_duration: int = discussion_settings.visibility_duration

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionSettings":
		return DiscussionSettings(client=self._client, discussion_id=self.discussion_id, read_once=self.read_once, existence_duration=self.existence_duration, visibility_duration=self.visibility_duration)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.discussion_pb2.DiscussionSettings, client: OlvidClient = None) -> "DiscussionSettings":
		return DiscussionSettings(client, discussion_id=native_message.discussion_id, read_once=native_message.read_once, existence_duration=native_message.existence_duration, visibility_duration=native_message.visibility_duration)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.discussion_pb2.DiscussionSettings], client: OlvidClient = None) -> list["DiscussionSettings"]:
		return [DiscussionSettings._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.discussion_pb2.DiscussionSettings], client: OlvidClient = None) -> "DiscussionSettings":
		native_message = await promise
		return DiscussionSettings._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionSettings"]):
		if messages is None:
			return []
		return [DiscussionSettings._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionSettings"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.discussion_pb2.DiscussionSettings(discussion_id=message.discussion_id if message.discussion_id else None, read_once=message.read_once if message.read_once else None, existence_duration=message.existence_duration if message.existence_duration else None, visibility_duration=message.visibility_duration if message.visibility_duration else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.read_once:
			s += f'read_once: {self.read_once}, '
		if self.existence_duration:
			s += f'existence_duration: {self.existence_duration}, '
		if self.visibility_duration:
			s += f'visibility_duration: {self.visibility_duration}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionSettings):
			return False
		return self.discussion_id == other.discussion_id and self.read_once == other.read_once and self.existence_duration == other.existence_duration and self.visibility_duration == other.visibility_duration

	def __bool__(self):
		return self.discussion_id != 0 or self.read_once or self.existence_duration != 0 or self.visibility_duration != 0

	def __hash__(self):
		return hash((self.discussion_id, self.read_once, self.existence_duration, self.visibility_duration))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionSettings):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.read_once is False or self.read_once == expected.read_once, "Invalid value: read_once: " + str(expected.read_once) + " != " + str(self.read_once)
		assert expected.existence_duration == 0 or self.existence_duration == expected.existence_duration, "Invalid value: existence_duration: " + str(expected.existence_duration) + " != " + str(self.existence_duration)
		assert expected.visibility_duration == 0 or self.visibility_duration == expected.visibility_duration, "Invalid value: visibility_duration: " + str(expected.visibility_duration) + " != " + str(self.visibility_duration)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionFilter:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Type(Enum):
		TYPE_UNSPECIFIED = 0
		TYPE_OTO = 1
		TYPE_GROUP = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["DiscussionFilter.Type"]:
			return [DiscussionFilter.Type(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, type: "DiscussionFilter.Type" = 0, contact_id: int = None, group_id: int = None, title_search: str = ""):
		self._client: OlvidClient = client
		self.type: DiscussionFilter.Type = type
		self.contact_id: int = contact_id
		self.group_id: int = group_id
		self.title_search: str = title_search

	def _update_content(self, discussion_filter: DiscussionFilter) -> None:
		self.type: DiscussionFilter.Type = discussion_filter.type
		self.contact_id: int = discussion_filter.contact_id
		self.group_id: int = discussion_filter.group_id
		self.title_search: str = discussion_filter.title_search

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionFilter":
		return DiscussionFilter(client=self._client, type=self.type, contact_id=self.contact_id, group_id=self.group_id, title_search=self.title_search)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.discussion_pb2.DiscussionFilter, client: OlvidClient = None) -> "DiscussionFilter":
		return DiscussionFilter(client, type=DiscussionFilter.Type(native_message.type), contact_id=native_message.contact_id, group_id=native_message.group_id, title_search=native_message.title_search)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.discussion_pb2.DiscussionFilter], client: OlvidClient = None) -> list["DiscussionFilter"]:
		return [DiscussionFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.discussion_pb2.DiscussionFilter], client: OlvidClient = None) -> "DiscussionFilter":
		native_message = await promise
		return DiscussionFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionFilter"]):
		if messages is None:
			return []
		return [DiscussionFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.discussion_pb2.DiscussionFilter(type=message.type.value if message.type else None, contact_id=message.contact_id if message.contact_id else None, group_id=message.group_id if message.group_id else None, title_search=message.title_search if message.title_search else None)

	def __str__(self):
		s: str = ''
		if self.type:
			s += f'type: {self.type}, '
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		if self.title_search:
			s += f'title_search: {self.title_search}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionFilter):
			return False
		return self.type == other.type and self.contact_id == other.contact_id and self.group_id == other.group_id and self.title_search == other.title_search

	def __bool__(self):
		return bool(self.type) or self.contact_id is not None or self.group_id is not None or self.title_search != ""

	def __hash__(self):
		return hash((self.type, self.contact_id, self.group_id, self.title_search))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.type == 0 or self.type == expected.type, "Invalid value: type: " + str(expected.type) + " != " + str(self.type)
		assert expected.contact_id is None or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		assert expected.group_id is None or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		assert expected.title_search == "" or self.title_search == expected.title_search, "Invalid value: title_search: " + str(expected.title_search) + " != " + str(self.title_search)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class Group:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Type(Enum):
		TYPE_UNSPECIFIED = 0
		TYPE_STANDARD = 1
		TYPE_CONTROLLED = 2
		TYPE_READ_ONLY = 3
		TYPE_ADVANCED = 4
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["Group.Type"]:
			return [Group.Type(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	class AdvancedConfiguration:
		# noinspection PyProtectedMember,PyShadowingBuiltins
		class RemoteDelete(Enum):
			REMOTE_DELETE_UNSPECIFIED = 0
			REMOTE_DELETE_NOBODY = 1
			REMOTE_DELETE_ADMINS = 2
			REMOTE_DELETE_EVERYONE = 3
		
			def __str__(self):
				return self.name
		
			@staticmethod
			def _from_native_list(native_enum_list) -> list["Group.AdvancedConfiguration.RemoteDelete"]:
				return [Group.AdvancedConfiguration.RemoteDelete(native_enum) for native_enum in native_enum_list]
		
			def __bool__(self):
				return self.value != 0
	
		def __init__(self, client: OlvidClient = None, read_only: bool = False, remote_delete: "Group.AdvancedConfiguration.RemoteDelete" = 0):
			self._client: OlvidClient = client
			self.read_only: bool = read_only
			self.remote_delete: Group.AdvancedConfiguration.RemoteDelete = remote_delete
	
		def _update_content(self, advanced_configuration: Group.AdvancedConfiguration) -> None:
			self.read_only: bool = advanced_configuration.read_only
			self.remote_delete: Group.AdvancedConfiguration.RemoteDelete = advanced_configuration.remote_delete
	
		# noinspection PyProtectedMember
		def _clone(self) -> "Group.AdvancedConfiguration":
			return Group.AdvancedConfiguration(client=self._client, read_only=self.read_only, remote_delete=self.remote_delete)
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
		@staticmethod
		def _from_native(native_message: olvid.daemon.datatypes.v1.group_pb2.Group.AdvancedConfiguration, client: OlvidClient = None) -> "Group.AdvancedConfiguration":
			return Group.AdvancedConfiguration(client, read_only=native_message.read_only, remote_delete=Group.AdvancedConfiguration.RemoteDelete(native_message.remote_delete))
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
		@staticmethod
		def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.group_pb2.Group.AdvancedConfiguration], client: OlvidClient = None) -> list["Group.AdvancedConfiguration"]:
			return [Group.AdvancedConfiguration._from_native(native_message, client=client) for native_message in native_message_list]
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
		@staticmethod
		async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.group_pb2.Group.AdvancedConfiguration], client: OlvidClient = None) -> "Group.AdvancedConfiguration":
			native_message = await promise
			return Group.AdvancedConfiguration._from_native(native_message, client=client)
	
		# noinspection PyUnresolvedReferences,PyProtectedMember
		@staticmethod
		def _to_native_list(messages: list["Group.AdvancedConfiguration"]):
			if messages is None:
				return []
			return [Group.AdvancedConfiguration._to_native(message) for message in messages]
	
		# noinspection PyUnresolvedReferences,PyProtectedMember
		@staticmethod
		def _to_native(message: Optional["Group.AdvancedConfiguration"]):
			if message is None:
				return None
			return olvid.daemon.datatypes.v1.group_pb2.Group.AdvancedConfiguration(read_only=message.read_only if message.read_only else None, remote_delete=message.remote_delete.value if message.remote_delete else None)
	
		def __str__(self):
			s: str = ''
			if self.read_only:
				s += f'read_only: {self.read_only}, '
			if self.remote_delete:
				s += f'remote_delete: {self.remote_delete}, '
			return s.removesuffix(', ')
	
		def __eq__(self, other):
			if not isinstance(other, Group.AdvancedConfiguration):
				return False
			return self.read_only == other.read_only and self.remote_delete == other.remote_delete
	
		def __bool__(self):
			return self.read_only or bool(self.remote_delete)
	
		def __hash__(self):
			return hash((self.read_only, self.remote_delete))
	
		# For tests routines
		# noinspection DuplicatedCode,PyProtectedMember
		def _test_assertion(self, expected):
			if not isinstance(expected, Group.AdvancedConfiguration):
				assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
			assert expected.read_only is False or self.read_only == expected.read_only, "Invalid value: read_only: " + str(expected.read_only) + " != " + str(self.read_only)
			assert expected.remote_delete == 0 or self.remote_delete == expected.remote_delete, "Invalid value: remote_delete: " + str(expected.remote_delete) + " != " + str(self.remote_delete)
			return True

	def __init__(self, client: OlvidClient = None, id: int = 0, type: "Group.Type" = 0, advanced_configuration: "Group.AdvancedConfiguration" = None, own_permissions: "GroupMemberPermissions" = None, members: "list[GroupMember]" = None, pending_members: "list[PendingGroupMember]" = None, update_in_progress: bool = False, keycloak_managed: bool = False, name: str = "", description: str = "", has_a_photo: bool = False):
		self._client: OlvidClient = client
		self.id: int = id
		self.type: Group.Type = type
		self.advanced_configuration: Group.AdvancedConfiguration = advanced_configuration
		self.own_permissions: GroupMemberPermissions = own_permissions
		self.members: list[GroupMember] = members
		self.pending_members: list[PendingGroupMember] = pending_members
		self.update_in_progress: bool = update_in_progress
		self.keycloak_managed: bool = keycloak_managed
		self.name: str = name
		self.description: str = description
		self.has_a_photo: bool = has_a_photo

	def _update_content(self, group: Group) -> None:
		self.id: int = group.id
		self.type: Group.Type = group.type
		self.advanced_configuration: Group.AdvancedConfiguration = group.advanced_configuration
		self.own_permissions: GroupMemberPermissions = group.own_permissions
		self.members: list[GroupMember] = group.members
		self.pending_members: list[PendingGroupMember] = group.pending_members
		self.update_in_progress: bool = group.update_in_progress
		self.keycloak_managed: bool = group.keycloak_managed
		self.name: str = group.name
		self.description: str = group.description
		self.has_a_photo: bool = group.has_a_photo

	# noinspection PyProtectedMember
	def _clone(self) -> "Group":
		return Group(client=self._client, id=self.id, type=self.type, advanced_configuration=self.advanced_configuration._clone(), own_permissions=self.own_permissions._clone(), members=[e._clone() for e in self.members], pending_members=[e._clone() for e in self.pending_members], update_in_progress=self.update_in_progress, keycloak_managed=self.keycloak_managed, name=self.name, description=self.description, has_a_photo=self.has_a_photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.group_pb2.Group, client: OlvidClient = None) -> "Group":
		return Group(client, id=native_message.id, type=Group.Type(native_message.type), advanced_configuration=Group.AdvancedConfiguration._from_native(native_message.advanced_configuration, client=client), own_permissions=GroupMemberPermissions._from_native(native_message.own_permissions, client=client), members=GroupMember._from_native_list(native_message.members, client=client), pending_members=PendingGroupMember._from_native_list(native_message.pending_members, client=client), update_in_progress=native_message.update_in_progress, keycloak_managed=native_message.keycloak_managed, name=native_message.name, description=native_message.description, has_a_photo=native_message.has_a_photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.group_pb2.Group], client: OlvidClient = None) -> list["Group"]:
		return [Group._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.group_pb2.Group], client: OlvidClient = None) -> "Group":
		native_message = await promise
		return Group._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["Group"]):
		if messages is None:
			return []
		return [Group._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["Group"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.group_pb2.Group(id=message.id if message.id else None, type=message.type.value if message.type else None, advanced_configuration=Group.AdvancedConfiguration._to_native(message.advanced_configuration if message.advanced_configuration else None), own_permissions=GroupMemberPermissions._to_native(message.own_permissions if message.own_permissions else None), members=GroupMember._to_native_list(message.members if message.members else None), pending_members=PendingGroupMember._to_native_list(message.pending_members if message.pending_members else None), update_in_progress=message.update_in_progress if message.update_in_progress else None, keycloak_managed=message.keycloak_managed if message.keycloak_managed else None, name=message.name if message.name else None, description=message.description if message.description else None, has_a_photo=message.has_a_photo if message.has_a_photo else None)

	def __str__(self):
		s: str = ''
		if self.id:
			s += f'id: {self.id}, '
		if self.type:
			s += f'type: {self.type}, '
		if self.advanced_configuration:
			s += f'advanced_configuration: ({self.advanced_configuration}), '
		if self.own_permissions:
			s += f'own_permissions: ({self.own_permissions}), '
		if self.members:
			s += f'members: {[str(el) for el in self.members]}, '
		if self.pending_members:
			s += f'pending_members: {[str(el) for el in self.pending_members]}, '
		if self.update_in_progress:
			s += f'update_in_progress: {self.update_in_progress}, '
		if self.keycloak_managed:
			s += f'keycloak_managed: {self.keycloak_managed}, '
		if self.name:
			s += f'name: {self.name}, '
		if self.description:
			s += f'description: {self.description}, '
		if self.has_a_photo:
			s += f'has_a_photo: {self.has_a_photo}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, Group):
			return False
		return self.id == other.id and self.type == other.type and self.advanced_configuration == other.advanced_configuration and self.own_permissions == other.own_permissions and self.members == other.members and self.pending_members == other.pending_members and self.update_in_progress == other.update_in_progress and self.keycloak_managed == other.keycloak_managed and self.name == other.name and self.description == other.description and self.has_a_photo == other.has_a_photo

	def __bool__(self):
		return self.id != 0 or bool(self.type) or bool(self.advanced_configuration) or bool(self.own_permissions) or bool(self.members) or bool(self.pending_members) or self.update_in_progress or self.keycloak_managed or self.name != "" or self.description != "" or self.has_a_photo

	def __hash__(self):
		return hash((self.id, self.type, self.advanced_configuration, self.own_permissions, tuple(self.members), tuple(self.pending_members), self.update_in_progress, self.keycloak_managed, self.name, self.description, self.has_a_photo))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, Group):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.id == 0 or self.id == expected.id, "Invalid value: id: " + str(expected.id) + " != " + str(self.id)
		assert expected.type == 0 or self.type == expected.type, "Invalid value: type: " + str(expected.type) + " != " + str(self.type)
		try:
			assert expected.advanced_configuration is None or self.advanced_configuration._test_assertion(expected.advanced_configuration)
		except AssertionError as e:
			raise AssertionError("advanced_configuration: " + str(e))
		try:
			assert expected.own_permissions is None or self.own_permissions._test_assertion(expected.own_permissions)
		except AssertionError as e:
			raise AssertionError("own_permissions: " + str(e))
		pass  # print("Warning: test_assertion: skipped a list field members")
		pass  # print("Warning: test_assertion: skipped a list field pending_members")
		assert expected.update_in_progress is False or self.update_in_progress == expected.update_in_progress, "Invalid value: update_in_progress: " + str(expected.update_in_progress) + " != " + str(self.update_in_progress)
		assert expected.keycloak_managed is False or self.keycloak_managed == expected.keycloak_managed, "Invalid value: keycloak_managed: " + str(expected.keycloak_managed) + " != " + str(self.keycloak_managed)
		assert expected.name == "" or self.name == expected.name, "Invalid value: name: " + str(expected.name) + " != " + str(self.name)
		assert expected.description == "" or self.description == expected.description, "Invalid value: description: " + str(expected.description) + " != " + str(self.description)
		assert expected.has_a_photo is False or self.has_a_photo == expected.has_a_photo, "Invalid value: has_a_photo: " + str(expected.has_a_photo) + " != " + str(self.has_a_photo)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupMember:
	def __init__(self, client: OlvidClient = None, contact_id: int = 0, permissions: "GroupMemberPermissions" = None):
		self._client: OlvidClient = client
		self.contact_id: int = contact_id
		self.permissions: GroupMemberPermissions = permissions

	def _update_content(self, group_member: GroupMember) -> None:
		self.contact_id: int = group_member.contact_id
		self.permissions: GroupMemberPermissions = group_member.permissions

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupMember":
		return GroupMember(client=self._client, contact_id=self.contact_id, permissions=self.permissions._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.group_pb2.GroupMember, client: OlvidClient = None) -> "GroupMember":
		return GroupMember(client, contact_id=native_message.contact_id, permissions=GroupMemberPermissions._from_native(native_message.permissions, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.group_pb2.GroupMember], client: OlvidClient = None) -> list["GroupMember"]:
		return [GroupMember._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.group_pb2.GroupMember], client: OlvidClient = None) -> "GroupMember":
		native_message = await promise
		return GroupMember._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupMember"]):
		if messages is None:
			return []
		return [GroupMember._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupMember"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.group_pb2.GroupMember(contact_id=message.contact_id if message.contact_id else None, permissions=GroupMemberPermissions._to_native(message.permissions if message.permissions else None))

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		if self.permissions:
			s += f'permissions: ({self.permissions}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupMember):
			return False
		return self.contact_id == other.contact_id and self.permissions == other.permissions

	def __bool__(self):
		return self.contact_id != 0 or bool(self.permissions)

	def __hash__(self):
		return hash((self.contact_id, self.permissions))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupMember):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		try:
			assert expected.permissions is None or self.permissions._test_assertion(expected.permissions)
		except AssertionError as e:
			raise AssertionError("permissions: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class PendingGroupMember:
	def __init__(self, client: OlvidClient = None, pending_member_id: int = 0, contact_id: int = 0, display_name: str = "", declined: bool = False, permissions: "GroupMemberPermissions" = None):
		self._client: OlvidClient = client
		self.pending_member_id: int = pending_member_id
		self.contact_id: int = contact_id
		self.display_name: str = display_name
		self.declined: bool = declined
		self.permissions: GroupMemberPermissions = permissions

	def _update_content(self, pending_group_member: PendingGroupMember) -> None:
		self.pending_member_id: int = pending_group_member.pending_member_id
		self.contact_id: int = pending_group_member.contact_id
		self.display_name: str = pending_group_member.display_name
		self.declined: bool = pending_group_member.declined
		self.permissions: GroupMemberPermissions = pending_group_member.permissions

	# noinspection PyProtectedMember
	def _clone(self) -> "PendingGroupMember":
		return PendingGroupMember(client=self._client, pending_member_id=self.pending_member_id, contact_id=self.contact_id, display_name=self.display_name, declined=self.declined, permissions=self.permissions._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.group_pb2.PendingGroupMember, client: OlvidClient = None) -> "PendingGroupMember":
		return PendingGroupMember(client, pending_member_id=native_message.pending_member_id, contact_id=native_message.contact_id, display_name=native_message.display_name, declined=native_message.declined, permissions=GroupMemberPermissions._from_native(native_message.permissions, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.group_pb2.PendingGroupMember], client: OlvidClient = None) -> list["PendingGroupMember"]:
		return [PendingGroupMember._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.group_pb2.PendingGroupMember], client: OlvidClient = None) -> "PendingGroupMember":
		native_message = await promise
		return PendingGroupMember._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["PendingGroupMember"]):
		if messages is None:
			return []
		return [PendingGroupMember._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["PendingGroupMember"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.group_pb2.PendingGroupMember(pending_member_id=message.pending_member_id if message.pending_member_id else None, contact_id=message.contact_id if message.contact_id else None, display_name=message.display_name if message.display_name else None, declined=message.declined if message.declined else None, permissions=GroupMemberPermissions._to_native(message.permissions if message.permissions else None))

	def __str__(self):
		s: str = ''
		if self.pending_member_id:
			s += f'pending_member_id: {self.pending_member_id}, '
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		if self.display_name:
			s += f'display_name: {self.display_name}, '
		if self.declined:
			s += f'declined: {self.declined}, '
		if self.permissions:
			s += f'permissions: ({self.permissions}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, PendingGroupMember):
			return False
		return self.pending_member_id == other.pending_member_id and self.contact_id == other.contact_id and self.display_name == other.display_name and self.declined == other.declined and self.permissions == other.permissions

	def __bool__(self):
		return self.pending_member_id != 0 or self.contact_id != 0 or self.display_name != "" or self.declined or bool(self.permissions)

	def __hash__(self):
		return hash((self.pending_member_id, self.contact_id, self.display_name, self.declined, self.permissions))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, PendingGroupMember):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.pending_member_id == 0 or self.pending_member_id == expected.pending_member_id, "Invalid value: pending_member_id: " + str(expected.pending_member_id) + " != " + str(self.pending_member_id)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		assert expected.display_name == "" or self.display_name == expected.display_name, "Invalid value: display_name: " + str(expected.display_name) + " != " + str(self.display_name)
		assert expected.declined is False or self.declined == expected.declined, "Invalid value: declined: " + str(expected.declined) + " != " + str(self.declined)
		try:
			assert expected.permissions is None or self.permissions._test_assertion(expected.permissions)
		except AssertionError as e:
			raise AssertionError("permissions: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupMemberPermissions:
	def __init__(self, client: OlvidClient = None, admin: bool = False, remote_delete_anything: bool = False, edit_or_remote_delete_own_messages: bool = False, change_settings: bool = False, send_message: bool = False):
		self._client: OlvidClient = client
		self.admin: bool = admin
		self.remote_delete_anything: bool = remote_delete_anything
		self.edit_or_remote_delete_own_messages: bool = edit_or_remote_delete_own_messages
		self.change_settings: bool = change_settings
		self.send_message: bool = send_message

	def _update_content(self, group_member_permissions: GroupMemberPermissions) -> None:
		self.admin: bool = group_member_permissions.admin
		self.remote_delete_anything: bool = group_member_permissions.remote_delete_anything
		self.edit_or_remote_delete_own_messages: bool = group_member_permissions.edit_or_remote_delete_own_messages
		self.change_settings: bool = group_member_permissions.change_settings
		self.send_message: bool = group_member_permissions.send_message

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupMemberPermissions":
		return GroupMemberPermissions(client=self._client, admin=self.admin, remote_delete_anything=self.remote_delete_anything, edit_or_remote_delete_own_messages=self.edit_or_remote_delete_own_messages, change_settings=self.change_settings, send_message=self.send_message)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.group_pb2.GroupMemberPermissions, client: OlvidClient = None) -> "GroupMemberPermissions":
		return GroupMemberPermissions(client, admin=native_message.admin, remote_delete_anything=native_message.remote_delete_anything, edit_or_remote_delete_own_messages=native_message.edit_or_remote_delete_own_messages, change_settings=native_message.change_settings, send_message=native_message.send_message)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.group_pb2.GroupMemberPermissions], client: OlvidClient = None) -> list["GroupMemberPermissions"]:
		return [GroupMemberPermissions._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.group_pb2.GroupMemberPermissions], client: OlvidClient = None) -> "GroupMemberPermissions":
		native_message = await promise
		return GroupMemberPermissions._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupMemberPermissions"]):
		if messages is None:
			return []
		return [GroupMemberPermissions._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupMemberPermissions"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.group_pb2.GroupMemberPermissions(admin=message.admin if message.admin else None, remote_delete_anything=message.remote_delete_anything if message.remote_delete_anything else None, edit_or_remote_delete_own_messages=message.edit_or_remote_delete_own_messages if message.edit_or_remote_delete_own_messages else None, change_settings=message.change_settings if message.change_settings else None, send_message=message.send_message if message.send_message else None)

	def __str__(self):
		s: str = ''
		if self.admin:
			s += f'admin: {self.admin}, '
		if self.remote_delete_anything:
			s += f'remote_delete_anything: {self.remote_delete_anything}, '
		if self.edit_or_remote_delete_own_messages:
			s += f'edit_or_remote_delete_own_messages: {self.edit_or_remote_delete_own_messages}, '
		if self.change_settings:
			s += f'change_settings: {self.change_settings}, '
		if self.send_message:
			s += f'send_message: {self.send_message}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupMemberPermissions):
			return False
		return self.admin == other.admin and self.remote_delete_anything == other.remote_delete_anything and self.edit_or_remote_delete_own_messages == other.edit_or_remote_delete_own_messages and self.change_settings == other.change_settings and self.send_message == other.send_message

	def __bool__(self):
		return self.admin or self.remote_delete_anything or self.edit_or_remote_delete_own_messages or self.change_settings or self.send_message

	def __hash__(self):
		return hash((self.admin, self.remote_delete_anything, self.edit_or_remote_delete_own_messages, self.change_settings, self.send_message))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupMemberPermissions):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.admin is False or self.admin == expected.admin, "Invalid value: admin: " + str(expected.admin) + " != " + str(self.admin)
		assert expected.remote_delete_anything is False or self.remote_delete_anything == expected.remote_delete_anything, "Invalid value: remote_delete_anything: " + str(expected.remote_delete_anything) + " != " + str(self.remote_delete_anything)
		assert expected.edit_or_remote_delete_own_messages is False or self.edit_or_remote_delete_own_messages == expected.edit_or_remote_delete_own_messages, "Invalid value: edit_or_remote_delete_own_messages: " + str(expected.edit_or_remote_delete_own_messages) + " != " + str(self.edit_or_remote_delete_own_messages)
		assert expected.change_settings is False or self.change_settings == expected.change_settings, "Invalid value: change_settings: " + str(expected.change_settings) + " != " + str(self.change_settings)
		assert expected.send_message is False or self.send_message == expected.send_message, "Invalid value: send_message: " + str(expected.send_message) + " != " + str(self.send_message)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupFilter:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Empty(Enum):
		EMPTY_UNSPECIFIED = 0
		EMPTY_IS = 2
		EMPTY_IS_NOT = 1
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["GroupFilter.Empty"]:
			return [GroupFilter.Empty(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Keycloak(Enum):
		KEYCLOAK_UNSPECIFIED = 0
		KEYCLOAK_IS = 2
		KEYCLOAK_IS_NOT = 1
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["GroupFilter.Keycloak"]:
			return [GroupFilter.Keycloak(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Photo(Enum):
		PHOTO_UNSPECIFIED = 0
		PHOTO_HAS = 2
		PHOTO_HAS_NOT = 1
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["GroupFilter.Photo"]:
			return [GroupFilter.Photo(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, type: "Group.Type" = 0, empty: "GroupFilter.Empty" = 0, photo: "GroupFilter.Photo" = 0, keycloak: "GroupFilter.Keycloak" = 0, own_permissions_filter: "GroupPermissionFilter" = None, name_search: str = "", description_search: str = "", member_filters: "list[GroupMemberFilter]" = None, pending_member_filters: "list[PendingGroupMemberFilter]" = None):
		self._client: OlvidClient = client
		self.type: Group.Type = type
		self.empty: GroupFilter.Empty = empty
		self.photo: GroupFilter.Photo = photo
		self.keycloak: GroupFilter.Keycloak = keycloak
		self.own_permissions_filter: GroupPermissionFilter = own_permissions_filter
		self.name_search: str = name_search
		self.description_search: str = description_search
		self.member_filters: list[GroupMemberFilter] = member_filters
		self.pending_member_filters: list[PendingGroupMemberFilter] = pending_member_filters

	def _update_content(self, group_filter: GroupFilter) -> None:
		self.type: Group.Type = group_filter.type
		self.empty: GroupFilter.Empty = group_filter.empty
		self.photo: GroupFilter.Photo = group_filter.photo
		self.keycloak: GroupFilter.Keycloak = group_filter.keycloak
		self.own_permissions_filter: GroupPermissionFilter = group_filter.own_permissions_filter
		self.name_search: str = group_filter.name_search
		self.description_search: str = group_filter.description_search
		self.member_filters: list[GroupMemberFilter] = group_filter.member_filters
		self.pending_member_filters: list[PendingGroupMemberFilter] = group_filter.pending_member_filters

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupFilter":
		return GroupFilter(client=self._client, type=self.type, empty=self.empty, photo=self.photo, keycloak=self.keycloak, own_permissions_filter=self.own_permissions_filter._clone(), name_search=self.name_search, description_search=self.description_search, member_filters=[e._clone() for e in self.member_filters], pending_member_filters=[e._clone() for e in self.pending_member_filters])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.group_pb2.GroupFilter, client: OlvidClient = None) -> "GroupFilter":
		return GroupFilter(client, type=Group.Type(native_message.type), empty=GroupFilter.Empty(native_message.empty), photo=GroupFilter.Photo(native_message.photo), keycloak=GroupFilter.Keycloak(native_message.keycloak), own_permissions_filter=GroupPermissionFilter._from_native(native_message.own_permissions_filter, client=client), name_search=native_message.name_search, description_search=native_message.description_search, member_filters=GroupMemberFilter._from_native_list(native_message.member_filters, client=client), pending_member_filters=PendingGroupMemberFilter._from_native_list(native_message.pending_member_filters, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.group_pb2.GroupFilter], client: OlvidClient = None) -> list["GroupFilter"]:
		return [GroupFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.group_pb2.GroupFilter], client: OlvidClient = None) -> "GroupFilter":
		native_message = await promise
		return GroupFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupFilter"]):
		if messages is None:
			return []
		return [GroupFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.group_pb2.GroupFilter(type=message.type.value if message.type else None, empty=message.empty.value if message.empty else None, photo=message.photo.value if message.photo else None, keycloak=message.keycloak.value if message.keycloak else None, own_permissions_filter=GroupPermissionFilter._to_native(message.own_permissions_filter if message.own_permissions_filter else None), name_search=message.name_search if message.name_search else None, description_search=message.description_search if message.description_search else None, member_filters=GroupMemberFilter._to_native_list(message.member_filters if message.member_filters else None), pending_member_filters=PendingGroupMemberFilter._to_native_list(message.pending_member_filters if message.pending_member_filters else None))

	def __str__(self):
		s: str = ''
		if self.type:
			s += f'type: {self.type}, '
		if self.empty:
			s += f'empty: {self.empty}, '
		if self.photo:
			s += f'photo: {self.photo}, '
		if self.keycloak:
			s += f'keycloak: {self.keycloak}, '
		if self.own_permissions_filter:
			s += f'own_permissions_filter: ({self.own_permissions_filter}), '
		if self.name_search:
			s += f'name_search: {self.name_search}, '
		if self.description_search:
			s += f'description_search: {self.description_search}, '
		if self.member_filters:
			s += f'member_filters: {[str(el) for el in self.member_filters]}, '
		if self.pending_member_filters:
			s += f'pending_member_filters: {[str(el) for el in self.pending_member_filters]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupFilter):
			return False
		return self.type == other.type and self.empty == other.empty and self.photo == other.photo and self.keycloak == other.keycloak and self.own_permissions_filter == other.own_permissions_filter and self.name_search == other.name_search and self.description_search == other.description_search and self.member_filters == other.member_filters and self.pending_member_filters == other.pending_member_filters

	def __bool__(self):
		return bool(self.type) or bool(self.empty) or bool(self.photo) or bool(self.keycloak) or bool(self.own_permissions_filter) or self.name_search != "" or self.description_search != "" or bool(self.member_filters) or bool(self.pending_member_filters)

	def __hash__(self):
		return hash((self.type, self.empty, self.photo, self.keycloak, self.own_permissions_filter, self.name_search, self.description_search, tuple(self.member_filters), tuple(self.pending_member_filters)))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.type == 0 or self.type == expected.type, "Invalid value: type: " + str(expected.type) + " != " + str(self.type)
		assert expected.empty == 0 or self.empty == expected.empty, "Invalid value: empty: " + str(expected.empty) + " != " + str(self.empty)
		assert expected.photo == 0 or self.photo == expected.photo, "Invalid value: photo: " + str(expected.photo) + " != " + str(self.photo)
		assert expected.keycloak == 0 or self.keycloak == expected.keycloak, "Invalid value: keycloak: " + str(expected.keycloak) + " != " + str(self.keycloak)
		try:
			assert expected.own_permissions_filter is None or self.own_permissions_filter._test_assertion(expected.own_permissions_filter)
		except AssertionError as e:
			raise AssertionError("own_permissions_filter: " + str(e))
		assert expected.name_search == "" or self.name_search == expected.name_search, "Invalid value: name_search: " + str(expected.name_search) + " != " + str(self.name_search)
		assert expected.description_search == "" or self.description_search == expected.description_search, "Invalid value: description_search: " + str(expected.description_search) + " != " + str(self.description_search)
		pass  # print("Warning: test_assertion: skipped a list field member_filters")
		pass  # print("Warning: test_assertion: skipped a list field pending_member_filters")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupMemberFilter:
	def __init__(self, client: OlvidClient = None, contact_id: int = 0, permissions: "GroupPermissionFilter" = None):
		self._client: OlvidClient = client
		self.contact_id: int = contact_id
		self.permissions: GroupPermissionFilter = permissions

	def _update_content(self, group_member_filter: GroupMemberFilter) -> None:
		self.contact_id: int = group_member_filter.contact_id
		self.permissions: GroupPermissionFilter = group_member_filter.permissions

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupMemberFilter":
		return GroupMemberFilter(client=self._client, contact_id=self.contact_id, permissions=self.permissions._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.group_pb2.GroupMemberFilter, client: OlvidClient = None) -> "GroupMemberFilter":
		return GroupMemberFilter(client, contact_id=native_message.contact_id, permissions=GroupPermissionFilter._from_native(native_message.permissions, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.group_pb2.GroupMemberFilter], client: OlvidClient = None) -> list["GroupMemberFilter"]:
		return [GroupMemberFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.group_pb2.GroupMemberFilter], client: OlvidClient = None) -> "GroupMemberFilter":
		native_message = await promise
		return GroupMemberFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupMemberFilter"]):
		if messages is None:
			return []
		return [GroupMemberFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupMemberFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.group_pb2.GroupMemberFilter(contact_id=message.contact_id if message.contact_id else None, permissions=GroupPermissionFilter._to_native(message.permissions if message.permissions else None))

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		if self.permissions:
			s += f'permissions: ({self.permissions}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupMemberFilter):
			return False
		return self.contact_id == other.contact_id and self.permissions == other.permissions

	def __bool__(self):
		return self.contact_id != 0 or bool(self.permissions)

	def __hash__(self):
		return hash((self.contact_id, self.permissions))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupMemberFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		try:
			assert expected.permissions is None or self.permissions._test_assertion(expected.permissions)
		except AssertionError as e:
			raise AssertionError("permissions: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class PendingGroupMemberFilter:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Contact(Enum):
		CONTACT_UNSPECIFIED = 0
		CONTACT_IS = 1
		CONTACT_IS_NOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["PendingGroupMemberFilter.Contact"]:
			return [PendingGroupMemberFilter.Contact(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Declined(Enum):
		DECLINED_UNSPECIFIED = 0
		DECLINED_HAS = 1
		DECLINED_HAS_NOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["PendingGroupMemberFilter.Declined"]:
			return [PendingGroupMemberFilter.Declined(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, is_contact: "PendingGroupMemberFilter.Contact" = 0, has_declined: "PendingGroupMemberFilter.Declined" = 0, contact_id: int = 0, display_name_search: str = "", permissions: "GroupPermissionFilter" = None):
		self._client: OlvidClient = client
		self.is_contact: PendingGroupMemberFilter.Contact = is_contact
		self.has_declined: PendingGroupMemberFilter.Declined = has_declined
		self.contact_id: int = contact_id
		self.display_name_search: str = display_name_search
		self.permissions: GroupPermissionFilter = permissions

	def _update_content(self, pending_group_member_filter: PendingGroupMemberFilter) -> None:
		self.is_contact: PendingGroupMemberFilter.Contact = pending_group_member_filter.is_contact
		self.has_declined: PendingGroupMemberFilter.Declined = pending_group_member_filter.has_declined
		self.contact_id: int = pending_group_member_filter.contact_id
		self.display_name_search: str = pending_group_member_filter.display_name_search
		self.permissions: GroupPermissionFilter = pending_group_member_filter.permissions

	# noinspection PyProtectedMember
	def _clone(self) -> "PendingGroupMemberFilter":
		return PendingGroupMemberFilter(client=self._client, is_contact=self.is_contact, has_declined=self.has_declined, contact_id=self.contact_id, display_name_search=self.display_name_search, permissions=self.permissions._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.group_pb2.PendingGroupMemberFilter, client: OlvidClient = None) -> "PendingGroupMemberFilter":
		return PendingGroupMemberFilter(client, is_contact=PendingGroupMemberFilter.Contact(native_message.is_contact), has_declined=PendingGroupMemberFilter.Declined(native_message.has_declined), contact_id=native_message.contact_id, display_name_search=native_message.display_name_search, permissions=GroupPermissionFilter._from_native(native_message.permissions, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.group_pb2.PendingGroupMemberFilter], client: OlvidClient = None) -> list["PendingGroupMemberFilter"]:
		return [PendingGroupMemberFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.group_pb2.PendingGroupMemberFilter], client: OlvidClient = None) -> "PendingGroupMemberFilter":
		native_message = await promise
		return PendingGroupMemberFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["PendingGroupMemberFilter"]):
		if messages is None:
			return []
		return [PendingGroupMemberFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["PendingGroupMemberFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.group_pb2.PendingGroupMemberFilter(is_contact=message.is_contact.value if message.is_contact else None, has_declined=message.has_declined.value if message.has_declined else None, contact_id=message.contact_id if message.contact_id else None, display_name_search=message.display_name_search if message.display_name_search else None, permissions=GroupPermissionFilter._to_native(message.permissions if message.permissions else None))

	def __str__(self):
		s: str = ''
		if self.is_contact:
			s += f'is_contact: {self.is_contact}, '
		if self.has_declined:
			s += f'has_declined: {self.has_declined}, '
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		if self.display_name_search:
			s += f'display_name_search: {self.display_name_search}, '
		if self.permissions:
			s += f'permissions: ({self.permissions}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, PendingGroupMemberFilter):
			return False
		return self.is_contact == other.is_contact and self.has_declined == other.has_declined and self.contact_id == other.contact_id and self.display_name_search == other.display_name_search and self.permissions == other.permissions

	def __bool__(self):
		return bool(self.is_contact) or bool(self.has_declined) or self.contact_id != 0 or self.display_name_search != "" or bool(self.permissions)

	def __hash__(self):
		return hash((self.is_contact, self.has_declined, self.contact_id, self.display_name_search, self.permissions))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, PendingGroupMemberFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.is_contact == 0 or self.is_contact == expected.is_contact, "Invalid value: is_contact: " + str(expected.is_contact) + " != " + str(self.is_contact)
		assert expected.has_declined == 0 or self.has_declined == expected.has_declined, "Invalid value: has_declined: " + str(expected.has_declined) + " != " + str(self.has_declined)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		assert expected.display_name_search == "" or self.display_name_search == expected.display_name_search, "Invalid value: display_name_search: " + str(expected.display_name_search) + " != " + str(self.display_name_search)
		try:
			assert expected.permissions is None or self.permissions._test_assertion(expected.permissions)
		except AssertionError as e:
			raise AssertionError("permissions: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupPermissionFilter:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Admin(Enum):
		ADMIN_UNSPECIFIED = 0
		ADMIN_IS = 1
		ADMIN_IS_NOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["GroupPermissionFilter.Admin"]:
			return [GroupPermissionFilter.Admin(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class SendMessage(Enum):
		SEND_MESSAGE_UNSPECIFIED = 0
		SEND_MESSAGE_CAN = 1
		SEND_MESSAGE_CANNOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["GroupPermissionFilter.SendMessage"]:
			return [GroupPermissionFilter.SendMessage(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class RemoteDeleteAnything(Enum):
		REMOTE_DELETE_ANYTHING_UNSPECIFIED = 0
		REMOTE_DELETE_ANYTHING_CAN = 1
		REMOTE_DELETE_ANYTHING_CANNOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["GroupPermissionFilter.RemoteDeleteAnything"]:
			return [GroupPermissionFilter.RemoteDeleteAnything(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class EditOrRemoteDeleteOwnMessage(Enum):
		EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_UNSPECIFIED = 0
		EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_CAN = 1
		EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_CANNOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["GroupPermissionFilter.EditOrRemoteDeleteOwnMessage"]:
			return [GroupPermissionFilter.EditOrRemoteDeleteOwnMessage(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class ChangeSettings(Enum):
		CHANGE_SETTINGS_UNSPECIFIED = 0
		CHANGE_SETTINGS_CAN = 1
		CHANGE_SETTINGS_CANNOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["GroupPermissionFilter.ChangeSettings"]:
			return [GroupPermissionFilter.ChangeSettings(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, admin: "GroupPermissionFilter.Admin" = 0, send_message: "GroupPermissionFilter.SendMessage" = 0, remote_delete_anything: "GroupPermissionFilter.RemoteDeleteAnything" = 0, edit_or_remote_delete_own_messages: "GroupPermissionFilter.EditOrRemoteDeleteOwnMessage" = 0, change_settings: "GroupPermissionFilter.ChangeSettings" = 0):
		self._client: OlvidClient = client
		self.admin: GroupPermissionFilter.Admin = admin
		self.send_message: GroupPermissionFilter.SendMessage = send_message
		self.remote_delete_anything: GroupPermissionFilter.RemoteDeleteAnything = remote_delete_anything
		self.edit_or_remote_delete_own_messages: GroupPermissionFilter.EditOrRemoteDeleteOwnMessage = edit_or_remote_delete_own_messages
		self.change_settings: GroupPermissionFilter.ChangeSettings = change_settings

	def _update_content(self, group_permission_filter: GroupPermissionFilter) -> None:
		self.admin: GroupPermissionFilter.Admin = group_permission_filter.admin
		self.send_message: GroupPermissionFilter.SendMessage = group_permission_filter.send_message
		self.remote_delete_anything: GroupPermissionFilter.RemoteDeleteAnything = group_permission_filter.remote_delete_anything
		self.edit_or_remote_delete_own_messages: GroupPermissionFilter.EditOrRemoteDeleteOwnMessage = group_permission_filter.edit_or_remote_delete_own_messages
		self.change_settings: GroupPermissionFilter.ChangeSettings = group_permission_filter.change_settings

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupPermissionFilter":
		return GroupPermissionFilter(client=self._client, admin=self.admin, send_message=self.send_message, remote_delete_anything=self.remote_delete_anything, edit_or_remote_delete_own_messages=self.edit_or_remote_delete_own_messages, change_settings=self.change_settings)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.group_pb2.GroupPermissionFilter, client: OlvidClient = None) -> "GroupPermissionFilter":
		return GroupPermissionFilter(client, admin=GroupPermissionFilter.Admin(native_message.admin), send_message=GroupPermissionFilter.SendMessage(native_message.send_message), remote_delete_anything=GroupPermissionFilter.RemoteDeleteAnything(native_message.remote_delete_anything), edit_or_remote_delete_own_messages=GroupPermissionFilter.EditOrRemoteDeleteOwnMessage(native_message.edit_or_remote_delete_own_messages), change_settings=GroupPermissionFilter.ChangeSettings(native_message.change_settings))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.group_pb2.GroupPermissionFilter], client: OlvidClient = None) -> list["GroupPermissionFilter"]:
		return [GroupPermissionFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.group_pb2.GroupPermissionFilter], client: OlvidClient = None) -> "GroupPermissionFilter":
		native_message = await promise
		return GroupPermissionFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupPermissionFilter"]):
		if messages is None:
			return []
		return [GroupPermissionFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupPermissionFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.group_pb2.GroupPermissionFilter(admin=message.admin.value if message.admin else None, send_message=message.send_message.value if message.send_message else None, remote_delete_anything=message.remote_delete_anything.value if message.remote_delete_anything else None, edit_or_remote_delete_own_messages=message.edit_or_remote_delete_own_messages.value if message.edit_or_remote_delete_own_messages else None, change_settings=message.change_settings.value if message.change_settings else None)

	def __str__(self):
		s: str = ''
		if self.admin:
			s += f'admin: {self.admin}, '
		if self.send_message:
			s += f'send_message: {self.send_message}, '
		if self.remote_delete_anything:
			s += f'remote_delete_anything: {self.remote_delete_anything}, '
		if self.edit_or_remote_delete_own_messages:
			s += f'edit_or_remote_delete_own_messages: {self.edit_or_remote_delete_own_messages}, '
		if self.change_settings:
			s += f'change_settings: {self.change_settings}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupPermissionFilter):
			return False
		return self.admin == other.admin and self.send_message == other.send_message and self.remote_delete_anything == other.remote_delete_anything and self.edit_or_remote_delete_own_messages == other.edit_or_remote_delete_own_messages and self.change_settings == other.change_settings

	def __bool__(self):
		return bool(self.admin) or bool(self.send_message) or bool(self.remote_delete_anything) or bool(self.edit_or_remote_delete_own_messages) or bool(self.change_settings)

	def __hash__(self):
		return hash((self.admin, self.send_message, self.remote_delete_anything, self.edit_or_remote_delete_own_messages, self.change_settings))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupPermissionFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.admin == 0 or self.admin == expected.admin, "Invalid value: admin: " + str(expected.admin) + " != " + str(self.admin)
		assert expected.send_message == 0 or self.send_message == expected.send_message, "Invalid value: send_message: " + str(expected.send_message) + " != " + str(self.send_message)
		assert expected.remote_delete_anything == 0 or self.remote_delete_anything == expected.remote_delete_anything, "Invalid value: remote_delete_anything: " + str(expected.remote_delete_anything) + " != " + str(self.remote_delete_anything)
		assert expected.edit_or_remote_delete_own_messages == 0 or self.edit_or_remote_delete_own_messages == expected.edit_or_remote_delete_own_messages, "Invalid value: edit_or_remote_delete_own_messages: " + str(expected.edit_or_remote_delete_own_messages) + " != " + str(self.edit_or_remote_delete_own_messages)
		assert expected.change_settings == 0 or self.change_settings == expected.change_settings, "Invalid value: change_settings: " + str(expected.change_settings) + " != " + str(self.change_settings)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityDetails:
	def __init__(self, client: OlvidClient = None, first_name: str = "", last_name: str = "", company: str = "", position: str = ""):
		self._client: OlvidClient = client
		self.first_name: str = first_name
		self.last_name: str = last_name
		self.company: str = company
		self.position: str = position

	def _update_content(self, identity_details: IdentityDetails) -> None:
		self.first_name: str = identity_details.first_name
		self.last_name: str = identity_details.last_name
		self.company: str = identity_details.company
		self.position: str = identity_details.position

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityDetails":
		return IdentityDetails(client=self._client, first_name=self.first_name, last_name=self.last_name, company=self.company, position=self.position)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.identity_pb2.IdentityDetails, client: OlvidClient = None) -> "IdentityDetails":
		return IdentityDetails(client, first_name=native_message.first_name, last_name=native_message.last_name, company=native_message.company, position=native_message.position)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.identity_pb2.IdentityDetails], client: OlvidClient = None) -> list["IdentityDetails"]:
		return [IdentityDetails._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.identity_pb2.IdentityDetails], client: OlvidClient = None) -> "IdentityDetails":
		native_message = await promise
		return IdentityDetails._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityDetails"]):
		if messages is None:
			return []
		return [IdentityDetails._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityDetails"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.identity_pb2.IdentityDetails(first_name=message.first_name if message.first_name else None, last_name=message.last_name if message.last_name else None, company=message.company if message.company else None, position=message.position if message.position else None)

	def __str__(self):
		s: str = ''
		if self.first_name:
			s += f'first_name: {self.first_name}, '
		if self.last_name:
			s += f'last_name: {self.last_name}, '
		if self.company:
			s += f'company: {self.company}, '
		if self.position:
			s += f'position: {self.position}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityDetails):
			return False
		return self.first_name == other.first_name and self.last_name == other.last_name and self.company == other.company and self.position == other.position

	def __bool__(self):
		return self.first_name != "" or self.last_name != "" or self.company != "" or self.position != ""

	def __hash__(self):
		return hash((self.first_name, self.last_name, self.company, self.position))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityDetails):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.first_name == "" or self.first_name == expected.first_name, "Invalid value: first_name: " + str(expected.first_name) + " != " + str(self.first_name)
		assert expected.last_name == "" or self.last_name == expected.last_name, "Invalid value: last_name: " + str(expected.last_name) + " != " + str(self.last_name)
		assert expected.company == "" or self.company == expected.company, "Invalid value: company: " + str(expected.company) + " != " + str(self.company)
		assert expected.position == "" or self.position == expected.position, "Invalid value: position: " + str(expected.position) + " != " + str(self.position)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class Identity:
	class ApiKey:
		class Permission:
			def __init__(self, client: OlvidClient = None, call: bool = False, multi_device: bool = False):
				self._client: OlvidClient = client
				self.call: bool = call
				self.multi_device: bool = multi_device
		
			def _update_content(self, permission: Identity.ApiKey.Permission) -> None:
				self.call: bool = permission.call
				self.multi_device: bool = permission.multi_device
		
			# noinspection PyProtectedMember
			def _clone(self) -> "Identity.ApiKey.Permission":
				return Identity.ApiKey.Permission(client=self._client, call=self.call, multi_device=self.multi_device)
		
			# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
			@staticmethod
			def _from_native(native_message: olvid.daemon.datatypes.v1.identity_pb2.Identity.ApiKey.Permission, client: OlvidClient = None) -> "Identity.ApiKey.Permission":
				return Identity.ApiKey.Permission(client, call=native_message.call, multi_device=native_message.multi_device)
		
			# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
			@staticmethod
			def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.identity_pb2.Identity.ApiKey.Permission], client: OlvidClient = None) -> list["Identity.ApiKey.Permission"]:
				return [Identity.ApiKey.Permission._from_native(native_message, client=client) for native_message in native_message_list]
		
			# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
			@staticmethod
			async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.identity_pb2.Identity.ApiKey.Permission], client: OlvidClient = None) -> "Identity.ApiKey.Permission":
				native_message = await promise
				return Identity.ApiKey.Permission._from_native(native_message, client=client)
		
			# noinspection PyUnresolvedReferences,PyProtectedMember
			@staticmethod
			def _to_native_list(messages: list["Identity.ApiKey.Permission"]):
				if messages is None:
					return []
				return [Identity.ApiKey.Permission._to_native(message) for message in messages]
		
			# noinspection PyUnresolvedReferences,PyProtectedMember
			@staticmethod
			def _to_native(message: Optional["Identity.ApiKey.Permission"]):
				if message is None:
					return None
				return olvid.daemon.datatypes.v1.identity_pb2.Identity.ApiKey.Permission(call=message.call if message.call else None, multi_device=message.multi_device if message.multi_device else None)
		
			def __str__(self):
				s: str = ''
				if self.call:
					s += f'call: {self.call}, '
				if self.multi_device:
					s += f'multi_device: {self.multi_device}, '
				return s.removesuffix(', ')
		
			def __eq__(self, other):
				if not isinstance(other, Identity.ApiKey.Permission):
					return False
				return self.call == other.call and self.multi_device == other.multi_device
		
			def __bool__(self):
				return self.call or self.multi_device
		
			def __hash__(self):
				return hash((self.call, self.multi_device))
		
			# For tests routines
			# noinspection DuplicatedCode,PyProtectedMember
			def _test_assertion(self, expected):
				if not isinstance(expected, Identity.ApiKey.Permission):
					assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
				assert expected.call is False or self.call == expected.call, "Invalid value: call: " + str(expected.call) + " != " + str(self.call)
				assert expected.multi_device is False or self.multi_device == expected.multi_device, "Invalid value: multi_device: " + str(expected.multi_device) + " != " + str(self.multi_device)
				return True
	
		def __init__(self, client: OlvidClient = None, permission: "Identity.ApiKey.Permission" = None, expiration_timestamp: int = 0):
			self._client: OlvidClient = client
			self.permission: Identity.ApiKey.Permission = permission
			self.expiration_timestamp: int = expiration_timestamp
	
		def _update_content(self, api_key: Identity.ApiKey) -> None:
			self.permission: Identity.ApiKey.Permission = api_key.permission
			self.expiration_timestamp: int = api_key.expiration_timestamp
	
		# noinspection PyProtectedMember
		def _clone(self) -> "Identity.ApiKey":
			return Identity.ApiKey(client=self._client, permission=self.permission._clone(), expiration_timestamp=self.expiration_timestamp)
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
		@staticmethod
		def _from_native(native_message: olvid.daemon.datatypes.v1.identity_pb2.Identity.ApiKey, client: OlvidClient = None) -> "Identity.ApiKey":
			return Identity.ApiKey(client, permission=Identity.ApiKey.Permission._from_native(native_message.permission, client=client), expiration_timestamp=native_message.expiration_timestamp)
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
		@staticmethod
		def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.identity_pb2.Identity.ApiKey], client: OlvidClient = None) -> list["Identity.ApiKey"]:
			return [Identity.ApiKey._from_native(native_message, client=client) for native_message in native_message_list]
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
		@staticmethod
		async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.identity_pb2.Identity.ApiKey], client: OlvidClient = None) -> "Identity.ApiKey":
			native_message = await promise
			return Identity.ApiKey._from_native(native_message, client=client)
	
		# noinspection PyUnresolvedReferences,PyProtectedMember
		@staticmethod
		def _to_native_list(messages: list["Identity.ApiKey"]):
			if messages is None:
				return []
			return [Identity.ApiKey._to_native(message) for message in messages]
	
		# noinspection PyUnresolvedReferences,PyProtectedMember
		@staticmethod
		def _to_native(message: Optional["Identity.ApiKey"]):
			if message is None:
				return None
			return olvid.daemon.datatypes.v1.identity_pb2.Identity.ApiKey(permission=Identity.ApiKey.Permission._to_native(message.permission if message.permission else None), expiration_timestamp=message.expiration_timestamp if message.expiration_timestamp else None)
	
		def __str__(self):
			s: str = ''
			if self.permission:
				s += f'permission: ({self.permission}), '
			if self.expiration_timestamp:
				s += f'expiration_timestamp: {self.expiration_timestamp}, '
			return s.removesuffix(', ')
	
		def __eq__(self, other):
			if not isinstance(other, Identity.ApiKey):
				return False
			return self.permission == other.permission and self.expiration_timestamp == other.expiration_timestamp
	
		def __bool__(self):
			return bool(self.permission) or self.expiration_timestamp != 0
	
		def __hash__(self):
			return hash((self.permission, self.expiration_timestamp))
	
		# For tests routines
		# noinspection DuplicatedCode,PyProtectedMember
		def _test_assertion(self, expected):
			if not isinstance(expected, Identity.ApiKey):
				assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
			try:
				assert expected.permission is None or self.permission._test_assertion(expected.permission)
			except AssertionError as e:
				raise AssertionError("permission: " + str(e))
			assert expected.expiration_timestamp == 0 or self.expiration_timestamp == expected.expiration_timestamp, "Invalid value: expiration_timestamp: " + str(expected.expiration_timestamp) + " != " + str(self.expiration_timestamp)
			return True

	def __init__(self, client: OlvidClient = None, id: int = 0, display_name: str = "", details: "IdentityDetails" = None, invitation_url: str = "", keycloak_managed: bool = False, has_a_photo: bool = False, api_key: "Identity.ApiKey" = None):
		self._client: OlvidClient = client
		self.id: int = id
		self.display_name: str = display_name
		self.details: IdentityDetails = details
		self.invitation_url: str = invitation_url
		self.keycloak_managed: bool = keycloak_managed
		self.has_a_photo: bool = has_a_photo
		self.api_key: Identity.ApiKey = api_key

	def _update_content(self, identity: Identity) -> None:
		self.id: int = identity.id
		self.display_name: str = identity.display_name
		self.details: IdentityDetails = identity.details
		self.invitation_url: str = identity.invitation_url
		self.keycloak_managed: bool = identity.keycloak_managed
		self.has_a_photo: bool = identity.has_a_photo
		self.api_key: Identity.ApiKey = identity.api_key

	# noinspection PyProtectedMember
	def _clone(self) -> "Identity":
		return Identity(client=self._client, id=self.id, display_name=self.display_name, details=self.details._clone(), invitation_url=self.invitation_url, keycloak_managed=self.keycloak_managed, has_a_photo=self.has_a_photo, api_key=self.api_key._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.identity_pb2.Identity, client: OlvidClient = None) -> "Identity":
		return Identity(client, id=native_message.id, display_name=native_message.display_name, details=IdentityDetails._from_native(native_message.details, client=client), invitation_url=native_message.invitation_url, keycloak_managed=native_message.keycloak_managed, has_a_photo=native_message.has_a_photo, api_key=Identity.ApiKey._from_native(native_message.api_key, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.identity_pb2.Identity], client: OlvidClient = None) -> list["Identity"]:
		return [Identity._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.identity_pb2.Identity], client: OlvidClient = None) -> "Identity":
		native_message = await promise
		return Identity._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["Identity"]):
		if messages is None:
			return []
		return [Identity._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["Identity"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.identity_pb2.Identity(id=message.id if message.id else None, display_name=message.display_name if message.display_name else None, details=IdentityDetails._to_native(message.details if message.details else None), invitation_url=message.invitation_url if message.invitation_url else None, keycloak_managed=message.keycloak_managed if message.keycloak_managed else None, has_a_photo=message.has_a_photo if message.has_a_photo else None, api_key=Identity.ApiKey._to_native(message.api_key if message.api_key else None))

	def __str__(self):
		s: str = ''
		if self.id:
			s += f'id: {self.id}, '
		if self.display_name:
			s += f'display_name: {self.display_name}, '
		if self.details:
			s += f'details: ({self.details}), '
		if self.invitation_url:
			s += f'invitation_url: {self.invitation_url}, '
		if self.keycloak_managed:
			s += f'keycloak_managed: {self.keycloak_managed}, '
		if self.has_a_photo:
			s += f'has_a_photo: {self.has_a_photo}, '
		if self.api_key:
			s += f'api_key: ({self.api_key}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, Identity):
			return False
		return self.id == other.id and self.display_name == other.display_name and self.details == other.details and self.invitation_url == other.invitation_url and self.keycloak_managed == other.keycloak_managed and self.has_a_photo == other.has_a_photo and self.api_key == other.api_key

	def __bool__(self):
		return self.id != 0 or self.display_name != "" or bool(self.details) or self.invitation_url != "" or self.keycloak_managed or self.has_a_photo or bool(self.api_key)

	def __hash__(self):
		return hash((self.id, self.display_name, self.details, self.invitation_url, self.keycloak_managed, self.has_a_photo, self.api_key))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, Identity):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.id == 0 or self.id == expected.id, "Invalid value: id: " + str(expected.id) + " != " + str(self.id)
		assert expected.display_name == "" or self.display_name == expected.display_name, "Invalid value: display_name: " + str(expected.display_name) + " != " + str(self.display_name)
		try:
			assert expected.details is None or self.details._test_assertion(expected.details)
		except AssertionError as e:
			raise AssertionError("details: " + str(e))
		assert expected.invitation_url == "" or self.invitation_url == expected.invitation_url, "Invalid value: invitation_url: " + str(expected.invitation_url) + " != " + str(self.invitation_url)
		assert expected.keycloak_managed is False or self.keycloak_managed == expected.keycloak_managed, "Invalid value: keycloak_managed: " + str(expected.keycloak_managed) + " != " + str(self.keycloak_managed)
		assert expected.has_a_photo is False or self.has_a_photo == expected.has_a_photo, "Invalid value: has_a_photo: " + str(expected.has_a_photo) + " != " + str(self.has_a_photo)
		try:
			assert expected.api_key is None or self.api_key._test_assertion(expected.api_key)
		except AssertionError as e:
			raise AssertionError("api_key: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityFilter:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Keycloak(Enum):
		KEYCLOAK_UNSPECIFIED = 0
		KEYCLOAK_IS = 2
		KEYCLOAK_IS_NOT = 1
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["IdentityFilter.Keycloak"]:
			return [IdentityFilter.Keycloak(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Photo(Enum):
		PHOTO_UNSPECIFIED = 0
		PHOTO_HAS = 2
		PHOTO_HAS_NOT = 1
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["IdentityFilter.Photo"]:
			return [IdentityFilter.Photo(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class ApiKey(Enum):
		API_KEY_UNSPECIFIED = 0
		API_KEY_HAS = 2
		API_KEY_HAS_NOT = 1
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["IdentityFilter.ApiKey"]:
			return [IdentityFilter.ApiKey(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, keycloak: "IdentityFilter.Keycloak" = 0, photo: "IdentityFilter.Photo" = 0, api_key: "IdentityFilter.ApiKey" = 0, display_name_search: str = "", details_search: "IdentityDetails" = None):
		self._client: OlvidClient = client
		self.keycloak: IdentityFilter.Keycloak = keycloak
		self.photo: IdentityFilter.Photo = photo
		self.api_key: IdentityFilter.ApiKey = api_key
		self.display_name_search: str = display_name_search
		self.details_search: IdentityDetails = details_search

	def _update_content(self, identity_filter: IdentityFilter) -> None:
		self.keycloak: IdentityFilter.Keycloak = identity_filter.keycloak
		self.photo: IdentityFilter.Photo = identity_filter.photo
		self.api_key: IdentityFilter.ApiKey = identity_filter.api_key
		self.display_name_search: str = identity_filter.display_name_search
		self.details_search: IdentityDetails = identity_filter.details_search

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityFilter":
		return IdentityFilter(client=self._client, keycloak=self.keycloak, photo=self.photo, api_key=self.api_key, display_name_search=self.display_name_search, details_search=self.details_search._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.identity_pb2.IdentityFilter, client: OlvidClient = None) -> "IdentityFilter":
		return IdentityFilter(client, keycloak=IdentityFilter.Keycloak(native_message.keycloak), photo=IdentityFilter.Photo(native_message.photo), api_key=IdentityFilter.ApiKey(native_message.api_key), display_name_search=native_message.display_name_search, details_search=IdentityDetails._from_native(native_message.details_search, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.identity_pb2.IdentityFilter], client: OlvidClient = None) -> list["IdentityFilter"]:
		return [IdentityFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.identity_pb2.IdentityFilter], client: OlvidClient = None) -> "IdentityFilter":
		native_message = await promise
		return IdentityFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityFilter"]):
		if messages is None:
			return []
		return [IdentityFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.identity_pb2.IdentityFilter(keycloak=message.keycloak.value if message.keycloak else None, photo=message.photo.value if message.photo else None, api_key=message.api_key.value if message.api_key else None, display_name_search=message.display_name_search if message.display_name_search else None, details_search=IdentityDetails._to_native(message.details_search if message.details_search else None))

	def __str__(self):
		s: str = ''
		if self.keycloak:
			s += f'keycloak: {self.keycloak}, '
		if self.photo:
			s += f'photo: {self.photo}, '
		if self.api_key:
			s += f'api_key: {self.api_key}, '
		if self.display_name_search:
			s += f'display_name_search: {self.display_name_search}, '
		if self.details_search:
			s += f'details_search: ({self.details_search}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityFilter):
			return False
		return self.keycloak == other.keycloak and self.photo == other.photo and self.api_key == other.api_key and self.display_name_search == other.display_name_search and self.details_search == other.details_search

	def __bool__(self):
		return bool(self.keycloak) or bool(self.photo) or bool(self.api_key) or self.display_name_search != "" or bool(self.details_search)

	def __hash__(self):
		return hash((self.keycloak, self.photo, self.api_key, self.display_name_search, self.details_search))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.keycloak == 0 or self.keycloak == expected.keycloak, "Invalid value: keycloak: " + str(expected.keycloak) + " != " + str(self.keycloak)
		assert expected.photo == 0 or self.photo == expected.photo, "Invalid value: photo: " + str(expected.photo) + " != " + str(self.photo)
		assert expected.api_key == 0 or self.api_key == expected.api_key, "Invalid value: api_key: " + str(expected.api_key) + " != " + str(self.api_key)
		assert expected.display_name_search == "" or self.display_name_search == expected.display_name_search, "Invalid value: display_name_search: " + str(expected.display_name_search) + " != " + str(self.display_name_search)
		try:
			assert expected.details_search is None or self.details_search._test_assertion(expected.details_search)
		except AssertionError as e:
			raise AssertionError("details_search: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class Invitation:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Status(Enum):
		STATUS_UNSPECIFIED = 0
		STATUS_INVITATION_WAIT_YOU_TO_ACCEPT = 1
		STATUS_INVITATION_WAIT_IT_TO_ACCEPT = 2
		STATUS_INVITATION_STATUS_IN_PROGRESS = 3
		STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE = 4
		STATUS_INVITATION_WAIT_IT_FOR_SAS_EXCHANGE = 5
		STATUS_INTRODUCTION_WAIT_IT_TO_ACCEPT = 7
		STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT = 8
		STATUS_ONE_TO_ONE_INVITATION_WAIT_IT_TO_ACCEPT = 9
		STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT = 10
		STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT = 11
		STATUS_GROUP_INVITATION_FROZEN = 12
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["Invitation.Status"]:
			return [Invitation.Status(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, id: int = 0, status: "Invitation.Status" = 0, display_name: str = "", timestamp: int = 0, sas: str = ""):
		self._client: OlvidClient = client
		self.id: int = id
		self.status: Invitation.Status = status
		self.display_name: str = display_name
		self.timestamp: int = timestamp
		self.sas: str = sas

	def _update_content(self, invitation: Invitation) -> None:
		self.id: int = invitation.id
		self.status: Invitation.Status = invitation.status
		self.display_name: str = invitation.display_name
		self.timestamp: int = invitation.timestamp
		self.sas: str = invitation.sas

	# noinspection PyProtectedMember
	def _clone(self) -> "Invitation":
		return Invitation(client=self._client, id=self.id, status=self.status, display_name=self.display_name, timestamp=self.timestamp, sas=self.sas)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.invitation_pb2.Invitation, client: OlvidClient = None) -> "Invitation":
		return Invitation(client, id=native_message.id, status=Invitation.Status(native_message.status), display_name=native_message.display_name, timestamp=native_message.timestamp, sas=native_message.sas)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.invitation_pb2.Invitation], client: OlvidClient = None) -> list["Invitation"]:
		return [Invitation._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.invitation_pb2.Invitation], client: OlvidClient = None) -> "Invitation":
		native_message = await promise
		return Invitation._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["Invitation"]):
		if messages is None:
			return []
		return [Invitation._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["Invitation"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.invitation_pb2.Invitation(id=message.id if message.id else None, status=message.status.value if message.status else None, display_name=message.display_name if message.display_name else None, timestamp=message.timestamp if message.timestamp else None, sas=message.sas if message.sas else None)

	def __str__(self):
		s: str = ''
		if self.id:
			s += f'id: {self.id}, '
		if self.status:
			s += f'status: {self.status}, '
		if self.display_name:
			s += f'display_name: {self.display_name}, '
		if self.timestamp:
			s += f'timestamp: {self.timestamp}, '
		if self.sas:
			s += f'sas: {self.sas}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, Invitation):
			return False
		return self.id == other.id and self.status == other.status and self.display_name == other.display_name and self.timestamp == other.timestamp and self.sas == other.sas

	def __bool__(self):
		return self.id != 0 or bool(self.status) or self.display_name != "" or self.timestamp != 0 or self.sas != ""

	def __hash__(self):
		return hash((self.id, self.status, self.display_name, self.timestamp, self.sas))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, Invitation):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.id == 0 or self.id == expected.id, "Invalid value: id: " + str(expected.id) + " != " + str(self.id)
		assert expected.status == 0 or self.status == expected.status, "Invalid value: status: " + str(expected.status) + " != " + str(self.status)
		assert expected.display_name == "" or self.display_name == expected.display_name, "Invalid value: display_name: " + str(expected.display_name) + " != " + str(self.display_name)
		assert expected.timestamp == 0 or self.timestamp == expected.timestamp, "Invalid value: timestamp: " + str(expected.timestamp) + " != " + str(self.timestamp)
		assert expected.sas == "" or self.sas == expected.sas, "Invalid value: sas: " + str(expected.sas) + " != " + str(self.sas)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationFilter:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Type(Enum):
		TYPE_UNSPECIFIED = 0
		TYPE_INVITATION = 1
		TYPE_INTRODUCTION = 2
		TYPE_GROUP = 3
		TYPE_ONE_TO_ONE = 4
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["InvitationFilter.Type"]:
			return [InvitationFilter.Type(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, status: "Invitation.Status" = 0, type: "InvitationFilter.Type" = 0, display_name_search: str = "", min_timestamp: int = 0, max_timestamp: int = 0):
		self._client: OlvidClient = client
		self.status: Invitation.Status = status
		self.type: InvitationFilter.Type = type
		self.display_name_search: str = display_name_search
		self.min_timestamp: int = min_timestamp
		self.max_timestamp: int = max_timestamp

	def _update_content(self, invitation_filter: InvitationFilter) -> None:
		self.status: Invitation.Status = invitation_filter.status
		self.type: InvitationFilter.Type = invitation_filter.type
		self.display_name_search: str = invitation_filter.display_name_search
		self.min_timestamp: int = invitation_filter.min_timestamp
		self.max_timestamp: int = invitation_filter.max_timestamp

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationFilter":
		return InvitationFilter(client=self._client, status=self.status, type=self.type, display_name_search=self.display_name_search, min_timestamp=self.min_timestamp, max_timestamp=self.max_timestamp)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.invitation_pb2.InvitationFilter, client: OlvidClient = None) -> "InvitationFilter":
		return InvitationFilter(client, status=Invitation.Status(native_message.status), type=InvitationFilter.Type(native_message.type), display_name_search=native_message.display_name_search, min_timestamp=native_message.min_timestamp, max_timestamp=native_message.max_timestamp)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.invitation_pb2.InvitationFilter], client: OlvidClient = None) -> list["InvitationFilter"]:
		return [InvitationFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.invitation_pb2.InvitationFilter], client: OlvidClient = None) -> "InvitationFilter":
		native_message = await promise
		return InvitationFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationFilter"]):
		if messages is None:
			return []
		return [InvitationFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.invitation_pb2.InvitationFilter(status=message.status.value if message.status else None, type=message.type.value if message.type else None, display_name_search=message.display_name_search if message.display_name_search else None, min_timestamp=message.min_timestamp if message.min_timestamp else None, max_timestamp=message.max_timestamp if message.max_timestamp else None)

	def __str__(self):
		s: str = ''
		if self.status:
			s += f'status: {self.status}, '
		if self.type:
			s += f'type: {self.type}, '
		if self.display_name_search:
			s += f'display_name_search: {self.display_name_search}, '
		if self.min_timestamp:
			s += f'min_timestamp: {self.min_timestamp}, '
		if self.max_timestamp:
			s += f'max_timestamp: {self.max_timestamp}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationFilter):
			return False
		return self.status == other.status and self.type == other.type and self.display_name_search == other.display_name_search and self.min_timestamp == other.min_timestamp and self.max_timestamp == other.max_timestamp

	def __bool__(self):
		return bool(self.status) or bool(self.type) or self.display_name_search != "" or self.min_timestamp != 0 or self.max_timestamp != 0

	def __hash__(self):
		return hash((self.status, self.type, self.display_name_search, self.min_timestamp, self.max_timestamp))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.status == 0 or self.status == expected.status, "Invalid value: status: " + str(expected.status) + " != " + str(self.status)
		assert expected.type == 0 or self.type == expected.type, "Invalid value: type: " + str(expected.type) + " != " + str(self.type)
		assert expected.display_name_search == "" or self.display_name_search == expected.display_name_search, "Invalid value: display_name_search: " + str(expected.display_name_search) + " != " + str(self.display_name_search)
		assert expected.min_timestamp == 0 or self.min_timestamp == expected.min_timestamp, "Invalid value: min_timestamp: " + str(expected.min_timestamp) + " != " + str(self.min_timestamp)
		assert expected.max_timestamp == 0 or self.max_timestamp == expected.max_timestamp, "Invalid value: max_timestamp: " + str(expected.max_timestamp) + " != " + str(self.max_timestamp)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageId:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Type(Enum):
		TYPE_UNSPECIFIED = 0
		TYPE_INBOUND = 1
		TYPE_OUTBOUND = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["MessageId.Type"]:
			return [MessageId.Type(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, type: "MessageId.Type" = 0, id: int = 0):
		self._client: OlvidClient = client
		self.type: MessageId.Type = type
		self.id: int = id

	def _update_content(self, message_id: MessageId) -> None:
		self.type: MessageId.Type = message_id.type
		self.id: int = message_id.id

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageId":
		return MessageId(client=self._client, type=self.type, id=self.id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.message_pb2.MessageId, client: OlvidClient = None) -> "MessageId":
		return MessageId(client, type=MessageId.Type(native_message.type), id=native_message.id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.message_pb2.MessageId], client: OlvidClient = None) -> list["MessageId"]:
		return [MessageId._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.message_pb2.MessageId], client: OlvidClient = None) -> "MessageId":
		native_message = await promise
		return MessageId._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageId"]):
		if messages is None:
			return []
		return [MessageId._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageId"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.message_pb2.MessageId(type=message.type.value if message.type else None, id=message.id if message.id else None)

	def __str__(self):
		s: str = ''
		if self.type:
			s += f'type: {self.type}, '
		if self.id:
			s += f'id: {self.id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageId):
			return False
		return self.type == other.type and self.id == other.id

	def __bool__(self):
		return bool(self.type) or self.id != 0

	def __hash__(self):
		return hash((self.type, self.id))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageId):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.type == 0 or self.type == expected.type, "Invalid value: type: " + str(expected.type) + " != " + str(self.type)
		assert expected.id == 0 or self.id == expected.id, "Invalid value: id: " + str(expected.id) + " != " + str(self.id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class Message:
	def __init__(self, client: OlvidClient = None, id: "MessageId" = None, discussion_id: int = 0, sender_id: int = 0, body: str = "", sort_index: float = 0.0, timestamp: int = 0, attachments_count: int = 0, replied_message_id: "MessageId" = None, message_location: "MessageLocation" = None, reactions: "list[MessageReaction]" = None):
		self._client: OlvidClient = client
		self.id: MessageId = id
		self.discussion_id: int = discussion_id
		self.sender_id: int = sender_id
		self.body: str = body
		self.sort_index: float = sort_index
		self.timestamp: int = timestamp
		self.attachments_count: int = attachments_count
		self.replied_message_id: MessageId = replied_message_id
		self.message_location: MessageLocation = message_location
		self.reactions: list[MessageReaction] = reactions

	def _update_content(self, message: Message) -> None:
		self.id: MessageId = message.id
		self.discussion_id: int = message.discussion_id
		self.sender_id: int = message.sender_id
		self.body: str = message.body
		self.sort_index: float = message.sort_index
		self.timestamp: int = message.timestamp
		self.attachments_count: int = message.attachments_count
		self.replied_message_id: MessageId = message.replied_message_id
		self.message_location: MessageLocation = message.message_location
		self.reactions: list[MessageReaction] = message.reactions

	# noinspection PyProtectedMember
	def _clone(self) -> "Message":
		return Message(client=self._client, id=self.id._clone(), discussion_id=self.discussion_id, sender_id=self.sender_id, body=self.body, sort_index=self.sort_index, timestamp=self.timestamp, attachments_count=self.attachments_count, replied_message_id=self.replied_message_id._clone(), message_location=self.message_location._clone(), reactions=[e._clone() for e in self.reactions])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.message_pb2.Message, client: OlvidClient = None) -> "Message":
		return Message(client, id=MessageId._from_native(native_message.id, client=client), discussion_id=native_message.discussion_id, sender_id=native_message.sender_id, body=native_message.body, sort_index=native_message.sort_index, timestamp=native_message.timestamp, attachments_count=native_message.attachments_count, replied_message_id=MessageId._from_native(native_message.replied_message_id, client=client), message_location=MessageLocation._from_native(native_message.message_location, client=client), reactions=MessageReaction._from_native_list(native_message.reactions, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.message_pb2.Message], client: OlvidClient = None) -> list["Message"]:
		return [Message._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.message_pb2.Message], client: OlvidClient = None) -> "Message":
		native_message = await promise
		return Message._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["Message"]):
		if messages is None:
			return []
		return [Message._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["Message"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.message_pb2.Message(id=MessageId._to_native(message.id if message.id else None), discussion_id=message.discussion_id if message.discussion_id else None, sender_id=message.sender_id if message.sender_id else None, body=message.body if message.body else None, sort_index=message.sort_index if message.sort_index else None, timestamp=message.timestamp if message.timestamp else None, attachments_count=message.attachments_count if message.attachments_count else None, replied_message_id=MessageId._to_native(message.replied_message_id if message.replied_message_id else None), message_location=MessageLocation._to_native(message.message_location if message.message_location else None), reactions=MessageReaction._to_native_list(message.reactions if message.reactions else None))

	def __str__(self):
		s: str = ''
		if self.id:
			s += f'id: ({self.id}), '
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.sender_id:
			s += f'sender_id: {self.sender_id}, '
		if self.body:
			s += f'body: {self.body}, '
		if self.sort_index:
			s += f'sort_index: {self.sort_index}, '
		if self.timestamp:
			s += f'timestamp: {self.timestamp}, '
		if self.attachments_count:
			s += f'attachments_count: {self.attachments_count}, '
		if self.replied_message_id:
			s += f'replied_message_id: ({self.replied_message_id}), '
		if self.message_location:
			s += f'message_location: ({self.message_location}), '
		if self.reactions:
			s += f'reactions: {[str(el) for el in self.reactions]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, Message):
			return False
		return self.id == other.id and self.discussion_id == other.discussion_id and self.sender_id == other.sender_id and self.body == other.body and self.sort_index == other.sort_index and self.timestamp == other.timestamp and self.attachments_count == other.attachments_count and self.replied_message_id == other.replied_message_id and self.message_location == other.message_location and self.reactions == other.reactions

	def __bool__(self):
		return bool(self.id) or self.discussion_id != 0 or self.sender_id != 0 or self.body != "" or self.sort_index != 0.0 or self.timestamp != 0 or self.attachments_count != 0 or bool(self.replied_message_id) or bool(self.message_location) or bool(self.reactions)

	def __hash__(self):
		return hash((self.id, self.discussion_id, self.sender_id, self.body, self.sort_index, self.timestamp, self.attachments_count, self.replied_message_id, self.message_location, tuple(self.reactions)))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, Message):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.id is None or self.id._test_assertion(expected.id)
		except AssertionError as e:
			raise AssertionError("id: " + str(e))
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.sender_id == 0 or self.sender_id == expected.sender_id, "Invalid value: sender_id: " + str(expected.sender_id) + " != " + str(self.sender_id)
		assert expected.body == "" or self.body == expected.body, "Invalid value: body: " + str(expected.body) + " != " + str(self.body)
		assert expected.sort_index == 0.0 or self.sort_index == expected.sort_index, "Invalid value: sort_index: " + str(expected.sort_index) + " != " + str(self.sort_index)
		assert expected.timestamp == 0 or self.timestamp == expected.timestamp, "Invalid value: timestamp: " + str(expected.timestamp) + " != " + str(self.timestamp)
		assert expected.attachments_count == 0 or self.attachments_count == expected.attachments_count, "Invalid value: attachments_count: " + str(expected.attachments_count) + " != " + str(self.attachments_count)
		try:
			assert expected.replied_message_id is None or self.replied_message_id._test_assertion(expected.replied_message_id)
		except AssertionError as e:
			raise AssertionError("replied_message_id: " + str(e))
		try:
			assert expected.message_location is None or self.message_location._test_assertion(expected.message_location)
		except AssertionError as e:
			raise AssertionError("message_location: " + str(e))
		pass  # print("Warning: test_assertion: skipped a list field reactions")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageEphemerality:
	def __init__(self, client: OlvidClient = None, read_once: bool = False, existence_duration: int = 0, visibility_duration: int = 0):
		self._client: OlvidClient = client
		self.read_once: bool = read_once
		self.existence_duration: int = existence_duration
		self.visibility_duration: int = visibility_duration

	def _update_content(self, message_ephemerality: MessageEphemerality) -> None:
		self.read_once: bool = message_ephemerality.read_once
		self.existence_duration: int = message_ephemerality.existence_duration
		self.visibility_duration: int = message_ephemerality.visibility_duration

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageEphemerality":
		return MessageEphemerality(client=self._client, read_once=self.read_once, existence_duration=self.existence_duration, visibility_duration=self.visibility_duration)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.message_pb2.MessageEphemerality, client: OlvidClient = None) -> "MessageEphemerality":
		return MessageEphemerality(client, read_once=native_message.read_once, existence_duration=native_message.existence_duration, visibility_duration=native_message.visibility_duration)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.message_pb2.MessageEphemerality], client: OlvidClient = None) -> list["MessageEphemerality"]:
		return [MessageEphemerality._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.message_pb2.MessageEphemerality], client: OlvidClient = None) -> "MessageEphemerality":
		native_message = await promise
		return MessageEphemerality._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageEphemerality"]):
		if messages is None:
			return []
		return [MessageEphemerality._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageEphemerality"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.message_pb2.MessageEphemerality(read_once=message.read_once if message.read_once else None, existence_duration=message.existence_duration if message.existence_duration else None, visibility_duration=message.visibility_duration if message.visibility_duration else None)

	def __str__(self):
		s: str = ''
		if self.read_once:
			s += f'read_once: {self.read_once}, '
		if self.existence_duration:
			s += f'existence_duration: {self.existence_duration}, '
		if self.visibility_duration:
			s += f'visibility_duration: {self.visibility_duration}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageEphemerality):
			return False
		return self.read_once == other.read_once and self.existence_duration == other.existence_duration and self.visibility_duration == other.visibility_duration

	def __bool__(self):
		return self.read_once or self.existence_duration != 0 or self.visibility_duration != 0

	def __hash__(self):
		return hash((self.read_once, self.existence_duration, self.visibility_duration))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageEphemerality):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.read_once is False or self.read_once == expected.read_once, "Invalid value: read_once: " + str(expected.read_once) + " != " + str(self.read_once)
		assert expected.existence_duration == 0 or self.existence_duration == expected.existence_duration, "Invalid value: existence_duration: " + str(expected.existence_duration) + " != " + str(self.existence_duration)
		assert expected.visibility_duration == 0 or self.visibility_duration == expected.visibility_duration, "Invalid value: visibility_duration: " + str(expected.visibility_duration) + " != " + str(self.visibility_duration)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageReaction:
	def __init__(self, client: OlvidClient = None, contact_id: int = 0, reaction: str = "", timestamp: int = 0):
		self._client: OlvidClient = client
		self.contact_id: int = contact_id
		self.reaction: str = reaction
		self.timestamp: int = timestamp

	def _update_content(self, message_reaction: MessageReaction) -> None:
		self.contact_id: int = message_reaction.contact_id
		self.reaction: str = message_reaction.reaction
		self.timestamp: int = message_reaction.timestamp

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageReaction":
		return MessageReaction(client=self._client, contact_id=self.contact_id, reaction=self.reaction, timestamp=self.timestamp)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.message_pb2.MessageReaction, client: OlvidClient = None) -> "MessageReaction":
		return MessageReaction(client, contact_id=native_message.contact_id, reaction=native_message.reaction, timestamp=native_message.timestamp)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.message_pb2.MessageReaction], client: OlvidClient = None) -> list["MessageReaction"]:
		return [MessageReaction._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.message_pb2.MessageReaction], client: OlvidClient = None) -> "MessageReaction":
		native_message = await promise
		return MessageReaction._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageReaction"]):
		if messages is None:
			return []
		return [MessageReaction._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageReaction"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.message_pb2.MessageReaction(contact_id=message.contact_id if message.contact_id else None, reaction=message.reaction if message.reaction else None, timestamp=message.timestamp if message.timestamp else None)

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		if self.reaction:
			s += f'reaction: {self.reaction}, '
		if self.timestamp:
			s += f'timestamp: {self.timestamp}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageReaction):
			return False
		return self.contact_id == other.contact_id and self.reaction == other.reaction and self.timestamp == other.timestamp

	def __bool__(self):
		return self.contact_id != 0 or self.reaction != "" or self.timestamp != 0

	def __hash__(self):
		return hash((self.contact_id, self.reaction, self.timestamp))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageReaction):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		assert expected.reaction == "" or self.reaction == expected.reaction, "Invalid value: reaction: " + str(expected.reaction) + " != " + str(self.reaction)
		assert expected.timestamp == 0 or self.timestamp == expected.timestamp, "Invalid value: timestamp: " + str(expected.timestamp) + " != " + str(self.timestamp)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageLocation:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class LocationType(Enum):
		LOCATION_TYPE_UNSPECIFIED = 0
		LOCATION_TYPE_SEND = 1
		LOCATION_TYPE_SHARING = 2
		LOCATION_TYPE_SHARING_FINISHED = 3
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["MessageLocation.LocationType"]:
			return [MessageLocation.LocationType(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, type: "MessageLocation.LocationType" = 0, timestamp: int = 0, latitude: float = 0.0, longitude: float = 0.0, altitude: float = 0.0, precision: float = 0.0, address: str = ""):
		self._client: OlvidClient = client
		self.type: MessageLocation.LocationType = type
		self.timestamp: int = timestamp
		self.latitude: float = latitude
		self.longitude: float = longitude
		self.altitude: float = altitude
		self.precision: float = precision
		self.address: str = address

	def _update_content(self, message_location: MessageLocation) -> None:
		self.type: MessageLocation.LocationType = message_location.type
		self.timestamp: int = message_location.timestamp
		self.latitude: float = message_location.latitude
		self.longitude: float = message_location.longitude
		self.altitude: float = message_location.altitude
		self.precision: float = message_location.precision
		self.address: str = message_location.address

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageLocation":
		return MessageLocation(client=self._client, type=self.type, timestamp=self.timestamp, latitude=self.latitude, longitude=self.longitude, altitude=self.altitude, precision=self.precision, address=self.address)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.message_pb2.MessageLocation, client: OlvidClient = None) -> "MessageLocation":
		return MessageLocation(client, type=MessageLocation.LocationType(native_message.type), timestamp=native_message.timestamp, latitude=native_message.latitude, longitude=native_message.longitude, altitude=native_message.altitude, precision=native_message.precision, address=native_message.address)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.message_pb2.MessageLocation], client: OlvidClient = None) -> list["MessageLocation"]:
		return [MessageLocation._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.message_pb2.MessageLocation], client: OlvidClient = None) -> "MessageLocation":
		native_message = await promise
		return MessageLocation._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageLocation"]):
		if messages is None:
			return []
		return [MessageLocation._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageLocation"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.message_pb2.MessageLocation(type=message.type.value if message.type else None, timestamp=message.timestamp if message.timestamp else None, latitude=message.latitude if message.latitude else None, longitude=message.longitude if message.longitude else None, altitude=message.altitude if message.altitude else None, precision=message.precision if message.precision else None, address=message.address if message.address else None)

	def __str__(self):
		s: str = ''
		if self.type:
			s += f'type: {self.type}, '
		if self.timestamp:
			s += f'timestamp: {self.timestamp}, '
		if self.latitude:
			s += f'latitude: {self.latitude}, '
		if self.longitude:
			s += f'longitude: {self.longitude}, '
		if self.altitude:
			s += f'altitude: {self.altitude}, '
		if self.precision:
			s += f'precision: {self.precision}, '
		if self.address:
			s += f'address: {self.address}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageLocation):
			return False
		return self.type == other.type and self.timestamp == other.timestamp and self.latitude == other.latitude and self.longitude == other.longitude and self.altitude == other.altitude and self.precision == other.precision and self.address == other.address

	def __bool__(self):
		return bool(self.type) or self.timestamp != 0 or self.latitude != 0.0 or self.longitude != 0.0 or self.altitude != 0.0 or self.precision != 0.0 or self.address != ""

	def __hash__(self):
		return hash((self.type, self.timestamp, self.latitude, self.longitude, self.altitude, self.precision, self.address))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageLocation):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.type == 0 or self.type == expected.type, "Invalid value: type: " + str(expected.type) + " != " + str(self.type)
		assert expected.timestamp == 0 or self.timestamp == expected.timestamp, "Invalid value: timestamp: " + str(expected.timestamp) + " != " + str(self.timestamp)
		assert expected.latitude == 0.0 or self.latitude == expected.latitude, "Invalid value: latitude: " + str(expected.latitude) + " != " + str(self.latitude)
		assert expected.longitude == 0.0 or self.longitude == expected.longitude, "Invalid value: longitude: " + str(expected.longitude) + " != " + str(self.longitude)
		assert expected.altitude == 0.0 or self.altitude == expected.altitude, "Invalid value: altitude: " + str(expected.altitude) + " != " + str(self.altitude)
		assert expected.precision == 0.0 or self.precision == expected.precision, "Invalid value: precision: " + str(expected.precision) + " != " + str(self.precision)
		assert expected.address == "" or self.address == expected.address, "Invalid value: address: " + str(expected.address) + " != " + str(self.address)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageFilter:
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Attachment(Enum):
		ATTACHMENT_UNSPECIFIED = 0
		ATTACHMENT_HAVE = 1
		ATTACHMENT_HAVE_NOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["MessageFilter.Attachment"]:
			return [MessageFilter.Attachment(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Location(Enum):
		LOCATION_UNSPECIFIED = 0
		LOCATION_HAVE = 1
		LOCATION_HAVE_NOT = 2
		LOCATION_IS_SEND = 3
		LOCATION_IS_SHARING = 5
		LOCATION_IS_SHARING_FINISHED = 6
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["MessageFilter.Location"]:
			return [MessageFilter.Location(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0
	
	# noinspection PyProtectedMember,PyShadowingBuiltins
	class Reaction(Enum):
		REACTION_UNSPECIFIED = 0
		REACTION_HAS = 1
		REACTION_HAS_NOT = 2
	
		def __str__(self):
			return self.name
	
		@staticmethod
		def _from_native_list(native_enum_list) -> list["MessageFilter.Reaction"]:
			return [MessageFilter.Reaction(native_enum) for native_enum in native_enum_list]
	
		def __bool__(self):
			return self.value != 0

	def __init__(self, client: OlvidClient = None, type: "MessageId.Type" = 0, discussion_id: int = 0, sender_contact_id: int = 0, body_search: str = "", attachment: "MessageFilter.Attachment" = 0, location: "MessageFilter.Location" = 0, min_timestamp: int = 0, max_timestamp: int = 0, reaction: "MessageFilter.Reaction" = 0, reactions_filter: "list[ReactionFilter]" = None, reply_to_a_message: bool = None, do_not_reply_to_a_message: bool = None, replied_message_id: "MessageId" = None):
		self._client: OlvidClient = client
		self.type: MessageId.Type = type
		self.discussion_id: int = discussion_id
		self.sender_contact_id: int = sender_contact_id
		self.body_search: str = body_search
		self.attachment: MessageFilter.Attachment = attachment
		self.location: MessageFilter.Location = location
		self.min_timestamp: int = min_timestamp
		self.max_timestamp: int = max_timestamp
		self.reaction: MessageFilter.Reaction = reaction
		self.reactions_filter: list[ReactionFilter] = reactions_filter
		self.reply_to_a_message: bool = reply_to_a_message
		self.do_not_reply_to_a_message: bool = do_not_reply_to_a_message
		self.replied_message_id: MessageId = replied_message_id

	def _update_content(self, message_filter: MessageFilter) -> None:
		self.type: MessageId.Type = message_filter.type
		self.discussion_id: int = message_filter.discussion_id
		self.sender_contact_id: int = message_filter.sender_contact_id
		self.body_search: str = message_filter.body_search
		self.attachment: MessageFilter.Attachment = message_filter.attachment
		self.location: MessageFilter.Location = message_filter.location
		self.min_timestamp: int = message_filter.min_timestamp
		self.max_timestamp: int = message_filter.max_timestamp
		self.reaction: MessageFilter.Reaction = message_filter.reaction
		self.reactions_filter: list[ReactionFilter] = message_filter.reactions_filter
		self.reply_to_a_message: bool = message_filter.reply_to_a_message
		self.do_not_reply_to_a_message: bool = message_filter.do_not_reply_to_a_message
		self.replied_message_id: MessageId = message_filter.replied_message_id

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageFilter":
		return MessageFilter(client=self._client, type=self.type, discussion_id=self.discussion_id, sender_contact_id=self.sender_contact_id, body_search=self.body_search, attachment=self.attachment, location=self.location, min_timestamp=self.min_timestamp, max_timestamp=self.max_timestamp, reaction=self.reaction, reactions_filter=[e._clone() for e in self.reactions_filter], reply_to_a_message=self.reply_to_a_message, do_not_reply_to_a_message=self.do_not_reply_to_a_message, replied_message_id=self.replied_message_id._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.message_pb2.MessageFilter, client: OlvidClient = None) -> "MessageFilter":
		return MessageFilter(client, type=MessageId.Type(native_message.type), discussion_id=native_message.discussion_id, sender_contact_id=native_message.sender_contact_id, body_search=native_message.body_search, attachment=MessageFilter.Attachment(native_message.attachment), location=MessageFilter.Location(native_message.location), min_timestamp=native_message.min_timestamp, max_timestamp=native_message.max_timestamp, reaction=MessageFilter.Reaction(native_message.reaction), reactions_filter=ReactionFilter._from_native_list(native_message.reactions_filter, client=client), reply_to_a_message=native_message.reply_to_a_message, do_not_reply_to_a_message=native_message.do_not_reply_to_a_message, replied_message_id=MessageId._from_native(native_message.replied_message_id, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.message_pb2.MessageFilter], client: OlvidClient = None) -> list["MessageFilter"]:
		return [MessageFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.message_pb2.MessageFilter], client: OlvidClient = None) -> "MessageFilter":
		native_message = await promise
		return MessageFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageFilter"]):
		if messages is None:
			return []
		return [MessageFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.message_pb2.MessageFilter(type=message.type.value if message.type else None, discussion_id=message.discussion_id if message.discussion_id else None, sender_contact_id=message.sender_contact_id if message.sender_contact_id else None, body_search=message.body_search if message.body_search else None, attachment=message.attachment.value if message.attachment else None, location=message.location.value if message.location else None, min_timestamp=message.min_timestamp if message.min_timestamp else None, max_timestamp=message.max_timestamp if message.max_timestamp else None, reaction=message.reaction.value if message.reaction else None, reactions_filter=ReactionFilter._to_native_list(message.reactions_filter if message.reactions_filter else None), reply_to_a_message=message.reply_to_a_message if message.reply_to_a_message else None, do_not_reply_to_a_message=message.do_not_reply_to_a_message if message.do_not_reply_to_a_message else None, replied_message_id=MessageId._to_native(message.replied_message_id if message.replied_message_id else None))

	def __str__(self):
		s: str = ''
		if self.type:
			s += f'type: {self.type}, '
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.sender_contact_id:
			s += f'sender_contact_id: {self.sender_contact_id}, '
		if self.body_search:
			s += f'body_search: {self.body_search}, '
		if self.attachment:
			s += f'attachment: {self.attachment}, '
		if self.location:
			s += f'location: {self.location}, '
		if self.min_timestamp:
			s += f'min_timestamp: {self.min_timestamp}, '
		if self.max_timestamp:
			s += f'max_timestamp: {self.max_timestamp}, '
		if self.reaction:
			s += f'reaction: {self.reaction}, '
		if self.reactions_filter:
			s += f'reactions_filter: {[str(el) for el in self.reactions_filter]}, '
		if self.reply_to_a_message:
			s += f'reply_to_a_message: {self.reply_to_a_message}, '
		if self.do_not_reply_to_a_message:
			s += f'do_not_reply_to_a_message: {self.do_not_reply_to_a_message}, '
		if self.replied_message_id:
			s += f'replied_message_id: ({self.replied_message_id}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageFilter):
			return False
		return self.type == other.type and self.discussion_id == other.discussion_id and self.sender_contact_id == other.sender_contact_id and self.body_search == other.body_search and self.attachment == other.attachment and self.location == other.location and self.min_timestamp == other.min_timestamp and self.max_timestamp == other.max_timestamp and self.reaction == other.reaction and self.reactions_filter == other.reactions_filter and self.reply_to_a_message == other.reply_to_a_message and self.do_not_reply_to_a_message == other.do_not_reply_to_a_message and self.replied_message_id == other.replied_message_id

	def __bool__(self):
		return bool(self.type) or self.discussion_id != 0 or self.sender_contact_id != 0 or self.body_search != "" or bool(self.attachment) or bool(self.location) or self.min_timestamp != 0 or self.max_timestamp != 0 or bool(self.reaction) or bool(self.reactions_filter) or self.reply_to_a_message is not None or self.do_not_reply_to_a_message is not None or bool(self.replied_message_id)

	def __hash__(self):
		return hash((self.type, self.discussion_id, self.sender_contact_id, self.body_search, self.attachment, self.location, self.min_timestamp, self.max_timestamp, self.reaction, tuple(self.reactions_filter), self.reply_to_a_message, self.do_not_reply_to_a_message, self.replied_message_id))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.type == 0 or self.type == expected.type, "Invalid value: type: " + str(expected.type) + " != " + str(self.type)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.sender_contact_id == 0 or self.sender_contact_id == expected.sender_contact_id, "Invalid value: sender_contact_id: " + str(expected.sender_contact_id) + " != " + str(self.sender_contact_id)
		assert expected.body_search == "" or self.body_search == expected.body_search, "Invalid value: body_search: " + str(expected.body_search) + " != " + str(self.body_search)
		assert expected.attachment == 0 or self.attachment == expected.attachment, "Invalid value: attachment: " + str(expected.attachment) + " != " + str(self.attachment)
		assert expected.location == 0 or self.location == expected.location, "Invalid value: location: " + str(expected.location) + " != " + str(self.location)
		assert expected.min_timestamp == 0 or self.min_timestamp == expected.min_timestamp, "Invalid value: min_timestamp: " + str(expected.min_timestamp) + " != " + str(self.min_timestamp)
		assert expected.max_timestamp == 0 or self.max_timestamp == expected.max_timestamp, "Invalid value: max_timestamp: " + str(expected.max_timestamp) + " != " + str(self.max_timestamp)
		assert expected.reaction == 0 or self.reaction == expected.reaction, "Invalid value: reaction: " + str(expected.reaction) + " != " + str(self.reaction)
		pass  # print("Warning: test_assertion: skipped a list field reactions_filter")
		assert expected.reply_to_a_message is None or self.reply_to_a_message == expected.reply_to_a_message, "Invalid value: reply_to_a_message: " + str(expected.reply_to_a_message) + " != " + str(self.reply_to_a_message)
		assert expected.do_not_reply_to_a_message is None or self.do_not_reply_to_a_message == expected.do_not_reply_to_a_message, "Invalid value: do_not_reply_to_a_message: " + str(expected.do_not_reply_to_a_message) + " != " + str(self.do_not_reply_to_a_message)
		try:
			assert expected.replied_message_id is None or self.replied_message_id._test_assertion(expected.replied_message_id)
		except AssertionError as e:
			raise AssertionError("replied_message_id: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ReactionFilter:
	def __init__(self, client: OlvidClient = None, reacted_by_me: bool = None, reacted_by_contact_id: int = None, reaction: str = ""):
		self._client: OlvidClient = client
		self.reacted_by_me: bool = reacted_by_me
		self.reacted_by_contact_id: int = reacted_by_contact_id
		self.reaction: str = reaction

	def _update_content(self, reaction_filter: ReactionFilter) -> None:
		self.reacted_by_me: bool = reaction_filter.reacted_by_me
		self.reacted_by_contact_id: int = reaction_filter.reacted_by_contact_id
		self.reaction: str = reaction_filter.reaction

	# noinspection PyProtectedMember
	def _clone(self) -> "ReactionFilter":
		return ReactionFilter(client=self._client, reacted_by_me=self.reacted_by_me, reacted_by_contact_id=self.reacted_by_contact_id, reaction=self.reaction)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.message_pb2.ReactionFilter, client: OlvidClient = None) -> "ReactionFilter":
		return ReactionFilter(client, reacted_by_me=native_message.reacted_by_me, reacted_by_contact_id=native_message.reacted_by_contact_id, reaction=native_message.reaction)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.message_pb2.ReactionFilter], client: OlvidClient = None) -> list["ReactionFilter"]:
		return [ReactionFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.message_pb2.ReactionFilter], client: OlvidClient = None) -> "ReactionFilter":
		native_message = await promise
		return ReactionFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ReactionFilter"]):
		if messages is None:
			return []
		return [ReactionFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ReactionFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.message_pb2.ReactionFilter(reacted_by_me=message.reacted_by_me if message.reacted_by_me else None, reacted_by_contact_id=message.reacted_by_contact_id if message.reacted_by_contact_id else None, reaction=message.reaction if message.reaction else None)

	def __str__(self):
		s: str = ''
		if self.reacted_by_me:
			s += f'reacted_by_me: {self.reacted_by_me}, '
		if self.reacted_by_contact_id:
			s += f'reacted_by_contact_id: {self.reacted_by_contact_id}, '
		if self.reaction:
			s += f'reaction: {self.reaction}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ReactionFilter):
			return False
		return self.reacted_by_me == other.reacted_by_me and self.reacted_by_contact_id == other.reacted_by_contact_id and self.reaction == other.reaction

	def __bool__(self):
		return self.reacted_by_me is not None or self.reacted_by_contact_id is not None or self.reaction != ""

	def __hash__(self):
		return hash((self.reacted_by_me, self.reacted_by_contact_id, self.reaction))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ReactionFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.reacted_by_me is None or self.reacted_by_me == expected.reacted_by_me, "Invalid value: reacted_by_me: " + str(expected.reacted_by_me) + " != " + str(self.reacted_by_me)
		assert expected.reacted_by_contact_id is None or self.reacted_by_contact_id == expected.reacted_by_contact_id, "Invalid value: reacted_by_contact_id: " + str(expected.reacted_by_contact_id) + " != " + str(self.reacted_by_contact_id)
		assert expected.reaction == "" or self.reaction == expected.reaction, "Invalid value: reaction: " + str(expected.reaction) + " != " + str(self.reaction)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageElement:
	def __init__(self, client: OlvidClient = None, key: str = "", value: str = ""):
		self._client: OlvidClient = client
		self.key: str = key
		self.value: str = value

	def _update_content(self, storage_element: StorageElement) -> None:
		self.key: str = storage_element.key
		self.value: str = storage_element.value

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageElement":
		return StorageElement(client=self._client, key=self.key, value=self.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.storage_pb2.StorageElement, client: OlvidClient = None) -> "StorageElement":
		return StorageElement(client, key=native_message.key, value=native_message.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.storage_pb2.StorageElement], client: OlvidClient = None) -> list["StorageElement"]:
		return [StorageElement._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.storage_pb2.StorageElement], client: OlvidClient = None) -> "StorageElement":
		native_message = await promise
		return StorageElement._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["StorageElement"]):
		if messages is None:
			return []
		return [StorageElement._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["StorageElement"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.storage_pb2.StorageElement(key=message.key if message.key else None, value=message.value if message.value else None)

	def __str__(self):
		s: str = ''
		if self.key:
			s += f'key: {self.key}, '
		if self.value:
			s += f'value: {self.value}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, StorageElement):
			return False
		return self.key == other.key and self.value == other.value

	def __bool__(self):
		return self.key != "" or self.value != ""

	def __hash__(self):
		return hash((self.key, self.value))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, StorageElement):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.key == "" or self.key == expected.key, "Invalid value: key: " + str(expected.key) + " != " + str(self.key)
		assert expected.value == "" or self.value == expected.value, "Invalid value: value: " + str(expected.value) + " != " + str(self.value)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageElementFilter:
	def __init__(self, client: OlvidClient = None, key_search: str = "", value_search: str = ""):
		self._client: OlvidClient = client
		self.key_search: str = key_search
		self.value_search: str = value_search

	def _update_content(self, storage_element_filter: StorageElementFilter) -> None:
		self.key_search: str = storage_element_filter.key_search
		self.value_search: str = storage_element_filter.value_search

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageElementFilter":
		return StorageElementFilter(client=self._client, key_search=self.key_search, value_search=self.value_search)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.datatypes.v1.storage_pb2.StorageElementFilter, client: OlvidClient = None) -> "StorageElementFilter":
		return StorageElementFilter(client, key_search=native_message.key_search, value_search=native_message.value_search)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.datatypes.v1.storage_pb2.StorageElementFilter], client: OlvidClient = None) -> list["StorageElementFilter"]:
		return [StorageElementFilter._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.datatypes.v1.storage_pb2.StorageElementFilter], client: OlvidClient = None) -> "StorageElementFilter":
		native_message = await promise
		return StorageElementFilter._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["StorageElementFilter"]):
		if messages is None:
			return []
		return [StorageElementFilter._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["StorageElementFilter"]):
		if message is None:
			return None
		return olvid.daemon.datatypes.v1.storage_pb2.StorageElementFilter(key_search=message.key_search if message.key_search else None, value_search=message.value_search if message.value_search else None)

	def __str__(self):
		s: str = ''
		if self.key_search:
			s += f'key_search: {self.key_search}, '
		if self.value_search:
			s += f'value_search: {self.value_search}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, StorageElementFilter):
			return False
		return self.key_search == other.key_search and self.value_search == other.value_search

	def __bool__(self):
		return self.key_search != "" or self.value_search != ""

	def __hash__(self):
		return hash((self.key_search, self.value_search))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, StorageElementFilter):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.key_search == "" or self.key_search == expected.key_search, "Invalid value: key_search: " + str(expected.key_search) + " != " + str(self.key_search)
		assert expected.value_search == "" or self.value_search == expected.value_search, "Invalid value: value_search: " + str(expected.value_search) + " != " + str(self.value_search)
		return True


#####
# enhanced classes from ./enhancer/datatypes/enhancer.py
#####
DatatypesEntity = Union[Message, Discussion, Contact, Attachment, Group]
DatatypesEntityId = Union[MessageId, AttachmentId, int]


# listener_class: use listeners implementations (MessageReceivedListener, InvitationSentReceivedListener, ...)
def _on_entity_something(parent_client: "OlvidClient", listener_class: type["listeners.GenericNotificationListener"], handler: Callable[..., Optional[Coroutine[..., None, None]]], checkers: list[Callable[[...], bool]]):
	import asyncio
	from olvid import OlvidClient
	client = OlvidClient(parent_client=parent_client)

	async def wrapped_handler(*args):
		ret = handler(*args)
		if asyncio.iscoroutine(ret):
			await ret
		await client.stop()

	# noinspection PyArgumentList
	client.add_listener(listener_class(handler=wrapped_handler, count=1, checkers=checkers))


# listener_class: use listeners implementations (MessageReceivedListener, InvitationSentReceivedListener, ...)
async def _wait_for_entity_something(parent_client: "OlvidClient", listener_class: type["listeners.GenericNotificationListener"], checkers: list[[Callable[[...], bool]]]) -> tuple:
	from olvid import OlvidClient
	client = OlvidClient(parent_client=parent_client)
	entity_store: list = []
	# noinspection PyArgumentList
	client.add_listener(listener_class(lambda *args: [entity_store.append(a) for a in args], count=1, checkers=checkers))
	await client.wait_for_listeners_end()
	return tuple(entity_store)


def get_generic_entity_checker(expected_id: DatatypesEntityId):
	# noinspection PyUnusedLocal
	def generic_entity_checker(entity: DatatypesEntity, *args):
		return entity.id == expected_id
	return generic_entity_checker


# noinspection PyRedeclaration
class Identity(Identity):
	async def update(self, first_name: str = None, last_name: str = None, position: str = None, company: str = None):
		await self._client.identity_update_details(IdentityDetails(first_name=first_name, last_name=last_name, company=company, position=position))

	async def set_photo(self, filepath: str):
		await self._client.identity_set_photo(filepath)

	async def remove_photo(self, filepath: str):
		await self._client.identity_remove_photo()

	async def set_api_key(self, api_key: str) -> Identity.ApiKey:
		return await self._client.identity_set_api_key(api_key=api_key)

	async def set_configuration_link(self, configuration_link: str) -> Identity.ApiKey:
		return await self._client.identity_set_configuration_link(configuration_link=configuration_link)


# noinspection PyRedeclaration
class Invitation(Invitation):
	async def wait_for(self, listener_class: type["listeners.GenericNotificationListener"], extra_checker=None) -> Invitation:
		checkers: list = [get_generic_entity_checker(self.id)]
		if extra_checker is not None:
			checkers.append(extra_checker)
		ret = await _wait_for_entity_something(parent_client=self._client, listener_class=listener_class, checkers=checkers)
		return ret[0]

	def on(self, listener_class: type["listeners.GenericNotificationListener"], handler: Callable, extra_checker=None):
		checkers: list = [get_generic_entity_checker(self.id)]
		if extra_checker is not None:
			checkers.append(extra_checker)
		_on_entity_something(parent_client=self._client, listener_class=listener_class, handler=handler, checkers=checkers)


# noinspection PyRedeclaration
class Discussion(Discussion):
	def is_contact_discussion(self) -> bool:
		return self.contact_id != 0

	def is_group_discussion(self) -> bool:
		return self.group_id != 0

	async def can_post_message(self):
		# contact discussion: check
		if self.is_contact_discussion():
			contact: Contact = await self.get_contact()
			return contact.can_send_message()
		# group discussion: check permissions
		elif self.is_group_discussion():
			group: Group = await self.get_group()
			return group.can_send_message()
		# locked discussion
		else:
			return False

	async def post_message(self, body: str, reply_id: MessageId = None, ephemerality: MessageEphemerality = None, attachments_filename_with_payload: list[tuple[str, bytes]] = None) -> Message:
		if attachments_filename_with_payload is None:
			return await self._client.message_send(discussion_id=self.id, body=body, reply_id=reply_id, ephemerality=ephemerality)
		else:
			return (await self._client.message_send_with_attachments(discussion_id=self.id, body=body, reply_id=reply_id, ephemerality=ephemerality, attachments_filename_with_payload=attachments_filename_with_payload))[0]

	async def empty_discussion(self, delete_everywhere: bool = False) -> None:
		await self._client.discussion_empty(discussion_id=self.id, delete_everywhere=delete_everywhere)

	async def get_contact(self) -> Contact:
		assert self.is_contact_discussion(), "Cannot get contact, not a contact discussion"
		return await self._client.contact_get(contact_id=self.contact_id)

	async def get_group(self) -> Group:
		assert self.is_group_discussion(), "Cannot get group, not a group discussion"
		return await self._client.group_get(group_id=self.group_id)

	async def wait_for_next_message(self) -> Message:
		from olvid.listeners import MessageReceivedListener
		message, = await _wait_for_entity_something(parent_client=self._client, listener_class=MessageReceivedListener, checkers=[get_generic_entity_checker(self.id)])
		return message

	async def get_settings(self) -> DiscussionSettings:
		return await self._client.discussion_settings_get(discussion_id=self.id)

	async def set_settings(self, settings: DiscussionSettings) -> DiscussionSettings:
		return await self._client.discussion_settings_set(settings=settings)


# noinspection PyRedeclaration
class Contact(Contact):
	def can_send_message(self) -> bool:
		return self.has_one_to_one_discussion

	async def send_message(self, body: str, reply_id: MessageId = None, ephemerality: MessageEphemerality = None, attachments_filename_with_payload: list[tuple[str, bytes]] = None) -> Message:
		if not self.can_send_message():
			raise ValueError("Cannot send a message to a non one to one contact")
		discussion_id: int = (await self._client.discussion_get_by_contact(contact_id=self.id)).id
		if attachments_filename_with_payload is None:
			return await self._client.message_send(discussion_id=discussion_id, body=body, reply_id=reply_id, ephemerality=ephemerality)
		else:
			return (await self._client.message_send_with_attachments(discussion_id=discussion_id, body=body, reply_id=reply_id, ephemerality=ephemerality, attachments_filename_with_payload=attachments_filename_with_payload))[0]

	async def get_discussion(self) -> Discussion:
		return await self._client.discussion_get_by_contact(contact_id=self.id)

	async def get_groups(self) -> list[Group]:
		return ([g async for g in self._client.group_list(filter=GroupFilter(member_filters=[GroupMemberFilter(contact_id=self.id)]))]
			+ [g async for g in self._client.group_list(filter=GroupFilter(pending_member_filters=[PendingGroupMemberFilter(contact_id=self.id)]))])

	async def introduce(self, contact_id: int) -> None:
		await self._client.contact_introduction(first_contact_id=self.id, second_contact_id=contact_id)

	async def invite_one_to_one(self) -> None:
		assert not self.has_one_to_one_discussion, "Contact is already one to one"
		await self._client.contact_downgrade_one_to_one_discussion(contact_id=self.id)

	async def downgrade_one_to_one(self) -> None:
		assert self.has_one_to_one_discussion, "Contact is not one to one"
		await self._client.contact_downgrade_one_to_one_discussion(contact_id=self.id)

	async def delete(self) -> None:
		await self._client.contact_delete(contact_id=self.id)


# noinspection PyRedeclaration
class Group(Group):
	def can_send_message(self) -> bool:
		return self.own_permissions.send_message

	def has_admin_permissions(self) -> bool:
		return self.own_permissions.admin

	async def send_message(self, body: str, reply_id: MessageId = None, ephemerality: MessageEphemerality = None, attachments_filename_with_payload: list[tuple[str, bytes]] = None) -> Message:
		if not self.can_send_message():
			raise ValueError("Cannot send a message in this group")
		discussion_id: int = (await self._client.discussion_get_by_group(group_id=self.id)).id
		if attachments_filename_with_payload is None:
			return await self._client.message_send(discussion_id=discussion_id, body=body, reply_id=reply_id, ephemerality=ephemerality)
		else:
			return (await self._client.message_send_with_attachments(discussion_id=discussion_id, body=body, reply_id=reply_id, ephemerality=ephemerality, attachments_filename_with_payload=attachments_filename_with_payload))[0]

	async def leave(self) -> Group:
		return await self._client.group_leave(group_id=self.id)

	async def disband(self) -> Group:
		return await self._client.group_disband(group_id=self.id)

	async def add_members(self, contact_ids: list[int], permissions: GroupMemberPermissions) -> Group:
		assert self.has_admin_permissions(), "Cannot add member if you are not admin"
		for cid in contact_ids:
			self.members.append(GroupMember(client=self._client, contact_id=cid, permissions=permissions))
		self._update_content(await self._client.group_update(self))
		return self

	async def set_photo(self, file_path: str):
		await self._client.group_set_photo(group_id=self.id, file_path=file_path)

	async def unset_photo(self):
		await self._client.group_unset_photo(group_id=self.id)


# noinspection PyRedeclaration
class Attachment(Attachment):
	def is_inbound(self) -> bool:
		return self.id.type == AttachmentId.Type.TYPE_INBOUND

	def is_outbound(self) -> bool:
		return self.id.type == AttachmentId.Type.TYPE_OUTBOUND

	async def save(self, save_dir: str, filename: str = None):
		if not os.path.isdir(save_dir):
			os.mkdir(save_dir)
		if filename is None:
			filename = self.file_name
		# create file
		with open(os.path.join(save_dir, filename), "wb") as fd:
			async for chunk in self._client.attachment_download(attachment_id=self.id):
				fd.write(chunk)

	async def delete(self, delete_everywhere: bool = False):
		await self._client.attachment_delete(attachment_id=self.id, delete_everywhere=delete_everywhere)

	async def wait_for_upload(self):
		if not self.is_outbound():
			raise ValueError("Cannot wait for an inbound attachment to be uploaded")
		from olvid.listeners import AttachmentUploadedListener
		await _wait_for_entity_something(parent_client=self._client, listener_class=AttachmentUploadedListener, checkers=[get_generic_entity_checker(self.id)])

	async def on_upload(self, handler: Callable[[Attachment], Optional[Coroutine]]):
		if not self.is_outbound():
			raise ValueError("Cannot wait for an inbound attachment to be uploaded")
		from olvid.listeners import AttachmentUploadedListener
		_on_entity_something(parent_client=self._client, listener_class=AttachmentUploadedListener, handler=handler, checkers=[get_generic_entity_checker(self.id)])


# noinspection PyRedeclaration
class Message(Message):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.on: Message.OnMessageEventListener = self.OnMessageEventListener(self, self._client)
		self.wait_for: Message.WaitForMessageEventListener = self.WaitForMessageEventListener(self, self._client)

	####
	# Access attributes api
	####
	def is_inbound(self) -> bool:
		return self.sender_id != 0

	def is_outbound(self) -> bool:
		return self.sender_id == 0

	async def is_one_to_one_message(self) -> bool:
		return (await self._client.discussion_get(self.discussion_id)).contact_id != 0

	async def is_group_message(self) -> bool:
		return (await self._client.discussion_get(self.discussion_id)).group_id != 0

	async def get_discussion(self) -> Discussion:
		return await self._client.discussion_get(self.discussion_id)

	async def get_sender_contact(self) -> Contact:
		assert self.is_inbound(), "Cannot get_sender_contact of outbound message"
		return await self._client.contact_get(self.sender_id)

	####
	# Interaction api
	####
	async def reply(self, body: str, quote_message: bool = False, ephemerality: MessageEphemerality = None, attachments_filename_with_payload: list[tuple[str, bytes]] = None) -> Message:
		if attachments_filename_with_payload is None:
			return await self._client.message_send(
				discussion_id=self.discussion_id,
				body=body,
				reply_id=self.id if quote_message else None,
				ephemerality=ephemerality if ephemerality else None
			)
		else:
			return (await self._client.message_send_with_attachments(
				discussion_id=self.discussion_id,
				body=body,
				reply_id=self.id if quote_message else None,
				ephemerality=ephemerality if ephemerality else None,
				attachments_filename_with_payload=attachments_filename_with_payload
			))[0]
	async def delete(self, delete_everywhere: bool = False) -> None:
		await self._client.message_delete(message_id=self.id, delete_everywhere=delete_everywhere)

	async def edit_body(self, new_body: str) -> None:
		await self._client.message_update_body(self.id, new_body)

	async def react(self, reaction: str) -> None:
		await self._client.message_react(self.id, reaction)

	async def remove_reaction(self) -> None:
		await self._client.message_react(self.id, "")

	class WaitForMessageEventListener:
		def __init__(self, message: Message, client: OlvidClient):
			self._message = message
			self._client = client

		async def message_to_be_uploaded(self):
			if not self._message.is_outbound():
				raise ValueError("Cannot wait for an inbound message to be uploaded")
			# TODO check for current status and return now if necessary when a message.status will be implemented
			from olvid.listeners import MessageUploadedListener
			await _wait_for_entity_something(parent_client=self._client, listener_class=MessageUploadedListener, checkers=[get_generic_entity_checker(self._message.id)])

		async def message_to_be_delivered(self):
			if not self._message.is_outbound():
				raise ValueError("Cannot wait for an inbound message to be uploaded")
			# TODO check for current status and return now if necessary when a message.status will be implemented
			from olvid.listeners import MessageDeliveredListener
			await _wait_for_entity_something(parent_client=self._client, listener_class=MessageDeliveredListener, checkers=[get_generic_entity_checker(self._message.id)])

		async def message_to_be_read(self):
			if not self._message.is_outbound():
				raise ValueError("Cannot wait for an inbound message to be read")
			# TODO check for current status and return now if necessary when a message.status will be implemented
			from olvid.listeners import MessageReadListener
			await _wait_for_entity_something(parent_client=self._client, listener_class=MessageReadListener, checkers=[get_generic_entity_checker(self._message.id)])

		async def message_to_be_edited(self) -> [Message, str]:
			from olvid.listeners import MessageBodyUpdatedListener
			message, body = await _wait_for_entity_something(parent_client=self._client, listener_class=MessageBodyUpdatedListener, checkers=[get_generic_entity_checker(self._message.id)])
			return message, body

	class OnMessageEventListener:
		def __init__(self, message: Message, client: OlvidClient):
			self._message = message
			self._client = client

		def message_uploaded(self, handler: Callable[[Message], Optional[Coroutine]]):
			if not self._message.is_outbound():
				raise ValueError("Cannot wait for an inbound message to be uploaded")
			from olvid.listeners import MessageUploadedListener
			_on_entity_something(parent_client=self._client, listener_class=MessageUploadedListener, handler=handler, checkers=[get_generic_entity_checker(self._message.id)])

		def message_delivered(self, handler: Callable[[Message], Optional[Coroutine]]):
			if not self._message.is_outbound():
				raise ValueError("Cannot wait for an inbound message to be delivered")
			from olvid.listeners import MessageDeliveredListener
			_on_entity_something(parent_client=self._client, listener_class=MessageDeliveredListener, handler=handler, checkers=[get_generic_entity_checker(self._message.id)])

		def message_read(self, handler: Callable[[Message], Optional[Coroutine]]):
			if not self._message.is_outbound():
				raise ValueError("Cannot wait for an inbound message to be read")
			from olvid.listeners import MessageReadListener
			_on_entity_something(parent_client=self._client, listener_class=MessageReadListener, handler=handler, checkers=[get_generic_entity_checker(self._message.id)])

		def message_edited(self, handler: Callable[[Message], Optional[Coroutine]]):
			from olvid.listeners import MessageBodyUpdatedListener
			_on_entity_something(parent_client=self._client, listener_class=MessageBodyUpdatedListener, handler=handler, checkers=[get_generic_entity_checker(self._message.id)])


# noinspection PyRedeclaration
class MessageId(MessageId):
	def __str__(self):
		return f"{'I' if self.type == MessageId.Type.TYPE_INBOUND else 'O'}{self.id}"


# noinspection PyRedeclaration
class AttachmentId(AttachmentId):
	def __str__(self):
		return f"{'I' if self.type == AttachmentId.Type.TYPE_INBOUND else 'O'}{self.id}"
