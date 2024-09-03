####
# WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_protobuf_overlay
####

from __future__ import annotations  # this block is necessary for compilation
from typing import TYPE_CHECKING  # this block is necessary for compilation
if TYPE_CHECKING:  # this block is necessary for compilation
	from ...core.OlvidClient import OlvidClient  # this block is necessary for compilation
import grpc
from typing import AsyncIterator, Coroutine, Any
from ...protobuf import olvid
from ...datatypes import *


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentListRequest:
	def __init__(self, client: OlvidClient = None, filter: "AttachmentFilter" = None):
		self._client: OlvidClient = client
		self.filter: AttachmentFilter = filter

	def _update_content(self, attachment_list_request: AttachmentListRequest) -> None:
		self.filter: AttachmentFilter = attachment_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentListRequest":
		return AttachmentListRequest(client=self._client, filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListRequest, client: OlvidClient = None) -> "AttachmentListRequest":
		return AttachmentListRequest(client, filter=AttachmentFilter._from_native(native_message.filter, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListRequest], client: OlvidClient = None) -> list["AttachmentListRequest"]:
		return [AttachmentListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListRequest], client: OlvidClient = None) -> "AttachmentListRequest":
		native_message = await promise
		return AttachmentListRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentListRequest"]):
		if messages is None:
			return []
		return [AttachmentListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentListRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListRequest(filter=AttachmentFilter._to_native(message.filter if message.filter else None))

	def __str__(self):
		s: str = ''
		if self.filter:
			s += f'filter: ({self.filter}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentListRequest):
			return False
		return self.filter == other.filter

	def __bool__(self):
		return bool(self.filter)

	def __hash__(self):
		return hash(self.filter)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentListResponse:
	def __init__(self, client: OlvidClient = None, attachments: "list[Attachment]" = None):
		self._client: OlvidClient = client
		self.attachments: list[Attachment] = attachments

	def _update_content(self, attachment_list_response: AttachmentListResponse) -> None:
		self.attachments: list[Attachment] = attachment_list_response.attachments

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentListResponse":
		return AttachmentListResponse(client=self._client, attachments=[e._clone() for e in self.attachments])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListResponse, client: OlvidClient = None) -> "AttachmentListResponse":
		return AttachmentListResponse(client, attachments=Attachment._from_native_list(native_message.attachments, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListResponse], client: OlvidClient = None) -> list["AttachmentListResponse"]:
		return [AttachmentListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListResponse], client: OlvidClient = None) -> "AttachmentListResponse":
		native_message = await promise
		return AttachmentListResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentListResponse"]):
		if messages is None:
			return []
		return [AttachmentListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentListResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListResponse(attachments=Attachment._to_native_list(message.attachments if message.attachments else None))

	def __str__(self):
		s: str = ''
		if self.attachments:
			s += f'attachments: {[str(el) for el in self.attachments]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentListResponse):
			return False
		return self.attachments == other.attachments

	def __bool__(self):
		return bool(self.attachments)

	def __hash__(self):
		return hash(tuple(self.attachments))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field attachments")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentGetRequest:
	def __init__(self, client: OlvidClient = None, attachment_id: "AttachmentId" = None):
		self._client: OlvidClient = client
		self.attachment_id: AttachmentId = attachment_id

	def _update_content(self, attachment_get_request: AttachmentGetRequest) -> None:
		self.attachment_id: AttachmentId = attachment_get_request.attachment_id

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentGetRequest":
		return AttachmentGetRequest(client=self._client, attachment_id=self.attachment_id._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetRequest, client: OlvidClient = None) -> "AttachmentGetRequest":
		return AttachmentGetRequest(client, attachment_id=AttachmentId._from_native(native_message.attachment_id, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetRequest], client: OlvidClient = None) -> list["AttachmentGetRequest"]:
		return [AttachmentGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetRequest], client: OlvidClient = None) -> "AttachmentGetRequest":
		native_message = await promise
		return AttachmentGetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentGetRequest"]):
		if messages is None:
			return []
		return [AttachmentGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetRequest(attachment_id=AttachmentId._to_native(message.attachment_id if message.attachment_id else None))

	def __str__(self):
		s: str = ''
		if self.attachment_id:
			s += f'attachment_id: ({self.attachment_id}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentGetRequest):
			return False
		return self.attachment_id == other.attachment_id

	def __bool__(self):
		return bool(self.attachment_id)

	def __hash__(self):
		return hash(self.attachment_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.attachment_id is None or self.attachment_id._test_assertion(expected.attachment_id)
		except AssertionError as e:
			raise AssertionError("attachment_id: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentGetResponse:
	def __init__(self, client: OlvidClient = None, attachment: "Attachment" = None):
		self._client: OlvidClient = client
		self.attachment: Attachment = attachment

	def _update_content(self, attachment_get_response: AttachmentGetResponse) -> None:
		self.attachment: Attachment = attachment_get_response.attachment

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentGetResponse":
		return AttachmentGetResponse(client=self._client, attachment=self.attachment._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetResponse, client: OlvidClient = None) -> "AttachmentGetResponse":
		return AttachmentGetResponse(client, attachment=Attachment._from_native(native_message.attachment, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetResponse], client: OlvidClient = None) -> list["AttachmentGetResponse"]:
		return [AttachmentGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetResponse], client: OlvidClient = None) -> "AttachmentGetResponse":
		native_message = await promise
		return AttachmentGetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentGetResponse"]):
		if messages is None:
			return []
		return [AttachmentGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetResponse(attachment=Attachment._to_native(message.attachment if message.attachment else None))

	def __str__(self):
		s: str = ''
		if self.attachment:
			s += f'attachment: ({self.attachment}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentGetResponse):
			return False
		return self.attachment == other.attachment

	def __bool__(self):
		return bool(self.attachment)

	def __hash__(self):
		return hash(self.attachment)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.attachment is None or self.attachment._test_assertion(expected.attachment)
		except AssertionError as e:
			raise AssertionError("attachment: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentDeleteRequest:
	def __init__(self, client: OlvidClient = None, attachment_id: "AttachmentId" = None, delete_everywhere: bool = False):
		self._client: OlvidClient = client
		self.attachment_id: AttachmentId = attachment_id
		self.delete_everywhere: bool = delete_everywhere

	def _update_content(self, attachment_delete_request: AttachmentDeleteRequest) -> None:
		self.attachment_id: AttachmentId = attachment_delete_request.attachment_id
		self.delete_everywhere: bool = attachment_delete_request.delete_everywhere

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentDeleteRequest":
		return AttachmentDeleteRequest(client=self._client, attachment_id=self.attachment_id._clone(), delete_everywhere=self.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteRequest, client: OlvidClient = None) -> "AttachmentDeleteRequest":
		return AttachmentDeleteRequest(client, attachment_id=AttachmentId._from_native(native_message.attachment_id, client=client), delete_everywhere=native_message.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteRequest], client: OlvidClient = None) -> list["AttachmentDeleteRequest"]:
		return [AttachmentDeleteRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteRequest], client: OlvidClient = None) -> "AttachmentDeleteRequest":
		native_message = await promise
		return AttachmentDeleteRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentDeleteRequest"]):
		if messages is None:
			return []
		return [AttachmentDeleteRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentDeleteRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteRequest(attachment_id=AttachmentId._to_native(message.attachment_id if message.attachment_id else None), delete_everywhere=message.delete_everywhere if message.delete_everywhere else None)

	def __str__(self):
		s: str = ''
		if self.attachment_id:
			s += f'attachment_id: ({self.attachment_id}), '
		if self.delete_everywhere:
			s += f'delete_everywhere: {self.delete_everywhere}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentDeleteRequest):
			return False
		return self.attachment_id == other.attachment_id and self.delete_everywhere == other.delete_everywhere

	def __bool__(self):
		return bool(self.attachment_id) or self.delete_everywhere

	def __hash__(self):
		return hash((self.attachment_id, self.delete_everywhere))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentDeleteRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.attachment_id is None or self.attachment_id._test_assertion(expected.attachment_id)
		except AssertionError as e:
			raise AssertionError("attachment_id: " + str(e))
		assert expected.delete_everywhere is False or self.delete_everywhere == expected.delete_everywhere, "Invalid value: delete_everywhere: " + str(expected.delete_everywhere) + " != " + str(self.delete_everywhere)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentDeleteResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, attachment_delete_response: AttachmentDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentDeleteResponse":
		return AttachmentDeleteResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteResponse, client: OlvidClient = None) -> "AttachmentDeleteResponse":
		return AttachmentDeleteResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteResponse], client: OlvidClient = None) -> list["AttachmentDeleteResponse"]:
		return [AttachmentDeleteResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteResponse], client: OlvidClient = None) -> "AttachmentDeleteResponse":
		native_message = await promise
		return AttachmentDeleteResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentDeleteResponse"]):
		if messages is None:
			return []
		return [AttachmentDeleteResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentDeleteResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentDeleteResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentDeleteResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentDownloadRequest:
	def __init__(self, client: OlvidClient = None, attachment_id: "AttachmentId" = None):
		self._client: OlvidClient = client
		self.attachment_id: AttachmentId = attachment_id

	def _update_content(self, attachment_download_request: AttachmentDownloadRequest) -> None:
		self.attachment_id: AttachmentId = attachment_download_request.attachment_id

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentDownloadRequest":
		return AttachmentDownloadRequest(client=self._client, attachment_id=self.attachment_id._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadRequest, client: OlvidClient = None) -> "AttachmentDownloadRequest":
		return AttachmentDownloadRequest(client, attachment_id=AttachmentId._from_native(native_message.attachment_id, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadRequest], client: OlvidClient = None) -> list["AttachmentDownloadRequest"]:
		return [AttachmentDownloadRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadRequest], client: OlvidClient = None) -> "AttachmentDownloadRequest":
		native_message = await promise
		return AttachmentDownloadRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentDownloadRequest"]):
		if messages is None:
			return []
		return [AttachmentDownloadRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentDownloadRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadRequest(attachment_id=AttachmentId._to_native(message.attachment_id if message.attachment_id else None))

	def __str__(self):
		s: str = ''
		if self.attachment_id:
			s += f'attachment_id: ({self.attachment_id}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentDownloadRequest):
			return False
		return self.attachment_id == other.attachment_id

	def __bool__(self):
		return bool(self.attachment_id)

	def __hash__(self):
		return hash(self.attachment_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentDownloadRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.attachment_id is None or self.attachment_id._test_assertion(expected.attachment_id)
		except AssertionError as e:
			raise AssertionError("attachment_id: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentDownloadResponse:
	def __init__(self, client: OlvidClient = None, chunk: bytes = b""):
		self._client: OlvidClient = client
		self.chunk: bytes = chunk

	def _update_content(self, attachment_download_response: AttachmentDownloadResponse) -> None:
		self.chunk: bytes = attachment_download_response.chunk

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentDownloadResponse":
		return AttachmentDownloadResponse(client=self._client, chunk=self.chunk)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadResponse, client: OlvidClient = None) -> "AttachmentDownloadResponse":
		return AttachmentDownloadResponse(client, chunk=native_message.chunk)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadResponse], client: OlvidClient = None) -> list["AttachmentDownloadResponse"]:
		return [AttachmentDownloadResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadResponse], client: OlvidClient = None) -> "AttachmentDownloadResponse":
		native_message = await promise
		return AttachmentDownloadResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AttachmentDownloadResponse"]):
		if messages is None:
			return []
		return [AttachmentDownloadResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AttachmentDownloadResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadResponse(chunk=message.chunk if message.chunk else None)

	def __str__(self):
		s: str = ''
		if self.chunk:
			s += f'chunk: {self.chunk}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AttachmentDownloadResponse):
			return False
		return self.chunk == other.chunk

	def __bool__(self):
		return self.chunk != b""

	def __hash__(self):
		return hash(self.chunk)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AttachmentDownloadResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.chunk == b"" or self.chunk == expected.chunk, "Invalid value: chunk: " + str(expected.chunk) + " != " + str(self.chunk)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactListRequest:
	def __init__(self, client: OlvidClient = None, filter: "ContactFilter" = None):
		self._client: OlvidClient = client
		self.filter: ContactFilter = filter

	def _update_content(self, contact_list_request: ContactListRequest) -> None:
		self.filter: ContactFilter = contact_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactListRequest":
		return ContactListRequest(client=self._client, filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactListRequest, client: OlvidClient = None) -> "ContactListRequest":
		return ContactListRequest(client, filter=ContactFilter._from_native(native_message.filter, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactListRequest], client: OlvidClient = None) -> list["ContactListRequest"]:
		return [ContactListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactListRequest], client: OlvidClient = None) -> "ContactListRequest":
		native_message = await promise
		return ContactListRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactListRequest"]):
		if messages is None:
			return []
		return [ContactListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactListRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactListRequest(filter=ContactFilter._to_native(message.filter if message.filter else None))

	def __str__(self):
		s: str = ''
		if self.filter:
			s += f'filter: ({self.filter}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactListRequest):
			return False
		return self.filter == other.filter

	def __bool__(self):
		return bool(self.filter)

	def __hash__(self):
		return hash(self.filter)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactListResponse:
	def __init__(self, client: OlvidClient = None, contacts: "list[Contact]" = None):
		self._client: OlvidClient = client
		self.contacts: list[Contact] = contacts

	def _update_content(self, contact_list_response: ContactListResponse) -> None:
		self.contacts: list[Contact] = contact_list_response.contacts

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactListResponse":
		return ContactListResponse(client=self._client, contacts=[e._clone() for e in self.contacts])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactListResponse, client: OlvidClient = None) -> "ContactListResponse":
		return ContactListResponse(client, contacts=Contact._from_native_list(native_message.contacts, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactListResponse], client: OlvidClient = None) -> list["ContactListResponse"]:
		return [ContactListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactListResponse], client: OlvidClient = None) -> "ContactListResponse":
		native_message = await promise
		return ContactListResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactListResponse"]):
		if messages is None:
			return []
		return [ContactListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactListResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactListResponse(contacts=Contact._to_native_list(message.contacts if message.contacts else None))

	def __str__(self):
		s: str = ''
		if self.contacts:
			s += f'contacts: {[str(el) for el in self.contacts]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactListResponse):
			return False
		return self.contacts == other.contacts

	def __bool__(self):
		return bool(self.contacts)

	def __hash__(self):
		return hash(tuple(self.contacts))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field contacts")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactGetRequest:
	def __init__(self, client: OlvidClient = None, contact_id: int = 0):
		self._client: OlvidClient = client
		self.contact_id: int = contact_id

	def _update_content(self, contact_get_request: ContactGetRequest) -> None:
		self.contact_id: int = contact_get_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactGetRequest":
		return ContactGetRequest(client=self._client, contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactGetRequest, client: OlvidClient = None) -> "ContactGetRequest":
		return ContactGetRequest(client, contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactGetRequest], client: OlvidClient = None) -> list["ContactGetRequest"]:
		return [ContactGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactGetRequest], client: OlvidClient = None) -> "ContactGetRequest":
		native_message = await promise
		return ContactGetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactGetRequest"]):
		if messages is None:
			return []
		return [ContactGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactGetRequest(contact_id=message.contact_id if message.contact_id else None)

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactGetRequest):
			return False
		return self.contact_id == other.contact_id

	def __bool__(self):
		return self.contact_id != 0

	def __hash__(self):
		return hash(self.contact_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactGetResponse:
	def __init__(self, client: OlvidClient = None, contact: "Contact" = None):
		self._client: OlvidClient = client
		self.contact: Contact = contact

	def _update_content(self, contact_get_response: ContactGetResponse) -> None:
		self.contact: Contact = contact_get_response.contact

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactGetResponse":
		return ContactGetResponse(client=self._client, contact=self.contact._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactGetResponse, client: OlvidClient = None) -> "ContactGetResponse":
		return ContactGetResponse(client, contact=Contact._from_native(native_message.contact, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactGetResponse], client: OlvidClient = None) -> list["ContactGetResponse"]:
		return [ContactGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactGetResponse], client: OlvidClient = None) -> "ContactGetResponse":
		native_message = await promise
		return ContactGetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactGetResponse"]):
		if messages is None:
			return []
		return [ContactGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactGetResponse(contact=Contact._to_native(message.contact if message.contact else None))

	def __str__(self):
		s: str = ''
		if self.contact:
			s += f'contact: ({self.contact}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactGetResponse):
			return False
		return self.contact == other.contact

	def __bool__(self):
		return bool(self.contact)

	def __hash__(self):
		return hash(self.contact)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.contact is None or self.contact._test_assertion(expected.contact)
		except AssertionError as e:
			raise AssertionError("contact: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactDeleteRequest:
	def __init__(self, client: OlvidClient = None, contact_id: int = 0):
		self._client: OlvidClient = client
		self.contact_id: int = contact_id

	def _update_content(self, contact_delete_request: ContactDeleteRequest) -> None:
		self.contact_id: int = contact_delete_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDeleteRequest":
		return ContactDeleteRequest(client=self._client, contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteRequest, client: OlvidClient = None) -> "ContactDeleteRequest":
		return ContactDeleteRequest(client, contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteRequest], client: OlvidClient = None) -> list["ContactDeleteRequest"]:
		return [ContactDeleteRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteRequest], client: OlvidClient = None) -> "ContactDeleteRequest":
		native_message = await promise
		return ContactDeleteRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactDeleteRequest"]):
		if messages is None:
			return []
		return [ContactDeleteRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactDeleteRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteRequest(contact_id=message.contact_id if message.contact_id else None)

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactDeleteRequest):
			return False
		return self.contact_id == other.contact_id

	def __bool__(self):
		return self.contact_id != 0

	def __hash__(self):
		return hash(self.contact_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactDeleteRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactDeleteResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, contact_delete_response: ContactDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDeleteResponse":
		return ContactDeleteResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteResponse, client: OlvidClient = None) -> "ContactDeleteResponse":
		return ContactDeleteResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteResponse], client: OlvidClient = None) -> list["ContactDeleteResponse"]:
		return [ContactDeleteResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteResponse], client: OlvidClient = None) -> "ContactDeleteResponse":
		native_message = await promise
		return ContactDeleteResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactDeleteResponse"]):
		if messages is None:
			return []
		return [ContactDeleteResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactDeleteResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactDeleteResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactDeleteResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactIntroductionRequest:
	def __init__(self, client: OlvidClient = None, first_contact_id: int = 0, second_contact_id: int = 0):
		self._client: OlvidClient = client
		self.first_contact_id: int = first_contact_id
		self.second_contact_id: int = second_contact_id

	def _update_content(self, contact_introduction_request: ContactIntroductionRequest) -> None:
		self.first_contact_id: int = contact_introduction_request.first_contact_id
		self.second_contact_id: int = contact_introduction_request.second_contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactIntroductionRequest":
		return ContactIntroductionRequest(client=self._client, first_contact_id=self.first_contact_id, second_contact_id=self.second_contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionRequest, client: OlvidClient = None) -> "ContactIntroductionRequest":
		return ContactIntroductionRequest(client, first_contact_id=native_message.first_contact_id, second_contact_id=native_message.second_contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionRequest], client: OlvidClient = None) -> list["ContactIntroductionRequest"]:
		return [ContactIntroductionRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionRequest], client: OlvidClient = None) -> "ContactIntroductionRequest":
		native_message = await promise
		return ContactIntroductionRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactIntroductionRequest"]):
		if messages is None:
			return []
		return [ContactIntroductionRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactIntroductionRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionRequest(first_contact_id=message.first_contact_id if message.first_contact_id else None, second_contact_id=message.second_contact_id if message.second_contact_id else None)

	def __str__(self):
		s: str = ''
		if self.first_contact_id:
			s += f'first_contact_id: {self.first_contact_id}, '
		if self.second_contact_id:
			s += f'second_contact_id: {self.second_contact_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactIntroductionRequest):
			return False
		return self.first_contact_id == other.first_contact_id and self.second_contact_id == other.second_contact_id

	def __bool__(self):
		return self.first_contact_id != 0 or self.second_contact_id != 0

	def __hash__(self):
		return hash((self.first_contact_id, self.second_contact_id))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactIntroductionRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.first_contact_id == 0 or self.first_contact_id == expected.first_contact_id, "Invalid value: first_contact_id: " + str(expected.first_contact_id) + " != " + str(self.first_contact_id)
		assert expected.second_contact_id == 0 or self.second_contact_id == expected.second_contact_id, "Invalid value: second_contact_id: " + str(expected.second_contact_id) + " != " + str(self.second_contact_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactIntroductionResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, contact_introduction_response: ContactIntroductionResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactIntroductionResponse":
		return ContactIntroductionResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionResponse, client: OlvidClient = None) -> "ContactIntroductionResponse":
		return ContactIntroductionResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionResponse], client: OlvidClient = None) -> list["ContactIntroductionResponse"]:
		return [ContactIntroductionResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionResponse], client: OlvidClient = None) -> "ContactIntroductionResponse":
		native_message = await promise
		return ContactIntroductionResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactIntroductionResponse"]):
		if messages is None:
			return []
		return [ContactIntroductionResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactIntroductionResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactIntroductionResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactIntroductionResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactInviteToOneToOneDiscussionRequest:
	def __init__(self, client: OlvidClient = None, contact_id: int = 0):
		self._client: OlvidClient = client
		self.contact_id: int = contact_id

	def _update_content(self, contact_invite_to_one_to_one_discussion_request: ContactInviteToOneToOneDiscussionRequest) -> None:
		self.contact_id: int = contact_invite_to_one_to_one_discussion_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactInviteToOneToOneDiscussionRequest":
		return ContactInviteToOneToOneDiscussionRequest(client=self._client, contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionRequest, client: OlvidClient = None) -> "ContactInviteToOneToOneDiscussionRequest":
		return ContactInviteToOneToOneDiscussionRequest(client, contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionRequest], client: OlvidClient = None) -> list["ContactInviteToOneToOneDiscussionRequest"]:
		return [ContactInviteToOneToOneDiscussionRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionRequest], client: OlvidClient = None) -> "ContactInviteToOneToOneDiscussionRequest":
		native_message = await promise
		return ContactInviteToOneToOneDiscussionRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactInviteToOneToOneDiscussionRequest"]):
		if messages is None:
			return []
		return [ContactInviteToOneToOneDiscussionRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactInviteToOneToOneDiscussionRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionRequest(contact_id=message.contact_id if message.contact_id else None)

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactInviteToOneToOneDiscussionRequest):
			return False
		return self.contact_id == other.contact_id

	def __bool__(self):
		return self.contact_id != 0

	def __hash__(self):
		return hash(self.contact_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactInviteToOneToOneDiscussionRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactInviteToOneToOneDiscussionResponse:
	def __init__(self, client: OlvidClient = None, invitation: "Invitation" = None):
		self._client: OlvidClient = client
		self.invitation: Invitation = invitation

	def _update_content(self, contact_invite_to_one_to_one_discussion_response: ContactInviteToOneToOneDiscussionResponse) -> None:
		self.invitation: Invitation = contact_invite_to_one_to_one_discussion_response.invitation

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactInviteToOneToOneDiscussionResponse":
		return ContactInviteToOneToOneDiscussionResponse(client=self._client, invitation=self.invitation._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionResponse, client: OlvidClient = None) -> "ContactInviteToOneToOneDiscussionResponse":
		return ContactInviteToOneToOneDiscussionResponse(client, invitation=Invitation._from_native(native_message.invitation, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionResponse], client: OlvidClient = None) -> list["ContactInviteToOneToOneDiscussionResponse"]:
		return [ContactInviteToOneToOneDiscussionResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionResponse], client: OlvidClient = None) -> "ContactInviteToOneToOneDiscussionResponse":
		native_message = await promise
		return ContactInviteToOneToOneDiscussionResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactInviteToOneToOneDiscussionResponse"]):
		if messages is None:
			return []
		return [ContactInviteToOneToOneDiscussionResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactInviteToOneToOneDiscussionResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionResponse(invitation=Invitation._to_native(message.invitation if message.invitation else None))

	def __str__(self):
		s: str = ''
		if self.invitation:
			s += f'invitation: ({self.invitation}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactInviteToOneToOneDiscussionResponse):
			return False
		return self.invitation == other.invitation

	def __bool__(self):
		return bool(self.invitation)

	def __hash__(self):
		return hash(self.invitation)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactInviteToOneToOneDiscussionResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.invitation is None or self.invitation._test_assertion(expected.invitation)
		except AssertionError as e:
			raise AssertionError("invitation: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactDowngradeOneToOneDiscussionRequest:
	def __init__(self, client: OlvidClient = None, contact_id: int = 0):
		self._client: OlvidClient = client
		self.contact_id: int = contact_id

	def _update_content(self, contact_downgrade_one_to_one_discussion_request: ContactDowngradeOneToOneDiscussionRequest) -> None:
		self.contact_id: int = contact_downgrade_one_to_one_discussion_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDowngradeOneToOneDiscussionRequest":
		return ContactDowngradeOneToOneDiscussionRequest(client=self._client, contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionRequest, client: OlvidClient = None) -> "ContactDowngradeOneToOneDiscussionRequest":
		return ContactDowngradeOneToOneDiscussionRequest(client, contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionRequest], client: OlvidClient = None) -> list["ContactDowngradeOneToOneDiscussionRequest"]:
		return [ContactDowngradeOneToOneDiscussionRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionRequest], client: OlvidClient = None) -> "ContactDowngradeOneToOneDiscussionRequest":
		native_message = await promise
		return ContactDowngradeOneToOneDiscussionRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactDowngradeOneToOneDiscussionRequest"]):
		if messages is None:
			return []
		return [ContactDowngradeOneToOneDiscussionRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactDowngradeOneToOneDiscussionRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionRequest(contact_id=message.contact_id if message.contact_id else None)

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactDowngradeOneToOneDiscussionRequest):
			return False
		return self.contact_id == other.contact_id

	def __bool__(self):
		return self.contact_id != 0

	def __hash__(self):
		return hash(self.contact_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactDowngradeOneToOneDiscussionRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactDowngradeOneToOneDiscussionResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, contact_downgrade_one_to_one_discussion_response: ContactDowngradeOneToOneDiscussionResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDowngradeOneToOneDiscussionResponse":
		return ContactDowngradeOneToOneDiscussionResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionResponse, client: OlvidClient = None) -> "ContactDowngradeOneToOneDiscussionResponse":
		return ContactDowngradeOneToOneDiscussionResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionResponse], client: OlvidClient = None) -> list["ContactDowngradeOneToOneDiscussionResponse"]:
		return [ContactDowngradeOneToOneDiscussionResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionResponse], client: OlvidClient = None) -> "ContactDowngradeOneToOneDiscussionResponse":
		native_message = await promise
		return ContactDowngradeOneToOneDiscussionResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactDowngradeOneToOneDiscussionResponse"]):
		if messages is None:
			return []
		return [ContactDowngradeOneToOneDiscussionResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactDowngradeOneToOneDiscussionResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactDowngradeOneToOneDiscussionResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactDowngradeOneToOneDiscussionResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionListRequest:
	def __init__(self, client: OlvidClient = None, filter: "DiscussionFilter" = None):
		self._client: OlvidClient = client
		self.filter: DiscussionFilter = filter

	def _update_content(self, discussion_list_request: DiscussionListRequest) -> None:
		self.filter: DiscussionFilter = discussion_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionListRequest":
		return DiscussionListRequest(client=self._client, filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListRequest, client: OlvidClient = None) -> "DiscussionListRequest":
		return DiscussionListRequest(client, filter=DiscussionFilter._from_native(native_message.filter, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListRequest], client: OlvidClient = None) -> list["DiscussionListRequest"]:
		return [DiscussionListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListRequest], client: OlvidClient = None) -> "DiscussionListRequest":
		native_message = await promise
		return DiscussionListRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionListRequest"]):
		if messages is None:
			return []
		return [DiscussionListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionListRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListRequest(filter=DiscussionFilter._to_native(message.filter if message.filter else None))

	def __str__(self):
		s: str = ''
		if self.filter:
			s += f'filter: ({self.filter}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionListRequest):
			return False
		return self.filter == other.filter

	def __bool__(self):
		return bool(self.filter)

	def __hash__(self):
		return hash(self.filter)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionListResponse:
	def __init__(self, client: OlvidClient = None, discussions: "list[Discussion]" = None):
		self._client: OlvidClient = client
		self.discussions: list[Discussion] = discussions

	def _update_content(self, discussion_list_response: DiscussionListResponse) -> None:
		self.discussions: list[Discussion] = discussion_list_response.discussions

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionListResponse":
		return DiscussionListResponse(client=self._client, discussions=[e._clone() for e in self.discussions])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListResponse, client: OlvidClient = None) -> "DiscussionListResponse":
		return DiscussionListResponse(client, discussions=Discussion._from_native_list(native_message.discussions, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListResponse], client: OlvidClient = None) -> list["DiscussionListResponse"]:
		return [DiscussionListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListResponse], client: OlvidClient = None) -> "DiscussionListResponse":
		native_message = await promise
		return DiscussionListResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionListResponse"]):
		if messages is None:
			return []
		return [DiscussionListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionListResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListResponse(discussions=Discussion._to_native_list(message.discussions if message.discussions else None))

	def __str__(self):
		s: str = ''
		if self.discussions:
			s += f'discussions: {[str(el) for el in self.discussions]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionListResponse):
			return False
		return self.discussions == other.discussions

	def __bool__(self):
		return bool(self.discussions)

	def __hash__(self):
		return hash(tuple(self.discussions))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field discussions")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionGetRequest:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id

	def _update_content(self, discussion_get_request: DiscussionGetRequest) -> None:
		self.discussion_id: int = discussion_get_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetRequest":
		return DiscussionGetRequest(client=self._client, discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetRequest, client: OlvidClient = None) -> "DiscussionGetRequest":
		return DiscussionGetRequest(client, discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetRequest], client: OlvidClient = None) -> list["DiscussionGetRequest"]:
		return [DiscussionGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetRequest], client: OlvidClient = None) -> "DiscussionGetRequest":
		native_message = await promise
		return DiscussionGetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionGetRequest"]):
		if messages is None:
			return []
		return [DiscussionGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetRequest(discussion_id=message.discussion_id if message.discussion_id else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionGetRequest):
			return False
		return self.discussion_id == other.discussion_id

	def __bool__(self):
		return self.discussion_id != 0

	def __hash__(self):
		return hash(self.discussion_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionGetResponse:
	def __init__(self, client: OlvidClient = None, discussion: "Discussion" = None):
		self._client: OlvidClient = client
		self.discussion: Discussion = discussion

	def _update_content(self, discussion_get_response: DiscussionGetResponse) -> None:
		self.discussion: Discussion = discussion_get_response.discussion

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetResponse":
		return DiscussionGetResponse(client=self._client, discussion=self.discussion._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetResponse, client: OlvidClient = None) -> "DiscussionGetResponse":
		return DiscussionGetResponse(client, discussion=Discussion._from_native(native_message.discussion, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetResponse], client: OlvidClient = None) -> list["DiscussionGetResponse"]:
		return [DiscussionGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetResponse], client: OlvidClient = None) -> "DiscussionGetResponse":
		native_message = await promise
		return DiscussionGetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionGetResponse"]):
		if messages is None:
			return []
		return [DiscussionGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetResponse(discussion=Discussion._to_native(message.discussion if message.discussion else None))

	def __str__(self):
		s: str = ''
		if self.discussion:
			s += f'discussion: ({self.discussion}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionGetResponse):
			return False
		return self.discussion == other.discussion

	def __bool__(self):
		return bool(self.discussion)

	def __hash__(self):
		return hash(self.discussion)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.discussion is None or self.discussion._test_assertion(expected.discussion)
		except AssertionError as e:
			raise AssertionError("discussion: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionGetByContactRequest:
	def __init__(self, client: OlvidClient = None, contact_id: int = 0):
		self._client: OlvidClient = client
		self.contact_id: int = contact_id

	def _update_content(self, discussion_get_by_contact_request: DiscussionGetByContactRequest) -> None:
		self.contact_id: int = discussion_get_by_contact_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetByContactRequest":
		return DiscussionGetByContactRequest(client=self._client, contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactRequest, client: OlvidClient = None) -> "DiscussionGetByContactRequest":
		return DiscussionGetByContactRequest(client, contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactRequest], client: OlvidClient = None) -> list["DiscussionGetByContactRequest"]:
		return [DiscussionGetByContactRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactRequest], client: OlvidClient = None) -> "DiscussionGetByContactRequest":
		native_message = await promise
		return DiscussionGetByContactRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionGetByContactRequest"]):
		if messages is None:
			return []
		return [DiscussionGetByContactRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionGetByContactRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactRequest(contact_id=message.contact_id if message.contact_id else None)

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionGetByContactRequest):
			return False
		return self.contact_id == other.contact_id

	def __bool__(self):
		return self.contact_id != 0

	def __hash__(self):
		return hash(self.contact_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionGetByContactRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionGetByContactResponse:
	def __init__(self, client: OlvidClient = None, discussion: "Discussion" = None):
		self._client: OlvidClient = client
		self.discussion: Discussion = discussion

	def _update_content(self, discussion_get_by_contact_response: DiscussionGetByContactResponse) -> None:
		self.discussion: Discussion = discussion_get_by_contact_response.discussion

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetByContactResponse":
		return DiscussionGetByContactResponse(client=self._client, discussion=self.discussion._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactResponse, client: OlvidClient = None) -> "DiscussionGetByContactResponse":
		return DiscussionGetByContactResponse(client, discussion=Discussion._from_native(native_message.discussion, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactResponse], client: OlvidClient = None) -> list["DiscussionGetByContactResponse"]:
		return [DiscussionGetByContactResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactResponse], client: OlvidClient = None) -> "DiscussionGetByContactResponse":
		native_message = await promise
		return DiscussionGetByContactResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionGetByContactResponse"]):
		if messages is None:
			return []
		return [DiscussionGetByContactResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionGetByContactResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactResponse(discussion=Discussion._to_native(message.discussion if message.discussion else None))

	def __str__(self):
		s: str = ''
		if self.discussion:
			s += f'discussion: ({self.discussion}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionGetByContactResponse):
			return False
		return self.discussion == other.discussion

	def __bool__(self):
		return bool(self.discussion)

	def __hash__(self):
		return hash(self.discussion)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionGetByContactResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.discussion is None or self.discussion._test_assertion(expected.discussion)
		except AssertionError as e:
			raise AssertionError("discussion: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionGetByGroupRequest:
	def __init__(self, client: OlvidClient = None, group_id: int = 0):
		self._client: OlvidClient = client
		self.group_id: int = group_id

	def _update_content(self, discussion_get_by_group_request: DiscussionGetByGroupRequest) -> None:
		self.group_id: int = discussion_get_by_group_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetByGroupRequest":
		return DiscussionGetByGroupRequest(client=self._client, group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupRequest, client: OlvidClient = None) -> "DiscussionGetByGroupRequest":
		return DiscussionGetByGroupRequest(client, group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupRequest], client: OlvidClient = None) -> list["DiscussionGetByGroupRequest"]:
		return [DiscussionGetByGroupRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupRequest], client: OlvidClient = None) -> "DiscussionGetByGroupRequest":
		native_message = await promise
		return DiscussionGetByGroupRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionGetByGroupRequest"]):
		if messages is None:
			return []
		return [DiscussionGetByGroupRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionGetByGroupRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupRequest(group_id=message.group_id if message.group_id else None)

	def __str__(self):
		s: str = ''
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionGetByGroupRequest):
			return False
		return self.group_id == other.group_id

	def __bool__(self):
		return self.group_id != 0

	def __hash__(self):
		return hash(self.group_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionGetByGroupRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.group_id == 0 or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionGetByGroupResponse:
	def __init__(self, client: OlvidClient = None, discussion: "Discussion" = None):
		self._client: OlvidClient = client
		self.discussion: Discussion = discussion

	def _update_content(self, discussion_get_by_group_response: DiscussionGetByGroupResponse) -> None:
		self.discussion: Discussion = discussion_get_by_group_response.discussion

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetByGroupResponse":
		return DiscussionGetByGroupResponse(client=self._client, discussion=self.discussion._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupResponse, client: OlvidClient = None) -> "DiscussionGetByGroupResponse":
		return DiscussionGetByGroupResponse(client, discussion=Discussion._from_native(native_message.discussion, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupResponse], client: OlvidClient = None) -> list["DiscussionGetByGroupResponse"]:
		return [DiscussionGetByGroupResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupResponse], client: OlvidClient = None) -> "DiscussionGetByGroupResponse":
		native_message = await promise
		return DiscussionGetByGroupResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionGetByGroupResponse"]):
		if messages is None:
			return []
		return [DiscussionGetByGroupResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionGetByGroupResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupResponse(discussion=Discussion._to_native(message.discussion if message.discussion else None))

	def __str__(self):
		s: str = ''
		if self.discussion:
			s += f'discussion: ({self.discussion}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionGetByGroupResponse):
			return False
		return self.discussion == other.discussion

	def __bool__(self):
		return bool(self.discussion)

	def __hash__(self):
		return hash(self.discussion)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionGetByGroupResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.discussion is None or self.discussion._test_assertion(expected.discussion)
		except AssertionError as e:
			raise AssertionError("discussion: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionEmptyRequest:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0, delete_everywhere: bool = False):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id
		self.delete_everywhere: bool = delete_everywhere

	def _update_content(self, discussion_empty_request: DiscussionEmptyRequest) -> None:
		self.discussion_id: int = discussion_empty_request.discussion_id
		self.delete_everywhere: bool = discussion_empty_request.delete_everywhere

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionEmptyRequest":
		return DiscussionEmptyRequest(client=self._client, discussion_id=self.discussion_id, delete_everywhere=self.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyRequest, client: OlvidClient = None) -> "DiscussionEmptyRequest":
		return DiscussionEmptyRequest(client, discussion_id=native_message.discussion_id, delete_everywhere=native_message.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyRequest], client: OlvidClient = None) -> list["DiscussionEmptyRequest"]:
		return [DiscussionEmptyRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyRequest], client: OlvidClient = None) -> "DiscussionEmptyRequest":
		native_message = await promise
		return DiscussionEmptyRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionEmptyRequest"]):
		if messages is None:
			return []
		return [DiscussionEmptyRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionEmptyRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyRequest(discussion_id=message.discussion_id if message.discussion_id else None, delete_everywhere=message.delete_everywhere if message.delete_everywhere else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.delete_everywhere:
			s += f'delete_everywhere: {self.delete_everywhere}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionEmptyRequest):
			return False
		return self.discussion_id == other.discussion_id and self.delete_everywhere == other.delete_everywhere

	def __bool__(self):
		return self.discussion_id != 0 or self.delete_everywhere

	def __hash__(self):
		return hash((self.discussion_id, self.delete_everywhere))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionEmptyRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.delete_everywhere is False or self.delete_everywhere == expected.delete_everywhere, "Invalid value: delete_everywhere: " + str(expected.delete_everywhere) + " != " + str(self.delete_everywhere)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionEmptyResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, discussion_empty_response: DiscussionEmptyResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionEmptyResponse":
		return DiscussionEmptyResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyResponse, client: OlvidClient = None) -> "DiscussionEmptyResponse":
		return DiscussionEmptyResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyResponse], client: OlvidClient = None) -> list["DiscussionEmptyResponse"]:
		return [DiscussionEmptyResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyResponse], client: OlvidClient = None) -> "DiscussionEmptyResponse":
		native_message = await promise
		return DiscussionEmptyResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionEmptyResponse"]):
		if messages is None:
			return []
		return [DiscussionEmptyResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionEmptyResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionEmptyResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionEmptyResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionSettingsGetRequest:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id

	def _update_content(self, discussion_settings_get_request: DiscussionSettingsGetRequest) -> None:
		self.discussion_id: int = discussion_settings_get_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionSettingsGetRequest":
		return DiscussionSettingsGetRequest(client=self._client, discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsGetRequest, client: OlvidClient = None) -> "DiscussionSettingsGetRequest":
		return DiscussionSettingsGetRequest(client, discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsGetRequest], client: OlvidClient = None) -> list["DiscussionSettingsGetRequest"]:
		return [DiscussionSettingsGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsGetRequest], client: OlvidClient = None) -> "DiscussionSettingsGetRequest":
		native_message = await promise
		return DiscussionSettingsGetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionSettingsGetRequest"]):
		if messages is None:
			return []
		return [DiscussionSettingsGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionSettingsGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsGetRequest(discussion_id=message.discussion_id if message.discussion_id else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionSettingsGetRequest):
			return False
		return self.discussion_id == other.discussion_id

	def __bool__(self):
		return self.discussion_id != 0

	def __hash__(self):
		return hash(self.discussion_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionSettingsGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionSettingsGetResponse:
	def __init__(self, client: OlvidClient = None, settings: "DiscussionSettings" = None):
		self._client: OlvidClient = client
		self.settings: DiscussionSettings = settings

	def _update_content(self, discussion_settings_get_response: DiscussionSettingsGetResponse) -> None:
		self.settings: DiscussionSettings = discussion_settings_get_response.settings

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionSettingsGetResponse":
		return DiscussionSettingsGetResponse(client=self._client, settings=self.settings._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsGetResponse, client: OlvidClient = None) -> "DiscussionSettingsGetResponse":
		return DiscussionSettingsGetResponse(client, settings=DiscussionSettings._from_native(native_message.settings, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsGetResponse], client: OlvidClient = None) -> list["DiscussionSettingsGetResponse"]:
		return [DiscussionSettingsGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsGetResponse], client: OlvidClient = None) -> "DiscussionSettingsGetResponse":
		native_message = await promise
		return DiscussionSettingsGetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionSettingsGetResponse"]):
		if messages is None:
			return []
		return [DiscussionSettingsGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionSettingsGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsGetResponse(settings=DiscussionSettings._to_native(message.settings if message.settings else None))

	def __str__(self):
		s: str = ''
		if self.settings:
			s += f'settings: ({self.settings}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionSettingsGetResponse):
			return False
		return self.settings == other.settings

	def __bool__(self):
		return bool(self.settings)

	def __hash__(self):
		return hash(self.settings)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionSettingsGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.settings is None or self.settings._test_assertion(expected.settings)
		except AssertionError as e:
			raise AssertionError("settings: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionSettingsSetRequest:
	def __init__(self, client: OlvidClient = None, settings: "DiscussionSettings" = None):
		self._client: OlvidClient = client
		self.settings: DiscussionSettings = settings

	def _update_content(self, discussion_settings_set_request: DiscussionSettingsSetRequest) -> None:
		self.settings: DiscussionSettings = discussion_settings_set_request.settings

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionSettingsSetRequest":
		return DiscussionSettingsSetRequest(client=self._client, settings=self.settings._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsSetRequest, client: OlvidClient = None) -> "DiscussionSettingsSetRequest":
		return DiscussionSettingsSetRequest(client, settings=DiscussionSettings._from_native(native_message.settings, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsSetRequest], client: OlvidClient = None) -> list["DiscussionSettingsSetRequest"]:
		return [DiscussionSettingsSetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsSetRequest], client: OlvidClient = None) -> "DiscussionSettingsSetRequest":
		native_message = await promise
		return DiscussionSettingsSetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionSettingsSetRequest"]):
		if messages is None:
			return []
		return [DiscussionSettingsSetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionSettingsSetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsSetRequest(settings=DiscussionSettings._to_native(message.settings if message.settings else None))

	def __str__(self):
		s: str = ''
		if self.settings:
			s += f'settings: ({self.settings}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionSettingsSetRequest):
			return False
		return self.settings == other.settings

	def __bool__(self):
		return bool(self.settings)

	def __hash__(self):
		return hash(self.settings)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionSettingsSetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.settings is None or self.settings._test_assertion(expected.settings)
		except AssertionError as e:
			raise AssertionError("settings: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionSettingsSetResponse:
	def __init__(self, client: OlvidClient = None, new_settings: "DiscussionSettings" = None):
		self._client: OlvidClient = client
		self.new_settings: DiscussionSettings = new_settings

	def _update_content(self, discussion_settings_set_response: DiscussionSettingsSetResponse) -> None:
		self.new_settings: DiscussionSettings = discussion_settings_set_response.new_settings

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionSettingsSetResponse":
		return DiscussionSettingsSetResponse(client=self._client, new_settings=self.new_settings._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsSetResponse, client: OlvidClient = None) -> "DiscussionSettingsSetResponse":
		return DiscussionSettingsSetResponse(client, new_settings=DiscussionSettings._from_native(native_message.new_settings, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsSetResponse], client: OlvidClient = None) -> list["DiscussionSettingsSetResponse"]:
		return [DiscussionSettingsSetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsSetResponse], client: OlvidClient = None) -> "DiscussionSettingsSetResponse":
		native_message = await promise
		return DiscussionSettingsSetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionSettingsSetResponse"]):
		if messages is None:
			return []
		return [DiscussionSettingsSetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionSettingsSetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsSetResponse(new_settings=DiscussionSettings._to_native(message.new_settings if message.new_settings else None))

	def __str__(self):
		s: str = ''
		if self.new_settings:
			s += f'new_settings: ({self.new_settings}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionSettingsSetResponse):
			return False
		return self.new_settings == other.new_settings

	def __bool__(self):
		return bool(self.new_settings)

	def __hash__(self):
		return hash(self.new_settings)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionSettingsSetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.new_settings is None or self.new_settings._test_assertion(expected.new_settings)
		except AssertionError as e:
			raise AssertionError("new_settings: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionLockedListRequest:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, discussion_locked_list_request: DiscussionLockedListRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionLockedListRequest":
		return DiscussionLockedListRequest(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListRequest, client: OlvidClient = None) -> "DiscussionLockedListRequest":
		return DiscussionLockedListRequest(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListRequest], client: OlvidClient = None) -> list["DiscussionLockedListRequest"]:
		return [DiscussionLockedListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListRequest], client: OlvidClient = None) -> "DiscussionLockedListRequest":
		native_message = await promise
		return DiscussionLockedListRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionLockedListRequest"]):
		if messages is None:
			return []
		return [DiscussionLockedListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionLockedListRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionLockedListRequest):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionLockedListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionLockedListResponse:
	def __init__(self, client: OlvidClient = None, discussions: "list[Discussion]" = None):
		self._client: OlvidClient = client
		self.discussions: list[Discussion] = discussions

	def _update_content(self, discussion_locked_list_response: DiscussionLockedListResponse) -> None:
		self.discussions: list[Discussion] = discussion_locked_list_response.discussions

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionLockedListResponse":
		return DiscussionLockedListResponse(client=self._client, discussions=[e._clone() for e in self.discussions])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListResponse, client: OlvidClient = None) -> "DiscussionLockedListResponse":
		return DiscussionLockedListResponse(client, discussions=Discussion._from_native_list(native_message.discussions, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListResponse], client: OlvidClient = None) -> list["DiscussionLockedListResponse"]:
		return [DiscussionLockedListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListResponse], client: OlvidClient = None) -> "DiscussionLockedListResponse":
		native_message = await promise
		return DiscussionLockedListResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionLockedListResponse"]):
		if messages is None:
			return []
		return [DiscussionLockedListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionLockedListResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListResponse(discussions=Discussion._to_native_list(message.discussions if message.discussions else None))

	def __str__(self):
		s: str = ''
		if self.discussions:
			s += f'discussions: {[str(el) for el in self.discussions]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionLockedListResponse):
			return False
		return self.discussions == other.discussions

	def __bool__(self):
		return bool(self.discussions)

	def __hash__(self):
		return hash(tuple(self.discussions))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionLockedListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field discussions")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionLockedDeleteRequest:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id

	def _update_content(self, discussion_locked_delete_request: DiscussionLockedDeleteRequest) -> None:
		self.discussion_id: int = discussion_locked_delete_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionLockedDeleteRequest":
		return DiscussionLockedDeleteRequest(client=self._client, discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteRequest, client: OlvidClient = None) -> "DiscussionLockedDeleteRequest":
		return DiscussionLockedDeleteRequest(client, discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteRequest], client: OlvidClient = None) -> list["DiscussionLockedDeleteRequest"]:
		return [DiscussionLockedDeleteRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteRequest], client: OlvidClient = None) -> "DiscussionLockedDeleteRequest":
		native_message = await promise
		return DiscussionLockedDeleteRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionLockedDeleteRequest"]):
		if messages is None:
			return []
		return [DiscussionLockedDeleteRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionLockedDeleteRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteRequest(discussion_id=message.discussion_id if message.discussion_id else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionLockedDeleteRequest):
			return False
		return self.discussion_id == other.discussion_id

	def __bool__(self):
		return self.discussion_id != 0

	def __hash__(self):
		return hash(self.discussion_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionLockedDeleteRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionLockedDeleteResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, discussion_locked_delete_response: DiscussionLockedDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionLockedDeleteResponse":
		return DiscussionLockedDeleteResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteResponse, client: OlvidClient = None) -> "DiscussionLockedDeleteResponse":
		return DiscussionLockedDeleteResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteResponse], client: OlvidClient = None) -> list["DiscussionLockedDeleteResponse"]:
		return [DiscussionLockedDeleteResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteResponse], client: OlvidClient = None) -> "DiscussionLockedDeleteResponse":
		native_message = await promise
		return DiscussionLockedDeleteResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionLockedDeleteResponse"]):
		if messages is None:
			return []
		return [DiscussionLockedDeleteResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionLockedDeleteResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionLockedDeleteResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionLockedDeleteResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupListRequest:
	def __init__(self, client: OlvidClient = None, filter: "GroupFilter" = None):
		self._client: OlvidClient = client
		self.filter: GroupFilter = filter

	def _update_content(self, group_list_request: GroupListRequest) -> None:
		self.filter: GroupFilter = group_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupListRequest":
		return GroupListRequest(client=self._client, filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupListRequest, client: OlvidClient = None) -> "GroupListRequest":
		return GroupListRequest(client, filter=GroupFilter._from_native(native_message.filter, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupListRequest], client: OlvidClient = None) -> list["GroupListRequest"]:
		return [GroupListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupListRequest], client: OlvidClient = None) -> "GroupListRequest":
		native_message = await promise
		return GroupListRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupListRequest"]):
		if messages is None:
			return []
		return [GroupListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupListRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupListRequest(filter=GroupFilter._to_native(message.filter if message.filter else None))

	def __str__(self):
		s: str = ''
		if self.filter:
			s += f'filter: ({self.filter}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupListRequest):
			return False
		return self.filter == other.filter

	def __bool__(self):
		return bool(self.filter)

	def __hash__(self):
		return hash(self.filter)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupListResponse:
	def __init__(self, client: OlvidClient = None, groups: "list[Group]" = None):
		self._client: OlvidClient = client
		self.groups: list[Group] = groups

	def _update_content(self, group_list_response: GroupListResponse) -> None:
		self.groups: list[Group] = group_list_response.groups

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupListResponse":
		return GroupListResponse(client=self._client, groups=[e._clone() for e in self.groups])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupListResponse, client: OlvidClient = None) -> "GroupListResponse":
		return GroupListResponse(client, groups=Group._from_native_list(native_message.groups, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupListResponse], client: OlvidClient = None) -> list["GroupListResponse"]:
		return [GroupListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupListResponse], client: OlvidClient = None) -> "GroupListResponse":
		native_message = await promise
		return GroupListResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupListResponse"]):
		if messages is None:
			return []
		return [GroupListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupListResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupListResponse(groups=Group._to_native_list(message.groups if message.groups else None))

	def __str__(self):
		s: str = ''
		if self.groups:
			s += f'groups: {[str(el) for el in self.groups]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupListResponse):
			return False
		return self.groups == other.groups

	def __bool__(self):
		return bool(self.groups)

	def __hash__(self):
		return hash(tuple(self.groups))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field groups")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupGetRequest:
	def __init__(self, client: OlvidClient = None, group_id: int = 0):
		self._client: OlvidClient = client
		self.group_id: int = group_id

	def _update_content(self, group_get_request: GroupGetRequest) -> None:
		self.group_id: int = group_get_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupGetRequest":
		return GroupGetRequest(client=self._client, group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupGetRequest, client: OlvidClient = None) -> "GroupGetRequest":
		return GroupGetRequest(client, group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupGetRequest], client: OlvidClient = None) -> list["GroupGetRequest"]:
		return [GroupGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupGetRequest], client: OlvidClient = None) -> "GroupGetRequest":
		native_message = await promise
		return GroupGetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupGetRequest"]):
		if messages is None:
			return []
		return [GroupGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupGetRequest(group_id=message.group_id if message.group_id else None)

	def __str__(self):
		s: str = ''
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupGetRequest):
			return False
		return self.group_id == other.group_id

	def __bool__(self):
		return self.group_id != 0

	def __hash__(self):
		return hash(self.group_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.group_id == 0 or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupGetResponse:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_get_response: GroupGetResponse) -> None:
		self.group: Group = group_get_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupGetResponse":
		return GroupGetResponse(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupGetResponse, client: OlvidClient = None) -> "GroupGetResponse":
		return GroupGetResponse(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupGetResponse], client: OlvidClient = None) -> list["GroupGetResponse"]:
		return [GroupGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupGetResponse], client: OlvidClient = None) -> "GroupGetResponse":
		native_message = await promise
		return GroupGetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupGetResponse"]):
		if messages is None:
			return []
		return [GroupGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupGetResponse(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupGetResponse):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNewStandardGroupRequest:
	def __init__(self, client: OlvidClient = None, name: str = "", description: str = "", admin_contact_ids: list[int] = ()):
		self._client: OlvidClient = client
		self.name: str = name
		self.description: str = description
		self.admin_contact_ids: list[int] = admin_contact_ids

	def _update_content(self, group_new_standard_group_request: GroupNewStandardGroupRequest) -> None:
		self.name: str = group_new_standard_group_request.name
		self.description: str = group_new_standard_group_request.description
		self.admin_contact_ids: list[int] = group_new_standard_group_request.admin_contact_ids

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewStandardGroupRequest":
		return GroupNewStandardGroupRequest(client=self._client, name=self.name, description=self.description, admin_contact_ids=[e for e in self.admin_contact_ids])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupRequest, client: OlvidClient = None) -> "GroupNewStandardGroupRequest":
		return GroupNewStandardGroupRequest(client, name=native_message.name, description=native_message.description, admin_contact_ids=native_message.admin_contact_ids)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupRequest], client: OlvidClient = None) -> list["GroupNewStandardGroupRequest"]:
		return [GroupNewStandardGroupRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupRequest], client: OlvidClient = None) -> "GroupNewStandardGroupRequest":
		native_message = await promise
		return GroupNewStandardGroupRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupNewStandardGroupRequest"]):
		if messages is None:
			return []
		return [GroupNewStandardGroupRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupNewStandardGroupRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupRequest(name=message.name if message.name else None, description=message.description if message.description else None, admin_contact_ids=message.admin_contact_ids if message.admin_contact_ids else None)

	def __str__(self):
		s: str = ''
		if self.name:
			s += f'name: {self.name}, '
		if self.description:
			s += f'description: {self.description}, '
		if self.admin_contact_ids:
			s += f'admin_contact_ids: {[str(el) for el in self.admin_contact_ids]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupNewStandardGroupRequest):
			return False
		return self.name == other.name and self.description == other.description and self.admin_contact_ids == other.admin_contact_ids

	def __bool__(self):
		return self.name != "" or self.description != "" or bool(self.admin_contact_ids)

	def __hash__(self):
		return hash((self.name, self.description, tuple(self.admin_contact_ids)))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupNewStandardGroupRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.name == "" or self.name == expected.name, "Invalid value: name: " + str(expected.name) + " != " + str(self.name)
		assert expected.description == "" or self.description == expected.description, "Invalid value: description: " + str(expected.description) + " != " + str(self.description)
		pass  # print("Warning: test_assertion: skipped a list field admin_contact_ids")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNewStandardGroupResponse:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_new_standard_group_response: GroupNewStandardGroupResponse) -> None:
		self.group: Group = group_new_standard_group_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewStandardGroupResponse":
		return GroupNewStandardGroupResponse(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupResponse, client: OlvidClient = None) -> "GroupNewStandardGroupResponse":
		return GroupNewStandardGroupResponse(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupResponse], client: OlvidClient = None) -> list["GroupNewStandardGroupResponse"]:
		return [GroupNewStandardGroupResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupResponse], client: OlvidClient = None) -> "GroupNewStandardGroupResponse":
		native_message = await promise
		return GroupNewStandardGroupResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupNewStandardGroupResponse"]):
		if messages is None:
			return []
		return [GroupNewStandardGroupResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupNewStandardGroupResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupResponse(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupNewStandardGroupResponse):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupNewStandardGroupResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNewControlledGroupRequest:
	def __init__(self, client: OlvidClient = None, name: str = "", description: str = "", admin_contact_ids: list[int] = (), contact_ids: list[int] = ()):
		self._client: OlvidClient = client
		self.name: str = name
		self.description: str = description
		self.admin_contact_ids: list[int] = admin_contact_ids
		self.contact_ids: list[int] = contact_ids

	def _update_content(self, group_new_controlled_group_request: GroupNewControlledGroupRequest) -> None:
		self.name: str = group_new_controlled_group_request.name
		self.description: str = group_new_controlled_group_request.description
		self.admin_contact_ids: list[int] = group_new_controlled_group_request.admin_contact_ids
		self.contact_ids: list[int] = group_new_controlled_group_request.contact_ids

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewControlledGroupRequest":
		return GroupNewControlledGroupRequest(client=self._client, name=self.name, description=self.description, admin_contact_ids=[e for e in self.admin_contact_ids], contact_ids=[e for e in self.contact_ids])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupRequest, client: OlvidClient = None) -> "GroupNewControlledGroupRequest":
		return GroupNewControlledGroupRequest(client, name=native_message.name, description=native_message.description, admin_contact_ids=native_message.admin_contact_ids, contact_ids=native_message.contact_ids)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupRequest], client: OlvidClient = None) -> list["GroupNewControlledGroupRequest"]:
		return [GroupNewControlledGroupRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupRequest], client: OlvidClient = None) -> "GroupNewControlledGroupRequest":
		native_message = await promise
		return GroupNewControlledGroupRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupNewControlledGroupRequest"]):
		if messages is None:
			return []
		return [GroupNewControlledGroupRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupNewControlledGroupRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupRequest(name=message.name if message.name else None, description=message.description if message.description else None, admin_contact_ids=message.admin_contact_ids if message.admin_contact_ids else None, contact_ids=message.contact_ids if message.contact_ids else None)

	def __str__(self):
		s: str = ''
		if self.name:
			s += f'name: {self.name}, '
		if self.description:
			s += f'description: {self.description}, '
		if self.admin_contact_ids:
			s += f'admin_contact_ids: {[str(el) for el in self.admin_contact_ids]}, '
		if self.contact_ids:
			s += f'contact_ids: {[str(el) for el in self.contact_ids]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupNewControlledGroupRequest):
			return False
		return self.name == other.name and self.description == other.description and self.admin_contact_ids == other.admin_contact_ids and self.contact_ids == other.contact_ids

	def __bool__(self):
		return self.name != "" or self.description != "" or bool(self.admin_contact_ids) or bool(self.contact_ids)

	def __hash__(self):
		return hash((self.name, self.description, tuple(self.admin_contact_ids), tuple(self.contact_ids)))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupNewControlledGroupRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.name == "" or self.name == expected.name, "Invalid value: name: " + str(expected.name) + " != " + str(self.name)
		assert expected.description == "" or self.description == expected.description, "Invalid value: description: " + str(expected.description) + " != " + str(self.description)
		pass  # print("Warning: test_assertion: skipped a list field admin_contact_ids")
		pass  # print("Warning: test_assertion: skipped a list field contact_ids")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNewControlledGroupResponse:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_new_controlled_group_response: GroupNewControlledGroupResponse) -> None:
		self.group: Group = group_new_controlled_group_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewControlledGroupResponse":
		return GroupNewControlledGroupResponse(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupResponse, client: OlvidClient = None) -> "GroupNewControlledGroupResponse":
		return GroupNewControlledGroupResponse(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupResponse], client: OlvidClient = None) -> list["GroupNewControlledGroupResponse"]:
		return [GroupNewControlledGroupResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupResponse], client: OlvidClient = None) -> "GroupNewControlledGroupResponse":
		native_message = await promise
		return GroupNewControlledGroupResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupNewControlledGroupResponse"]):
		if messages is None:
			return []
		return [GroupNewControlledGroupResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupNewControlledGroupResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupResponse(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupNewControlledGroupResponse):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupNewControlledGroupResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNewReadOnlyGroupRequest:
	def __init__(self, client: OlvidClient = None, name: str = "", description: str = "", admin_contact_ids: list[int] = (), contact_ids: list[int] = ()):
		self._client: OlvidClient = client
		self.name: str = name
		self.description: str = description
		self.admin_contact_ids: list[int] = admin_contact_ids
		self.contact_ids: list[int] = contact_ids

	def _update_content(self, group_new_read_only_group_request: GroupNewReadOnlyGroupRequest) -> None:
		self.name: str = group_new_read_only_group_request.name
		self.description: str = group_new_read_only_group_request.description
		self.admin_contact_ids: list[int] = group_new_read_only_group_request.admin_contact_ids
		self.contact_ids: list[int] = group_new_read_only_group_request.contact_ids

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewReadOnlyGroupRequest":
		return GroupNewReadOnlyGroupRequest(client=self._client, name=self.name, description=self.description, admin_contact_ids=[e for e in self.admin_contact_ids], contact_ids=[e for e in self.contact_ids])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupRequest, client: OlvidClient = None) -> "GroupNewReadOnlyGroupRequest":
		return GroupNewReadOnlyGroupRequest(client, name=native_message.name, description=native_message.description, admin_contact_ids=native_message.admin_contact_ids, contact_ids=native_message.contact_ids)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupRequest], client: OlvidClient = None) -> list["GroupNewReadOnlyGroupRequest"]:
		return [GroupNewReadOnlyGroupRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupRequest], client: OlvidClient = None) -> "GroupNewReadOnlyGroupRequest":
		native_message = await promise
		return GroupNewReadOnlyGroupRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupNewReadOnlyGroupRequest"]):
		if messages is None:
			return []
		return [GroupNewReadOnlyGroupRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupNewReadOnlyGroupRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupRequest(name=message.name if message.name else None, description=message.description if message.description else None, admin_contact_ids=message.admin_contact_ids if message.admin_contact_ids else None, contact_ids=message.contact_ids if message.contact_ids else None)

	def __str__(self):
		s: str = ''
		if self.name:
			s += f'name: {self.name}, '
		if self.description:
			s += f'description: {self.description}, '
		if self.admin_contact_ids:
			s += f'admin_contact_ids: {[str(el) for el in self.admin_contact_ids]}, '
		if self.contact_ids:
			s += f'contact_ids: {[str(el) for el in self.contact_ids]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupNewReadOnlyGroupRequest):
			return False
		return self.name == other.name and self.description == other.description and self.admin_contact_ids == other.admin_contact_ids and self.contact_ids == other.contact_ids

	def __bool__(self):
		return self.name != "" or self.description != "" or bool(self.admin_contact_ids) or bool(self.contact_ids)

	def __hash__(self):
		return hash((self.name, self.description, tuple(self.admin_contact_ids), tuple(self.contact_ids)))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupNewReadOnlyGroupRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.name == "" or self.name == expected.name, "Invalid value: name: " + str(expected.name) + " != " + str(self.name)
		assert expected.description == "" or self.description == expected.description, "Invalid value: description: " + str(expected.description) + " != " + str(self.description)
		pass  # print("Warning: test_assertion: skipped a list field admin_contact_ids")
		pass  # print("Warning: test_assertion: skipped a list field contact_ids")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNewReadOnlyGroupResponse:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_new_read_only_group_response: GroupNewReadOnlyGroupResponse) -> None:
		self.group: Group = group_new_read_only_group_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewReadOnlyGroupResponse":
		return GroupNewReadOnlyGroupResponse(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupResponse, client: OlvidClient = None) -> "GroupNewReadOnlyGroupResponse":
		return GroupNewReadOnlyGroupResponse(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupResponse], client: OlvidClient = None) -> list["GroupNewReadOnlyGroupResponse"]:
		return [GroupNewReadOnlyGroupResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupResponse], client: OlvidClient = None) -> "GroupNewReadOnlyGroupResponse":
		native_message = await promise
		return GroupNewReadOnlyGroupResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupNewReadOnlyGroupResponse"]):
		if messages is None:
			return []
		return [GroupNewReadOnlyGroupResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupNewReadOnlyGroupResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupResponse(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupNewReadOnlyGroupResponse):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupNewReadOnlyGroupResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNewAdvancedGroupRequest:
	def __init__(self, client: OlvidClient = None, name: str = "", description: str = "", advanced_configuration: "Group.AdvancedConfiguration" = None, members: "list[GroupMember]" = None):
		self._client: OlvidClient = client
		self.name: str = name
		self.description: str = description
		self.advanced_configuration: Group.AdvancedConfiguration = advanced_configuration
		self.members: list[GroupMember] = members

	def _update_content(self, group_new_advanced_group_request: GroupNewAdvancedGroupRequest) -> None:
		self.name: str = group_new_advanced_group_request.name
		self.description: str = group_new_advanced_group_request.description
		self.advanced_configuration: Group.AdvancedConfiguration = group_new_advanced_group_request.advanced_configuration
		self.members: list[GroupMember] = group_new_advanced_group_request.members

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewAdvancedGroupRequest":
		return GroupNewAdvancedGroupRequest(client=self._client, name=self.name, description=self.description, advanced_configuration=self.advanced_configuration._clone(), members=[e._clone() for e in self.members])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupRequest, client: OlvidClient = None) -> "GroupNewAdvancedGroupRequest":
		return GroupNewAdvancedGroupRequest(client, name=native_message.name, description=native_message.description, advanced_configuration=Group.AdvancedConfiguration._from_native(native_message.advanced_configuration, client=client), members=GroupMember._from_native_list(native_message.members, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupRequest], client: OlvidClient = None) -> list["GroupNewAdvancedGroupRequest"]:
		return [GroupNewAdvancedGroupRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupRequest], client: OlvidClient = None) -> "GroupNewAdvancedGroupRequest":
		native_message = await promise
		return GroupNewAdvancedGroupRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupNewAdvancedGroupRequest"]):
		if messages is None:
			return []
		return [GroupNewAdvancedGroupRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupNewAdvancedGroupRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupRequest(name=message.name if message.name else None, description=message.description if message.description else None, advanced_configuration=Group.AdvancedConfiguration._to_native(message.advanced_configuration if message.advanced_configuration else None), members=GroupMember._to_native_list(message.members if message.members else None))

	def __str__(self):
		s: str = ''
		if self.name:
			s += f'name: {self.name}, '
		if self.description:
			s += f'description: {self.description}, '
		if self.advanced_configuration:
			s += f'advanced_configuration: ({self.advanced_configuration}), '
		if self.members:
			s += f'members: {[str(el) for el in self.members]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupNewAdvancedGroupRequest):
			return False
		return self.name == other.name and self.description == other.description and self.advanced_configuration == other.advanced_configuration and self.members == other.members

	def __bool__(self):
		return self.name != "" or self.description != "" or bool(self.advanced_configuration) or bool(self.members)

	def __hash__(self):
		return hash((self.name, self.description, self.advanced_configuration, tuple(self.members)))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupNewAdvancedGroupRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.name == "" or self.name == expected.name, "Invalid value: name: " + str(expected.name) + " != " + str(self.name)
		assert expected.description == "" or self.description == expected.description, "Invalid value: description: " + str(expected.description) + " != " + str(self.description)
		try:
			assert expected.advanced_configuration is None or self.advanced_configuration._test_assertion(expected.advanced_configuration)
		except AssertionError as e:
			raise AssertionError("advanced_configuration: " + str(e))
		pass  # print("Warning: test_assertion: skipped a list field members")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNewAdvancedGroupResponse:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_new_advanced_group_response: GroupNewAdvancedGroupResponse) -> None:
		self.group: Group = group_new_advanced_group_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewAdvancedGroupResponse":
		return GroupNewAdvancedGroupResponse(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupResponse, client: OlvidClient = None) -> "GroupNewAdvancedGroupResponse":
		return GroupNewAdvancedGroupResponse(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupResponse], client: OlvidClient = None) -> list["GroupNewAdvancedGroupResponse"]:
		return [GroupNewAdvancedGroupResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupResponse], client: OlvidClient = None) -> "GroupNewAdvancedGroupResponse":
		native_message = await promise
		return GroupNewAdvancedGroupResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupNewAdvancedGroupResponse"]):
		if messages is None:
			return []
		return [GroupNewAdvancedGroupResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupNewAdvancedGroupResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupResponse(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupNewAdvancedGroupResponse):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupNewAdvancedGroupResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupDisbandRequest:
	def __init__(self, client: OlvidClient = None, group_id: int = 0):
		self._client: OlvidClient = client
		self.group_id: int = group_id

	def _update_content(self, group_disband_request: GroupDisbandRequest) -> None:
		self.group_id: int = group_disband_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupDisbandRequest":
		return GroupDisbandRequest(client=self._client, group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupDisbandRequest, client: OlvidClient = None) -> "GroupDisbandRequest":
		return GroupDisbandRequest(client, group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupDisbandRequest], client: OlvidClient = None) -> list["GroupDisbandRequest"]:
		return [GroupDisbandRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupDisbandRequest], client: OlvidClient = None) -> "GroupDisbandRequest":
		native_message = await promise
		return GroupDisbandRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupDisbandRequest"]):
		if messages is None:
			return []
		return [GroupDisbandRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupDisbandRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupDisbandRequest(group_id=message.group_id if message.group_id else None)

	def __str__(self):
		s: str = ''
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupDisbandRequest):
			return False
		return self.group_id == other.group_id

	def __bool__(self):
		return self.group_id != 0

	def __hash__(self):
		return hash(self.group_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupDisbandRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.group_id == 0 or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupDisbandResponse:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_disband_response: GroupDisbandResponse) -> None:
		self.group: Group = group_disband_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupDisbandResponse":
		return GroupDisbandResponse(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupDisbandResponse, client: OlvidClient = None) -> "GroupDisbandResponse":
		return GroupDisbandResponse(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupDisbandResponse], client: OlvidClient = None) -> list["GroupDisbandResponse"]:
		return [GroupDisbandResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupDisbandResponse], client: OlvidClient = None) -> "GroupDisbandResponse":
		native_message = await promise
		return GroupDisbandResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupDisbandResponse"]):
		if messages is None:
			return []
		return [GroupDisbandResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupDisbandResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupDisbandResponse(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupDisbandResponse):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupDisbandResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupLeaveRequest:
	def __init__(self, client: OlvidClient = None, group_id: int = 0):
		self._client: OlvidClient = client
		self.group_id: int = group_id

	def _update_content(self, group_leave_request: GroupLeaveRequest) -> None:
		self.group_id: int = group_leave_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupLeaveRequest":
		return GroupLeaveRequest(client=self._client, group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupLeaveRequest, client: OlvidClient = None) -> "GroupLeaveRequest":
		return GroupLeaveRequest(client, group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupLeaveRequest], client: OlvidClient = None) -> list["GroupLeaveRequest"]:
		return [GroupLeaveRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupLeaveRequest], client: OlvidClient = None) -> "GroupLeaveRequest":
		native_message = await promise
		return GroupLeaveRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupLeaveRequest"]):
		if messages is None:
			return []
		return [GroupLeaveRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupLeaveRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupLeaveRequest(group_id=message.group_id if message.group_id else None)

	def __str__(self):
		s: str = ''
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupLeaveRequest):
			return False
		return self.group_id == other.group_id

	def __bool__(self):
		return self.group_id != 0

	def __hash__(self):
		return hash(self.group_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupLeaveRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.group_id == 0 or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupLeaveResponse:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_leave_response: GroupLeaveResponse) -> None:
		self.group: Group = group_leave_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupLeaveResponse":
		return GroupLeaveResponse(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupLeaveResponse, client: OlvidClient = None) -> "GroupLeaveResponse":
		return GroupLeaveResponse(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupLeaveResponse], client: OlvidClient = None) -> list["GroupLeaveResponse"]:
		return [GroupLeaveResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupLeaveResponse], client: OlvidClient = None) -> "GroupLeaveResponse":
		native_message = await promise
		return GroupLeaveResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupLeaveResponse"]):
		if messages is None:
			return []
		return [GroupLeaveResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupLeaveResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupLeaveResponse(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupLeaveResponse):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupLeaveResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupUpdateRequest:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_update_request: GroupUpdateRequest) -> None:
		self.group: Group = group_update_request.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupUpdateRequest":
		return GroupUpdateRequest(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupUpdateRequest, client: OlvidClient = None) -> "GroupUpdateRequest":
		return GroupUpdateRequest(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupUpdateRequest], client: OlvidClient = None) -> list["GroupUpdateRequest"]:
		return [GroupUpdateRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupUpdateRequest], client: OlvidClient = None) -> "GroupUpdateRequest":
		native_message = await promise
		return GroupUpdateRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupUpdateRequest"]):
		if messages is None:
			return []
		return [GroupUpdateRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupUpdateRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupUpdateRequest(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupUpdateRequest):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupUpdateRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupUpdateResponse:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_update_response: GroupUpdateResponse) -> None:
		self.group: Group = group_update_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupUpdateResponse":
		return GroupUpdateResponse(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupUpdateResponse, client: OlvidClient = None) -> "GroupUpdateResponse":
		return GroupUpdateResponse(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupUpdateResponse], client: OlvidClient = None) -> list["GroupUpdateResponse"]:
		return [GroupUpdateResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupUpdateResponse], client: OlvidClient = None) -> "GroupUpdateResponse":
		native_message = await promise
		return GroupUpdateResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupUpdateResponse"]):
		if messages is None:
			return []
		return [GroupUpdateResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupUpdateResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupUpdateResponse(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupUpdateResponse):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupUpdateResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupUnsetPhotoRequest:
	def __init__(self, client: OlvidClient = None, group_id: int = 0):
		self._client: OlvidClient = client
		self.group_id: int = group_id

	def _update_content(self, group_unset_photo_request: GroupUnsetPhotoRequest) -> None:
		self.group_id: int = group_unset_photo_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupUnsetPhotoRequest":
		return GroupUnsetPhotoRequest(client=self._client, group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoRequest, client: OlvidClient = None) -> "GroupUnsetPhotoRequest":
		return GroupUnsetPhotoRequest(client, group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoRequest], client: OlvidClient = None) -> list["GroupUnsetPhotoRequest"]:
		return [GroupUnsetPhotoRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoRequest], client: OlvidClient = None) -> "GroupUnsetPhotoRequest":
		native_message = await promise
		return GroupUnsetPhotoRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupUnsetPhotoRequest"]):
		if messages is None:
			return []
		return [GroupUnsetPhotoRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupUnsetPhotoRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoRequest(group_id=message.group_id if message.group_id else None)

	def __str__(self):
		s: str = ''
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupUnsetPhotoRequest):
			return False
		return self.group_id == other.group_id

	def __bool__(self):
		return self.group_id != 0

	def __hash__(self):
		return hash(self.group_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupUnsetPhotoRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.group_id == 0 or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupUnsetPhotoResponse:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_unset_photo_response: GroupUnsetPhotoResponse) -> None:
		self.group: Group = group_unset_photo_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupUnsetPhotoResponse":
		return GroupUnsetPhotoResponse(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoResponse, client: OlvidClient = None) -> "GroupUnsetPhotoResponse":
		return GroupUnsetPhotoResponse(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoResponse], client: OlvidClient = None) -> list["GroupUnsetPhotoResponse"]:
		return [GroupUnsetPhotoResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoResponse], client: OlvidClient = None) -> "GroupUnsetPhotoResponse":
		native_message = await promise
		return GroupUnsetPhotoResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupUnsetPhotoResponse"]):
		if messages is None:
			return []
		return [GroupUnsetPhotoResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupUnsetPhotoResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoResponse(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupUnsetPhotoResponse):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupUnsetPhotoResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupSetPhotoRequestMetadata:
	def __init__(self, client: OlvidClient = None, group_id: int = 0, filename: str = "", file_size: int = 0):
		self._client: OlvidClient = client
		self.group_id: int = group_id
		self.filename: str = filename
		self.file_size: int = file_size

	def _update_content(self, group_set_photo_request_metadata: GroupSetPhotoRequestMetadata) -> None:
		self.group_id: int = group_set_photo_request_metadata.group_id
		self.filename: str = group_set_photo_request_metadata.filename
		self.file_size: int = group_set_photo_request_metadata.file_size

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupSetPhotoRequestMetadata":
		return GroupSetPhotoRequestMetadata(client=self._client, group_id=self.group_id, filename=self.filename, file_size=self.file_size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequestMetadata, client: OlvidClient = None) -> "GroupSetPhotoRequestMetadata":
		return GroupSetPhotoRequestMetadata(client, group_id=native_message.group_id, filename=native_message.filename, file_size=native_message.file_size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequestMetadata], client: OlvidClient = None) -> list["GroupSetPhotoRequestMetadata"]:
		return [GroupSetPhotoRequestMetadata._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequestMetadata], client: OlvidClient = None) -> "GroupSetPhotoRequestMetadata":
		native_message = await promise
		return GroupSetPhotoRequestMetadata._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupSetPhotoRequestMetadata"]):
		if messages is None:
			return []
		return [GroupSetPhotoRequestMetadata._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupSetPhotoRequestMetadata"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequestMetadata(group_id=message.group_id if message.group_id else None, filename=message.filename if message.filename else None, file_size=message.file_size if message.file_size else None)

	def __str__(self):
		s: str = ''
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		if self.filename:
			s += f'filename: {self.filename}, '
		if self.file_size:
			s += f'file_size: {self.file_size}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupSetPhotoRequestMetadata):
			return False
		return self.group_id == other.group_id and self.filename == other.filename and self.file_size == other.file_size

	def __bool__(self):
		return self.group_id != 0 or self.filename != "" or self.file_size != 0

	def __hash__(self):
		return hash((self.group_id, self.filename, self.file_size))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupSetPhotoRequestMetadata):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.group_id == 0 or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		assert expected.filename == "" or self.filename == expected.filename, "Invalid value: filename: " + str(expected.filename) + " != " + str(self.filename)
		assert expected.file_size == 0 or self.file_size == expected.file_size, "Invalid value: file_size: " + str(expected.file_size) + " != " + str(self.file_size)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupSetPhotoRequest:
	def __init__(self, client: OlvidClient = None, metadata: "GroupSetPhotoRequestMetadata" = None, payload: bytes = None):
		self._client: OlvidClient = client
		self.metadata: GroupSetPhotoRequestMetadata = metadata
		self.payload: bytes = payload

	def _update_content(self, group_set_photo_request: GroupSetPhotoRequest) -> None:
		self.metadata: GroupSetPhotoRequestMetadata = group_set_photo_request.metadata
		self.payload: bytes = group_set_photo_request.payload

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupSetPhotoRequest":
		return GroupSetPhotoRequest(client=self._client, metadata=self.metadata._clone(), payload=self.payload)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequest, client: OlvidClient = None) -> "GroupSetPhotoRequest":
		return GroupSetPhotoRequest(client, metadata=GroupSetPhotoRequestMetadata._from_native(native_message.metadata, client=client), payload=native_message.payload)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequest], client: OlvidClient = None) -> list["GroupSetPhotoRequest"]:
		return [GroupSetPhotoRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequest], client: OlvidClient = None) -> "GroupSetPhotoRequest":
		native_message = await promise
		return GroupSetPhotoRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupSetPhotoRequest"]):
		if messages is None:
			return []
		return [GroupSetPhotoRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupSetPhotoRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequest(metadata=GroupSetPhotoRequestMetadata._to_native(message.metadata if message.metadata else None), payload=message.payload if message.payload else None)

	def __str__(self):
		s: str = ''
		if self.metadata:
			s += f'metadata: ({self.metadata}), '
		if self.payload:
			s += f'payload: {self.payload}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupSetPhotoRequest):
			return False
		return self.metadata == other.metadata and self.payload == other.payload

	def __bool__(self):
		return bool(self.metadata) or self.payload is not None

	def __hash__(self):
		return hash((self.metadata, self.payload))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupSetPhotoRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.metadata is None or self.metadata._test_assertion(expected.metadata)
		except AssertionError as e:
			raise AssertionError("metadata: " + str(e))
		assert expected.payload is None or self.payload == expected.payload, "Invalid value: payload: " + str(expected.payload) + " != " + str(self.payload)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupSetPhotoResponse:
	def __init__(self, client: OlvidClient = None, group: "Group" = None):
		self._client: OlvidClient = client
		self.group: Group = group

	def _update_content(self, group_set_photo_response: GroupSetPhotoResponse) -> None:
		self.group: Group = group_set_photo_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupSetPhotoResponse":
		return GroupSetPhotoResponse(client=self._client, group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoResponse, client: OlvidClient = None) -> "GroupSetPhotoResponse":
		return GroupSetPhotoResponse(client, group=Group._from_native(native_message.group, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoResponse], client: OlvidClient = None) -> list["GroupSetPhotoResponse"]:
		return [GroupSetPhotoResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoResponse], client: OlvidClient = None) -> "GroupSetPhotoResponse":
		native_message = await promise
		return GroupSetPhotoResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupSetPhotoResponse"]):
		if messages is None:
			return []
		return [GroupSetPhotoResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupSetPhotoResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoResponse(group=Group._to_native(message.group if message.group else None))

	def __str__(self):
		s: str = ''
		if self.group:
			s += f'group: ({self.group}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupSetPhotoResponse):
			return False
		return self.group == other.group

	def __bool__(self):
		return bool(self.group)

	def __hash__(self):
		return hash(self.group)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupSetPhotoResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.group is None or self.group._test_assertion(expected.group)
		except AssertionError as e:
			raise AssertionError("group: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityGetRequest:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, identity_get_request: IdentityGetRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityGetRequest":
		return IdentityGetRequest(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityGetRequest, client: OlvidClient = None) -> "IdentityGetRequest":
		return IdentityGetRequest(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityGetRequest], client: OlvidClient = None) -> list["IdentityGetRequest"]:
		return [IdentityGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityGetRequest], client: OlvidClient = None) -> "IdentityGetRequest":
		native_message = await promise
		return IdentityGetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityGetRequest"]):
		if messages is None:
			return []
		return [IdentityGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityGetRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityGetRequest):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityGetResponse:
	def __init__(self, client: OlvidClient = None, identity: "Identity" = None):
		self._client: OlvidClient = client
		self.identity: Identity = identity

	def _update_content(self, identity_get_response: IdentityGetResponse) -> None:
		self.identity: Identity = identity_get_response.identity

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityGetResponse":
		return IdentityGetResponse(client=self._client, identity=self.identity._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityGetResponse, client: OlvidClient = None) -> "IdentityGetResponse":
		return IdentityGetResponse(client, identity=Identity._from_native(native_message.identity, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityGetResponse], client: OlvidClient = None) -> list["IdentityGetResponse"]:
		return [IdentityGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityGetResponse], client: OlvidClient = None) -> "IdentityGetResponse":
		native_message = await promise
		return IdentityGetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityGetResponse"]):
		if messages is None:
			return []
		return [IdentityGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityGetResponse(identity=Identity._to_native(message.identity if message.identity else None))

	def __str__(self):
		s: str = ''
		if self.identity:
			s += f'identity: ({self.identity}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityGetResponse):
			return False
		return self.identity == other.identity

	def __bool__(self):
		return bool(self.identity)

	def __hash__(self):
		return hash(self.identity)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity is None or self.identity._test_assertion(expected.identity)
		except AssertionError as e:
			raise AssertionError("identity: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityUpdateDetailsRequest:
	def __init__(self, client: OlvidClient = None, new_details: "IdentityDetails" = None):
		self._client: OlvidClient = client
		self.new_details: IdentityDetails = new_details

	def _update_content(self, identity_update_details_request: IdentityUpdateDetailsRequest) -> None:
		self.new_details: IdentityDetails = identity_update_details_request.new_details

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityUpdateDetailsRequest":
		return IdentityUpdateDetailsRequest(client=self._client, new_details=self.new_details._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsRequest, client: OlvidClient = None) -> "IdentityUpdateDetailsRequest":
		return IdentityUpdateDetailsRequest(client, new_details=IdentityDetails._from_native(native_message.new_details, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsRequest], client: OlvidClient = None) -> list["IdentityUpdateDetailsRequest"]:
		return [IdentityUpdateDetailsRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsRequest], client: OlvidClient = None) -> "IdentityUpdateDetailsRequest":
		native_message = await promise
		return IdentityUpdateDetailsRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityUpdateDetailsRequest"]):
		if messages is None:
			return []
		return [IdentityUpdateDetailsRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityUpdateDetailsRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsRequest(new_details=IdentityDetails._to_native(message.new_details if message.new_details else None))

	def __str__(self):
		s: str = ''
		if self.new_details:
			s += f'new_details: ({self.new_details}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityUpdateDetailsRequest):
			return False
		return self.new_details == other.new_details

	def __bool__(self):
		return bool(self.new_details)

	def __hash__(self):
		return hash(self.new_details)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityUpdateDetailsRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.new_details is None or self.new_details._test_assertion(expected.new_details)
		except AssertionError as e:
			raise AssertionError("new_details: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityUpdateDetailsResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, identity_update_details_response: IdentityUpdateDetailsResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityUpdateDetailsResponse":
		return IdentityUpdateDetailsResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsResponse, client: OlvidClient = None) -> "IdentityUpdateDetailsResponse":
		return IdentityUpdateDetailsResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsResponse], client: OlvidClient = None) -> list["IdentityUpdateDetailsResponse"]:
		return [IdentityUpdateDetailsResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsResponse], client: OlvidClient = None) -> "IdentityUpdateDetailsResponse":
		native_message = await promise
		return IdentityUpdateDetailsResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityUpdateDetailsResponse"]):
		if messages is None:
			return []
		return [IdentityUpdateDetailsResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityUpdateDetailsResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityUpdateDetailsResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityUpdateDetailsResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityRemovePhotoRequest:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, identity_remove_photo_request: IdentityRemovePhotoRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityRemovePhotoRequest":
		return IdentityRemovePhotoRequest(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoRequest, client: OlvidClient = None) -> "IdentityRemovePhotoRequest":
		return IdentityRemovePhotoRequest(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoRequest], client: OlvidClient = None) -> list["IdentityRemovePhotoRequest"]:
		return [IdentityRemovePhotoRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoRequest], client: OlvidClient = None) -> "IdentityRemovePhotoRequest":
		native_message = await promise
		return IdentityRemovePhotoRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityRemovePhotoRequest"]):
		if messages is None:
			return []
		return [IdentityRemovePhotoRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityRemovePhotoRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityRemovePhotoRequest):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityRemovePhotoRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityRemovePhotoResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, identity_remove_photo_response: IdentityRemovePhotoResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityRemovePhotoResponse":
		return IdentityRemovePhotoResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoResponse, client: OlvidClient = None) -> "IdentityRemovePhotoResponse":
		return IdentityRemovePhotoResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoResponse], client: OlvidClient = None) -> list["IdentityRemovePhotoResponse"]:
		return [IdentityRemovePhotoResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoResponse], client: OlvidClient = None) -> "IdentityRemovePhotoResponse":
		native_message = await promise
		return IdentityRemovePhotoResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityRemovePhotoResponse"]):
		if messages is None:
			return []
		return [IdentityRemovePhotoResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityRemovePhotoResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityRemovePhotoResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityRemovePhotoResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentitySetPhotoRequestMetadata:
	def __init__(self, client: OlvidClient = None, filename: str = "", file_size: int = 0):
		self._client: OlvidClient = client
		self.filename: str = filename
		self.file_size: int = file_size

	def _update_content(self, identity_set_photo_request_metadata: IdentitySetPhotoRequestMetadata) -> None:
		self.filename: str = identity_set_photo_request_metadata.filename
		self.file_size: int = identity_set_photo_request_metadata.file_size

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetPhotoRequestMetadata":
		return IdentitySetPhotoRequestMetadata(client=self._client, filename=self.filename, file_size=self.file_size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequestMetadata, client: OlvidClient = None) -> "IdentitySetPhotoRequestMetadata":
		return IdentitySetPhotoRequestMetadata(client, filename=native_message.filename, file_size=native_message.file_size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequestMetadata], client: OlvidClient = None) -> list["IdentitySetPhotoRequestMetadata"]:
		return [IdentitySetPhotoRequestMetadata._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequestMetadata], client: OlvidClient = None) -> "IdentitySetPhotoRequestMetadata":
		native_message = await promise
		return IdentitySetPhotoRequestMetadata._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentitySetPhotoRequestMetadata"]):
		if messages is None:
			return []
		return [IdentitySetPhotoRequestMetadata._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentitySetPhotoRequestMetadata"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequestMetadata(filename=message.filename if message.filename else None, file_size=message.file_size if message.file_size else None)

	def __str__(self):
		s: str = ''
		if self.filename:
			s += f'filename: {self.filename}, '
		if self.file_size:
			s += f'file_size: {self.file_size}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentitySetPhotoRequestMetadata):
			return False
		return self.filename == other.filename and self.file_size == other.file_size

	def __bool__(self):
		return self.filename != "" or self.file_size != 0

	def __hash__(self):
		return hash((self.filename, self.file_size))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentitySetPhotoRequestMetadata):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.filename == "" or self.filename == expected.filename, "Invalid value: filename: " + str(expected.filename) + " != " + str(self.filename)
		assert expected.file_size == 0 or self.file_size == expected.file_size, "Invalid value: file_size: " + str(expected.file_size) + " != " + str(self.file_size)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentitySetPhotoRequest:
	def __init__(self, client: OlvidClient = None, metadata: "IdentitySetPhotoRequestMetadata" = None, payload: bytes = None):
		self._client: OlvidClient = client
		self.metadata: IdentitySetPhotoRequestMetadata = metadata
		self.payload: bytes = payload

	def _update_content(self, identity_set_photo_request: IdentitySetPhotoRequest) -> None:
		self.metadata: IdentitySetPhotoRequestMetadata = identity_set_photo_request.metadata
		self.payload: bytes = identity_set_photo_request.payload

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetPhotoRequest":
		return IdentitySetPhotoRequest(client=self._client, metadata=self.metadata._clone(), payload=self.payload)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequest, client: OlvidClient = None) -> "IdentitySetPhotoRequest":
		return IdentitySetPhotoRequest(client, metadata=IdentitySetPhotoRequestMetadata._from_native(native_message.metadata, client=client), payload=native_message.payload)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequest], client: OlvidClient = None) -> list["IdentitySetPhotoRequest"]:
		return [IdentitySetPhotoRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequest], client: OlvidClient = None) -> "IdentitySetPhotoRequest":
		native_message = await promise
		return IdentitySetPhotoRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentitySetPhotoRequest"]):
		if messages is None:
			return []
		return [IdentitySetPhotoRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentitySetPhotoRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequest(metadata=IdentitySetPhotoRequestMetadata._to_native(message.metadata if message.metadata else None), payload=message.payload if message.payload else None)

	def __str__(self):
		s: str = ''
		if self.metadata:
			s += f'metadata: ({self.metadata}), '
		if self.payload:
			s += f'payload: {self.payload}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentitySetPhotoRequest):
			return False
		return self.metadata == other.metadata and self.payload == other.payload

	def __bool__(self):
		return bool(self.metadata) or self.payload is not None

	def __hash__(self):
		return hash((self.metadata, self.payload))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentitySetPhotoRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.metadata is None or self.metadata._test_assertion(expected.metadata)
		except AssertionError as e:
			raise AssertionError("metadata: " + str(e))
		assert expected.payload is None or self.payload == expected.payload, "Invalid value: payload: " + str(expected.payload) + " != " + str(self.payload)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentitySetPhotoResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, identity_set_photo_response: IdentitySetPhotoResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetPhotoResponse":
		return IdentitySetPhotoResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoResponse, client: OlvidClient = None) -> "IdentitySetPhotoResponse":
		return IdentitySetPhotoResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoResponse], client: OlvidClient = None) -> list["IdentitySetPhotoResponse"]:
		return [IdentitySetPhotoResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoResponse], client: OlvidClient = None) -> "IdentitySetPhotoResponse":
		native_message = await promise
		return IdentitySetPhotoResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentitySetPhotoResponse"]):
		if messages is None:
			return []
		return [IdentitySetPhotoResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentitySetPhotoResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentitySetPhotoResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentitySetPhotoResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityKeycloakBindRequest:
	def __init__(self, client: OlvidClient = None, configuration_link: str = ""):
		self._client: OlvidClient = client
		self.configuration_link: str = configuration_link

	def _update_content(self, identity_keycloak_bind_request: IdentityKeycloakBindRequest) -> None:
		self.configuration_link: str = identity_keycloak_bind_request.configuration_link

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityKeycloakBindRequest":
		return IdentityKeycloakBindRequest(client=self._client, configuration_link=self.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakBindRequest, client: OlvidClient = None) -> "IdentityKeycloakBindRequest":
		return IdentityKeycloakBindRequest(client, configuration_link=native_message.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakBindRequest], client: OlvidClient = None) -> list["IdentityKeycloakBindRequest"]:
		return [IdentityKeycloakBindRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakBindRequest], client: OlvidClient = None) -> "IdentityKeycloakBindRequest":
		native_message = await promise
		return IdentityKeycloakBindRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityKeycloakBindRequest"]):
		if messages is None:
			return []
		return [IdentityKeycloakBindRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityKeycloakBindRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakBindRequest(configuration_link=message.configuration_link if message.configuration_link else None)

	def __str__(self):
		s: str = ''
		if self.configuration_link:
			s += f'configuration_link: {self.configuration_link}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityKeycloakBindRequest):
			return False
		return self.configuration_link == other.configuration_link

	def __bool__(self):
		return self.configuration_link != ""

	def __hash__(self):
		return hash(self.configuration_link)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityKeycloakBindRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.configuration_link == "" or self.configuration_link == expected.configuration_link, "Invalid value: configuration_link: " + str(expected.configuration_link) + " != " + str(self.configuration_link)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityKeycloakBindResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, identity_keycloak_bind_response: IdentityKeycloakBindResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityKeycloakBindResponse":
		return IdentityKeycloakBindResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakBindResponse, client: OlvidClient = None) -> "IdentityKeycloakBindResponse":
		return IdentityKeycloakBindResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakBindResponse], client: OlvidClient = None) -> list["IdentityKeycloakBindResponse"]:
		return [IdentityKeycloakBindResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakBindResponse], client: OlvidClient = None) -> "IdentityKeycloakBindResponse":
		native_message = await promise
		return IdentityKeycloakBindResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityKeycloakBindResponse"]):
		if messages is None:
			return []
		return [IdentityKeycloakBindResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityKeycloakBindResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakBindResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityKeycloakBindResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityKeycloakBindResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityKeycloakUnbindRequest:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, identity_keycloak_unbind_request: IdentityKeycloakUnbindRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityKeycloakUnbindRequest":
		return IdentityKeycloakUnbindRequest(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakUnbindRequest, client: OlvidClient = None) -> "IdentityKeycloakUnbindRequest":
		return IdentityKeycloakUnbindRequest(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakUnbindRequest], client: OlvidClient = None) -> list["IdentityKeycloakUnbindRequest"]:
		return [IdentityKeycloakUnbindRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakUnbindRequest], client: OlvidClient = None) -> "IdentityKeycloakUnbindRequest":
		native_message = await promise
		return IdentityKeycloakUnbindRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityKeycloakUnbindRequest"]):
		if messages is None:
			return []
		return [IdentityKeycloakUnbindRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityKeycloakUnbindRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakUnbindRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityKeycloakUnbindRequest):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityKeycloakUnbindRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityKeycloakUnbindResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, identity_keycloak_unbind_response: IdentityKeycloakUnbindResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityKeycloakUnbindResponse":
		return IdentityKeycloakUnbindResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakUnbindResponse, client: OlvidClient = None) -> "IdentityKeycloakUnbindResponse":
		return IdentityKeycloakUnbindResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakUnbindResponse], client: OlvidClient = None) -> list["IdentityKeycloakUnbindResponse"]:
		return [IdentityKeycloakUnbindResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakUnbindResponse], client: OlvidClient = None) -> "IdentityKeycloakUnbindResponse":
		native_message = await promise
		return IdentityKeycloakUnbindResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityKeycloakUnbindResponse"]):
		if messages is None:
			return []
		return [IdentityKeycloakUnbindResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityKeycloakUnbindResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakUnbindResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityKeycloakUnbindResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityKeycloakUnbindResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentitySetApiKeyRequest:
	def __init__(self, client: OlvidClient = None, api_key: str = ""):
		self._client: OlvidClient = client
		self.api_key: str = api_key

	def _update_content(self, identity_set_api_key_request: IdentitySetApiKeyRequest) -> None:
		self.api_key: str = identity_set_api_key_request.api_key

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetApiKeyRequest":
		return IdentitySetApiKeyRequest(client=self._client, api_key=self.api_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyRequest, client: OlvidClient = None) -> "IdentitySetApiKeyRequest":
		return IdentitySetApiKeyRequest(client, api_key=native_message.api_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyRequest], client: OlvidClient = None) -> list["IdentitySetApiKeyRequest"]:
		return [IdentitySetApiKeyRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyRequest], client: OlvidClient = None) -> "IdentitySetApiKeyRequest":
		native_message = await promise
		return IdentitySetApiKeyRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentitySetApiKeyRequest"]):
		if messages is None:
			return []
		return [IdentitySetApiKeyRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentitySetApiKeyRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyRequest(api_key=message.api_key if message.api_key else None)

	def __str__(self):
		s: str = ''
		if self.api_key:
			s += f'api_key: {self.api_key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentitySetApiKeyRequest):
			return False
		return self.api_key == other.api_key

	def __bool__(self):
		return self.api_key != ""

	def __hash__(self):
		return hash(self.api_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentitySetApiKeyRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.api_key == "" or self.api_key == expected.api_key, "Invalid value: api_key: " + str(expected.api_key) + " != " + str(self.api_key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentitySetApiKeyResponse:
	def __init__(self, client: OlvidClient = None, api_key: "Identity.ApiKey" = None):
		self._client: OlvidClient = client
		self.api_key: Identity.ApiKey = api_key

	def _update_content(self, identity_set_api_key_response: IdentitySetApiKeyResponse) -> None:
		self.api_key: Identity.ApiKey = identity_set_api_key_response.api_key

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetApiKeyResponse":
		return IdentitySetApiKeyResponse(client=self._client, api_key=self.api_key._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyResponse, client: OlvidClient = None) -> "IdentitySetApiKeyResponse":
		return IdentitySetApiKeyResponse(client, api_key=Identity.ApiKey._from_native(native_message.api_key, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyResponse], client: OlvidClient = None) -> list["IdentitySetApiKeyResponse"]:
		return [IdentitySetApiKeyResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyResponse], client: OlvidClient = None) -> "IdentitySetApiKeyResponse":
		native_message = await promise
		return IdentitySetApiKeyResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentitySetApiKeyResponse"]):
		if messages is None:
			return []
		return [IdentitySetApiKeyResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentitySetApiKeyResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyResponse(api_key=Identity.ApiKey._to_native(message.api_key if message.api_key else None))

	def __str__(self):
		s: str = ''
		if self.api_key:
			s += f'api_key: ({self.api_key}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentitySetApiKeyResponse):
			return False
		return self.api_key == other.api_key

	def __bool__(self):
		return bool(self.api_key)

	def __hash__(self):
		return hash(self.api_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentitySetApiKeyResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.api_key is None or self.api_key._test_assertion(expected.api_key)
		except AssertionError as e:
			raise AssertionError("api_key: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentitySetConfigurationLinkRequest:
	def __init__(self, client: OlvidClient = None, configuration_link: str = ""):
		self._client: OlvidClient = client
		self.configuration_link: str = configuration_link

	def _update_content(self, identity_set_configuration_link_request: IdentitySetConfigurationLinkRequest) -> None:
		self.configuration_link: str = identity_set_configuration_link_request.configuration_link

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetConfigurationLinkRequest":
		return IdentitySetConfigurationLinkRequest(client=self._client, configuration_link=self.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkRequest, client: OlvidClient = None) -> "IdentitySetConfigurationLinkRequest":
		return IdentitySetConfigurationLinkRequest(client, configuration_link=native_message.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkRequest], client: OlvidClient = None) -> list["IdentitySetConfigurationLinkRequest"]:
		return [IdentitySetConfigurationLinkRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkRequest], client: OlvidClient = None) -> "IdentitySetConfigurationLinkRequest":
		native_message = await promise
		return IdentitySetConfigurationLinkRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentitySetConfigurationLinkRequest"]):
		if messages is None:
			return []
		return [IdentitySetConfigurationLinkRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentitySetConfigurationLinkRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkRequest(configuration_link=message.configuration_link if message.configuration_link else None)

	def __str__(self):
		s: str = ''
		if self.configuration_link:
			s += f'configuration_link: {self.configuration_link}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentitySetConfigurationLinkRequest):
			return False
		return self.configuration_link == other.configuration_link

	def __bool__(self):
		return self.configuration_link != ""

	def __hash__(self):
		return hash(self.configuration_link)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentitySetConfigurationLinkRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.configuration_link == "" or self.configuration_link == expected.configuration_link, "Invalid value: configuration_link: " + str(expected.configuration_link) + " != " + str(self.configuration_link)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentitySetConfigurationLinkResponse:
	def __init__(self, client: OlvidClient = None, api_key: "Identity.ApiKey" = None):
		self._client: OlvidClient = client
		self.api_key: Identity.ApiKey = api_key

	def _update_content(self, identity_set_configuration_link_response: IdentitySetConfigurationLinkResponse) -> None:
		self.api_key: Identity.ApiKey = identity_set_configuration_link_response.api_key

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetConfigurationLinkResponse":
		return IdentitySetConfigurationLinkResponse(client=self._client, api_key=self.api_key._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkResponse, client: OlvidClient = None) -> "IdentitySetConfigurationLinkResponse":
		return IdentitySetConfigurationLinkResponse(client, api_key=Identity.ApiKey._from_native(native_message.api_key, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkResponse], client: OlvidClient = None) -> list["IdentitySetConfigurationLinkResponse"]:
		return [IdentitySetConfigurationLinkResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkResponse], client: OlvidClient = None) -> "IdentitySetConfigurationLinkResponse":
		native_message = await promise
		return IdentitySetConfigurationLinkResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentitySetConfigurationLinkResponse"]):
		if messages is None:
			return []
		return [IdentitySetConfigurationLinkResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentitySetConfigurationLinkResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkResponse(api_key=Identity.ApiKey._to_native(message.api_key if message.api_key else None))

	def __str__(self):
		s: str = ''
		if self.api_key:
			s += f'api_key: ({self.api_key}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentitySetConfigurationLinkResponse):
			return False
		return self.api_key == other.api_key

	def __bool__(self):
		return bool(self.api_key)

	def __hash__(self):
		return hash(self.api_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentitySetConfigurationLinkResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.api_key is None or self.api_key._test_assertion(expected.api_key)
		except AssertionError as e:
			raise AssertionError("api_key: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationListRequest:
	def __init__(self, client: OlvidClient = None, filter: "InvitationFilter" = None):
		self._client: OlvidClient = client
		self.filter: InvitationFilter = filter

	def _update_content(self, invitation_list_request: InvitationListRequest) -> None:
		self.filter: InvitationFilter = invitation_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationListRequest":
		return InvitationListRequest(client=self._client, filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationListRequest, client: OlvidClient = None) -> "InvitationListRequest":
		return InvitationListRequest(client, filter=InvitationFilter._from_native(native_message.filter, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationListRequest], client: OlvidClient = None) -> list["InvitationListRequest"]:
		return [InvitationListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationListRequest], client: OlvidClient = None) -> "InvitationListRequest":
		native_message = await promise
		return InvitationListRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationListRequest"]):
		if messages is None:
			return []
		return [InvitationListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationListRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationListRequest(filter=InvitationFilter._to_native(message.filter if message.filter else None))

	def __str__(self):
		s: str = ''
		if self.filter:
			s += f'filter: ({self.filter}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationListRequest):
			return False
		return self.filter == other.filter

	def __bool__(self):
		return bool(self.filter)

	def __hash__(self):
		return hash(self.filter)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationListResponse:
	def __init__(self, client: OlvidClient = None, invitations: "list[Invitation]" = None):
		self._client: OlvidClient = client
		self.invitations: list[Invitation] = invitations

	def _update_content(self, invitation_list_response: InvitationListResponse) -> None:
		self.invitations: list[Invitation] = invitation_list_response.invitations

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationListResponse":
		return InvitationListResponse(client=self._client, invitations=[e._clone() for e in self.invitations])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationListResponse, client: OlvidClient = None) -> "InvitationListResponse":
		return InvitationListResponse(client, invitations=Invitation._from_native_list(native_message.invitations, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationListResponse], client: OlvidClient = None) -> list["InvitationListResponse"]:
		return [InvitationListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationListResponse], client: OlvidClient = None) -> "InvitationListResponse":
		native_message = await promise
		return InvitationListResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationListResponse"]):
		if messages is None:
			return []
		return [InvitationListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationListResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationListResponse(invitations=Invitation._to_native_list(message.invitations if message.invitations else None))

	def __str__(self):
		s: str = ''
		if self.invitations:
			s += f'invitations: {[str(el) for el in self.invitations]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationListResponse):
			return False
		return self.invitations == other.invitations

	def __bool__(self):
		return bool(self.invitations)

	def __hash__(self):
		return hash(tuple(self.invitations))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field invitations")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationGetRequest:
	def __init__(self, client: OlvidClient = None, invitation_id: int = 0):
		self._client: OlvidClient = client
		self.invitation_id: int = invitation_id

	def _update_content(self, invitation_get_request: InvitationGetRequest) -> None:
		self.invitation_id: int = invitation_get_request.invitation_id

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationGetRequest":
		return InvitationGetRequest(client=self._client, invitation_id=self.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetRequest, client: OlvidClient = None) -> "InvitationGetRequest":
		return InvitationGetRequest(client, invitation_id=native_message.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetRequest], client: OlvidClient = None) -> list["InvitationGetRequest"]:
		return [InvitationGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetRequest], client: OlvidClient = None) -> "InvitationGetRequest":
		native_message = await promise
		return InvitationGetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationGetRequest"]):
		if messages is None:
			return []
		return [InvitationGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetRequest(invitation_id=message.invitation_id if message.invitation_id else None)

	def __str__(self):
		s: str = ''
		if self.invitation_id:
			s += f'invitation_id: {self.invitation_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationGetRequest):
			return False
		return self.invitation_id == other.invitation_id

	def __bool__(self):
		return self.invitation_id != 0

	def __hash__(self):
		return hash(self.invitation_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.invitation_id == 0 or self.invitation_id == expected.invitation_id, "Invalid value: invitation_id: " + str(expected.invitation_id) + " != " + str(self.invitation_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationGetResponse:
	def __init__(self, client: OlvidClient = None, invitation: "Invitation" = None):
		self._client: OlvidClient = client
		self.invitation: Invitation = invitation

	def _update_content(self, invitation_get_response: InvitationGetResponse) -> None:
		self.invitation: Invitation = invitation_get_response.invitation

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationGetResponse":
		return InvitationGetResponse(client=self._client, invitation=self.invitation._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetResponse, client: OlvidClient = None) -> "InvitationGetResponse":
		return InvitationGetResponse(client, invitation=Invitation._from_native(native_message.invitation, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetResponse], client: OlvidClient = None) -> list["InvitationGetResponse"]:
		return [InvitationGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetResponse], client: OlvidClient = None) -> "InvitationGetResponse":
		native_message = await promise
		return InvitationGetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationGetResponse"]):
		if messages is None:
			return []
		return [InvitationGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetResponse(invitation=Invitation._to_native(message.invitation if message.invitation else None))

	def __str__(self):
		s: str = ''
		if self.invitation:
			s += f'invitation: ({self.invitation}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationGetResponse):
			return False
		return self.invitation == other.invitation

	def __bool__(self):
		return bool(self.invitation)

	def __hash__(self):
		return hash(self.invitation)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.invitation is None or self.invitation._test_assertion(expected.invitation)
		except AssertionError as e:
			raise AssertionError("invitation: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationNewRequest:
	def __init__(self, client: OlvidClient = None, invitation_url: str = ""):
		self._client: OlvidClient = client
		self.invitation_url: str = invitation_url

	def _update_content(self, invitation_new_request: InvitationNewRequest) -> None:
		self.invitation_url: str = invitation_new_request.invitation_url

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationNewRequest":
		return InvitationNewRequest(client=self._client, invitation_url=self.invitation_url)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewRequest, client: OlvidClient = None) -> "InvitationNewRequest":
		return InvitationNewRequest(client, invitation_url=native_message.invitation_url)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewRequest], client: OlvidClient = None) -> list["InvitationNewRequest"]:
		return [InvitationNewRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewRequest], client: OlvidClient = None) -> "InvitationNewRequest":
		native_message = await promise
		return InvitationNewRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationNewRequest"]):
		if messages is None:
			return []
		return [InvitationNewRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationNewRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewRequest(invitation_url=message.invitation_url if message.invitation_url else None)

	def __str__(self):
		s: str = ''
		if self.invitation_url:
			s += f'invitation_url: {self.invitation_url}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationNewRequest):
			return False
		return self.invitation_url == other.invitation_url

	def __bool__(self):
		return self.invitation_url != ""

	def __hash__(self):
		return hash(self.invitation_url)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationNewRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.invitation_url == "" or self.invitation_url == expected.invitation_url, "Invalid value: invitation_url: " + str(expected.invitation_url) + " != " + str(self.invitation_url)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationNewResponse:
	def __init__(self, client: OlvidClient = None, invitation: "Invitation" = None):
		self._client: OlvidClient = client
		self.invitation: Invitation = invitation

	def _update_content(self, invitation_new_response: InvitationNewResponse) -> None:
		self.invitation: Invitation = invitation_new_response.invitation

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationNewResponse":
		return InvitationNewResponse(client=self._client, invitation=self.invitation._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewResponse, client: OlvidClient = None) -> "InvitationNewResponse":
		return InvitationNewResponse(client, invitation=Invitation._from_native(native_message.invitation, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewResponse], client: OlvidClient = None) -> list["InvitationNewResponse"]:
		return [InvitationNewResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewResponse], client: OlvidClient = None) -> "InvitationNewResponse":
		native_message = await promise
		return InvitationNewResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationNewResponse"]):
		if messages is None:
			return []
		return [InvitationNewResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationNewResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewResponse(invitation=Invitation._to_native(message.invitation if message.invitation else None))

	def __str__(self):
		s: str = ''
		if self.invitation:
			s += f'invitation: ({self.invitation}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationNewResponse):
			return False
		return self.invitation == other.invitation

	def __bool__(self):
		return bool(self.invitation)

	def __hash__(self):
		return hash(self.invitation)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationNewResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.invitation is None or self.invitation._test_assertion(expected.invitation)
		except AssertionError as e:
			raise AssertionError("invitation: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationAcceptRequest:
	def __init__(self, client: OlvidClient = None, invitation_id: int = 0):
		self._client: OlvidClient = client
		self.invitation_id: int = invitation_id

	def _update_content(self, invitation_accept_request: InvitationAcceptRequest) -> None:
		self.invitation_id: int = invitation_accept_request.invitation_id

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationAcceptRequest":
		return InvitationAcceptRequest(client=self._client, invitation_id=self.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptRequest, client: OlvidClient = None) -> "InvitationAcceptRequest":
		return InvitationAcceptRequest(client, invitation_id=native_message.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptRequest], client: OlvidClient = None) -> list["InvitationAcceptRequest"]:
		return [InvitationAcceptRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptRequest], client: OlvidClient = None) -> "InvitationAcceptRequest":
		native_message = await promise
		return InvitationAcceptRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationAcceptRequest"]):
		if messages is None:
			return []
		return [InvitationAcceptRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationAcceptRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptRequest(invitation_id=message.invitation_id if message.invitation_id else None)

	def __str__(self):
		s: str = ''
		if self.invitation_id:
			s += f'invitation_id: {self.invitation_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationAcceptRequest):
			return False
		return self.invitation_id == other.invitation_id

	def __bool__(self):
		return self.invitation_id != 0

	def __hash__(self):
		return hash(self.invitation_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationAcceptRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.invitation_id == 0 or self.invitation_id == expected.invitation_id, "Invalid value: invitation_id: " + str(expected.invitation_id) + " != " + str(self.invitation_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationAcceptResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, invitation_accept_response: InvitationAcceptResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationAcceptResponse":
		return InvitationAcceptResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptResponse, client: OlvidClient = None) -> "InvitationAcceptResponse":
		return InvitationAcceptResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptResponse], client: OlvidClient = None) -> list["InvitationAcceptResponse"]:
		return [InvitationAcceptResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptResponse], client: OlvidClient = None) -> "InvitationAcceptResponse":
		native_message = await promise
		return InvitationAcceptResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationAcceptResponse"]):
		if messages is None:
			return []
		return [InvitationAcceptResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationAcceptResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationAcceptResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationAcceptResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationDeclineRequest:
	def __init__(self, client: OlvidClient = None, invitation_id: int = 0):
		self._client: OlvidClient = client
		self.invitation_id: int = invitation_id

	def _update_content(self, invitation_decline_request: InvitationDeclineRequest) -> None:
		self.invitation_id: int = invitation_decline_request.invitation_id

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationDeclineRequest":
		return InvitationDeclineRequest(client=self._client, invitation_id=self.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineRequest, client: OlvidClient = None) -> "InvitationDeclineRequest":
		return InvitationDeclineRequest(client, invitation_id=native_message.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineRequest], client: OlvidClient = None) -> list["InvitationDeclineRequest"]:
		return [InvitationDeclineRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineRequest], client: OlvidClient = None) -> "InvitationDeclineRequest":
		native_message = await promise
		return InvitationDeclineRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationDeclineRequest"]):
		if messages is None:
			return []
		return [InvitationDeclineRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationDeclineRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineRequest(invitation_id=message.invitation_id if message.invitation_id else None)

	def __str__(self):
		s: str = ''
		if self.invitation_id:
			s += f'invitation_id: {self.invitation_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationDeclineRequest):
			return False
		return self.invitation_id == other.invitation_id

	def __bool__(self):
		return self.invitation_id != 0

	def __hash__(self):
		return hash(self.invitation_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationDeclineRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.invitation_id == 0 or self.invitation_id == expected.invitation_id, "Invalid value: invitation_id: " + str(expected.invitation_id) + " != " + str(self.invitation_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationDeclineResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, invitation_decline_response: InvitationDeclineResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationDeclineResponse":
		return InvitationDeclineResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineResponse, client: OlvidClient = None) -> "InvitationDeclineResponse":
		return InvitationDeclineResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineResponse], client: OlvidClient = None) -> list["InvitationDeclineResponse"]:
		return [InvitationDeclineResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineResponse], client: OlvidClient = None) -> "InvitationDeclineResponse":
		native_message = await promise
		return InvitationDeclineResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationDeclineResponse"]):
		if messages is None:
			return []
		return [InvitationDeclineResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationDeclineResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationDeclineResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationDeclineResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationSasRequest:
	def __init__(self, client: OlvidClient = None, invitation_id: int = 0, sas: str = ""):
		self._client: OlvidClient = client
		self.invitation_id: int = invitation_id
		self.sas: str = sas

	def _update_content(self, invitation_sas_request: InvitationSasRequest) -> None:
		self.invitation_id: int = invitation_sas_request.invitation_id
		self.sas: str = invitation_sas_request.sas

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationSasRequest":
		return InvitationSasRequest(client=self._client, invitation_id=self.invitation_id, sas=self.sas)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasRequest, client: OlvidClient = None) -> "InvitationSasRequest":
		return InvitationSasRequest(client, invitation_id=native_message.invitation_id, sas=native_message.sas)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasRequest], client: OlvidClient = None) -> list["InvitationSasRequest"]:
		return [InvitationSasRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasRequest], client: OlvidClient = None) -> "InvitationSasRequest":
		native_message = await promise
		return InvitationSasRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationSasRequest"]):
		if messages is None:
			return []
		return [InvitationSasRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationSasRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasRequest(invitation_id=message.invitation_id if message.invitation_id else None, sas=message.sas if message.sas else None)

	def __str__(self):
		s: str = ''
		if self.invitation_id:
			s += f'invitation_id: {self.invitation_id}, '
		if self.sas:
			s += f'sas: {self.sas}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationSasRequest):
			return False
		return self.invitation_id == other.invitation_id and self.sas == other.sas

	def __bool__(self):
		return self.invitation_id != 0 or self.sas != ""

	def __hash__(self):
		return hash((self.invitation_id, self.sas))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationSasRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.invitation_id == 0 or self.invitation_id == expected.invitation_id, "Invalid value: invitation_id: " + str(expected.invitation_id) + " != " + str(self.invitation_id)
		assert expected.sas == "" or self.sas == expected.sas, "Invalid value: sas: " + str(expected.sas) + " != " + str(self.sas)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationSasResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, invitation_sas_response: InvitationSasResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationSasResponse":
		return InvitationSasResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasResponse, client: OlvidClient = None) -> "InvitationSasResponse":
		return InvitationSasResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasResponse], client: OlvidClient = None) -> list["InvitationSasResponse"]:
		return [InvitationSasResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasResponse], client: OlvidClient = None) -> "InvitationSasResponse":
		native_message = await promise
		return InvitationSasResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationSasResponse"]):
		if messages is None:
			return []
		return [InvitationSasResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationSasResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationSasResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationSasResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationDeleteRequest:
	def __init__(self, client: OlvidClient = None, invitation_id: int = 0):
		self._client: OlvidClient = client
		self.invitation_id: int = invitation_id

	def _update_content(self, invitation_delete_request: InvitationDeleteRequest) -> None:
		self.invitation_id: int = invitation_delete_request.invitation_id

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationDeleteRequest":
		return InvitationDeleteRequest(client=self._client, invitation_id=self.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteRequest, client: OlvidClient = None) -> "InvitationDeleteRequest":
		return InvitationDeleteRequest(client, invitation_id=native_message.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteRequest], client: OlvidClient = None) -> list["InvitationDeleteRequest"]:
		return [InvitationDeleteRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteRequest], client: OlvidClient = None) -> "InvitationDeleteRequest":
		native_message = await promise
		return InvitationDeleteRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationDeleteRequest"]):
		if messages is None:
			return []
		return [InvitationDeleteRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationDeleteRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteRequest(invitation_id=message.invitation_id if message.invitation_id else None)

	def __str__(self):
		s: str = ''
		if self.invitation_id:
			s += f'invitation_id: {self.invitation_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationDeleteRequest):
			return False
		return self.invitation_id == other.invitation_id

	def __bool__(self):
		return self.invitation_id != 0

	def __hash__(self):
		return hash(self.invitation_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationDeleteRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.invitation_id == 0 or self.invitation_id == expected.invitation_id, "Invalid value: invitation_id: " + str(expected.invitation_id) + " != " + str(self.invitation_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class InvitationDeleteResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, invitation_delete_response: InvitationDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationDeleteResponse":
		return InvitationDeleteResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteResponse, client: OlvidClient = None) -> "InvitationDeleteResponse":
		return InvitationDeleteResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteResponse], client: OlvidClient = None) -> list["InvitationDeleteResponse"]:
		return [InvitationDeleteResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteResponse], client: OlvidClient = None) -> "InvitationDeleteResponse":
		native_message = await promise
		return InvitationDeleteResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["InvitationDeleteResponse"]):
		if messages is None:
			return []
		return [InvitationDeleteResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["InvitationDeleteResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, InvitationDeleteResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, InvitationDeleteResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageListRequest:
	def __init__(self, client: OlvidClient = None, filter: "MessageFilter" = None, unread: bool = False):
		self._client: OlvidClient = client
		self.filter: MessageFilter = filter
		self.unread: bool = unread

	def _update_content(self, message_list_request: MessageListRequest) -> None:
		self.filter: MessageFilter = message_list_request.filter
		self.unread: bool = message_list_request.unread

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageListRequest":
		return MessageListRequest(client=self._client, filter=self.filter._clone(), unread=self.unread)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageListRequest, client: OlvidClient = None) -> "MessageListRequest":
		return MessageListRequest(client, filter=MessageFilter._from_native(native_message.filter, client=client), unread=native_message.unread)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageListRequest], client: OlvidClient = None) -> list["MessageListRequest"]:
		return [MessageListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageListRequest], client: OlvidClient = None) -> "MessageListRequest":
		native_message = await promise
		return MessageListRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageListRequest"]):
		if messages is None:
			return []
		return [MessageListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageListRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageListRequest(filter=MessageFilter._to_native(message.filter if message.filter else None), unread=message.unread if message.unread else None)

	def __str__(self):
		s: str = ''
		if self.filter:
			s += f'filter: ({self.filter}), '
		if self.unread:
			s += f'unread: {self.unread}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageListRequest):
			return False
		return self.filter == other.filter and self.unread == other.unread

	def __bool__(self):
		return bool(self.filter) or self.unread

	def __hash__(self):
		return hash((self.filter, self.unread))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		assert expected.unread is False or self.unread == expected.unread, "Invalid value: unread: " + str(expected.unread) + " != " + str(self.unread)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageListResponse:
	def __init__(self, client: OlvidClient = None, messages: "list[Message]" = None):
		self._client: OlvidClient = client
		self.messages: list[Message] = messages

	def _update_content(self, message_list_response: MessageListResponse) -> None:
		self.messages: list[Message] = message_list_response.messages

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageListResponse":
		return MessageListResponse(client=self._client, messages=[e._clone() for e in self.messages])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageListResponse, client: OlvidClient = None) -> "MessageListResponse":
		return MessageListResponse(client, messages=Message._from_native_list(native_message.messages, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageListResponse], client: OlvidClient = None) -> list["MessageListResponse"]:
		return [MessageListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageListResponse], client: OlvidClient = None) -> "MessageListResponse":
		native_message = await promise
		return MessageListResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageListResponse"]):
		if messages is None:
			return []
		return [MessageListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageListResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageListResponse(messages=Message._to_native_list(message.messages if message.messages else None))

	def __str__(self):
		s: str = ''
		if self.messages:
			s += f'messages: {[str(el) for el in self.messages]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageListResponse):
			return False
		return self.messages == other.messages

	def __bool__(self):
		return bool(self.messages)

	def __hash__(self):
		return hash(tuple(self.messages))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field messages")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageGetRequest:
	def __init__(self, client: OlvidClient = None, message_id: "MessageId" = None):
		self._client: OlvidClient = client
		self.message_id: MessageId = message_id

	def _update_content(self, message_get_request: MessageGetRequest) -> None:
		self.message_id: MessageId = message_get_request.message_id

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageGetRequest":
		return MessageGetRequest(client=self._client, message_id=self.message_id._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageGetRequest, client: OlvidClient = None) -> "MessageGetRequest":
		return MessageGetRequest(client, message_id=MessageId._from_native(native_message.message_id, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageGetRequest], client: OlvidClient = None) -> list["MessageGetRequest"]:
		return [MessageGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageGetRequest], client: OlvidClient = None) -> "MessageGetRequest":
		native_message = await promise
		return MessageGetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageGetRequest"]):
		if messages is None:
			return []
		return [MessageGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageGetRequest(message_id=MessageId._to_native(message.message_id if message.message_id else None))

	def __str__(self):
		s: str = ''
		if self.message_id:
			s += f'message_id: ({self.message_id}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageGetRequest):
			return False
		return self.message_id == other.message_id

	def __bool__(self):
		return bool(self.message_id)

	def __hash__(self):
		return hash(self.message_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message_id is None or self.message_id._test_assertion(expected.message_id)
		except AssertionError as e:
			raise AssertionError("message_id: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageGetResponse:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_get_response: MessageGetResponse) -> None:
		self.message: Message = message_get_response.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageGetResponse":
		return MessageGetResponse(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageGetResponse, client: OlvidClient = None) -> "MessageGetResponse":
		return MessageGetResponse(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageGetResponse], client: OlvidClient = None) -> list["MessageGetResponse"]:
		return [MessageGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageGetResponse], client: OlvidClient = None) -> "MessageGetResponse":
		native_message = await promise
		return MessageGetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageGetResponse"]):
		if messages is None:
			return []
		return [MessageGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageGetResponse(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageGetResponse):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageRefreshRequest:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, message_refresh_request: MessageRefreshRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageRefreshRequest":
		return MessageRefreshRequest(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageRefreshRequest, client: OlvidClient = None) -> "MessageRefreshRequest":
		return MessageRefreshRequest(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageRefreshRequest], client: OlvidClient = None) -> list["MessageRefreshRequest"]:
		return [MessageRefreshRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageRefreshRequest], client: OlvidClient = None) -> "MessageRefreshRequest":
		native_message = await promise
		return MessageRefreshRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageRefreshRequest"]):
		if messages is None:
			return []
		return [MessageRefreshRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageRefreshRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageRefreshRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageRefreshRequest):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageRefreshRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageRefreshResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, message_refresh_response: MessageRefreshResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageRefreshResponse":
		return MessageRefreshResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageRefreshResponse, client: OlvidClient = None) -> "MessageRefreshResponse":
		return MessageRefreshResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageRefreshResponse], client: OlvidClient = None) -> list["MessageRefreshResponse"]:
		return [MessageRefreshResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageRefreshResponse], client: OlvidClient = None) -> "MessageRefreshResponse":
		native_message = await promise
		return MessageRefreshResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageRefreshResponse"]):
		if messages is None:
			return []
		return [MessageRefreshResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageRefreshResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageRefreshResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageRefreshResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageRefreshResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageDeleteRequest:
	def __init__(self, client: OlvidClient = None, message_id: "MessageId" = None, delete_everywhere: bool = False):
		self._client: OlvidClient = client
		self.message_id: MessageId = message_id
		self.delete_everywhere: bool = delete_everywhere

	def _update_content(self, message_delete_request: MessageDeleteRequest) -> None:
		self.message_id: MessageId = message_delete_request.message_id
		self.delete_everywhere: bool = message_delete_request.delete_everywhere

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageDeleteRequest":
		return MessageDeleteRequest(client=self._client, message_id=self.message_id._clone(), delete_everywhere=self.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageDeleteRequest, client: OlvidClient = None) -> "MessageDeleteRequest":
		return MessageDeleteRequest(client, message_id=MessageId._from_native(native_message.message_id, client=client), delete_everywhere=native_message.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageDeleteRequest], client: OlvidClient = None) -> list["MessageDeleteRequest"]:
		return [MessageDeleteRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageDeleteRequest], client: OlvidClient = None) -> "MessageDeleteRequest":
		native_message = await promise
		return MessageDeleteRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageDeleteRequest"]):
		if messages is None:
			return []
		return [MessageDeleteRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageDeleteRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageDeleteRequest(message_id=MessageId._to_native(message.message_id if message.message_id else None), delete_everywhere=message.delete_everywhere if message.delete_everywhere else None)

	def __str__(self):
		s: str = ''
		if self.message_id:
			s += f'message_id: ({self.message_id}), '
		if self.delete_everywhere:
			s += f'delete_everywhere: {self.delete_everywhere}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageDeleteRequest):
			return False
		return self.message_id == other.message_id and self.delete_everywhere == other.delete_everywhere

	def __bool__(self):
		return bool(self.message_id) or self.delete_everywhere

	def __hash__(self):
		return hash((self.message_id, self.delete_everywhere))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageDeleteRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message_id is None or self.message_id._test_assertion(expected.message_id)
		except AssertionError as e:
			raise AssertionError("message_id: " + str(e))
		assert expected.delete_everywhere is False or self.delete_everywhere == expected.delete_everywhere, "Invalid value: delete_everywhere: " + str(expected.delete_everywhere) + " != " + str(self.delete_everywhere)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageDeleteResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, message_delete_response: MessageDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageDeleteResponse":
		return MessageDeleteResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageDeleteResponse, client: OlvidClient = None) -> "MessageDeleteResponse":
		return MessageDeleteResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageDeleteResponse], client: OlvidClient = None) -> list["MessageDeleteResponse"]:
		return [MessageDeleteResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageDeleteResponse], client: OlvidClient = None) -> "MessageDeleteResponse":
		native_message = await promise
		return MessageDeleteResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageDeleteResponse"]):
		if messages is None:
			return []
		return [MessageDeleteResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageDeleteResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageDeleteResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageDeleteResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageDeleteResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageSendRequest:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0, body: str = "", reply_id: "MessageId" = None, ephemerality: "MessageEphemerality" = None, disable_link_preview: bool = False):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id
		self.body: str = body
		self.reply_id: MessageId = reply_id
		self.ephemerality: MessageEphemerality = ephemerality
		self.disable_link_preview: bool = disable_link_preview

	def _update_content(self, message_send_request: MessageSendRequest) -> None:
		self.discussion_id: int = message_send_request.discussion_id
		self.body: str = message_send_request.body
		self.reply_id: MessageId = message_send_request.reply_id
		self.ephemerality: MessageEphemerality = message_send_request.ephemerality
		self.disable_link_preview: bool = message_send_request.disable_link_preview

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendRequest":
		return MessageSendRequest(client=self._client, discussion_id=self.discussion_id, body=self.body, reply_id=self.reply_id._clone(), ephemerality=self.ephemerality._clone(), disable_link_preview=self.disable_link_preview)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendRequest, client: OlvidClient = None) -> "MessageSendRequest":
		return MessageSendRequest(client, discussion_id=native_message.discussion_id, body=native_message.body, reply_id=MessageId._from_native(native_message.reply_id, client=client), ephemerality=MessageEphemerality._from_native(native_message.ephemerality, client=client), disable_link_preview=native_message.disable_link_preview)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendRequest], client: OlvidClient = None) -> list["MessageSendRequest"]:
		return [MessageSendRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendRequest], client: OlvidClient = None) -> "MessageSendRequest":
		native_message = await promise
		return MessageSendRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageSendRequest"]):
		if messages is None:
			return []
		return [MessageSendRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageSendRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageSendRequest(discussion_id=message.discussion_id if message.discussion_id else None, body=message.body if message.body else None, reply_id=MessageId._to_native(message.reply_id if message.reply_id else None), ephemerality=MessageEphemerality._to_native(message.ephemerality if message.ephemerality else None), disable_link_preview=message.disable_link_preview if message.disable_link_preview else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.body:
			s += f'body: {self.body}, '
		if self.reply_id:
			s += f'reply_id: ({self.reply_id}), '
		if self.ephemerality:
			s += f'ephemerality: ({self.ephemerality}), '
		if self.disable_link_preview:
			s += f'disable_link_preview: {self.disable_link_preview}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageSendRequest):
			return False
		return self.discussion_id == other.discussion_id and self.body == other.body and self.reply_id == other.reply_id and self.ephemerality == other.ephemerality and self.disable_link_preview == other.disable_link_preview

	def __bool__(self):
		return self.discussion_id != 0 or self.body != "" or bool(self.reply_id) or bool(self.ephemerality) or self.disable_link_preview

	def __hash__(self):
		return hash((self.discussion_id, self.body, self.reply_id, self.ephemerality, self.disable_link_preview))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageSendRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.body == "" or self.body == expected.body, "Invalid value: body: " + str(expected.body) + " != " + str(self.body)
		try:
			assert expected.reply_id is None or self.reply_id._test_assertion(expected.reply_id)
		except AssertionError as e:
			raise AssertionError("reply_id: " + str(e))
		try:
			assert expected.ephemerality is None or self.ephemerality._test_assertion(expected.ephemerality)
		except AssertionError as e:
			raise AssertionError("ephemerality: " + str(e))
		assert expected.disable_link_preview is False or self.disable_link_preview == expected.disable_link_preview, "Invalid value: disable_link_preview: " + str(expected.disable_link_preview) + " != " + str(self.disable_link_preview)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageSendResponse:
	def __init__(self, client: OlvidClient = None, message: "Message" = None):
		self._client: OlvidClient = client
		self.message: Message = message

	def _update_content(self, message_send_response: MessageSendResponse) -> None:
		self.message: Message = message_send_response.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendResponse":
		return MessageSendResponse(client=self._client, message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendResponse, client: OlvidClient = None) -> "MessageSendResponse":
		return MessageSendResponse(client, message=Message._from_native(native_message.message, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendResponse], client: OlvidClient = None) -> list["MessageSendResponse"]:
		return [MessageSendResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendResponse], client: OlvidClient = None) -> "MessageSendResponse":
		native_message = await promise
		return MessageSendResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageSendResponse"]):
		if messages is None:
			return []
		return [MessageSendResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageSendResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageSendResponse(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageSendResponse):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageSendResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageSendWithAttachmentsRequest:
	def __init__(self, client: OlvidClient = None, metadata: "MessageSendWithAttachmentsRequestMetadata" = None, payload: bytes = None, file_delimiter: bool = None):
		self._client: OlvidClient = client
		self.metadata: MessageSendWithAttachmentsRequestMetadata = metadata
		self.payload: bytes = payload
		self.file_delimiter: bool = file_delimiter

	def _update_content(self, message_send_with_attachments_request: MessageSendWithAttachmentsRequest) -> None:
		self.metadata: MessageSendWithAttachmentsRequestMetadata = message_send_with_attachments_request.metadata
		self.payload: bytes = message_send_with_attachments_request.payload
		self.file_delimiter: bool = message_send_with_attachments_request.file_delimiter

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendWithAttachmentsRequest":
		return MessageSendWithAttachmentsRequest(client=self._client, metadata=self.metadata._clone(), payload=self.payload, file_delimiter=self.file_delimiter)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequest, client: OlvidClient = None) -> "MessageSendWithAttachmentsRequest":
		return MessageSendWithAttachmentsRequest(client, metadata=MessageSendWithAttachmentsRequestMetadata._from_native(native_message.metadata, client=client), payload=native_message.payload, file_delimiter=native_message.file_delimiter)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequest], client: OlvidClient = None) -> list["MessageSendWithAttachmentsRequest"]:
		return [MessageSendWithAttachmentsRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequest], client: OlvidClient = None) -> "MessageSendWithAttachmentsRequest":
		native_message = await promise
		return MessageSendWithAttachmentsRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageSendWithAttachmentsRequest"]):
		if messages is None:
			return []
		return [MessageSendWithAttachmentsRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageSendWithAttachmentsRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequest(metadata=MessageSendWithAttachmentsRequestMetadata._to_native(message.metadata if message.metadata else None), payload=message.payload if message.payload else None, file_delimiter=message.file_delimiter if message.file_delimiter else None)

	def __str__(self):
		s: str = ''
		if self.metadata:
			s += f'metadata: ({self.metadata}), '
		if self.payload:
			s += f'payload: {self.payload}, '
		if self.file_delimiter:
			s += f'file_delimiter: {self.file_delimiter}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageSendWithAttachmentsRequest):
			return False
		return self.metadata == other.metadata and self.payload == other.payload and self.file_delimiter == other.file_delimiter

	def __bool__(self):
		return bool(self.metadata) or self.payload is not None or self.file_delimiter is not None

	def __hash__(self):
		return hash((self.metadata, self.payload, self.file_delimiter))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageSendWithAttachmentsRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.metadata is None or self.metadata._test_assertion(expected.metadata)
		except AssertionError as e:
			raise AssertionError("metadata: " + str(e))
		assert expected.payload is None or self.payload == expected.payload, "Invalid value: payload: " + str(expected.payload) + " != " + str(self.payload)
		assert expected.file_delimiter is None or self.file_delimiter == expected.file_delimiter, "Invalid value: file_delimiter: " + str(expected.file_delimiter) + " != " + str(self.file_delimiter)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageSendWithAttachmentsRequestMetadata:
	class File:
		def __init__(self, client: OlvidClient = None, filename: str = "", file_size: int = 0):
			self._client: OlvidClient = client
			self.filename: str = filename
			self.file_size: int = file_size
	
		def _update_content(self, file: MessageSendWithAttachmentsRequestMetadata.File) -> None:
			self.filename: str = file.filename
			self.file_size: int = file.file_size
	
		# noinspection PyProtectedMember
		def _clone(self) -> "MessageSendWithAttachmentsRequestMetadata.File":
			return MessageSendWithAttachmentsRequestMetadata.File(client=self._client, filename=self.filename, file_size=self.file_size)
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
		@staticmethod
		def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata.File, client: OlvidClient = None) -> "MessageSendWithAttachmentsRequestMetadata.File":
			return MessageSendWithAttachmentsRequestMetadata.File(client, filename=native_message.filename, file_size=native_message.file_size)
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
		@staticmethod
		def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata.File], client: OlvidClient = None) -> list["MessageSendWithAttachmentsRequestMetadata.File"]:
			return [MessageSendWithAttachmentsRequestMetadata.File._from_native(native_message, client=client) for native_message in native_message_list]
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
		@staticmethod
		async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata.File], client: OlvidClient = None) -> "MessageSendWithAttachmentsRequestMetadata.File":
			native_message = await promise
			return MessageSendWithAttachmentsRequestMetadata.File._from_native(native_message, client=client)
	
		# noinspection PyUnresolvedReferences,PyProtectedMember
		@staticmethod
		def _to_native_list(messages: list["MessageSendWithAttachmentsRequestMetadata.File"]):
			if messages is None:
				return []
			return [MessageSendWithAttachmentsRequestMetadata.File._to_native(message) for message in messages]
	
		# noinspection PyUnresolvedReferences,PyProtectedMember
		@staticmethod
		def _to_native(message: Optional["MessageSendWithAttachmentsRequestMetadata.File"]):
			if message is None:
				return None
			return olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata.File(filename=message.filename if message.filename else None, file_size=message.file_size if message.file_size else None)
	
		def __str__(self):
			s: str = ''
			if self.filename:
				s += f'filename: {self.filename}, '
			if self.file_size:
				s += f'file_size: {self.file_size}, '
			return s.removesuffix(', ')
	
		def __eq__(self, other):
			if not isinstance(other, MessageSendWithAttachmentsRequestMetadata.File):
				return False
			return self.filename == other.filename and self.file_size == other.file_size
	
		def __bool__(self):
			return self.filename != "" or self.file_size != 0
	
		def __hash__(self):
			return hash((self.filename, self.file_size))
	
		# For tests routines
		# noinspection DuplicatedCode,PyProtectedMember
		def _test_assertion(self, expected):
			if not isinstance(expected, MessageSendWithAttachmentsRequestMetadata.File):
				assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
			assert expected.filename == "" or self.filename == expected.filename, "Invalid value: filename: " + str(expected.filename) + " != " + str(self.filename)
			assert expected.file_size == 0 or self.file_size == expected.file_size, "Invalid value: file_size: " + str(expected.file_size) + " != " + str(self.file_size)
			return True

	def __init__(self, client: OlvidClient = None, discussion_id: int = 0, body: str = "", reply_id: "MessageId" = None, ephemerality: "MessageEphemerality" = None, disable_link_preview: bool = False, files: "list[MessageSendWithAttachmentsRequestMetadata.File]" = None):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id
		self.body: str = body
		self.reply_id: MessageId = reply_id
		self.ephemerality: MessageEphemerality = ephemerality
		self.disable_link_preview: bool = disable_link_preview
		self.files: list[MessageSendWithAttachmentsRequestMetadata.File] = files

	def _update_content(self, message_send_with_attachments_request_metadata: MessageSendWithAttachmentsRequestMetadata) -> None:
		self.discussion_id: int = message_send_with_attachments_request_metadata.discussion_id
		self.body: str = message_send_with_attachments_request_metadata.body
		self.reply_id: MessageId = message_send_with_attachments_request_metadata.reply_id
		self.ephemerality: MessageEphemerality = message_send_with_attachments_request_metadata.ephemerality
		self.disable_link_preview: bool = message_send_with_attachments_request_metadata.disable_link_preview
		self.files: list[MessageSendWithAttachmentsRequestMetadata.File] = message_send_with_attachments_request_metadata.files

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendWithAttachmentsRequestMetadata":
		return MessageSendWithAttachmentsRequestMetadata(client=self._client, discussion_id=self.discussion_id, body=self.body, reply_id=self.reply_id._clone(), ephemerality=self.ephemerality._clone(), disable_link_preview=self.disable_link_preview, files=[e._clone() for e in self.files])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata, client: OlvidClient = None) -> "MessageSendWithAttachmentsRequestMetadata":
		return MessageSendWithAttachmentsRequestMetadata(client, discussion_id=native_message.discussion_id, body=native_message.body, reply_id=MessageId._from_native(native_message.reply_id, client=client), ephemerality=MessageEphemerality._from_native(native_message.ephemerality, client=client), disable_link_preview=native_message.disable_link_preview, files=MessageSendWithAttachmentsRequestMetadata.File._from_native_list(native_message.files, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata], client: OlvidClient = None) -> list["MessageSendWithAttachmentsRequestMetadata"]:
		return [MessageSendWithAttachmentsRequestMetadata._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata], client: OlvidClient = None) -> "MessageSendWithAttachmentsRequestMetadata":
		native_message = await promise
		return MessageSendWithAttachmentsRequestMetadata._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageSendWithAttachmentsRequestMetadata"]):
		if messages is None:
			return []
		return [MessageSendWithAttachmentsRequestMetadata._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageSendWithAttachmentsRequestMetadata"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata(discussion_id=message.discussion_id if message.discussion_id else None, body=message.body if message.body else None, reply_id=MessageId._to_native(message.reply_id if message.reply_id else None), ephemerality=MessageEphemerality._to_native(message.ephemerality if message.ephemerality else None), disable_link_preview=message.disable_link_preview if message.disable_link_preview else None, files=MessageSendWithAttachmentsRequestMetadata.File._to_native_list(message.files if message.files else None))

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.body:
			s += f'body: {self.body}, '
		if self.reply_id:
			s += f'reply_id: ({self.reply_id}), '
		if self.ephemerality:
			s += f'ephemerality: ({self.ephemerality}), '
		if self.disable_link_preview:
			s += f'disable_link_preview: {self.disable_link_preview}, '
		if self.files:
			s += f'files: {[str(el) for el in self.files]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageSendWithAttachmentsRequestMetadata):
			return False
		return self.discussion_id == other.discussion_id and self.body == other.body and self.reply_id == other.reply_id and self.ephemerality == other.ephemerality and self.disable_link_preview == other.disable_link_preview and self.files == other.files

	def __bool__(self):
		return self.discussion_id != 0 or self.body != "" or bool(self.reply_id) or bool(self.ephemerality) or self.disable_link_preview or bool(self.files)

	def __hash__(self):
		return hash((self.discussion_id, self.body, self.reply_id, self.ephemerality, self.disable_link_preview, tuple(self.files)))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageSendWithAttachmentsRequestMetadata):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.body == "" or self.body == expected.body, "Invalid value: body: " + str(expected.body) + " != " + str(self.body)
		try:
			assert expected.reply_id is None or self.reply_id._test_assertion(expected.reply_id)
		except AssertionError as e:
			raise AssertionError("reply_id: " + str(e))
		try:
			assert expected.ephemerality is None or self.ephemerality._test_assertion(expected.ephemerality)
		except AssertionError as e:
			raise AssertionError("ephemerality: " + str(e))
		assert expected.disable_link_preview is False or self.disable_link_preview == expected.disable_link_preview, "Invalid value: disable_link_preview: " + str(expected.disable_link_preview) + " != " + str(self.disable_link_preview)
		pass  # print("Warning: test_assertion: skipped a list field files")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageSendWithAttachmentsResponse:
	def __init__(self, client: OlvidClient = None, message: "Message" = None, attachments: "list[Attachment]" = None):
		self._client: OlvidClient = client
		self.message: Message = message
		self.attachments: list[Attachment] = attachments

	def _update_content(self, message_send_with_attachments_response: MessageSendWithAttachmentsResponse) -> None:
		self.message: Message = message_send_with_attachments_response.message
		self.attachments: list[Attachment] = message_send_with_attachments_response.attachments

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendWithAttachmentsResponse":
		return MessageSendWithAttachmentsResponse(client=self._client, message=self.message._clone(), attachments=[e._clone() for e in self.attachments])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsResponse, client: OlvidClient = None) -> "MessageSendWithAttachmentsResponse":
		return MessageSendWithAttachmentsResponse(client, message=Message._from_native(native_message.message, client=client), attachments=Attachment._from_native_list(native_message.attachments, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsResponse], client: OlvidClient = None) -> list["MessageSendWithAttachmentsResponse"]:
		return [MessageSendWithAttachmentsResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsResponse], client: OlvidClient = None) -> "MessageSendWithAttachmentsResponse":
		native_message = await promise
		return MessageSendWithAttachmentsResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageSendWithAttachmentsResponse"]):
		if messages is None:
			return []
		return [MessageSendWithAttachmentsResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageSendWithAttachmentsResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsResponse(message=Message._to_native(message.message if message.message else None), attachments=Attachment._to_native_list(message.attachments if message.attachments else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		if self.attachments:
			s += f'attachments: {[str(el) for el in self.attachments]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageSendWithAttachmentsResponse):
			return False
		return self.message == other.message and self.attachments == other.attachments

	def __bool__(self):
		return bool(self.message) or bool(self.attachments)

	def __hash__(self):
		return hash((self.message, tuple(self.attachments)))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageSendWithAttachmentsResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		pass  # print("Warning: test_assertion: skipped a list field attachments")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageReactRequest:
	def __init__(self, client: OlvidClient = None, message_id: "MessageId" = None, reaction: str = ""):
		self._client: OlvidClient = client
		self.message_id: MessageId = message_id
		self.reaction: str = reaction

	def _update_content(self, message_react_request: MessageReactRequest) -> None:
		self.message_id: MessageId = message_react_request.message_id
		self.reaction: str = message_react_request.reaction

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageReactRequest":
		return MessageReactRequest(client=self._client, message_id=self.message_id._clone(), reaction=self.reaction)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageReactRequest, client: OlvidClient = None) -> "MessageReactRequest":
		return MessageReactRequest(client, message_id=MessageId._from_native(native_message.message_id, client=client), reaction=native_message.reaction)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageReactRequest], client: OlvidClient = None) -> list["MessageReactRequest"]:
		return [MessageReactRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageReactRequest], client: OlvidClient = None) -> "MessageReactRequest":
		native_message = await promise
		return MessageReactRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageReactRequest"]):
		if messages is None:
			return []
		return [MessageReactRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageReactRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageReactRequest(message_id=MessageId._to_native(message.message_id if message.message_id else None), reaction=message.reaction if message.reaction else None)

	def __str__(self):
		s: str = ''
		if self.message_id:
			s += f'message_id: ({self.message_id}), '
		if self.reaction:
			s += f'reaction: {self.reaction}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageReactRequest):
			return False
		return self.message_id == other.message_id and self.reaction == other.reaction

	def __bool__(self):
		return bool(self.message_id) or self.reaction != ""

	def __hash__(self):
		return hash((self.message_id, self.reaction))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageReactRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message_id is None or self.message_id._test_assertion(expected.message_id)
		except AssertionError as e:
			raise AssertionError("message_id: " + str(e))
		assert expected.reaction == "" or self.reaction == expected.reaction, "Invalid value: reaction: " + str(expected.reaction) + " != " + str(self.reaction)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageReactResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, message_react_response: MessageReactResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageReactResponse":
		return MessageReactResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageReactResponse, client: OlvidClient = None) -> "MessageReactResponse":
		return MessageReactResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageReactResponse], client: OlvidClient = None) -> list["MessageReactResponse"]:
		return [MessageReactResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageReactResponse], client: OlvidClient = None) -> "MessageReactResponse":
		native_message = await promise
		return MessageReactResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageReactResponse"]):
		if messages is None:
			return []
		return [MessageReactResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageReactResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageReactResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageReactResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageReactResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageUpdateBodyRequest:
	def __init__(self, client: OlvidClient = None, message_id: "MessageId" = None, updated_body: str = ""):
		self._client: OlvidClient = client
		self.message_id: MessageId = message_id
		self.updated_body: str = updated_body

	def _update_content(self, message_update_body_request: MessageUpdateBodyRequest) -> None:
		self.message_id: MessageId = message_update_body_request.message_id
		self.updated_body: str = message_update_body_request.updated_body

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageUpdateBodyRequest":
		return MessageUpdateBodyRequest(client=self._client, message_id=self.message_id._clone(), updated_body=self.updated_body)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyRequest, client: OlvidClient = None) -> "MessageUpdateBodyRequest":
		return MessageUpdateBodyRequest(client, message_id=MessageId._from_native(native_message.message_id, client=client), updated_body=native_message.updated_body)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyRequest], client: OlvidClient = None) -> list["MessageUpdateBodyRequest"]:
		return [MessageUpdateBodyRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyRequest], client: OlvidClient = None) -> "MessageUpdateBodyRequest":
		native_message = await promise
		return MessageUpdateBodyRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageUpdateBodyRequest"]):
		if messages is None:
			return []
		return [MessageUpdateBodyRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageUpdateBodyRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyRequest(message_id=MessageId._to_native(message.message_id if message.message_id else None), updated_body=message.updated_body if message.updated_body else None)

	def __str__(self):
		s: str = ''
		if self.message_id:
			s += f'message_id: ({self.message_id}), '
		if self.updated_body:
			s += f'updated_body: {self.updated_body}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageUpdateBodyRequest):
			return False
		return self.message_id == other.message_id and self.updated_body == other.updated_body

	def __bool__(self):
		return bool(self.message_id) or self.updated_body != ""

	def __hash__(self):
		return hash((self.message_id, self.updated_body))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageUpdateBodyRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message_id is None or self.message_id._test_assertion(expected.message_id)
		except AssertionError as e:
			raise AssertionError("message_id: " + str(e))
		assert expected.updated_body == "" or self.updated_body == expected.updated_body, "Invalid value: updated_body: " + str(expected.updated_body) + " != " + str(self.updated_body)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageUpdateBodyResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, message_update_body_response: MessageUpdateBodyResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageUpdateBodyResponse":
		return MessageUpdateBodyResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyResponse, client: OlvidClient = None) -> "MessageUpdateBodyResponse":
		return MessageUpdateBodyResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyResponse], client: OlvidClient = None) -> list["MessageUpdateBodyResponse"]:
		return [MessageUpdateBodyResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyResponse], client: OlvidClient = None) -> "MessageUpdateBodyResponse":
		native_message = await promise
		return MessageUpdateBodyResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageUpdateBodyResponse"]):
		if messages is None:
			return []
		return [MessageUpdateBodyResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageUpdateBodyResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageUpdateBodyResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageUpdateBodyResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageSendVoipRequest:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id

	def _update_content(self, message_send_voip_request: MessageSendVoipRequest) -> None:
		self.discussion_id: int = message_send_voip_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendVoipRequest":
		return MessageSendVoipRequest(client=self._client, discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendVoipRequest, client: OlvidClient = None) -> "MessageSendVoipRequest":
		return MessageSendVoipRequest(client, discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendVoipRequest], client: OlvidClient = None) -> list["MessageSendVoipRequest"]:
		return [MessageSendVoipRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendVoipRequest], client: OlvidClient = None) -> "MessageSendVoipRequest":
		native_message = await promise
		return MessageSendVoipRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageSendVoipRequest"]):
		if messages is None:
			return []
		return [MessageSendVoipRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageSendVoipRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageSendVoipRequest(discussion_id=message.discussion_id if message.discussion_id else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageSendVoipRequest):
			return False
		return self.discussion_id == other.discussion_id

	def __bool__(self):
		return self.discussion_id != 0

	def __hash__(self):
		return hash(self.discussion_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageSendVoipRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageSendVoipResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, message_send_voip_response: MessageSendVoipResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendVoipResponse":
		return MessageSendVoipResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendVoipResponse, client: OlvidClient = None) -> "MessageSendVoipResponse":
		return MessageSendVoipResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendVoipResponse], client: OlvidClient = None) -> list["MessageSendVoipResponse"]:
		return [MessageSendVoipResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendVoipResponse], client: OlvidClient = None) -> "MessageSendVoipResponse":
		native_message = await promise
		return MessageSendVoipResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageSendVoipResponse"]):
		if messages is None:
			return []
		return [MessageSendVoipResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageSendVoipResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageSendVoipResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageSendVoipResponse):
			return False
		return 

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageSendVoipResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageListRequest:
	def __init__(self, client: OlvidClient = None, filter: "StorageElementFilter" = None):
		self._client: OlvidClient = client
		self.filter: StorageElementFilter = filter

	def _update_content(self, storage_list_request: StorageListRequest) -> None:
		self.filter: StorageElementFilter = storage_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageListRequest":
		return StorageListRequest(client=self._client, filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageListRequest, client: OlvidClient = None) -> "StorageListRequest":
		return StorageListRequest(client, filter=StorageElementFilter._from_native(native_message.filter, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageListRequest], client: OlvidClient = None) -> list["StorageListRequest"]:
		return [StorageListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageListRequest], client: OlvidClient = None) -> "StorageListRequest":
		native_message = await promise
		return StorageListRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["StorageListRequest"]):
		if messages is None:
			return []
		return [StorageListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["StorageListRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.StorageListRequest(filter=StorageElementFilter._to_native(message.filter if message.filter else None))

	def __str__(self):
		s: str = ''
		if self.filter:
			s += f'filter: ({self.filter}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, StorageListRequest):
			return False
		return self.filter == other.filter

	def __bool__(self):
		return bool(self.filter)

	def __hash__(self):
		return hash(self.filter)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, StorageListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageListResponse:
	def __init__(self, client: OlvidClient = None, elements: "list[StorageElement]" = None):
		self._client: OlvidClient = client
		self.elements: list[StorageElement] = elements

	def _update_content(self, storage_list_response: StorageListResponse) -> None:
		self.elements: list[StorageElement] = storage_list_response.elements

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageListResponse":
		return StorageListResponse(client=self._client, elements=[e._clone() for e in self.elements])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageListResponse, client: OlvidClient = None) -> "StorageListResponse":
		return StorageListResponse(client, elements=StorageElement._from_native_list(native_message.elements, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageListResponse], client: OlvidClient = None) -> list["StorageListResponse"]:
		return [StorageListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageListResponse], client: OlvidClient = None) -> "StorageListResponse":
		native_message = await promise
		return StorageListResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["StorageListResponse"]):
		if messages is None:
			return []
		return [StorageListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["StorageListResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.StorageListResponse(elements=StorageElement._to_native_list(message.elements if message.elements else None))

	def __str__(self):
		s: str = ''
		if self.elements:
			s += f'elements: {[str(el) for el in self.elements]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, StorageListResponse):
			return False
		return self.elements == other.elements

	def __bool__(self):
		return bool(self.elements)

	def __hash__(self):
		return hash(tuple(self.elements))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, StorageListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field elements")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageGetRequest:
	def __init__(self, client: OlvidClient = None, key: str = ""):
		self._client: OlvidClient = client
		self.key: str = key

	def _update_content(self, storage_get_request: StorageGetRequest) -> None:
		self.key: str = storage_get_request.key

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageGetRequest":
		return StorageGetRequest(client=self._client, key=self.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageGetRequest, client: OlvidClient = None) -> "StorageGetRequest":
		return StorageGetRequest(client, key=native_message.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageGetRequest], client: OlvidClient = None) -> list["StorageGetRequest"]:
		return [StorageGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageGetRequest], client: OlvidClient = None) -> "StorageGetRequest":
		native_message = await promise
		return StorageGetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["StorageGetRequest"]):
		if messages is None:
			return []
		return [StorageGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["StorageGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.StorageGetRequest(key=message.key if message.key else None)

	def __str__(self):
		s: str = ''
		if self.key:
			s += f'key: {self.key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, StorageGetRequest):
			return False
		return self.key == other.key

	def __bool__(self):
		return self.key != ""

	def __hash__(self):
		return hash(self.key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, StorageGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.key == "" or self.key == expected.key, "Invalid value: key: " + str(expected.key) + " != " + str(self.key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageGetResponse:
	def __init__(self, client: OlvidClient = None, value: str = ""):
		self._client: OlvidClient = client
		self.value: str = value

	def _update_content(self, storage_get_response: StorageGetResponse) -> None:
		self.value: str = storage_get_response.value

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageGetResponse":
		return StorageGetResponse(client=self._client, value=self.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageGetResponse, client: OlvidClient = None) -> "StorageGetResponse":
		return StorageGetResponse(client, value=native_message.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageGetResponse], client: OlvidClient = None) -> list["StorageGetResponse"]:
		return [StorageGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageGetResponse], client: OlvidClient = None) -> "StorageGetResponse":
		native_message = await promise
		return StorageGetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["StorageGetResponse"]):
		if messages is None:
			return []
		return [StorageGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["StorageGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.StorageGetResponse(value=message.value if message.value else None)

	def __str__(self):
		s: str = ''
		if self.value:
			s += f'value: {self.value}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, StorageGetResponse):
			return False
		return self.value == other.value

	def __bool__(self):
		return self.value != ""

	def __hash__(self):
		return hash(self.value)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, StorageGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.value == "" or self.value == expected.value, "Invalid value: value: " + str(expected.value) + " != " + str(self.value)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageSetRequest:
	def __init__(self, client: OlvidClient = None, key: str = "", value: str = ""):
		self._client: OlvidClient = client
		self.key: str = key
		self.value: str = value

	def _update_content(self, storage_set_request: StorageSetRequest) -> None:
		self.key: str = storage_set_request.key
		self.value: str = storage_set_request.value

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageSetRequest":
		return StorageSetRequest(client=self._client, key=self.key, value=self.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageSetRequest, client: OlvidClient = None) -> "StorageSetRequest":
		return StorageSetRequest(client, key=native_message.key, value=native_message.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageSetRequest], client: OlvidClient = None) -> list["StorageSetRequest"]:
		return [StorageSetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageSetRequest], client: OlvidClient = None) -> "StorageSetRequest":
		native_message = await promise
		return StorageSetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["StorageSetRequest"]):
		if messages is None:
			return []
		return [StorageSetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["StorageSetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.StorageSetRequest(key=message.key if message.key else None, value=message.value if message.value else None)

	def __str__(self):
		s: str = ''
		if self.key:
			s += f'key: {self.key}, '
		if self.value:
			s += f'value: {self.value}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, StorageSetRequest):
			return False
		return self.key == other.key and self.value == other.value

	def __bool__(self):
		return self.key != "" or self.value != ""

	def __hash__(self):
		return hash((self.key, self.value))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, StorageSetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.key == "" or self.key == expected.key, "Invalid value: key: " + str(expected.key) + " != " + str(self.key)
		assert expected.value == "" or self.value == expected.value, "Invalid value: value: " + str(expected.value) + " != " + str(self.value)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageSetResponse:
	def __init__(self, client: OlvidClient = None, previous_value: str = ""):
		self._client: OlvidClient = client
		self.previous_value: str = previous_value

	def _update_content(self, storage_set_response: StorageSetResponse) -> None:
		self.previous_value: str = storage_set_response.previous_value

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageSetResponse":
		return StorageSetResponse(client=self._client, previous_value=self.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageSetResponse, client: OlvidClient = None) -> "StorageSetResponse":
		return StorageSetResponse(client, previous_value=native_message.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageSetResponse], client: OlvidClient = None) -> list["StorageSetResponse"]:
		return [StorageSetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageSetResponse], client: OlvidClient = None) -> "StorageSetResponse":
		native_message = await promise
		return StorageSetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["StorageSetResponse"]):
		if messages is None:
			return []
		return [StorageSetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["StorageSetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.StorageSetResponse(previous_value=message.previous_value if message.previous_value else None)

	def __str__(self):
		s: str = ''
		if self.previous_value:
			s += f'previous_value: {self.previous_value}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, StorageSetResponse):
			return False
		return self.previous_value == other.previous_value

	def __bool__(self):
		return self.previous_value != ""

	def __hash__(self):
		return hash(self.previous_value)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, StorageSetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.previous_value == "" or self.previous_value == expected.previous_value, "Invalid value: previous_value: " + str(expected.previous_value) + " != " + str(self.previous_value)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageUnsetRequest:
	def __init__(self, client: OlvidClient = None, key: str = ""):
		self._client: OlvidClient = client
		self.key: str = key

	def _update_content(self, storage_unset_request: StorageUnsetRequest) -> None:
		self.key: str = storage_unset_request.key

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageUnsetRequest":
		return StorageUnsetRequest(client=self._client, key=self.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetRequest, client: OlvidClient = None) -> "StorageUnsetRequest":
		return StorageUnsetRequest(client, key=native_message.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetRequest], client: OlvidClient = None) -> list["StorageUnsetRequest"]:
		return [StorageUnsetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetRequest], client: OlvidClient = None) -> "StorageUnsetRequest":
		native_message = await promise
		return StorageUnsetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["StorageUnsetRequest"]):
		if messages is None:
			return []
		return [StorageUnsetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["StorageUnsetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetRequest(key=message.key if message.key else None)

	def __str__(self):
		s: str = ''
		if self.key:
			s += f'key: {self.key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, StorageUnsetRequest):
			return False
		return self.key == other.key

	def __bool__(self):
		return self.key != ""

	def __hash__(self):
		return hash(self.key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, StorageUnsetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.key == "" or self.key == expected.key, "Invalid value: key: " + str(expected.key) + " != " + str(self.key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageUnsetResponse:
	def __init__(self, client: OlvidClient = None, previous_value: str = ""):
		self._client: OlvidClient = client
		self.previous_value: str = previous_value

	def _update_content(self, storage_unset_response: StorageUnsetResponse) -> None:
		self.previous_value: str = storage_unset_response.previous_value

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageUnsetResponse":
		return StorageUnsetResponse(client=self._client, previous_value=self.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetResponse, client: OlvidClient = None) -> "StorageUnsetResponse":
		return StorageUnsetResponse(client, previous_value=native_message.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetResponse], client: OlvidClient = None) -> list["StorageUnsetResponse"]:
		return [StorageUnsetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetResponse], client: OlvidClient = None) -> "StorageUnsetResponse":
		native_message = await promise
		return StorageUnsetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["StorageUnsetResponse"]):
		if messages is None:
			return []
		return [StorageUnsetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["StorageUnsetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetResponse(previous_value=message.previous_value if message.previous_value else None)

	def __str__(self):
		s: str = ''
		if self.previous_value:
			s += f'previous_value: {self.previous_value}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, StorageUnsetResponse):
			return False
		return self.previous_value == other.previous_value

	def __bool__(self):
		return self.previous_value != ""

	def __hash__(self):
		return hash(self.previous_value)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, StorageUnsetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.previous_value == "" or self.previous_value == expected.previous_value, "Invalid value: previous_value: " + str(expected.previous_value) + " != " + str(self.previous_value)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionStorageListRequest:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0, filter: "StorageElementFilter" = None):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id
		self.filter: StorageElementFilter = filter

	def _update_content(self, discussion_storage_list_request: DiscussionStorageListRequest) -> None:
		self.discussion_id: int = discussion_storage_list_request.discussion_id
		self.filter: StorageElementFilter = discussion_storage_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageListRequest":
		return DiscussionStorageListRequest(client=self._client, discussion_id=self.discussion_id, filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListRequest, client: OlvidClient = None) -> "DiscussionStorageListRequest":
		return DiscussionStorageListRequest(client, discussion_id=native_message.discussion_id, filter=StorageElementFilter._from_native(native_message.filter, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListRequest], client: OlvidClient = None) -> list["DiscussionStorageListRequest"]:
		return [DiscussionStorageListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListRequest], client: OlvidClient = None) -> "DiscussionStorageListRequest":
		native_message = await promise
		return DiscussionStorageListRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionStorageListRequest"]):
		if messages is None:
			return []
		return [DiscussionStorageListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionStorageListRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListRequest(discussion_id=message.discussion_id if message.discussion_id else None, filter=StorageElementFilter._to_native(message.filter if message.filter else None))

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.filter:
			s += f'filter: ({self.filter}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionStorageListRequest):
			return False
		return self.discussion_id == other.discussion_id and self.filter == other.filter

	def __bool__(self):
		return self.discussion_id != 0 or bool(self.filter)

	def __hash__(self):
		return hash((self.discussion_id, self.filter))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionStorageListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionStorageListResponse:
	def __init__(self, client: OlvidClient = None, elements: "list[StorageElement]" = None):
		self._client: OlvidClient = client
		self.elements: list[StorageElement] = elements

	def _update_content(self, discussion_storage_list_response: DiscussionStorageListResponse) -> None:
		self.elements: list[StorageElement] = discussion_storage_list_response.elements

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageListResponse":
		return DiscussionStorageListResponse(client=self._client, elements=[e._clone() for e in self.elements])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListResponse, client: OlvidClient = None) -> "DiscussionStorageListResponse":
		return DiscussionStorageListResponse(client, elements=StorageElement._from_native_list(native_message.elements, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListResponse], client: OlvidClient = None) -> list["DiscussionStorageListResponse"]:
		return [DiscussionStorageListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListResponse], client: OlvidClient = None) -> "DiscussionStorageListResponse":
		native_message = await promise
		return DiscussionStorageListResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionStorageListResponse"]):
		if messages is None:
			return []
		return [DiscussionStorageListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionStorageListResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListResponse(elements=StorageElement._to_native_list(message.elements if message.elements else None))

	def __str__(self):
		s: str = ''
		if self.elements:
			s += f'elements: {[str(el) for el in self.elements]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionStorageListResponse):
			return False
		return self.elements == other.elements

	def __bool__(self):
		return bool(self.elements)

	def __hash__(self):
		return hash(tuple(self.elements))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionStorageListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field elements")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionStorageGetRequest:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0, key: str = ""):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id
		self.key: str = key

	def _update_content(self, discussion_storage_get_request: DiscussionStorageGetRequest) -> None:
		self.discussion_id: int = discussion_storage_get_request.discussion_id
		self.key: str = discussion_storage_get_request.key

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageGetRequest":
		return DiscussionStorageGetRequest(client=self._client, discussion_id=self.discussion_id, key=self.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetRequest, client: OlvidClient = None) -> "DiscussionStorageGetRequest":
		return DiscussionStorageGetRequest(client, discussion_id=native_message.discussion_id, key=native_message.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetRequest], client: OlvidClient = None) -> list["DiscussionStorageGetRequest"]:
		return [DiscussionStorageGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetRequest], client: OlvidClient = None) -> "DiscussionStorageGetRequest":
		native_message = await promise
		return DiscussionStorageGetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionStorageGetRequest"]):
		if messages is None:
			return []
		return [DiscussionStorageGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionStorageGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetRequest(discussion_id=message.discussion_id if message.discussion_id else None, key=message.key if message.key else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.key:
			s += f'key: {self.key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionStorageGetRequest):
			return False
		return self.discussion_id == other.discussion_id and self.key == other.key

	def __bool__(self):
		return self.discussion_id != 0 or self.key != ""

	def __hash__(self):
		return hash((self.discussion_id, self.key))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionStorageGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.key == "" or self.key == expected.key, "Invalid value: key: " + str(expected.key) + " != " + str(self.key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionStorageGetResponse:
	def __init__(self, client: OlvidClient = None, value: str = ""):
		self._client: OlvidClient = client
		self.value: str = value

	def _update_content(self, discussion_storage_get_response: DiscussionStorageGetResponse) -> None:
		self.value: str = discussion_storage_get_response.value

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageGetResponse":
		return DiscussionStorageGetResponse(client=self._client, value=self.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetResponse, client: OlvidClient = None) -> "DiscussionStorageGetResponse":
		return DiscussionStorageGetResponse(client, value=native_message.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetResponse], client: OlvidClient = None) -> list["DiscussionStorageGetResponse"]:
		return [DiscussionStorageGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetResponse], client: OlvidClient = None) -> "DiscussionStorageGetResponse":
		native_message = await promise
		return DiscussionStorageGetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionStorageGetResponse"]):
		if messages is None:
			return []
		return [DiscussionStorageGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionStorageGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetResponse(value=message.value if message.value else None)

	def __str__(self):
		s: str = ''
		if self.value:
			s += f'value: {self.value}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionStorageGetResponse):
			return False
		return self.value == other.value

	def __bool__(self):
		return self.value != ""

	def __hash__(self):
		return hash(self.value)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionStorageGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.value == "" or self.value == expected.value, "Invalid value: value: " + str(expected.value) + " != " + str(self.value)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionStorageSetRequest:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0, key: str = "", value: str = ""):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id
		self.key: str = key
		self.value: str = value

	def _update_content(self, discussion_storage_set_request: DiscussionStorageSetRequest) -> None:
		self.discussion_id: int = discussion_storage_set_request.discussion_id
		self.key: str = discussion_storage_set_request.key
		self.value: str = discussion_storage_set_request.value

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageSetRequest":
		return DiscussionStorageSetRequest(client=self._client, discussion_id=self.discussion_id, key=self.key, value=self.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetRequest, client: OlvidClient = None) -> "DiscussionStorageSetRequest":
		return DiscussionStorageSetRequest(client, discussion_id=native_message.discussion_id, key=native_message.key, value=native_message.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetRequest], client: OlvidClient = None) -> list["DiscussionStorageSetRequest"]:
		return [DiscussionStorageSetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetRequest], client: OlvidClient = None) -> "DiscussionStorageSetRequest":
		native_message = await promise
		return DiscussionStorageSetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionStorageSetRequest"]):
		if messages is None:
			return []
		return [DiscussionStorageSetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionStorageSetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetRequest(discussion_id=message.discussion_id if message.discussion_id else None, key=message.key if message.key else None, value=message.value if message.value else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.key:
			s += f'key: {self.key}, '
		if self.value:
			s += f'value: {self.value}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionStorageSetRequest):
			return False
		return self.discussion_id == other.discussion_id and self.key == other.key and self.value == other.value

	def __bool__(self):
		return self.discussion_id != 0 or self.key != "" or self.value != ""

	def __hash__(self):
		return hash((self.discussion_id, self.key, self.value))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionStorageSetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.key == "" or self.key == expected.key, "Invalid value: key: " + str(expected.key) + " != " + str(self.key)
		assert expected.value == "" or self.value == expected.value, "Invalid value: value: " + str(expected.value) + " != " + str(self.value)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionStorageSetResponse:
	def __init__(self, client: OlvidClient = None, previous_value: str = ""):
		self._client: OlvidClient = client
		self.previous_value: str = previous_value

	def _update_content(self, discussion_storage_set_response: DiscussionStorageSetResponse) -> None:
		self.previous_value: str = discussion_storage_set_response.previous_value

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageSetResponse":
		return DiscussionStorageSetResponse(client=self._client, previous_value=self.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetResponse, client: OlvidClient = None) -> "DiscussionStorageSetResponse":
		return DiscussionStorageSetResponse(client, previous_value=native_message.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetResponse], client: OlvidClient = None) -> list["DiscussionStorageSetResponse"]:
		return [DiscussionStorageSetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetResponse], client: OlvidClient = None) -> "DiscussionStorageSetResponse":
		native_message = await promise
		return DiscussionStorageSetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionStorageSetResponse"]):
		if messages is None:
			return []
		return [DiscussionStorageSetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionStorageSetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetResponse(previous_value=message.previous_value if message.previous_value else None)

	def __str__(self):
		s: str = ''
		if self.previous_value:
			s += f'previous_value: {self.previous_value}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionStorageSetResponse):
			return False
		return self.previous_value == other.previous_value

	def __bool__(self):
		return self.previous_value != ""

	def __hash__(self):
		return hash(self.previous_value)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionStorageSetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.previous_value == "" or self.previous_value == expected.previous_value, "Invalid value: previous_value: " + str(expected.previous_value) + " != " + str(self.previous_value)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionStorageUnsetRequest:
	def __init__(self, client: OlvidClient = None, discussion_id: int = 0, key: str = ""):
		self._client: OlvidClient = client
		self.discussion_id: int = discussion_id
		self.key: str = key

	def _update_content(self, discussion_storage_unset_request: DiscussionStorageUnsetRequest) -> None:
		self.discussion_id: int = discussion_storage_unset_request.discussion_id
		self.key: str = discussion_storage_unset_request.key

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageUnsetRequest":
		return DiscussionStorageUnsetRequest(client=self._client, discussion_id=self.discussion_id, key=self.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetRequest, client: OlvidClient = None) -> "DiscussionStorageUnsetRequest":
		return DiscussionStorageUnsetRequest(client, discussion_id=native_message.discussion_id, key=native_message.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetRequest], client: OlvidClient = None) -> list["DiscussionStorageUnsetRequest"]:
		return [DiscussionStorageUnsetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetRequest], client: OlvidClient = None) -> "DiscussionStorageUnsetRequest":
		native_message = await promise
		return DiscussionStorageUnsetRequest._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionStorageUnsetRequest"]):
		if messages is None:
			return []
		return [DiscussionStorageUnsetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionStorageUnsetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetRequest(discussion_id=message.discussion_id if message.discussion_id else None, key=message.key if message.key else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.key:
			s += f'key: {self.key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionStorageUnsetRequest):
			return False
		return self.discussion_id == other.discussion_id and self.key == other.key

	def __bool__(self):
		return self.discussion_id != 0 or self.key != ""

	def __hash__(self):
		return hash((self.discussion_id, self.key))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionStorageUnsetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.key == "" or self.key == expected.key, "Invalid value: key: " + str(expected.key) + " != " + str(self.key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionStorageUnsetResponse:
	def __init__(self, client: OlvidClient = None, previous_value: str = ""):
		self._client: OlvidClient = client
		self.previous_value: str = previous_value

	def _update_content(self, discussion_storage_unset_response: DiscussionStorageUnsetResponse) -> None:
		self.previous_value: str = discussion_storage_unset_response.previous_value

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageUnsetResponse":
		return DiscussionStorageUnsetResponse(client=self._client, previous_value=self.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetResponse, client: OlvidClient = None) -> "DiscussionStorageUnsetResponse":
		return DiscussionStorageUnsetResponse(client, previous_value=native_message.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetResponse], client: OlvidClient = None) -> list["DiscussionStorageUnsetResponse"]:
		return [DiscussionStorageUnsetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetResponse], client: OlvidClient = None) -> "DiscussionStorageUnsetResponse":
		native_message = await promise
		return DiscussionStorageUnsetResponse._from_native(native_message, client=client)

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionStorageUnsetResponse"]):
		if messages is None:
			return []
		return [DiscussionStorageUnsetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionStorageUnsetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetResponse(previous_value=message.previous_value if message.previous_value else None)

	def __str__(self):
		s: str = ''
		if self.previous_value:
			s += f'previous_value: {self.previous_value}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionStorageUnsetResponse):
			return False
		return self.previous_value == other.previous_value

	def __bool__(self):
		return self.previous_value != ""

	def __hash__(self):
		return hash(self.previous_value)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionStorageUnsetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.previous_value == "" or self.previous_value == expected.previous_value, "Invalid value: previous_value: " + str(expected.previous_value) + " != " + str(self.previous_value)
		return True


class IdentityCommandServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.IdentityCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.IdentityCommandServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_get(self, identity_get_request: IdentityGetRequest) -> Coroutine[Any, Any, IdentityGetResponse]:
		overlay_object = identity_get_request
		return IdentityGetResponse._from_native_promise(self.__stub.IdentityGet(olvid.daemon.command.v1.identity_commands_pb2.IdentityGetRequest(), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_update_details(self, identity_update_details_request: IdentityUpdateDetailsRequest) -> Coroutine[Any, Any, IdentityUpdateDetailsResponse]:
		overlay_object = identity_update_details_request
		return IdentityUpdateDetailsResponse._from_native_promise(self.__stub.IdentityUpdateDetails(olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsRequest(new_details=IdentityDetails._to_native(overlay_object.new_details)), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_remove_photo(self, identity_remove_photo_request: IdentityRemovePhotoRequest) -> Coroutine[Any, Any, IdentityRemovePhotoResponse]:
		overlay_object = identity_remove_photo_request
		return IdentityRemovePhotoResponse._from_native_promise(self.__stub.IdentityRemovePhoto(olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoRequest(), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_set_photo(self, identity_set_photo_request_iterator: AsyncIterator[IdentitySetPhotoRequest]) -> Coroutine[Any, Any, IdentitySetPhotoResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def request_iterator(iterator: AsyncIterator[IdentitySetPhotoRequest]):
			async for message in iterator.__aiter__():
				yield IdentitySetPhotoRequest._to_native(message)
		return IdentitySetPhotoResponse._from_native_promise(self.__stub.IdentitySetPhoto(request_iterator(identity_set_photo_request_iterator), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_keycloak_bind(self, identity_keycloak_bind_request: IdentityKeycloakBindRequest) -> Coroutine[Any, Any, IdentityKeycloakBindResponse]:
		overlay_object = identity_keycloak_bind_request
		return IdentityKeycloakBindResponse._from_native_promise(self.__stub.IdentityKeycloakBind(olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakBindRequest(configuration_link=overlay_object.configuration_link), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_keycloak_unbind(self, identity_keycloak_unbind_request: IdentityKeycloakUnbindRequest) -> Coroutine[Any, Any, IdentityKeycloakUnbindResponse]:
		overlay_object = identity_keycloak_unbind_request
		return IdentityKeycloakUnbindResponse._from_native_promise(self.__stub.IdentityKeycloakUnbind(olvid.daemon.command.v1.identity_commands_pb2.IdentityKeycloakUnbindRequest(), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_set_api_key(self, identity_set_api_key_request: IdentitySetApiKeyRequest) -> Coroutine[Any, Any, IdentitySetApiKeyResponse]:
		overlay_object = identity_set_api_key_request
		return IdentitySetApiKeyResponse._from_native_promise(self.__stub.IdentitySetApiKey(olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyRequest(api_key=overlay_object.api_key), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_set_configuration_link(self, identity_set_configuration_link_request: IdentitySetConfigurationLinkRequest) -> Coroutine[Any, Any, IdentitySetConfigurationLinkResponse]:
		overlay_object = identity_set_configuration_link_request
		return IdentitySetConfigurationLinkResponse._from_native_promise(self.__stub.IdentitySetConfigurationLink(olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkRequest(configuration_link=overlay_object.configuration_link), metadata=self._client.grpc_metadata), client=self._client)


class InvitationCommandServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.InvitationCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.InvitationCommandServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_list(self, invitation_list_request: InvitationListRequest) -> AsyncIterator[InvitationListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.invitation_commands_pb2.InvitationListResponse]) -> AsyncIterator[InvitationListResponse]:
			async for native_message in iterator.__aiter__():
				yield InvitationListResponse._from_native(native_message, client=self._client)
		overlay_object = invitation_list_request
		return response_iterator(self.__stub.InvitationList(olvid.daemon.command.v1.invitation_commands_pb2.InvitationListRequest(filter=InvitationFilter._to_native(overlay_object.filter)), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_get(self, invitation_get_request: InvitationGetRequest) -> Coroutine[Any, Any, InvitationGetResponse]:
		overlay_object = invitation_get_request
		return InvitationGetResponse._from_native_promise(self.__stub.InvitationGet(olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetRequest(invitation_id=overlay_object.invitation_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_new(self, invitation_new_request: InvitationNewRequest) -> Coroutine[Any, Any, InvitationNewResponse]:
		overlay_object = invitation_new_request
		return InvitationNewResponse._from_native_promise(self.__stub.InvitationNew(olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewRequest(invitation_url=overlay_object.invitation_url), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_accept(self, invitation_accept_request: InvitationAcceptRequest) -> Coroutine[Any, Any, InvitationAcceptResponse]:
		overlay_object = invitation_accept_request
		return InvitationAcceptResponse._from_native_promise(self.__stub.InvitationAccept(olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptRequest(invitation_id=overlay_object.invitation_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_decline(self, invitation_decline_request: InvitationDeclineRequest) -> Coroutine[Any, Any, InvitationDeclineResponse]:
		overlay_object = invitation_decline_request
		return InvitationDeclineResponse._from_native_promise(self.__stub.InvitationDecline(olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineRequest(invitation_id=overlay_object.invitation_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_sas(self, invitation_sas_request: InvitationSasRequest) -> Coroutine[Any, Any, InvitationSasResponse]:
		overlay_object = invitation_sas_request
		return InvitationSasResponse._from_native_promise(self.__stub.InvitationSas(olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasRequest(invitation_id=overlay_object.invitation_id, sas=overlay_object.sas), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_delete(self, invitation_delete_request: InvitationDeleteRequest) -> Coroutine[Any, Any, InvitationDeleteResponse]:
		overlay_object = invitation_delete_request
		return InvitationDeleteResponse._from_native_promise(self.__stub.InvitationDelete(olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteRequest(invitation_id=overlay_object.invitation_id), metadata=self._client.grpc_metadata), client=self._client)


class ContactCommandServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.ContactCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.ContactCommandServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_list(self, contact_list_request: ContactListRequest) -> AsyncIterator[ContactListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.contact_commands_pb2.ContactListResponse]) -> AsyncIterator[ContactListResponse]:
			async for native_message in iterator.__aiter__():
				yield ContactListResponse._from_native(native_message, client=self._client)
		overlay_object = contact_list_request
		return response_iterator(self.__stub.ContactList(olvid.daemon.command.v1.contact_commands_pb2.ContactListRequest(filter=ContactFilter._to_native(overlay_object.filter)), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_get(self, contact_get_request: ContactGetRequest) -> Coroutine[Any, Any, ContactGetResponse]:
		overlay_object = contact_get_request
		return ContactGetResponse._from_native_promise(self.__stub.ContactGet(olvid.daemon.command.v1.contact_commands_pb2.ContactGetRequest(contact_id=overlay_object.contact_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_delete(self, contact_delete_request: ContactDeleteRequest) -> Coroutine[Any, Any, ContactDeleteResponse]:
		overlay_object = contact_delete_request
		return ContactDeleteResponse._from_native_promise(self.__stub.ContactDelete(olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteRequest(contact_id=overlay_object.contact_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_introduction(self, contact_introduction_request: ContactIntroductionRequest) -> Coroutine[Any, Any, ContactIntroductionResponse]:
		overlay_object = contact_introduction_request
		return ContactIntroductionResponse._from_native_promise(self.__stub.ContactIntroduction(olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionRequest(first_contact_id=overlay_object.first_contact_id, second_contact_id=overlay_object.second_contact_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_invite_to_one_to_one_discussion(self, contact_invite_to_one_to_one_discussion_request: ContactInviteToOneToOneDiscussionRequest) -> Coroutine[Any, Any, ContactInviteToOneToOneDiscussionResponse]:
		overlay_object = contact_invite_to_one_to_one_discussion_request
		return ContactInviteToOneToOneDiscussionResponse._from_native_promise(self.__stub.ContactInviteToOneToOneDiscussion(olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionRequest(contact_id=overlay_object.contact_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_downgrade_one_to_one_discussion(self, contact_downgrade_one_to_one_discussion_request: ContactDowngradeOneToOneDiscussionRequest) -> Coroutine[Any, Any, ContactDowngradeOneToOneDiscussionResponse]:
		overlay_object = contact_downgrade_one_to_one_discussion_request
		return ContactDowngradeOneToOneDiscussionResponse._from_native_promise(self.__stub.ContactDowngradeOneToOneDiscussion(olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionRequest(contact_id=overlay_object.contact_id), metadata=self._client.grpc_metadata), client=self._client)


class GroupCommandServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.GroupCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.GroupCommandServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_list(self, group_list_request: GroupListRequest) -> AsyncIterator[GroupListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.group_commands_pb2.GroupListResponse]) -> AsyncIterator[GroupListResponse]:
			async for native_message in iterator.__aiter__():
				yield GroupListResponse._from_native(native_message, client=self._client)
		overlay_object = group_list_request
		return response_iterator(self.__stub.GroupList(olvid.daemon.command.v1.group_commands_pb2.GroupListRequest(filter=GroupFilter._to_native(overlay_object.filter)), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_get(self, group_get_request: GroupGetRequest) -> Coroutine[Any, Any, GroupGetResponse]:
		overlay_object = group_get_request
		return GroupGetResponse._from_native_promise(self.__stub.GroupGet(olvid.daemon.command.v1.group_commands_pb2.GroupGetRequest(group_id=overlay_object.group_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_new_standard_group(self, group_new_standard_group_request: GroupNewStandardGroupRequest) -> Coroutine[Any, Any, GroupNewStandardGroupResponse]:
		overlay_object = group_new_standard_group_request
		return GroupNewStandardGroupResponse._from_native_promise(self.__stub.GroupNewStandardGroup(olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupRequest(name=overlay_object.name, description=overlay_object.description, admin_contact_ids=overlay_object.admin_contact_ids), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_new_controlled_group(self, group_new_controlled_group_request: GroupNewControlledGroupRequest) -> Coroutine[Any, Any, GroupNewControlledGroupResponse]:
		overlay_object = group_new_controlled_group_request
		return GroupNewControlledGroupResponse._from_native_promise(self.__stub.GroupNewControlledGroup(olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupRequest(name=overlay_object.name, description=overlay_object.description, admin_contact_ids=overlay_object.admin_contact_ids, contact_ids=overlay_object.contact_ids), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_new_read_only_group(self, group_new_read_only_group_request: GroupNewReadOnlyGroupRequest) -> Coroutine[Any, Any, GroupNewReadOnlyGroupResponse]:
		overlay_object = group_new_read_only_group_request
		return GroupNewReadOnlyGroupResponse._from_native_promise(self.__stub.GroupNewReadOnlyGroup(olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupRequest(name=overlay_object.name, description=overlay_object.description, admin_contact_ids=overlay_object.admin_contact_ids, contact_ids=overlay_object.contact_ids), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_new_advanced_group(self, group_new_advanced_group_request: GroupNewAdvancedGroupRequest) -> Coroutine[Any, Any, GroupNewAdvancedGroupResponse]:
		overlay_object = group_new_advanced_group_request
		return GroupNewAdvancedGroupResponse._from_native_promise(self.__stub.GroupNewAdvancedGroup(olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupRequest(name=overlay_object.name, description=overlay_object.description, advanced_configuration=Group.AdvancedConfiguration._to_native(overlay_object.advanced_configuration), members=GroupMember._to_native_list(overlay_object.members)), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_disband(self, group_disband_request: GroupDisbandRequest) -> Coroutine[Any, Any, GroupDisbandResponse]:
		overlay_object = group_disband_request
		return GroupDisbandResponse._from_native_promise(self.__stub.GroupDisband(olvid.daemon.command.v1.group_commands_pb2.GroupDisbandRequest(group_id=overlay_object.group_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_leave(self, group_leave_request: GroupLeaveRequest) -> Coroutine[Any, Any, GroupLeaveResponse]:
		overlay_object = group_leave_request
		return GroupLeaveResponse._from_native_promise(self.__stub.GroupLeave(olvid.daemon.command.v1.group_commands_pb2.GroupLeaveRequest(group_id=overlay_object.group_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_update(self, group_update_request: GroupUpdateRequest) -> Coroutine[Any, Any, GroupUpdateResponse]:
		overlay_object = group_update_request
		return GroupUpdateResponse._from_native_promise(self.__stub.GroupUpdate(olvid.daemon.command.v1.group_commands_pb2.GroupUpdateRequest(group=Group._to_native(overlay_object.group)), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_unset_photo(self, group_unset_photo_request: GroupUnsetPhotoRequest) -> Coroutine[Any, Any, GroupUnsetPhotoResponse]:
		overlay_object = group_unset_photo_request
		return GroupUnsetPhotoResponse._from_native_promise(self.__stub.GroupUnsetPhoto(olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoRequest(group_id=overlay_object.group_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_set_photo(self, group_set_photo_request_iterator: AsyncIterator[GroupSetPhotoRequest]) -> Coroutine[Any, Any, GroupSetPhotoResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def request_iterator(iterator: AsyncIterator[GroupSetPhotoRequest]):
			async for message in iterator.__aiter__():
				yield GroupSetPhotoRequest._to_native(message)
		return GroupSetPhotoResponse._from_native_promise(self.__stub.GroupSetPhoto(request_iterator(group_set_photo_request_iterator), metadata=self._client.grpc_metadata), client=self._client)


class DiscussionCommandServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.DiscussionCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.DiscussionCommandServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_list(self, discussion_list_request: DiscussionListRequest) -> AsyncIterator[DiscussionListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListResponse]) -> AsyncIterator[DiscussionListResponse]:
			async for native_message in iterator.__aiter__():
				yield DiscussionListResponse._from_native(native_message, client=self._client)
		overlay_object = discussion_list_request
		return response_iterator(self.__stub.DiscussionList(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListRequest(filter=DiscussionFilter._to_native(overlay_object.filter)), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_get(self, discussion_get_request: DiscussionGetRequest) -> Coroutine[Any, Any, DiscussionGetResponse]:
		overlay_object = discussion_get_request
		return DiscussionGetResponse._from_native_promise(self.__stub.DiscussionGet(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetRequest(discussion_id=overlay_object.discussion_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_get_by_contact(self, discussion_get_by_contact_request: DiscussionGetByContactRequest) -> Coroutine[Any, Any, DiscussionGetByContactResponse]:
		overlay_object = discussion_get_by_contact_request
		return DiscussionGetByContactResponse._from_native_promise(self.__stub.DiscussionGetByContact(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactRequest(contact_id=overlay_object.contact_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_get_by_group(self, discussion_get_by_group_request: DiscussionGetByGroupRequest) -> Coroutine[Any, Any, DiscussionGetByGroupResponse]:
		overlay_object = discussion_get_by_group_request
		return DiscussionGetByGroupResponse._from_native_promise(self.__stub.DiscussionGetByGroup(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupRequest(group_id=overlay_object.group_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_empty(self, discussion_empty_request: DiscussionEmptyRequest) -> Coroutine[Any, Any, DiscussionEmptyResponse]:
		overlay_object = discussion_empty_request
		return DiscussionEmptyResponse._from_native_promise(self.__stub.DiscussionEmpty(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyRequest(discussion_id=overlay_object.discussion_id, delete_everywhere=overlay_object.delete_everywhere), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_settings_get(self, discussion_settings_get_request: DiscussionSettingsGetRequest) -> Coroutine[Any, Any, DiscussionSettingsGetResponse]:
		overlay_object = discussion_settings_get_request
		return DiscussionSettingsGetResponse._from_native_promise(self.__stub.DiscussionSettingsGet(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsGetRequest(discussion_id=overlay_object.discussion_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_settings_set(self, discussion_settings_set_request: DiscussionSettingsSetRequest) -> Coroutine[Any, Any, DiscussionSettingsSetResponse]:
		overlay_object = discussion_settings_set_request
		return DiscussionSettingsSetResponse._from_native_promise(self.__stub.DiscussionSettingsSet(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionSettingsSetRequest(settings=DiscussionSettings._to_native(overlay_object.settings)), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_locked_list(self, discussion_locked_list_request: DiscussionLockedListRequest) -> AsyncIterator[DiscussionLockedListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListResponse]) -> AsyncIterator[DiscussionLockedListResponse]:
			async for native_message in iterator.__aiter__():
				yield DiscussionLockedListResponse._from_native(native_message, client=self._client)
		overlay_object = discussion_locked_list_request
		return response_iterator(self.__stub.DiscussionLockedList(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListRequest(), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_locked_delete(self, discussion_locked_delete_request: DiscussionLockedDeleteRequest) -> Coroutine[Any, Any, DiscussionLockedDeleteResponse]:
		overlay_object = discussion_locked_delete_request
		return DiscussionLockedDeleteResponse._from_native_promise(self.__stub.DiscussionLockedDelete(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteRequest(discussion_id=overlay_object.discussion_id), metadata=self._client.grpc_metadata), client=self._client)


class MessageCommandServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.MessageCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.MessageCommandServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_list(self, message_list_request: MessageListRequest) -> AsyncIterator[MessageListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.message_commands_pb2.MessageListResponse]) -> AsyncIterator[MessageListResponse]:
			async for native_message in iterator.__aiter__():
				yield MessageListResponse._from_native(native_message, client=self._client)
		overlay_object = message_list_request
		return response_iterator(self.__stub.MessageList(olvid.daemon.command.v1.message_commands_pb2.MessageListRequest(filter=MessageFilter._to_native(overlay_object.filter), unread=overlay_object.unread), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_get(self, message_get_request: MessageGetRequest) -> Coroutine[Any, Any, MessageGetResponse]:
		overlay_object = message_get_request
		return MessageGetResponse._from_native_promise(self.__stub.MessageGet(olvid.daemon.command.v1.message_commands_pb2.MessageGetRequest(message_id=MessageId._to_native(overlay_object.message_id)), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_refresh(self, message_refresh_request: MessageRefreshRequest) -> Coroutine[Any, Any, MessageRefreshResponse]:
		overlay_object = message_refresh_request
		return MessageRefreshResponse._from_native_promise(self.__stub.MessageRefresh(olvid.daemon.command.v1.message_commands_pb2.MessageRefreshRequest(), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_delete(self, message_delete_request: MessageDeleteRequest) -> Coroutine[Any, Any, MessageDeleteResponse]:
		overlay_object = message_delete_request
		return MessageDeleteResponse._from_native_promise(self.__stub.MessageDelete(olvid.daemon.command.v1.message_commands_pb2.MessageDeleteRequest(message_id=MessageId._to_native(overlay_object.message_id), delete_everywhere=overlay_object.delete_everywhere), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_send(self, message_send_request: MessageSendRequest) -> Coroutine[Any, Any, MessageSendResponse]:
		overlay_object = message_send_request
		return MessageSendResponse._from_native_promise(self.__stub.MessageSend(olvid.daemon.command.v1.message_commands_pb2.MessageSendRequest(discussion_id=overlay_object.discussion_id, body=overlay_object.body, reply_id=MessageId._to_native(overlay_object.reply_id), ephemerality=MessageEphemerality._to_native(overlay_object.ephemerality), disable_link_preview=overlay_object.disable_link_preview), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_send_with_attachments(self, message_send_with_attachments_request_iterator: AsyncIterator[MessageSendWithAttachmentsRequest]) -> Coroutine[Any, Any, MessageSendWithAttachmentsResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def request_iterator(iterator: AsyncIterator[MessageSendWithAttachmentsRequest]):
			async for message in iterator.__aiter__():
				yield MessageSendWithAttachmentsRequest._to_native(message)
		return MessageSendWithAttachmentsResponse._from_native_promise(self.__stub.MessageSendWithAttachments(request_iterator(message_send_with_attachments_request_iterator), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_react(self, message_react_request: MessageReactRequest) -> Coroutine[Any, Any, MessageReactResponse]:
		overlay_object = message_react_request
		return MessageReactResponse._from_native_promise(self.__stub.MessageReact(olvid.daemon.command.v1.message_commands_pb2.MessageReactRequest(message_id=MessageId._to_native(overlay_object.message_id), reaction=overlay_object.reaction), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_update_body(self, message_update_body_request: MessageUpdateBodyRequest) -> Coroutine[Any, Any, MessageUpdateBodyResponse]:
		overlay_object = message_update_body_request
		return MessageUpdateBodyResponse._from_native_promise(self.__stub.MessageUpdateBody(olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyRequest(message_id=MessageId._to_native(overlay_object.message_id), updated_body=overlay_object.updated_body), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_send_voip(self, message_send_voip_request: MessageSendVoipRequest) -> Coroutine[Any, Any, MessageSendVoipResponse]:
		overlay_object = message_send_voip_request
		return MessageSendVoipResponse._from_native_promise(self.__stub.MessageSendVoip(olvid.daemon.command.v1.message_commands_pb2.MessageSendVoipRequest(discussion_id=overlay_object.discussion_id), metadata=self._client.grpc_metadata), client=self._client)


class AttachmentCommandServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.AttachmentCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.AttachmentCommandServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def attachment_list(self, attachment_list_request: AttachmentListRequest) -> AsyncIterator[AttachmentListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListResponse]) -> AsyncIterator[AttachmentListResponse]:
			async for native_message in iterator.__aiter__():
				yield AttachmentListResponse._from_native(native_message, client=self._client)
		overlay_object = attachment_list_request
		return response_iterator(self.__stub.AttachmentList(olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListRequest(filter=AttachmentFilter._to_native(overlay_object.filter)), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def attachment_get(self, attachment_get_request: AttachmentGetRequest) -> Coroutine[Any, Any, AttachmentGetResponse]:
		overlay_object = attachment_get_request
		return AttachmentGetResponse._from_native_promise(self.__stub.AttachmentGet(olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetRequest(attachment_id=AttachmentId._to_native(overlay_object.attachment_id)), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def attachment_delete(self, attachment_delete_request: AttachmentDeleteRequest) -> Coroutine[Any, Any, AttachmentDeleteResponse]:
		overlay_object = attachment_delete_request
		return AttachmentDeleteResponse._from_native_promise(self.__stub.AttachmentDelete(olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteRequest(attachment_id=AttachmentId._to_native(overlay_object.attachment_id), delete_everywhere=overlay_object.delete_everywhere), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def attachment_download(self, attachment_download_request: AttachmentDownloadRequest) -> AsyncIterator[AttachmentDownloadResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadResponse]) -> AsyncIterator[AttachmentDownloadResponse]:
			async for native_message in iterator.__aiter__():
				yield AttachmentDownloadResponse._from_native(native_message, client=self._client)
		overlay_object = attachment_download_request
		return response_iterator(self.__stub.AttachmentDownload(olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadRequest(attachment_id=AttachmentId._to_native(overlay_object.attachment_id)), metadata=self._client.grpc_metadata))


class StorageCommandServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.StorageCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.StorageCommandServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def storage_list(self, storage_list_request: StorageListRequest) -> AsyncIterator[StorageListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.storage_commands_pb2.StorageListResponse]) -> AsyncIterator[StorageListResponse]:
			async for native_message in iterator.__aiter__():
				yield StorageListResponse._from_native(native_message, client=self._client)
		overlay_object = storage_list_request
		return response_iterator(self.__stub.StorageList(olvid.daemon.command.v1.storage_commands_pb2.StorageListRequest(filter=StorageElementFilter._to_native(overlay_object.filter)), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def storage_get(self, storage_get_request: StorageGetRequest) -> Coroutine[Any, Any, StorageGetResponse]:
		overlay_object = storage_get_request
		return StorageGetResponse._from_native_promise(self.__stub.StorageGet(olvid.daemon.command.v1.storage_commands_pb2.StorageGetRequest(key=overlay_object.key), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def storage_set(self, storage_set_request: StorageSetRequest) -> Coroutine[Any, Any, StorageSetResponse]:
		overlay_object = storage_set_request
		return StorageSetResponse._from_native_promise(self.__stub.StorageSet(olvid.daemon.command.v1.storage_commands_pb2.StorageSetRequest(key=overlay_object.key, value=overlay_object.value), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def storage_unset(self, storage_unset_request: StorageUnsetRequest) -> Coroutine[Any, Any, StorageUnsetResponse]:
		overlay_object = storage_unset_request
		return StorageUnsetResponse._from_native_promise(self.__stub.StorageUnset(olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetRequest(key=overlay_object.key), metadata=self._client.grpc_metadata), client=self._client)


class DiscussionStorageCommandServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.DiscussionStorageCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.DiscussionStorageCommandServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_storage_list(self, discussion_storage_list_request: DiscussionStorageListRequest) -> AsyncIterator[DiscussionStorageListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListResponse]) -> AsyncIterator[DiscussionStorageListResponse]:
			async for native_message in iterator.__aiter__():
				yield DiscussionStorageListResponse._from_native(native_message, client=self._client)
		overlay_object = discussion_storage_list_request
		return response_iterator(self.__stub.DiscussionStorageList(olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListRequest(discussion_id=overlay_object.discussion_id, filter=StorageElementFilter._to_native(overlay_object.filter)), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_storage_get(self, discussion_storage_get_request: DiscussionStorageGetRequest) -> Coroutine[Any, Any, DiscussionStorageGetResponse]:
		overlay_object = discussion_storage_get_request
		return DiscussionStorageGetResponse._from_native_promise(self.__stub.DiscussionStorageGet(olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetRequest(discussion_id=overlay_object.discussion_id, key=overlay_object.key), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_storage_set(self, discussion_storage_set_request: DiscussionStorageSetRequest) -> Coroutine[Any, Any, DiscussionStorageSetResponse]:
		overlay_object = discussion_storage_set_request
		return DiscussionStorageSetResponse._from_native_promise(self.__stub.DiscussionStorageSet(olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetRequest(discussion_id=overlay_object.discussion_id, key=overlay_object.key, value=overlay_object.value), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_storage_unset(self, discussion_storage_unset_request: DiscussionStorageUnsetRequest) -> Coroutine[Any, Any, DiscussionStorageUnsetResponse]:
		overlay_object = discussion_storage_unset_request
		return DiscussionStorageUnsetResponse._from_native_promise(self.__stub.DiscussionStorageUnset(olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetRequest(discussion_id=overlay_object.discussion_id, key=overlay_object.key), metadata=self._client.grpc_metadata), client=self._client)
