####
# WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_protobuf_overlay
####

from __future__ import annotations  # this block is necessary for compilation
from grpc.aio import Channel
from typing import AsyncIterator, Coroutine, Any, Callable
from ...protobuf import olvid
from ...datatypes import *
from ...core import errors


# noinspection PyProtectedMember,PyShadowingBuiltins
class AttachmentListRequest:
	def __init__(self, filter: "AttachmentFilter" = None):
		self.filter: AttachmentFilter = filter

	def _update_content(self, attachment_list_request: AttachmentListRequest) -> None:
		self.filter: AttachmentFilter = attachment_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentListRequest":
		return AttachmentListRequest(filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListRequest) -> "AttachmentListRequest":
		return AttachmentListRequest(filter=AttachmentFilter._from_native(native_message.filter))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListRequest]) -> list["AttachmentListRequest"]:
		return [AttachmentListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListRequest]) -> "AttachmentListRequest":
		try:
			native_message = await promise
			return AttachmentListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, attachments: "list[Attachment]" = None):
		self.attachments: list[Attachment] = attachments

	def _update_content(self, attachment_list_response: AttachmentListResponse) -> None:
		self.attachments: list[Attachment] = attachment_list_response.attachments

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentListResponse":
		return AttachmentListResponse(attachments=[e._clone() for e in self.attachments])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListResponse) -> "AttachmentListResponse":
		return AttachmentListResponse(attachments=Attachment._from_native_list(native_message.attachments))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListResponse]) -> list["AttachmentListResponse"]:
		return [AttachmentListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListResponse]) -> "AttachmentListResponse":
		try:
			native_message = await promise
			return AttachmentListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, attachment_id: "AttachmentId" = None):
		self.attachment_id: AttachmentId = attachment_id

	def _update_content(self, attachment_get_request: AttachmentGetRequest) -> None:
		self.attachment_id: AttachmentId = attachment_get_request.attachment_id

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentGetRequest":
		return AttachmentGetRequest(attachment_id=self.attachment_id._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetRequest) -> "AttachmentGetRequest":
		return AttachmentGetRequest(attachment_id=AttachmentId._from_native(native_message.attachment_id))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetRequest]) -> list["AttachmentGetRequest"]:
		return [AttachmentGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetRequest]) -> "AttachmentGetRequest":
		try:
			native_message = await promise
			return AttachmentGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, attachment: "Attachment" = None):
		self.attachment: Attachment = attachment

	def _update_content(self, attachment_get_response: AttachmentGetResponse) -> None:
		self.attachment: Attachment = attachment_get_response.attachment

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentGetResponse":
		return AttachmentGetResponse(attachment=self.attachment._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetResponse) -> "AttachmentGetResponse":
		return AttachmentGetResponse(attachment=Attachment._from_native(native_message.attachment))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetResponse]) -> list["AttachmentGetResponse"]:
		return [AttachmentGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetResponse]) -> "AttachmentGetResponse":
		try:
			native_message = await promise
			return AttachmentGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, attachment_id: "AttachmentId" = None, delete_everywhere: bool = False):
		self.attachment_id: AttachmentId = attachment_id
		self.delete_everywhere: bool = delete_everywhere

	def _update_content(self, attachment_delete_request: AttachmentDeleteRequest) -> None:
		self.attachment_id: AttachmentId = attachment_delete_request.attachment_id
		self.delete_everywhere: bool = attachment_delete_request.delete_everywhere

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentDeleteRequest":
		return AttachmentDeleteRequest(attachment_id=self.attachment_id._clone(), delete_everywhere=self.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteRequest) -> "AttachmentDeleteRequest":
		return AttachmentDeleteRequest(attachment_id=AttachmentId._from_native(native_message.attachment_id), delete_everywhere=native_message.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteRequest]) -> list["AttachmentDeleteRequest"]:
		return [AttachmentDeleteRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteRequest]) -> "AttachmentDeleteRequest":
		try:
			native_message = await promise
			return AttachmentDeleteRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, attachment_delete_response: AttachmentDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentDeleteResponse":
		return AttachmentDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteResponse) -> "AttachmentDeleteResponse":
		return AttachmentDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteResponse]) -> list["AttachmentDeleteResponse"]:
		return [AttachmentDeleteResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteResponse]) -> "AttachmentDeleteResponse":
		try:
			native_message = await promise
			return AttachmentDeleteResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, attachment_id: "AttachmentId" = None):
		self.attachment_id: AttachmentId = attachment_id

	def _update_content(self, attachment_download_request: AttachmentDownloadRequest) -> None:
		self.attachment_id: AttachmentId = attachment_download_request.attachment_id

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentDownloadRequest":
		return AttachmentDownloadRequest(attachment_id=self.attachment_id._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadRequest) -> "AttachmentDownloadRequest":
		return AttachmentDownloadRequest(attachment_id=AttachmentId._from_native(native_message.attachment_id))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadRequest]) -> list["AttachmentDownloadRequest"]:
		return [AttachmentDownloadRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadRequest]) -> "AttachmentDownloadRequest":
		try:
			native_message = await promise
			return AttachmentDownloadRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, chunk: bytes = b""):
		self.chunk: bytes = chunk

	def _update_content(self, attachment_download_response: AttachmentDownloadResponse) -> None:
		self.chunk: bytes = attachment_download_response.chunk

	# noinspection PyProtectedMember
	def _clone(self) -> "AttachmentDownloadResponse":
		return AttachmentDownloadResponse(chunk=self.chunk)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadResponse) -> "AttachmentDownloadResponse":
		return AttachmentDownloadResponse(chunk=native_message.chunk)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadResponse]) -> list["AttachmentDownloadResponse"]:
		return [AttachmentDownloadResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadResponse]) -> "AttachmentDownloadResponse":
		try:
			native_message = await promise
			return AttachmentDownloadResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
class CallStartDiscussionCallRequest:
	def __init__(self, discussion_id: int = 0):
		self.discussion_id: int = discussion_id

	def _update_content(self, call_start_discussion_call_request: CallStartDiscussionCallRequest) -> None:
		self.discussion_id: int = call_start_discussion_call_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "CallStartDiscussionCallRequest":
		return CallStartDiscussionCallRequest(discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.call_commands_pb2.CallStartDiscussionCallRequest) -> "CallStartDiscussionCallRequest":
		return CallStartDiscussionCallRequest(discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.call_commands_pb2.CallStartDiscussionCallRequest]) -> list["CallStartDiscussionCallRequest"]:
		return [CallStartDiscussionCallRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.call_commands_pb2.CallStartDiscussionCallRequest]) -> "CallStartDiscussionCallRequest":
		try:
			native_message = await promise
			return CallStartDiscussionCallRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["CallStartDiscussionCallRequest"]):
		if messages is None:
			return []
		return [CallStartDiscussionCallRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["CallStartDiscussionCallRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.call_commands_pb2.CallStartDiscussionCallRequest(discussion_id=message.discussion_id if message.discussion_id else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, CallStartDiscussionCallRequest):
			return False
		return self.discussion_id == other.discussion_id

	def __bool__(self):
		return self.discussion_id != 0

	def __hash__(self):
		return hash(self.discussion_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, CallStartDiscussionCallRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class CallStartDiscussionCallResponse:
	def __init__(self, call_identifier: str = ""):
		self.call_identifier: str = call_identifier

	def _update_content(self, call_start_discussion_call_response: CallStartDiscussionCallResponse) -> None:
		self.call_identifier: str = call_start_discussion_call_response.call_identifier

	# noinspection PyProtectedMember
	def _clone(self) -> "CallStartDiscussionCallResponse":
		return CallStartDiscussionCallResponse(call_identifier=self.call_identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.call_commands_pb2.CallStartDiscussionCallResponse) -> "CallStartDiscussionCallResponse":
		return CallStartDiscussionCallResponse(call_identifier=native_message.call_identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.call_commands_pb2.CallStartDiscussionCallResponse]) -> list["CallStartDiscussionCallResponse"]:
		return [CallStartDiscussionCallResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.call_commands_pb2.CallStartDiscussionCallResponse]) -> "CallStartDiscussionCallResponse":
		try:
			native_message = await promise
			return CallStartDiscussionCallResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["CallStartDiscussionCallResponse"]):
		if messages is None:
			return []
		return [CallStartDiscussionCallResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["CallStartDiscussionCallResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.call_commands_pb2.CallStartDiscussionCallResponse(call_identifier=message.call_identifier if message.call_identifier else None)

	def __str__(self):
		s: str = ''
		if self.call_identifier:
			s += f'call_identifier: {self.call_identifier}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, CallStartDiscussionCallResponse):
			return False
		return self.call_identifier == other.call_identifier

	def __bool__(self):
		return self.call_identifier != ""

	def __hash__(self):
		return hash(self.call_identifier)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, CallStartDiscussionCallResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.call_identifier == "" or self.call_identifier == expected.call_identifier, "Invalid value: call_identifier: " + str(expected.call_identifier) + " != " + str(self.call_identifier)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class CallStartCustomCallRequest:
	def __init__(self, contact_ids: list[int] = (), discussion_id: int = 0):
		self.contact_ids: list[int] = contact_ids
		self.discussion_id: int = discussion_id

	def _update_content(self, call_start_custom_call_request: CallStartCustomCallRequest) -> None:
		self.contact_ids: list[int] = call_start_custom_call_request.contact_ids
		self.discussion_id: int = call_start_custom_call_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "CallStartCustomCallRequest":
		return CallStartCustomCallRequest(contact_ids=[e for e in self.contact_ids], discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.call_commands_pb2.CallStartCustomCallRequest) -> "CallStartCustomCallRequest":
		return CallStartCustomCallRequest(contact_ids=native_message.contact_ids, discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.call_commands_pb2.CallStartCustomCallRequest]) -> list["CallStartCustomCallRequest"]:
		return [CallStartCustomCallRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.call_commands_pb2.CallStartCustomCallRequest]) -> "CallStartCustomCallRequest":
		try:
			native_message = await promise
			return CallStartCustomCallRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["CallStartCustomCallRequest"]):
		if messages is None:
			return []
		return [CallStartCustomCallRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["CallStartCustomCallRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.call_commands_pb2.CallStartCustomCallRequest(contact_ids=message.contact_ids if message.contact_ids else None, discussion_id=message.discussion_id if message.discussion_id else None)

	def __str__(self):
		s: str = ''
		if self.contact_ids:
			s += f'contact_ids: {[str(el) for el in self.contact_ids]}, '
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, CallStartCustomCallRequest):
			return False
		return self.contact_ids == other.contact_ids and self.discussion_id == other.discussion_id

	def __bool__(self):
		return bool(self.contact_ids) or self.discussion_id != 0

	def __hash__(self):
		return hash((tuple(self.contact_ids), self.discussion_id))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, CallStartCustomCallRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field contact_ids")
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class CallStartCustomCallResponse:
	def __init__(self, call_identifier: str = ""):
		self.call_identifier: str = call_identifier

	def _update_content(self, call_start_custom_call_response: CallStartCustomCallResponse) -> None:
		self.call_identifier: str = call_start_custom_call_response.call_identifier

	# noinspection PyProtectedMember
	def _clone(self) -> "CallStartCustomCallResponse":
		return CallStartCustomCallResponse(call_identifier=self.call_identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.call_commands_pb2.CallStartCustomCallResponse) -> "CallStartCustomCallResponse":
		return CallStartCustomCallResponse(call_identifier=native_message.call_identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.call_commands_pb2.CallStartCustomCallResponse]) -> list["CallStartCustomCallResponse"]:
		return [CallStartCustomCallResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.call_commands_pb2.CallStartCustomCallResponse]) -> "CallStartCustomCallResponse":
		try:
			native_message = await promise
			return CallStartCustomCallResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["CallStartCustomCallResponse"]):
		if messages is None:
			return []
		return [CallStartCustomCallResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["CallStartCustomCallResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.call_commands_pb2.CallStartCustomCallResponse(call_identifier=message.call_identifier if message.call_identifier else None)

	def __str__(self):
		s: str = ''
		if self.call_identifier:
			s += f'call_identifier: {self.call_identifier}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, CallStartCustomCallResponse):
			return False
		return self.call_identifier == other.call_identifier

	def __bool__(self):
		return self.call_identifier != ""

	def __hash__(self):
		return hash(self.call_identifier)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, CallStartCustomCallResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.call_identifier == "" or self.call_identifier == expected.call_identifier, "Invalid value: call_identifier: " + str(expected.call_identifier) + " != " + str(self.call_identifier)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactListRequest:
	def __init__(self, filter: "ContactFilter" = None):
		self.filter: ContactFilter = filter

	def _update_content(self, contact_list_request: ContactListRequest) -> None:
		self.filter: ContactFilter = contact_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactListRequest":
		return ContactListRequest(filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactListRequest) -> "ContactListRequest":
		return ContactListRequest(filter=ContactFilter._from_native(native_message.filter))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactListRequest]) -> list["ContactListRequest"]:
		return [ContactListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactListRequest]) -> "ContactListRequest":
		try:
			native_message = await promise
			return ContactListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, contacts: "list[Contact]" = None):
		self.contacts: list[Contact] = contacts

	def _update_content(self, contact_list_response: ContactListResponse) -> None:
		self.contacts: list[Contact] = contact_list_response.contacts

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactListResponse":
		return ContactListResponse(contacts=[e._clone() for e in self.contacts])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactListResponse) -> "ContactListResponse":
		return ContactListResponse(contacts=Contact._from_native_list(native_message.contacts))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactListResponse]) -> list["ContactListResponse"]:
		return [ContactListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactListResponse]) -> "ContactListResponse":
		try:
			native_message = await promise
			return ContactListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, contact_id: int = 0):
		self.contact_id: int = contact_id

	def _update_content(self, contact_get_request: ContactGetRequest) -> None:
		self.contact_id: int = contact_get_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactGetRequest":
		return ContactGetRequest(contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactGetRequest) -> "ContactGetRequest":
		return ContactGetRequest(contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactGetRequest]) -> list["ContactGetRequest"]:
		return [ContactGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactGetRequest]) -> "ContactGetRequest":
		try:
			native_message = await promise
			return ContactGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, contact: "Contact" = None):
		self.contact: Contact = contact

	def _update_content(self, contact_get_response: ContactGetResponse) -> None:
		self.contact: Contact = contact_get_response.contact

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactGetResponse":
		return ContactGetResponse(contact=self.contact._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactGetResponse) -> "ContactGetResponse":
		return ContactGetResponse(contact=Contact._from_native(native_message.contact))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactGetResponse]) -> list["ContactGetResponse"]:
		return [ContactGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactGetResponse]) -> "ContactGetResponse":
		try:
			native_message = await promise
			return ContactGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
class ContactGetBytesIdentifierRequest:
	def __init__(self, contact_id: int = 0):
		self.contact_id: int = contact_id

	def _update_content(self, contact_get_bytes_identifier_request: ContactGetBytesIdentifierRequest) -> None:
		self.contact_id: int = contact_get_bytes_identifier_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactGetBytesIdentifierRequest":
		return ContactGetBytesIdentifierRequest(contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactGetBytesIdentifierRequest) -> "ContactGetBytesIdentifierRequest":
		return ContactGetBytesIdentifierRequest(contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactGetBytesIdentifierRequest]) -> list["ContactGetBytesIdentifierRequest"]:
		return [ContactGetBytesIdentifierRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactGetBytesIdentifierRequest]) -> "ContactGetBytesIdentifierRequest":
		try:
			native_message = await promise
			return ContactGetBytesIdentifierRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactGetBytesIdentifierRequest"]):
		if messages is None:
			return []
		return [ContactGetBytesIdentifierRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactGetBytesIdentifierRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactGetBytesIdentifierRequest(contact_id=message.contact_id if message.contact_id else None)

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactGetBytesIdentifierRequest):
			return False
		return self.contact_id == other.contact_id

	def __bool__(self):
		return self.contact_id != 0

	def __hash__(self):
		return hash(self.contact_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactGetBytesIdentifierRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactGetBytesIdentifierResponse:
	def __init__(self, identifier: bytes = b""):
		self.identifier: bytes = identifier

	def _update_content(self, contact_get_bytes_identifier_response: ContactGetBytesIdentifierResponse) -> None:
		self.identifier: bytes = contact_get_bytes_identifier_response.identifier

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactGetBytesIdentifierResponse":
		return ContactGetBytesIdentifierResponse(identifier=self.identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactGetBytesIdentifierResponse) -> "ContactGetBytesIdentifierResponse":
		return ContactGetBytesIdentifierResponse(identifier=native_message.identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactGetBytesIdentifierResponse]) -> list["ContactGetBytesIdentifierResponse"]:
		return [ContactGetBytesIdentifierResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactGetBytesIdentifierResponse]) -> "ContactGetBytesIdentifierResponse":
		try:
			native_message = await promise
			return ContactGetBytesIdentifierResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactGetBytesIdentifierResponse"]):
		if messages is None:
			return []
		return [ContactGetBytesIdentifierResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactGetBytesIdentifierResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactGetBytesIdentifierResponse(identifier=message.identifier if message.identifier else None)

	def __str__(self):
		s: str = ''
		if self.identifier:
			s += f'identifier: {self.identifier}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactGetBytesIdentifierResponse):
			return False
		return self.identifier == other.identifier

	def __bool__(self):
		return self.identifier != b""

	def __hash__(self):
		return hash(self.identifier)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactGetBytesIdentifierResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identifier == b"" or self.identifier == expected.identifier, "Invalid value: identifier: " + str(expected.identifier) + " != " + str(self.identifier)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactGetInvitationLinkRequest:
	def __init__(self, contact_id: int = 0):
		self.contact_id: int = contact_id

	def _update_content(self, contact_get_invitation_link_request: ContactGetInvitationLinkRequest) -> None:
		self.contact_id: int = contact_get_invitation_link_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactGetInvitationLinkRequest":
		return ContactGetInvitationLinkRequest(contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactGetInvitationLinkRequest) -> "ContactGetInvitationLinkRequest":
		return ContactGetInvitationLinkRequest(contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactGetInvitationLinkRequest]) -> list["ContactGetInvitationLinkRequest"]:
		return [ContactGetInvitationLinkRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactGetInvitationLinkRequest]) -> "ContactGetInvitationLinkRequest":
		try:
			native_message = await promise
			return ContactGetInvitationLinkRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactGetInvitationLinkRequest"]):
		if messages is None:
			return []
		return [ContactGetInvitationLinkRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactGetInvitationLinkRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactGetInvitationLinkRequest(contact_id=message.contact_id if message.contact_id else None)

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactGetInvitationLinkRequest):
			return False
		return self.contact_id == other.contact_id

	def __bool__(self):
		return self.contact_id != 0

	def __hash__(self):
		return hash(self.contact_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactGetInvitationLinkRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactGetInvitationLinkResponse:
	def __init__(self, invitation_link: str = ""):
		self.invitation_link: str = invitation_link

	def _update_content(self, contact_get_invitation_link_response: ContactGetInvitationLinkResponse) -> None:
		self.invitation_link: str = contact_get_invitation_link_response.invitation_link

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactGetInvitationLinkResponse":
		return ContactGetInvitationLinkResponse(invitation_link=self.invitation_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactGetInvitationLinkResponse) -> "ContactGetInvitationLinkResponse":
		return ContactGetInvitationLinkResponse(invitation_link=native_message.invitation_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactGetInvitationLinkResponse]) -> list["ContactGetInvitationLinkResponse"]:
		return [ContactGetInvitationLinkResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactGetInvitationLinkResponse]) -> "ContactGetInvitationLinkResponse":
		try:
			native_message = await promise
			return ContactGetInvitationLinkResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactGetInvitationLinkResponse"]):
		if messages is None:
			return []
		return [ContactGetInvitationLinkResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactGetInvitationLinkResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactGetInvitationLinkResponse(invitation_link=message.invitation_link if message.invitation_link else None)

	def __str__(self):
		s: str = ''
		if self.invitation_link:
			s += f'invitation_link: {self.invitation_link}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactGetInvitationLinkResponse):
			return False
		return self.invitation_link == other.invitation_link

	def __bool__(self):
		return self.invitation_link != ""

	def __hash__(self):
		return hash(self.invitation_link)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactGetInvitationLinkResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.invitation_link == "" or self.invitation_link == expected.invitation_link, "Invalid value: invitation_link: " + str(expected.invitation_link) + " != " + str(self.invitation_link)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactDeleteRequest:
	def __init__(self, contact_id: int = 0):
		self.contact_id: int = contact_id

	def _update_content(self, contact_delete_request: ContactDeleteRequest) -> None:
		self.contact_id: int = contact_delete_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDeleteRequest":
		return ContactDeleteRequest(contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteRequest) -> "ContactDeleteRequest":
		return ContactDeleteRequest(contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteRequest]) -> list["ContactDeleteRequest"]:
		return [ContactDeleteRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteRequest]) -> "ContactDeleteRequest":
		try:
			native_message = await promise
			return ContactDeleteRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, contact_delete_response: ContactDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDeleteResponse":
		return ContactDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteResponse) -> "ContactDeleteResponse":
		return ContactDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteResponse]) -> list["ContactDeleteResponse"]:
		return [ContactDeleteResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteResponse]) -> "ContactDeleteResponse":
		try:
			native_message = await promise
			return ContactDeleteResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, first_contact_id: int = 0, second_contact_id: int = 0):
		self.first_contact_id: int = first_contact_id
		self.second_contact_id: int = second_contact_id

	def _update_content(self, contact_introduction_request: ContactIntroductionRequest) -> None:
		self.first_contact_id: int = contact_introduction_request.first_contact_id
		self.second_contact_id: int = contact_introduction_request.second_contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactIntroductionRequest":
		return ContactIntroductionRequest(first_contact_id=self.first_contact_id, second_contact_id=self.second_contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionRequest) -> "ContactIntroductionRequest":
		return ContactIntroductionRequest(first_contact_id=native_message.first_contact_id, second_contact_id=native_message.second_contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionRequest]) -> list["ContactIntroductionRequest"]:
		return [ContactIntroductionRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionRequest]) -> "ContactIntroductionRequest":
		try:
			native_message = await promise
			return ContactIntroductionRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, contact_introduction_response: ContactIntroductionResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactIntroductionResponse":
		return ContactIntroductionResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionResponse) -> "ContactIntroductionResponse":
		return ContactIntroductionResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionResponse]) -> list["ContactIntroductionResponse"]:
		return [ContactIntroductionResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionResponse]) -> "ContactIntroductionResponse":
		try:
			native_message = await promise
			return ContactIntroductionResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, contact_id: int = 0):
		self.contact_id: int = contact_id

	def _update_content(self, contact_invite_to_one_to_one_discussion_request: ContactInviteToOneToOneDiscussionRequest) -> None:
		self.contact_id: int = contact_invite_to_one_to_one_discussion_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactInviteToOneToOneDiscussionRequest":
		return ContactInviteToOneToOneDiscussionRequest(contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionRequest) -> "ContactInviteToOneToOneDiscussionRequest":
		return ContactInviteToOneToOneDiscussionRequest(contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionRequest]) -> list["ContactInviteToOneToOneDiscussionRequest"]:
		return [ContactInviteToOneToOneDiscussionRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionRequest]) -> "ContactInviteToOneToOneDiscussionRequest":
		try:
			native_message = await promise
			return ContactInviteToOneToOneDiscussionRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, invitation: "Invitation" = None):
		self.invitation: Invitation = invitation

	def _update_content(self, contact_invite_to_one_to_one_discussion_response: ContactInviteToOneToOneDiscussionResponse) -> None:
		self.invitation: Invitation = contact_invite_to_one_to_one_discussion_response.invitation

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactInviteToOneToOneDiscussionResponse":
		return ContactInviteToOneToOneDiscussionResponse(invitation=self.invitation._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionResponse) -> "ContactInviteToOneToOneDiscussionResponse":
		return ContactInviteToOneToOneDiscussionResponse(invitation=Invitation._from_native(native_message.invitation))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionResponse]) -> list["ContactInviteToOneToOneDiscussionResponse"]:
		return [ContactInviteToOneToOneDiscussionResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionResponse]) -> "ContactInviteToOneToOneDiscussionResponse":
		try:
			native_message = await promise
			return ContactInviteToOneToOneDiscussionResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, contact_id: int = 0):
		self.contact_id: int = contact_id

	def _update_content(self, contact_downgrade_one_to_one_discussion_request: ContactDowngradeOneToOneDiscussionRequest) -> None:
		self.contact_id: int = contact_downgrade_one_to_one_discussion_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDowngradeOneToOneDiscussionRequest":
		return ContactDowngradeOneToOneDiscussionRequest(contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionRequest) -> "ContactDowngradeOneToOneDiscussionRequest":
		return ContactDowngradeOneToOneDiscussionRequest(contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionRequest]) -> list["ContactDowngradeOneToOneDiscussionRequest"]:
		return [ContactDowngradeOneToOneDiscussionRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionRequest]) -> "ContactDowngradeOneToOneDiscussionRequest":
		try:
			native_message = await promise
			return ContactDowngradeOneToOneDiscussionRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, contact_downgrade_one_to_one_discussion_response: ContactDowngradeOneToOneDiscussionResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDowngradeOneToOneDiscussionResponse":
		return ContactDowngradeOneToOneDiscussionResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionResponse) -> "ContactDowngradeOneToOneDiscussionResponse":
		return ContactDowngradeOneToOneDiscussionResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionResponse]) -> list["ContactDowngradeOneToOneDiscussionResponse"]:
		return [ContactDowngradeOneToOneDiscussionResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionResponse]) -> "ContactDowngradeOneToOneDiscussionResponse":
		try:
			native_message = await promise
			return ContactDowngradeOneToOneDiscussionResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
class ContactDownloadPhotoRequest:
	def __init__(self, contact_id: int = 0):
		self.contact_id: int = contact_id

	def _update_content(self, contact_download_photo_request: ContactDownloadPhotoRequest) -> None:
		self.contact_id: int = contact_download_photo_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDownloadPhotoRequest":
		return ContactDownloadPhotoRequest(contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactDownloadPhotoRequest) -> "ContactDownloadPhotoRequest":
		return ContactDownloadPhotoRequest(contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactDownloadPhotoRequest]) -> list["ContactDownloadPhotoRequest"]:
		return [ContactDownloadPhotoRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactDownloadPhotoRequest]) -> "ContactDownloadPhotoRequest":
		try:
			native_message = await promise
			return ContactDownloadPhotoRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactDownloadPhotoRequest"]):
		if messages is None:
			return []
		return [ContactDownloadPhotoRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactDownloadPhotoRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactDownloadPhotoRequest(contact_id=message.contact_id if message.contact_id else None)

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactDownloadPhotoRequest):
			return False
		return self.contact_id == other.contact_id

	def __bool__(self):
		return self.contact_id != 0

	def __hash__(self):
		return hash(self.contact_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactDownloadPhotoRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactDownloadPhotoResponse:
	def __init__(self, photo: bytes = b""):
		self.photo: bytes = photo

	def _update_content(self, contact_download_photo_response: ContactDownloadPhotoResponse) -> None:
		self.photo: bytes = contact_download_photo_response.photo

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactDownloadPhotoResponse":
		return ContactDownloadPhotoResponse(photo=self.photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactDownloadPhotoResponse) -> "ContactDownloadPhotoResponse":
		return ContactDownloadPhotoResponse(photo=native_message.photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactDownloadPhotoResponse]) -> list["ContactDownloadPhotoResponse"]:
		return [ContactDownloadPhotoResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactDownloadPhotoResponse]) -> "ContactDownloadPhotoResponse":
		try:
			native_message = await promise
			return ContactDownloadPhotoResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactDownloadPhotoResponse"]):
		if messages is None:
			return []
		return [ContactDownloadPhotoResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactDownloadPhotoResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactDownloadPhotoResponse(photo=message.photo if message.photo else None)

	def __str__(self):
		s: str = ''
		if self.photo:
			s += f'photo: {self.photo}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactDownloadPhotoResponse):
			return False
		return self.photo == other.photo

	def __bool__(self):
		return self.photo != b""

	def __hash__(self):
		return hash(self.photo)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactDownloadPhotoResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.photo == b"" or self.photo == expected.photo, "Invalid value: photo: " + str(expected.photo) + " != " + str(self.photo)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactRecreateChannelsRequest:
	def __init__(self, contact_id: int = 0):
		self.contact_id: int = contact_id

	def _update_content(self, contact_recreate_channels_request: ContactRecreateChannelsRequest) -> None:
		self.contact_id: int = contact_recreate_channels_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactRecreateChannelsRequest":
		return ContactRecreateChannelsRequest(contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactRecreateChannelsRequest) -> "ContactRecreateChannelsRequest":
		return ContactRecreateChannelsRequest(contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactRecreateChannelsRequest]) -> list["ContactRecreateChannelsRequest"]:
		return [ContactRecreateChannelsRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactRecreateChannelsRequest]) -> "ContactRecreateChannelsRequest":
		try:
			native_message = await promise
			return ContactRecreateChannelsRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactRecreateChannelsRequest"]):
		if messages is None:
			return []
		return [ContactRecreateChannelsRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactRecreateChannelsRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactRecreateChannelsRequest(contact_id=message.contact_id if message.contact_id else None)

	def __str__(self):
		s: str = ''
		if self.contact_id:
			s += f'contact_id: {self.contact_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactRecreateChannelsRequest):
			return False
		return self.contact_id == other.contact_id

	def __bool__(self):
		return self.contact_id != 0

	def __hash__(self):
		return hash(self.contact_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactRecreateChannelsRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.contact_id == 0 or self.contact_id == expected.contact_id, "Invalid value: contact_id: " + str(expected.contact_id) + " != " + str(self.contact_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ContactRecreateChannelsResponse:
	def __init__(self):
		pass

	def _update_content(self, contact_recreate_channels_response: ContactRecreateChannelsResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "ContactRecreateChannelsResponse":
		return ContactRecreateChannelsResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.contact_commands_pb2.ContactRecreateChannelsResponse) -> "ContactRecreateChannelsResponse":
		return ContactRecreateChannelsResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.contact_commands_pb2.ContactRecreateChannelsResponse]) -> list["ContactRecreateChannelsResponse"]:
		return [ContactRecreateChannelsResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.contact_commands_pb2.ContactRecreateChannelsResponse]) -> "ContactRecreateChannelsResponse":
		try:
			native_message = await promise
			return ContactRecreateChannelsResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ContactRecreateChannelsResponse"]):
		if messages is None:
			return []
		return [ContactRecreateChannelsResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ContactRecreateChannelsResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.contact_commands_pb2.ContactRecreateChannelsResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ContactRecreateChannelsResponse):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ContactRecreateChannelsResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionListRequest:
	def __init__(self, filter: "DiscussionFilter" = None):
		self.filter: DiscussionFilter = filter

	def _update_content(self, discussion_list_request: DiscussionListRequest) -> None:
		self.filter: DiscussionFilter = discussion_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionListRequest":
		return DiscussionListRequest(filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListRequest) -> "DiscussionListRequest":
		return DiscussionListRequest(filter=DiscussionFilter._from_native(native_message.filter))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListRequest]) -> list["DiscussionListRequest"]:
		return [DiscussionListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListRequest]) -> "DiscussionListRequest":
		try:
			native_message = await promise
			return DiscussionListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussions: "list[Discussion]" = None):
		self.discussions: list[Discussion] = discussions

	def _update_content(self, discussion_list_response: DiscussionListResponse) -> None:
		self.discussions: list[Discussion] = discussion_list_response.discussions

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionListResponse":
		return DiscussionListResponse(discussions=[e._clone() for e in self.discussions])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListResponse) -> "DiscussionListResponse":
		return DiscussionListResponse(discussions=Discussion._from_native_list(native_message.discussions))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListResponse]) -> list["DiscussionListResponse"]:
		return [DiscussionListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListResponse]) -> "DiscussionListResponse":
		try:
			native_message = await promise
			return DiscussionListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussion_id: int = 0):
		self.discussion_id: int = discussion_id

	def _update_content(self, discussion_get_request: DiscussionGetRequest) -> None:
		self.discussion_id: int = discussion_get_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetRequest":
		return DiscussionGetRequest(discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetRequest) -> "DiscussionGetRequest":
		return DiscussionGetRequest(discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetRequest]) -> list["DiscussionGetRequest"]:
		return [DiscussionGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetRequest]) -> "DiscussionGetRequest":
		try:
			native_message = await promise
			return DiscussionGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussion: "Discussion" = None):
		self.discussion: Discussion = discussion

	def _update_content(self, discussion_get_response: DiscussionGetResponse) -> None:
		self.discussion: Discussion = discussion_get_response.discussion

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetResponse":
		return DiscussionGetResponse(discussion=self.discussion._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetResponse) -> "DiscussionGetResponse":
		return DiscussionGetResponse(discussion=Discussion._from_native(native_message.discussion))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetResponse]) -> list["DiscussionGetResponse"]:
		return [DiscussionGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetResponse]) -> "DiscussionGetResponse":
		try:
			native_message = await promise
			return DiscussionGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
class DiscussionGetBytesIdentifierRequest:
	def __init__(self, discussion_id: int = 0):
		self.discussion_id: int = discussion_id

	def _update_content(self, discussion_get_bytes_identifier_request: DiscussionGetBytesIdentifierRequest) -> None:
		self.discussion_id: int = discussion_get_bytes_identifier_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetBytesIdentifierRequest":
		return DiscussionGetBytesIdentifierRequest(discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetBytesIdentifierRequest) -> "DiscussionGetBytesIdentifierRequest":
		return DiscussionGetBytesIdentifierRequest(discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetBytesIdentifierRequest]) -> list["DiscussionGetBytesIdentifierRequest"]:
		return [DiscussionGetBytesIdentifierRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetBytesIdentifierRequest]) -> "DiscussionGetBytesIdentifierRequest":
		try:
			native_message = await promise
			return DiscussionGetBytesIdentifierRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionGetBytesIdentifierRequest"]):
		if messages is None:
			return []
		return [DiscussionGetBytesIdentifierRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionGetBytesIdentifierRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetBytesIdentifierRequest(discussion_id=message.discussion_id if message.discussion_id else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionGetBytesIdentifierRequest):
			return False
		return self.discussion_id == other.discussion_id

	def __bool__(self):
		return self.discussion_id != 0

	def __hash__(self):
		return hash(self.discussion_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionGetBytesIdentifierRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionGetBytesIdentifierResponse:
	def __init__(self, identifier: bytes = b""):
		self.identifier: bytes = identifier

	def _update_content(self, discussion_get_bytes_identifier_response: DiscussionGetBytesIdentifierResponse) -> None:
		self.identifier: bytes = discussion_get_bytes_identifier_response.identifier

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetBytesIdentifierResponse":
		return DiscussionGetBytesIdentifierResponse(identifier=self.identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetBytesIdentifierResponse) -> "DiscussionGetBytesIdentifierResponse":
		return DiscussionGetBytesIdentifierResponse(identifier=native_message.identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetBytesIdentifierResponse]) -> list["DiscussionGetBytesIdentifierResponse"]:
		return [DiscussionGetBytesIdentifierResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetBytesIdentifierResponse]) -> "DiscussionGetBytesIdentifierResponse":
		try:
			native_message = await promise
			return DiscussionGetBytesIdentifierResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionGetBytesIdentifierResponse"]):
		if messages is None:
			return []
		return [DiscussionGetBytesIdentifierResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionGetBytesIdentifierResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetBytesIdentifierResponse(identifier=message.identifier if message.identifier else None)

	def __str__(self):
		s: str = ''
		if self.identifier:
			s += f'identifier: {self.identifier}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionGetBytesIdentifierResponse):
			return False
		return self.identifier == other.identifier

	def __bool__(self):
		return self.identifier != b""

	def __hash__(self):
		return hash(self.identifier)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionGetBytesIdentifierResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identifier == b"" or self.identifier == expected.identifier, "Invalid value: identifier: " + str(expected.identifier) + " != " + str(self.identifier)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionGetByContactRequest:
	def __init__(self, contact_id: int = 0):
		self.contact_id: int = contact_id

	def _update_content(self, discussion_get_by_contact_request: DiscussionGetByContactRequest) -> None:
		self.contact_id: int = discussion_get_by_contact_request.contact_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetByContactRequest":
		return DiscussionGetByContactRequest(contact_id=self.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactRequest) -> "DiscussionGetByContactRequest":
		return DiscussionGetByContactRequest(contact_id=native_message.contact_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactRequest]) -> list["DiscussionGetByContactRequest"]:
		return [DiscussionGetByContactRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactRequest]) -> "DiscussionGetByContactRequest":
		try:
			native_message = await promise
			return DiscussionGetByContactRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussion: "Discussion" = None):
		self.discussion: Discussion = discussion

	def _update_content(self, discussion_get_by_contact_response: DiscussionGetByContactResponse) -> None:
		self.discussion: Discussion = discussion_get_by_contact_response.discussion

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetByContactResponse":
		return DiscussionGetByContactResponse(discussion=self.discussion._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactResponse) -> "DiscussionGetByContactResponse":
		return DiscussionGetByContactResponse(discussion=Discussion._from_native(native_message.discussion))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactResponse]) -> list["DiscussionGetByContactResponse"]:
		return [DiscussionGetByContactResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactResponse]) -> "DiscussionGetByContactResponse":
		try:
			native_message = await promise
			return DiscussionGetByContactResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group_id: int = 0):
		self.group_id: int = group_id

	def _update_content(self, discussion_get_by_group_request: DiscussionGetByGroupRequest) -> None:
		self.group_id: int = discussion_get_by_group_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetByGroupRequest":
		return DiscussionGetByGroupRequest(group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupRequest) -> "DiscussionGetByGroupRequest":
		return DiscussionGetByGroupRequest(group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupRequest]) -> list["DiscussionGetByGroupRequest"]:
		return [DiscussionGetByGroupRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupRequest]) -> "DiscussionGetByGroupRequest":
		try:
			native_message = await promise
			return DiscussionGetByGroupRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussion: "Discussion" = None):
		self.discussion: Discussion = discussion

	def _update_content(self, discussion_get_by_group_response: DiscussionGetByGroupResponse) -> None:
		self.discussion: Discussion = discussion_get_by_group_response.discussion

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionGetByGroupResponse":
		return DiscussionGetByGroupResponse(discussion=self.discussion._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupResponse) -> "DiscussionGetByGroupResponse":
		return DiscussionGetByGroupResponse(discussion=Discussion._from_native(native_message.discussion))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupResponse]) -> list["DiscussionGetByGroupResponse"]:
		return [DiscussionGetByGroupResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupResponse]) -> "DiscussionGetByGroupResponse":
		try:
			native_message = await promise
			return DiscussionGetByGroupResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussion_id: int = 0):
		self.discussion_id: int = discussion_id

	def _update_content(self, discussion_empty_request: DiscussionEmptyRequest) -> None:
		self.discussion_id: int = discussion_empty_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionEmptyRequest":
		return DiscussionEmptyRequest(discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyRequest) -> "DiscussionEmptyRequest":
		return DiscussionEmptyRequest(discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyRequest]) -> list["DiscussionEmptyRequest"]:
		return [DiscussionEmptyRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyRequest]) -> "DiscussionEmptyRequest":
		try:
			native_message = await promise
			return DiscussionEmptyRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyRequest(discussion_id=message.discussion_id if message.discussion_id else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionEmptyRequest):
			return False
		return self.discussion_id == other.discussion_id

	def __bool__(self):
		return self.discussion_id != 0

	def __hash__(self):
		return hash(self.discussion_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionEmptyRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionEmptyResponse:
	def __init__(self):
		pass

	def _update_content(self, discussion_empty_response: DiscussionEmptyResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionEmptyResponse":
		return DiscussionEmptyResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyResponse) -> "DiscussionEmptyResponse":
		return DiscussionEmptyResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyResponse]) -> list["DiscussionEmptyResponse"]:
		return [DiscussionEmptyResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyResponse]) -> "DiscussionEmptyResponse":
		try:
			native_message = await promise
			return DiscussionEmptyResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
class DiscussionDownloadPhotoRequest:
	def __init__(self, discussion_id: int = 0):
		self.discussion_id: int = discussion_id

	def _update_content(self, discussion_download_photo_request: DiscussionDownloadPhotoRequest) -> None:
		self.discussion_id: int = discussion_download_photo_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionDownloadPhotoRequest":
		return DiscussionDownloadPhotoRequest(discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionDownloadPhotoRequest) -> "DiscussionDownloadPhotoRequest":
		return DiscussionDownloadPhotoRequest(discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionDownloadPhotoRequest]) -> list["DiscussionDownloadPhotoRequest"]:
		return [DiscussionDownloadPhotoRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionDownloadPhotoRequest]) -> "DiscussionDownloadPhotoRequest":
		try:
			native_message = await promise
			return DiscussionDownloadPhotoRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionDownloadPhotoRequest"]):
		if messages is None:
			return []
		return [DiscussionDownloadPhotoRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionDownloadPhotoRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionDownloadPhotoRequest(discussion_id=message.discussion_id if message.discussion_id else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionDownloadPhotoRequest):
			return False
		return self.discussion_id == other.discussion_id

	def __bool__(self):
		return self.discussion_id != 0

	def __hash__(self):
		return hash(self.discussion_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionDownloadPhotoRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionDownloadPhotoResponse:
	def __init__(self, photo: bytes = b""):
		self.photo: bytes = photo

	def _update_content(self, discussion_download_photo_response: DiscussionDownloadPhotoResponse) -> None:
		self.photo: bytes = discussion_download_photo_response.photo

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionDownloadPhotoResponse":
		return DiscussionDownloadPhotoResponse(photo=self.photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionDownloadPhotoResponse) -> "DiscussionDownloadPhotoResponse":
		return DiscussionDownloadPhotoResponse(photo=native_message.photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionDownloadPhotoResponse]) -> list["DiscussionDownloadPhotoResponse"]:
		return [DiscussionDownloadPhotoResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionDownloadPhotoResponse]) -> "DiscussionDownloadPhotoResponse":
		try:
			native_message = await promise
			return DiscussionDownloadPhotoResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DiscussionDownloadPhotoResponse"]):
		if messages is None:
			return []
		return [DiscussionDownloadPhotoResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DiscussionDownloadPhotoResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.discussion_commands_pb2.DiscussionDownloadPhotoResponse(photo=message.photo if message.photo else None)

	def __str__(self):
		s: str = ''
		if self.photo:
			s += f'photo: {self.photo}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DiscussionDownloadPhotoResponse):
			return False
		return self.photo == other.photo

	def __bool__(self):
		return self.photo != b""

	def __hash__(self):
		return hash(self.photo)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DiscussionDownloadPhotoResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.photo == b"" or self.photo == expected.photo, "Invalid value: photo: " + str(expected.photo) + " != " + str(self.photo)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DiscussionLockedListRequest:
	def __init__(self):
		pass

	def _update_content(self, discussion_locked_list_request: DiscussionLockedListRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionLockedListRequest":
		return DiscussionLockedListRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListRequest) -> "DiscussionLockedListRequest":
		return DiscussionLockedListRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListRequest]) -> list["DiscussionLockedListRequest"]:
		return [DiscussionLockedListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListRequest]) -> "DiscussionLockedListRequest":
		try:
			native_message = await promise
			return DiscussionLockedListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, discussions: "list[Discussion]" = None):
		self.discussions: list[Discussion] = discussions

	def _update_content(self, discussion_locked_list_response: DiscussionLockedListResponse) -> None:
		self.discussions: list[Discussion] = discussion_locked_list_response.discussions

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionLockedListResponse":
		return DiscussionLockedListResponse(discussions=[e._clone() for e in self.discussions])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListResponse) -> "DiscussionLockedListResponse":
		return DiscussionLockedListResponse(discussions=Discussion._from_native_list(native_message.discussions))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListResponse]) -> list["DiscussionLockedListResponse"]:
		return [DiscussionLockedListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListResponse]) -> "DiscussionLockedListResponse":
		try:
			native_message = await promise
			return DiscussionLockedListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussion_id: int = 0):
		self.discussion_id: int = discussion_id

	def _update_content(self, discussion_locked_delete_request: DiscussionLockedDeleteRequest) -> None:
		self.discussion_id: int = discussion_locked_delete_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionLockedDeleteRequest":
		return DiscussionLockedDeleteRequest(discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteRequest) -> "DiscussionLockedDeleteRequest":
		return DiscussionLockedDeleteRequest(discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteRequest]) -> list["DiscussionLockedDeleteRequest"]:
		return [DiscussionLockedDeleteRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteRequest]) -> "DiscussionLockedDeleteRequest":
		try:
			native_message = await promise
			return DiscussionLockedDeleteRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, discussion_locked_delete_response: DiscussionLockedDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionLockedDeleteResponse":
		return DiscussionLockedDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteResponse) -> "DiscussionLockedDeleteResponse":
		return DiscussionLockedDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteResponse]) -> list["DiscussionLockedDeleteResponse"]:
		return [DiscussionLockedDeleteResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteResponse]) -> "DiscussionLockedDeleteResponse":
		try:
			native_message = await promise
			return DiscussionLockedDeleteResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, filter: "GroupFilter" = None):
		self.filter: GroupFilter = filter

	def _update_content(self, group_list_request: GroupListRequest) -> None:
		self.filter: GroupFilter = group_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupListRequest":
		return GroupListRequest(filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupListRequest) -> "GroupListRequest":
		return GroupListRequest(filter=GroupFilter._from_native(native_message.filter))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupListRequest]) -> list["GroupListRequest"]:
		return [GroupListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupListRequest]) -> "GroupListRequest":
		try:
			native_message = await promise
			return GroupListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, groups: "list[Group]" = None):
		self.groups: list[Group] = groups

	def _update_content(self, group_list_response: GroupListResponse) -> None:
		self.groups: list[Group] = group_list_response.groups

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupListResponse":
		return GroupListResponse(groups=[e._clone() for e in self.groups])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupListResponse) -> "GroupListResponse":
		return GroupListResponse(groups=Group._from_native_list(native_message.groups))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupListResponse]) -> list["GroupListResponse"]:
		return [GroupListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupListResponse]) -> "GroupListResponse":
		try:
			native_message = await promise
			return GroupListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group_id: int = 0):
		self.group_id: int = group_id

	def _update_content(self, group_get_request: GroupGetRequest) -> None:
		self.group_id: int = group_get_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupGetRequest":
		return GroupGetRequest(group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupGetRequest) -> "GroupGetRequest":
		return GroupGetRequest(group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupGetRequest]) -> list["GroupGetRequest"]:
		return [GroupGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupGetRequest]) -> "GroupGetRequest":
		try:
			native_message = await promise
			return GroupGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_get_response: GroupGetResponse) -> None:
		self.group: Group = group_get_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupGetResponse":
		return GroupGetResponse(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupGetResponse) -> "GroupGetResponse":
		return GroupGetResponse(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupGetResponse]) -> list["GroupGetResponse"]:
		return [GroupGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupGetResponse]) -> "GroupGetResponse":
		try:
			native_message = await promise
			return GroupGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
class GroupGetBytesIdentifierRequest:
	def __init__(self, group_id: int = 0):
		self.group_id: int = group_id

	def _update_content(self, group_get_bytes_identifier_request: GroupGetBytesIdentifierRequest) -> None:
		self.group_id: int = group_get_bytes_identifier_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupGetBytesIdentifierRequest":
		return GroupGetBytesIdentifierRequest(group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupGetBytesIdentifierRequest) -> "GroupGetBytesIdentifierRequest":
		return GroupGetBytesIdentifierRequest(group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupGetBytesIdentifierRequest]) -> list["GroupGetBytesIdentifierRequest"]:
		return [GroupGetBytesIdentifierRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupGetBytesIdentifierRequest]) -> "GroupGetBytesIdentifierRequest":
		try:
			native_message = await promise
			return GroupGetBytesIdentifierRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupGetBytesIdentifierRequest"]):
		if messages is None:
			return []
		return [GroupGetBytesIdentifierRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupGetBytesIdentifierRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupGetBytesIdentifierRequest(group_id=message.group_id if message.group_id else None)

	def __str__(self):
		s: str = ''
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupGetBytesIdentifierRequest):
			return False
		return self.group_id == other.group_id

	def __bool__(self):
		return self.group_id != 0

	def __hash__(self):
		return hash(self.group_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupGetBytesIdentifierRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.group_id == 0 or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupGetBytesIdentifierResponse:
	def __init__(self, identifier: bytes = b""):
		self.identifier: bytes = identifier

	def _update_content(self, group_get_bytes_identifier_response: GroupGetBytesIdentifierResponse) -> None:
		self.identifier: bytes = group_get_bytes_identifier_response.identifier

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupGetBytesIdentifierResponse":
		return GroupGetBytesIdentifierResponse(identifier=self.identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupGetBytesIdentifierResponse) -> "GroupGetBytesIdentifierResponse":
		return GroupGetBytesIdentifierResponse(identifier=native_message.identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupGetBytesIdentifierResponse]) -> list["GroupGetBytesIdentifierResponse"]:
		return [GroupGetBytesIdentifierResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupGetBytesIdentifierResponse]) -> "GroupGetBytesIdentifierResponse":
		try:
			native_message = await promise
			return GroupGetBytesIdentifierResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupGetBytesIdentifierResponse"]):
		if messages is None:
			return []
		return [GroupGetBytesIdentifierResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupGetBytesIdentifierResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupGetBytesIdentifierResponse(identifier=message.identifier if message.identifier else None)

	def __str__(self):
		s: str = ''
		if self.identifier:
			s += f'identifier: {self.identifier}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupGetBytesIdentifierResponse):
			return False
		return self.identifier == other.identifier

	def __bool__(self):
		return self.identifier != b""

	def __hash__(self):
		return hash(self.identifier)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupGetBytesIdentifierResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identifier == b"" or self.identifier == expected.identifier, "Invalid value: identifier: " + str(expected.identifier) + " != " + str(self.identifier)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupNewStandardGroupRequest:
	def __init__(self, name: str = "", description: str = "", admin_contact_ids: list[int] = ()):
		self.name: str = name
		self.description: str = description
		self.admin_contact_ids: list[int] = admin_contact_ids

	def _update_content(self, group_new_standard_group_request: GroupNewStandardGroupRequest) -> None:
		self.name: str = group_new_standard_group_request.name
		self.description: str = group_new_standard_group_request.description
		self.admin_contact_ids: list[int] = group_new_standard_group_request.admin_contact_ids

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewStandardGroupRequest":
		return GroupNewStandardGroupRequest(name=self.name, description=self.description, admin_contact_ids=[e for e in self.admin_contact_ids])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupRequest) -> "GroupNewStandardGroupRequest":
		return GroupNewStandardGroupRequest(name=native_message.name, description=native_message.description, admin_contact_ids=native_message.admin_contact_ids)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupRequest]) -> list["GroupNewStandardGroupRequest"]:
		return [GroupNewStandardGroupRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupRequest]) -> "GroupNewStandardGroupRequest":
		try:
			native_message = await promise
			return GroupNewStandardGroupRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_new_standard_group_response: GroupNewStandardGroupResponse) -> None:
		self.group: Group = group_new_standard_group_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewStandardGroupResponse":
		return GroupNewStandardGroupResponse(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupResponse) -> "GroupNewStandardGroupResponse":
		return GroupNewStandardGroupResponse(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupResponse]) -> list["GroupNewStandardGroupResponse"]:
		return [GroupNewStandardGroupResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupResponse]) -> "GroupNewStandardGroupResponse":
		try:
			native_message = await promise
			return GroupNewStandardGroupResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, name: str = "", description: str = "", admin_contact_ids: list[int] = (), contact_ids: list[int] = ()):
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
		return GroupNewControlledGroupRequest(name=self.name, description=self.description, admin_contact_ids=[e for e in self.admin_contact_ids], contact_ids=[e for e in self.contact_ids])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupRequest) -> "GroupNewControlledGroupRequest":
		return GroupNewControlledGroupRequest(name=native_message.name, description=native_message.description, admin_contact_ids=native_message.admin_contact_ids, contact_ids=native_message.contact_ids)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupRequest]) -> list["GroupNewControlledGroupRequest"]:
		return [GroupNewControlledGroupRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupRequest]) -> "GroupNewControlledGroupRequest":
		try:
			native_message = await promise
			return GroupNewControlledGroupRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_new_controlled_group_response: GroupNewControlledGroupResponse) -> None:
		self.group: Group = group_new_controlled_group_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewControlledGroupResponse":
		return GroupNewControlledGroupResponse(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupResponse) -> "GroupNewControlledGroupResponse":
		return GroupNewControlledGroupResponse(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupResponse]) -> list["GroupNewControlledGroupResponse"]:
		return [GroupNewControlledGroupResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupResponse]) -> "GroupNewControlledGroupResponse":
		try:
			native_message = await promise
			return GroupNewControlledGroupResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, name: str = "", description: str = "", admin_contact_ids: list[int] = (), contact_ids: list[int] = ()):
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
		return GroupNewReadOnlyGroupRequest(name=self.name, description=self.description, admin_contact_ids=[e for e in self.admin_contact_ids], contact_ids=[e for e in self.contact_ids])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupRequest) -> "GroupNewReadOnlyGroupRequest":
		return GroupNewReadOnlyGroupRequest(name=native_message.name, description=native_message.description, admin_contact_ids=native_message.admin_contact_ids, contact_ids=native_message.contact_ids)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupRequest]) -> list["GroupNewReadOnlyGroupRequest"]:
		return [GroupNewReadOnlyGroupRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupRequest]) -> "GroupNewReadOnlyGroupRequest":
		try:
			native_message = await promise
			return GroupNewReadOnlyGroupRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_new_read_only_group_response: GroupNewReadOnlyGroupResponse) -> None:
		self.group: Group = group_new_read_only_group_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewReadOnlyGroupResponse":
		return GroupNewReadOnlyGroupResponse(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupResponse) -> "GroupNewReadOnlyGroupResponse":
		return GroupNewReadOnlyGroupResponse(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupResponse]) -> list["GroupNewReadOnlyGroupResponse"]:
		return [GroupNewReadOnlyGroupResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupResponse]) -> "GroupNewReadOnlyGroupResponse":
		try:
			native_message = await promise
			return GroupNewReadOnlyGroupResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, name: str = "", description: str = "", advanced_configuration: "Group.AdvancedConfiguration" = None, members: "list[GroupMember]" = None):
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
		return GroupNewAdvancedGroupRequest(name=self.name, description=self.description, advanced_configuration=self.advanced_configuration._clone(), members=[e._clone() for e in self.members])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupRequest) -> "GroupNewAdvancedGroupRequest":
		return GroupNewAdvancedGroupRequest(name=native_message.name, description=native_message.description, advanced_configuration=Group.AdvancedConfiguration._from_native(native_message.advanced_configuration), members=GroupMember._from_native_list(native_message.members))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupRequest]) -> list["GroupNewAdvancedGroupRequest"]:
		return [GroupNewAdvancedGroupRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupRequest]) -> "GroupNewAdvancedGroupRequest":
		try:
			native_message = await promise
			return GroupNewAdvancedGroupRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_new_advanced_group_response: GroupNewAdvancedGroupResponse) -> None:
		self.group: Group = group_new_advanced_group_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupNewAdvancedGroupResponse":
		return GroupNewAdvancedGroupResponse(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupResponse) -> "GroupNewAdvancedGroupResponse":
		return GroupNewAdvancedGroupResponse(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupResponse]) -> list["GroupNewAdvancedGroupResponse"]:
		return [GroupNewAdvancedGroupResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupResponse]) -> "GroupNewAdvancedGroupResponse":
		try:
			native_message = await promise
			return GroupNewAdvancedGroupResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group_id: int = 0):
		self.group_id: int = group_id

	def _update_content(self, group_disband_request: GroupDisbandRequest) -> None:
		self.group_id: int = group_disband_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupDisbandRequest":
		return GroupDisbandRequest(group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupDisbandRequest) -> "GroupDisbandRequest":
		return GroupDisbandRequest(group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupDisbandRequest]) -> list["GroupDisbandRequest"]:
		return [GroupDisbandRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupDisbandRequest]) -> "GroupDisbandRequest":
		try:
			native_message = await promise
			return GroupDisbandRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_disband_response: GroupDisbandResponse) -> None:
		self.group: Group = group_disband_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupDisbandResponse":
		return GroupDisbandResponse(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupDisbandResponse) -> "GroupDisbandResponse":
		return GroupDisbandResponse(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupDisbandResponse]) -> list["GroupDisbandResponse"]:
		return [GroupDisbandResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupDisbandResponse]) -> "GroupDisbandResponse":
		try:
			native_message = await promise
			return GroupDisbandResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group_id: int = 0):
		self.group_id: int = group_id

	def _update_content(self, group_leave_request: GroupLeaveRequest) -> None:
		self.group_id: int = group_leave_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupLeaveRequest":
		return GroupLeaveRequest(group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupLeaveRequest) -> "GroupLeaveRequest":
		return GroupLeaveRequest(group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupLeaveRequest]) -> list["GroupLeaveRequest"]:
		return [GroupLeaveRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupLeaveRequest]) -> "GroupLeaveRequest":
		try:
			native_message = await promise
			return GroupLeaveRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_leave_response: GroupLeaveResponse) -> None:
		self.group: Group = group_leave_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupLeaveResponse":
		return GroupLeaveResponse(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupLeaveResponse) -> "GroupLeaveResponse":
		return GroupLeaveResponse(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupLeaveResponse]) -> list["GroupLeaveResponse"]:
		return [GroupLeaveResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupLeaveResponse]) -> "GroupLeaveResponse":
		try:
			native_message = await promise
			return GroupLeaveResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_update_request: GroupUpdateRequest) -> None:
		self.group: Group = group_update_request.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupUpdateRequest":
		return GroupUpdateRequest(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupUpdateRequest) -> "GroupUpdateRequest":
		return GroupUpdateRequest(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupUpdateRequest]) -> list["GroupUpdateRequest"]:
		return [GroupUpdateRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupUpdateRequest]) -> "GroupUpdateRequest":
		try:
			native_message = await promise
			return GroupUpdateRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_update_response: GroupUpdateResponse) -> None:
		self.group: Group = group_update_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupUpdateResponse":
		return GroupUpdateResponse(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupUpdateResponse) -> "GroupUpdateResponse":
		return GroupUpdateResponse(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupUpdateResponse]) -> list["GroupUpdateResponse"]:
		return [GroupUpdateResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupUpdateResponse]) -> "GroupUpdateResponse":
		try:
			native_message = await promise
			return GroupUpdateResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group_id: int = 0):
		self.group_id: int = group_id

	def _update_content(self, group_unset_photo_request: GroupUnsetPhotoRequest) -> None:
		self.group_id: int = group_unset_photo_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupUnsetPhotoRequest":
		return GroupUnsetPhotoRequest(group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoRequest) -> "GroupUnsetPhotoRequest":
		return GroupUnsetPhotoRequest(group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoRequest]) -> list["GroupUnsetPhotoRequest"]:
		return [GroupUnsetPhotoRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoRequest]) -> "GroupUnsetPhotoRequest":
		try:
			native_message = await promise
			return GroupUnsetPhotoRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_unset_photo_response: GroupUnsetPhotoResponse) -> None:
		self.group: Group = group_unset_photo_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupUnsetPhotoResponse":
		return GroupUnsetPhotoResponse(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoResponse) -> "GroupUnsetPhotoResponse":
		return GroupUnsetPhotoResponse(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoResponse]) -> list["GroupUnsetPhotoResponse"]:
		return [GroupUnsetPhotoResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoResponse]) -> "GroupUnsetPhotoResponse":
		try:
			native_message = await promise
			return GroupUnsetPhotoResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group_id: int = 0, filename: str = "", file_size: int = 0):
		self.group_id: int = group_id
		self.filename: str = filename
		self.file_size: int = file_size

	def _update_content(self, group_set_photo_request_metadata: GroupSetPhotoRequestMetadata) -> None:
		self.group_id: int = group_set_photo_request_metadata.group_id
		self.filename: str = group_set_photo_request_metadata.filename
		self.file_size: int = group_set_photo_request_metadata.file_size

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupSetPhotoRequestMetadata":
		return GroupSetPhotoRequestMetadata(group_id=self.group_id, filename=self.filename, file_size=self.file_size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequestMetadata) -> "GroupSetPhotoRequestMetadata":
		return GroupSetPhotoRequestMetadata(group_id=native_message.group_id, filename=native_message.filename, file_size=native_message.file_size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequestMetadata]) -> list["GroupSetPhotoRequestMetadata"]:
		return [GroupSetPhotoRequestMetadata._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequestMetadata]) -> "GroupSetPhotoRequestMetadata":
		try:
			native_message = await promise
			return GroupSetPhotoRequestMetadata._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, metadata: "GroupSetPhotoRequestMetadata" = None, payload: bytes = None):
		self.metadata: GroupSetPhotoRequestMetadata = metadata
		self.payload: bytes = payload

	def _update_content(self, group_set_photo_request: GroupSetPhotoRequest) -> None:
		self.metadata: GroupSetPhotoRequestMetadata = group_set_photo_request.metadata
		self.payload: bytes = group_set_photo_request.payload

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupSetPhotoRequest":
		return GroupSetPhotoRequest(metadata=self.metadata._clone(), payload=self.payload)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequest) -> "GroupSetPhotoRequest":
		return GroupSetPhotoRequest(metadata=GroupSetPhotoRequestMetadata._from_native(native_message.metadata), payload=native_message.payload)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequest]) -> list["GroupSetPhotoRequest"]:
		return [GroupSetPhotoRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoRequest]) -> "GroupSetPhotoRequest":
		try:
			native_message = await promise
			return GroupSetPhotoRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, group: "Group" = None):
		self.group: Group = group

	def _update_content(self, group_set_photo_response: GroupSetPhotoResponse) -> None:
		self.group: Group = group_set_photo_response.group

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupSetPhotoResponse":
		return GroupSetPhotoResponse(group=self.group._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoResponse) -> "GroupSetPhotoResponse":
		return GroupSetPhotoResponse(group=Group._from_native(native_message.group))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoResponse]) -> list["GroupSetPhotoResponse"]:
		return [GroupSetPhotoResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupSetPhotoResponse]) -> "GroupSetPhotoResponse":
		try:
			native_message = await promise
			return GroupSetPhotoResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
class GroupDownloadPhotoRequest:
	def __init__(self, group_id: int = 0):
		self.group_id: int = group_id

	def _update_content(self, group_download_photo_request: GroupDownloadPhotoRequest) -> None:
		self.group_id: int = group_download_photo_request.group_id

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupDownloadPhotoRequest":
		return GroupDownloadPhotoRequest(group_id=self.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupDownloadPhotoRequest) -> "GroupDownloadPhotoRequest":
		return GroupDownloadPhotoRequest(group_id=native_message.group_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupDownloadPhotoRequest]) -> list["GroupDownloadPhotoRequest"]:
		return [GroupDownloadPhotoRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupDownloadPhotoRequest]) -> "GroupDownloadPhotoRequest":
		try:
			native_message = await promise
			return GroupDownloadPhotoRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupDownloadPhotoRequest"]):
		if messages is None:
			return []
		return [GroupDownloadPhotoRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupDownloadPhotoRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupDownloadPhotoRequest(group_id=message.group_id if message.group_id else None)

	def __str__(self):
		s: str = ''
		if self.group_id:
			s += f'group_id: {self.group_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupDownloadPhotoRequest):
			return False
		return self.group_id == other.group_id

	def __bool__(self):
		return self.group_id != 0

	def __hash__(self):
		return hash(self.group_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupDownloadPhotoRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.group_id == 0 or self.group_id == expected.group_id, "Invalid value: group_id: " + str(expected.group_id) + " != " + str(self.group_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class GroupDownloadPhotoResponse:
	def __init__(self, photo: bytes = b""):
		self.photo: bytes = photo

	def _update_content(self, group_download_photo_response: GroupDownloadPhotoResponse) -> None:
		self.photo: bytes = group_download_photo_response.photo

	# noinspection PyProtectedMember
	def _clone(self) -> "GroupDownloadPhotoResponse":
		return GroupDownloadPhotoResponse(photo=self.photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.group_commands_pb2.GroupDownloadPhotoResponse) -> "GroupDownloadPhotoResponse":
		return GroupDownloadPhotoResponse(photo=native_message.photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.group_commands_pb2.GroupDownloadPhotoResponse]) -> list["GroupDownloadPhotoResponse"]:
		return [GroupDownloadPhotoResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.group_commands_pb2.GroupDownloadPhotoResponse]) -> "GroupDownloadPhotoResponse":
		try:
			native_message = await promise
			return GroupDownloadPhotoResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["GroupDownloadPhotoResponse"]):
		if messages is None:
			return []
		return [GroupDownloadPhotoResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["GroupDownloadPhotoResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.group_commands_pb2.GroupDownloadPhotoResponse(photo=message.photo if message.photo else None)

	def __str__(self):
		s: str = ''
		if self.photo:
			s += f'photo: {self.photo}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, GroupDownloadPhotoResponse):
			return False
		return self.photo == other.photo

	def __bool__(self):
		return self.photo != b""

	def __hash__(self):
		return hash(self.photo)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, GroupDownloadPhotoResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.photo == b"" or self.photo == expected.photo, "Invalid value: photo: " + str(expected.photo) + " != " + str(self.photo)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityGetRequest:
	def __init__(self):
		pass

	def _update_content(self, identity_get_request: IdentityGetRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityGetRequest":
		return IdentityGetRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityGetRequest) -> "IdentityGetRequest":
		return IdentityGetRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityGetRequest]) -> list["IdentityGetRequest"]:
		return [IdentityGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityGetRequest]) -> "IdentityGetRequest":
		try:
			native_message = await promise
			return IdentityGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, identity: "Identity" = None):
		self.identity: Identity = identity

	def _update_content(self, identity_get_response: IdentityGetResponse) -> None:
		self.identity: Identity = identity_get_response.identity

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityGetResponse":
		return IdentityGetResponse(identity=self.identity._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityGetResponse) -> "IdentityGetResponse":
		return IdentityGetResponse(identity=Identity._from_native(native_message.identity))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityGetResponse]) -> list["IdentityGetResponse"]:
		return [IdentityGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityGetResponse]) -> "IdentityGetResponse":
		try:
			native_message = await promise
			return IdentityGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
class IdentityGetBytesIdentifierRequest:
	def __init__(self):
		pass

	def _update_content(self, identity_get_bytes_identifier_request: IdentityGetBytesIdentifierRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityGetBytesIdentifierRequest":
		return IdentityGetBytesIdentifierRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityGetBytesIdentifierRequest) -> "IdentityGetBytesIdentifierRequest":
		return IdentityGetBytesIdentifierRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityGetBytesIdentifierRequest]) -> list["IdentityGetBytesIdentifierRequest"]:
		return [IdentityGetBytesIdentifierRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityGetBytesIdentifierRequest]) -> "IdentityGetBytesIdentifierRequest":
		try:
			native_message = await promise
			return IdentityGetBytesIdentifierRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityGetBytesIdentifierRequest"]):
		if messages is None:
			return []
		return [IdentityGetBytesIdentifierRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityGetBytesIdentifierRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityGetBytesIdentifierRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityGetBytesIdentifierRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityGetBytesIdentifierRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityGetBytesIdentifierResponse:
	def __init__(self, identifier: bytes = b""):
		self.identifier: bytes = identifier

	def _update_content(self, identity_get_bytes_identifier_response: IdentityGetBytesIdentifierResponse) -> None:
		self.identifier: bytes = identity_get_bytes_identifier_response.identifier

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityGetBytesIdentifierResponse":
		return IdentityGetBytesIdentifierResponse(identifier=self.identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityGetBytesIdentifierResponse) -> "IdentityGetBytesIdentifierResponse":
		return IdentityGetBytesIdentifierResponse(identifier=native_message.identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityGetBytesIdentifierResponse]) -> list["IdentityGetBytesIdentifierResponse"]:
		return [IdentityGetBytesIdentifierResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityGetBytesIdentifierResponse]) -> "IdentityGetBytesIdentifierResponse":
		try:
			native_message = await promise
			return IdentityGetBytesIdentifierResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityGetBytesIdentifierResponse"]):
		if messages is None:
			return []
		return [IdentityGetBytesIdentifierResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityGetBytesIdentifierResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityGetBytesIdentifierResponse(identifier=message.identifier if message.identifier else None)

	def __str__(self):
		s: str = ''
		if self.identifier:
			s += f'identifier: {self.identifier}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityGetBytesIdentifierResponse):
			return False
		return self.identifier == other.identifier

	def __bool__(self):
		return self.identifier != b""

	def __hash__(self):
		return hash(self.identifier)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityGetBytesIdentifierResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identifier == b"" or self.identifier == expected.identifier, "Invalid value: identifier: " + str(expected.identifier) + " != " + str(self.identifier)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityGetInvitationLinkRequest:
	def __init__(self):
		pass

	def _update_content(self, identity_get_invitation_link_request: IdentityGetInvitationLinkRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityGetInvitationLinkRequest":
		return IdentityGetInvitationLinkRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityGetInvitationLinkRequest) -> "IdentityGetInvitationLinkRequest":
		return IdentityGetInvitationLinkRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityGetInvitationLinkRequest]) -> list["IdentityGetInvitationLinkRequest"]:
		return [IdentityGetInvitationLinkRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityGetInvitationLinkRequest]) -> "IdentityGetInvitationLinkRequest":
		try:
			native_message = await promise
			return IdentityGetInvitationLinkRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityGetInvitationLinkRequest"]):
		if messages is None:
			return []
		return [IdentityGetInvitationLinkRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityGetInvitationLinkRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityGetInvitationLinkRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityGetInvitationLinkRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityGetInvitationLinkRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityGetInvitationLinkResponse:
	def __init__(self, invitation_link: str = ""):
		self.invitation_link: str = invitation_link

	def _update_content(self, identity_get_invitation_link_response: IdentityGetInvitationLinkResponse) -> None:
		self.invitation_link: str = identity_get_invitation_link_response.invitation_link

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityGetInvitationLinkResponse":
		return IdentityGetInvitationLinkResponse(invitation_link=self.invitation_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityGetInvitationLinkResponse) -> "IdentityGetInvitationLinkResponse":
		return IdentityGetInvitationLinkResponse(invitation_link=native_message.invitation_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityGetInvitationLinkResponse]) -> list["IdentityGetInvitationLinkResponse"]:
		return [IdentityGetInvitationLinkResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityGetInvitationLinkResponse]) -> "IdentityGetInvitationLinkResponse":
		try:
			native_message = await promise
			return IdentityGetInvitationLinkResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityGetInvitationLinkResponse"]):
		if messages is None:
			return []
		return [IdentityGetInvitationLinkResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityGetInvitationLinkResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityGetInvitationLinkResponse(invitation_link=message.invitation_link if message.invitation_link else None)

	def __str__(self):
		s: str = ''
		if self.invitation_link:
			s += f'invitation_link: {self.invitation_link}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityGetInvitationLinkResponse):
			return False
		return self.invitation_link == other.invitation_link

	def __bool__(self):
		return self.invitation_link != ""

	def __hash__(self):
		return hash(self.invitation_link)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityGetInvitationLinkResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.invitation_link == "" or self.invitation_link == expected.invitation_link, "Invalid value: invitation_link: " + str(expected.invitation_link) + " != " + str(self.invitation_link)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityUpdateDetailsRequest:
	def __init__(self, new_details: "IdentityDetails" = None):
		self.new_details: IdentityDetails = new_details

	def _update_content(self, identity_update_details_request: IdentityUpdateDetailsRequest) -> None:
		self.new_details: IdentityDetails = identity_update_details_request.new_details

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityUpdateDetailsRequest":
		return IdentityUpdateDetailsRequest(new_details=self.new_details._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsRequest) -> "IdentityUpdateDetailsRequest":
		return IdentityUpdateDetailsRequest(new_details=IdentityDetails._from_native(native_message.new_details))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsRequest]) -> list["IdentityUpdateDetailsRequest"]:
		return [IdentityUpdateDetailsRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsRequest]) -> "IdentityUpdateDetailsRequest":
		try:
			native_message = await promise
			return IdentityUpdateDetailsRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, identity_update_details_response: IdentityUpdateDetailsResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityUpdateDetailsResponse":
		return IdentityUpdateDetailsResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsResponse) -> "IdentityUpdateDetailsResponse":
		return IdentityUpdateDetailsResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsResponse]) -> list["IdentityUpdateDetailsResponse"]:
		return [IdentityUpdateDetailsResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsResponse]) -> "IdentityUpdateDetailsResponse":
		try:
			native_message = await promise
			return IdentityUpdateDetailsResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self):
		pass

	def _update_content(self, identity_remove_photo_request: IdentityRemovePhotoRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityRemovePhotoRequest":
		return IdentityRemovePhotoRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoRequest) -> "IdentityRemovePhotoRequest":
		return IdentityRemovePhotoRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoRequest]) -> list["IdentityRemovePhotoRequest"]:
		return [IdentityRemovePhotoRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoRequest]) -> "IdentityRemovePhotoRequest":
		try:
			native_message = await promise
			return IdentityRemovePhotoRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self):
		pass

	def _update_content(self, identity_remove_photo_response: IdentityRemovePhotoResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityRemovePhotoResponse":
		return IdentityRemovePhotoResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoResponse) -> "IdentityRemovePhotoResponse":
		return IdentityRemovePhotoResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoResponse]) -> list["IdentityRemovePhotoResponse"]:
		return [IdentityRemovePhotoResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoResponse]) -> "IdentityRemovePhotoResponse":
		try:
			native_message = await promise
			return IdentityRemovePhotoResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, filename: str = "", file_size: int = 0):
		self.filename: str = filename
		self.file_size: int = file_size

	def _update_content(self, identity_set_photo_request_metadata: IdentitySetPhotoRequestMetadata) -> None:
		self.filename: str = identity_set_photo_request_metadata.filename
		self.file_size: int = identity_set_photo_request_metadata.file_size

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetPhotoRequestMetadata":
		return IdentitySetPhotoRequestMetadata(filename=self.filename, file_size=self.file_size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequestMetadata) -> "IdentitySetPhotoRequestMetadata":
		return IdentitySetPhotoRequestMetadata(filename=native_message.filename, file_size=native_message.file_size)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequestMetadata]) -> list["IdentitySetPhotoRequestMetadata"]:
		return [IdentitySetPhotoRequestMetadata._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequestMetadata]) -> "IdentitySetPhotoRequestMetadata":
		try:
			native_message = await promise
			return IdentitySetPhotoRequestMetadata._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, metadata: "IdentitySetPhotoRequestMetadata" = None, payload: bytes = None):
		self.metadata: IdentitySetPhotoRequestMetadata = metadata
		self.payload: bytes = payload

	def _update_content(self, identity_set_photo_request: IdentitySetPhotoRequest) -> None:
		self.metadata: IdentitySetPhotoRequestMetadata = identity_set_photo_request.metadata
		self.payload: bytes = identity_set_photo_request.payload

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetPhotoRequest":
		return IdentitySetPhotoRequest(metadata=self.metadata._clone(), payload=self.payload)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequest) -> "IdentitySetPhotoRequest":
		return IdentitySetPhotoRequest(metadata=IdentitySetPhotoRequestMetadata._from_native(native_message.metadata), payload=native_message.payload)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequest]) -> list["IdentitySetPhotoRequest"]:
		return [IdentitySetPhotoRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoRequest]) -> "IdentitySetPhotoRequest":
		try:
			native_message = await promise
			return IdentitySetPhotoRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, identity_set_photo_response: IdentitySetPhotoResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetPhotoResponse":
		return IdentitySetPhotoResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoResponse) -> "IdentitySetPhotoResponse":
		return IdentitySetPhotoResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoResponse]) -> list["IdentitySetPhotoResponse"]:
		return [IdentitySetPhotoResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetPhotoResponse]) -> "IdentitySetPhotoResponse":
		try:
			native_message = await promise
			return IdentitySetPhotoResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
class IdentityDownloadPhotoRequest:
	def __init__(self):
		pass

	def _update_content(self, identity_download_photo_request: IdentityDownloadPhotoRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityDownloadPhotoRequest":
		return IdentityDownloadPhotoRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityDownloadPhotoRequest) -> "IdentityDownloadPhotoRequest":
		return IdentityDownloadPhotoRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityDownloadPhotoRequest]) -> list["IdentityDownloadPhotoRequest"]:
		return [IdentityDownloadPhotoRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityDownloadPhotoRequest]) -> "IdentityDownloadPhotoRequest":
		try:
			native_message = await promise
			return IdentityDownloadPhotoRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityDownloadPhotoRequest"]):
		if messages is None:
			return []
		return [IdentityDownloadPhotoRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityDownloadPhotoRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityDownloadPhotoRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityDownloadPhotoRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityDownloadPhotoRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityDownloadPhotoResponse:
	def __init__(self, photo: bytes = b""):
		self.photo: bytes = photo

	def _update_content(self, identity_download_photo_response: IdentityDownloadPhotoResponse) -> None:
		self.photo: bytes = identity_download_photo_response.photo

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityDownloadPhotoResponse":
		return IdentityDownloadPhotoResponse(photo=self.photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityDownloadPhotoResponse) -> "IdentityDownloadPhotoResponse":
		return IdentityDownloadPhotoResponse(photo=native_message.photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityDownloadPhotoResponse]) -> list["IdentityDownloadPhotoResponse"]:
		return [IdentityDownloadPhotoResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityDownloadPhotoResponse]) -> "IdentityDownloadPhotoResponse":
		try:
			native_message = await promise
			return IdentityDownloadPhotoResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityDownloadPhotoResponse"]):
		if messages is None:
			return []
		return [IdentityDownloadPhotoResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityDownloadPhotoResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityDownloadPhotoResponse(photo=message.photo if message.photo else None)

	def __str__(self):
		s: str = ''
		if self.photo:
			s += f'photo: {self.photo}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityDownloadPhotoResponse):
			return False
		return self.photo == other.photo

	def __bool__(self):
		return self.photo != b""

	def __hash__(self):
		return hash(self.photo)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityDownloadPhotoResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.photo == b"" or self.photo == expected.photo, "Invalid value: photo: " + str(expected.photo) + " != " + str(self.photo)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityGetApiKeyStatusRequest:
	def __init__(self):
		pass

	def _update_content(self, identity_get_api_key_status_request: IdentityGetApiKeyStatusRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityGetApiKeyStatusRequest":
		return IdentityGetApiKeyStatusRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityGetApiKeyStatusRequest) -> "IdentityGetApiKeyStatusRequest":
		return IdentityGetApiKeyStatusRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityGetApiKeyStatusRequest]) -> list["IdentityGetApiKeyStatusRequest"]:
		return [IdentityGetApiKeyStatusRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityGetApiKeyStatusRequest]) -> "IdentityGetApiKeyStatusRequest":
		try:
			native_message = await promise
			return IdentityGetApiKeyStatusRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityGetApiKeyStatusRequest"]):
		if messages is None:
			return []
		return [IdentityGetApiKeyStatusRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityGetApiKeyStatusRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityGetApiKeyStatusRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityGetApiKeyStatusRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityGetApiKeyStatusRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityGetApiKeyStatusResponse:
	def __init__(self, api_key: "Identity.ApiKey" = None):
		self.api_key: Identity.ApiKey = api_key

	def _update_content(self, identity_get_api_key_status_response: IdentityGetApiKeyStatusResponse) -> None:
		self.api_key: Identity.ApiKey = identity_get_api_key_status_response.api_key

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityGetApiKeyStatusResponse":
		return IdentityGetApiKeyStatusResponse(api_key=self.api_key._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentityGetApiKeyStatusResponse) -> "IdentityGetApiKeyStatusResponse":
		return IdentityGetApiKeyStatusResponse(api_key=Identity.ApiKey._from_native(native_message.api_key))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentityGetApiKeyStatusResponse]) -> list["IdentityGetApiKeyStatusResponse"]:
		return [IdentityGetApiKeyStatusResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentityGetApiKeyStatusResponse]) -> "IdentityGetApiKeyStatusResponse":
		try:
			native_message = await promise
			return IdentityGetApiKeyStatusResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityGetApiKeyStatusResponse"]):
		if messages is None:
			return []
		return [IdentityGetApiKeyStatusResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityGetApiKeyStatusResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.identity_commands_pb2.IdentityGetApiKeyStatusResponse(api_key=Identity.ApiKey._to_native(message.api_key if message.api_key else None))

	def __str__(self):
		s: str = ''
		if self.api_key:
			s += f'api_key: ({self.api_key}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityGetApiKeyStatusResponse):
			return False
		return self.api_key == other.api_key

	def __bool__(self):
		return bool(self.api_key)

	def __hash__(self):
		return hash(self.api_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityGetApiKeyStatusResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.api_key is None or self.api_key._test_assertion(expected.api_key)
		except AssertionError as e:
			raise AssertionError("api_key: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentitySetApiKeyRequest:
	def __init__(self, api_key: str = ""):
		self.api_key: str = api_key

	def _update_content(self, identity_set_api_key_request: IdentitySetApiKeyRequest) -> None:
		self.api_key: str = identity_set_api_key_request.api_key

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetApiKeyRequest":
		return IdentitySetApiKeyRequest(api_key=self.api_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyRequest) -> "IdentitySetApiKeyRequest":
		return IdentitySetApiKeyRequest(api_key=native_message.api_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyRequest]) -> list["IdentitySetApiKeyRequest"]:
		return [IdentitySetApiKeyRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyRequest]) -> "IdentitySetApiKeyRequest":
		try:
			native_message = await promise
			return IdentitySetApiKeyRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, api_key: "Identity.ApiKey" = None):
		self.api_key: Identity.ApiKey = api_key

	def _update_content(self, identity_set_api_key_response: IdentitySetApiKeyResponse) -> None:
		self.api_key: Identity.ApiKey = identity_set_api_key_response.api_key

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetApiKeyResponse":
		return IdentitySetApiKeyResponse(api_key=self.api_key._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyResponse) -> "IdentitySetApiKeyResponse":
		return IdentitySetApiKeyResponse(api_key=Identity.ApiKey._from_native(native_message.api_key))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyResponse]) -> list["IdentitySetApiKeyResponse"]:
		return [IdentitySetApiKeyResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyResponse]) -> "IdentitySetApiKeyResponse":
		try:
			native_message = await promise
			return IdentitySetApiKeyResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, configuration_link: str = ""):
		self.configuration_link: str = configuration_link

	def _update_content(self, identity_set_configuration_link_request: IdentitySetConfigurationLinkRequest) -> None:
		self.configuration_link: str = identity_set_configuration_link_request.configuration_link

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetConfigurationLinkRequest":
		return IdentitySetConfigurationLinkRequest(configuration_link=self.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkRequest) -> "IdentitySetConfigurationLinkRequest":
		return IdentitySetConfigurationLinkRequest(configuration_link=native_message.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkRequest]) -> list["IdentitySetConfigurationLinkRequest"]:
		return [IdentitySetConfigurationLinkRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkRequest]) -> "IdentitySetConfigurationLinkRequest":
		try:
			native_message = await promise
			return IdentitySetConfigurationLinkRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, api_key: "Identity.ApiKey" = None):
		self.api_key: Identity.ApiKey = api_key

	def _update_content(self, identity_set_configuration_link_response: IdentitySetConfigurationLinkResponse) -> None:
		self.api_key: Identity.ApiKey = identity_set_configuration_link_response.api_key

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentitySetConfigurationLinkResponse":
		return IdentitySetConfigurationLinkResponse(api_key=self.api_key._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkResponse) -> "IdentitySetConfigurationLinkResponse":
		return IdentitySetConfigurationLinkResponse(api_key=Identity.ApiKey._from_native(native_message.api_key))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkResponse]) -> list["IdentitySetConfigurationLinkResponse"]:
		return [IdentitySetConfigurationLinkResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkResponse]) -> "IdentitySetConfigurationLinkResponse":
		try:
			native_message = await promise
			return IdentitySetConfigurationLinkResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, filter: "InvitationFilter" = None):
		self.filter: InvitationFilter = filter

	def _update_content(self, invitation_list_request: InvitationListRequest) -> None:
		self.filter: InvitationFilter = invitation_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationListRequest":
		return InvitationListRequest(filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationListRequest) -> "InvitationListRequest":
		return InvitationListRequest(filter=InvitationFilter._from_native(native_message.filter))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationListRequest]) -> list["InvitationListRequest"]:
		return [InvitationListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationListRequest]) -> "InvitationListRequest":
		try:
			native_message = await promise
			return InvitationListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, invitations: "list[Invitation]" = None):
		self.invitations: list[Invitation] = invitations

	def _update_content(self, invitation_list_response: InvitationListResponse) -> None:
		self.invitations: list[Invitation] = invitation_list_response.invitations

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationListResponse":
		return InvitationListResponse(invitations=[e._clone() for e in self.invitations])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationListResponse) -> "InvitationListResponse":
		return InvitationListResponse(invitations=Invitation._from_native_list(native_message.invitations))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationListResponse]) -> list["InvitationListResponse"]:
		return [InvitationListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationListResponse]) -> "InvitationListResponse":
		try:
			native_message = await promise
			return InvitationListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, invitation_id: int = 0):
		self.invitation_id: int = invitation_id

	def _update_content(self, invitation_get_request: InvitationGetRequest) -> None:
		self.invitation_id: int = invitation_get_request.invitation_id

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationGetRequest":
		return InvitationGetRequest(invitation_id=self.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetRequest) -> "InvitationGetRequest":
		return InvitationGetRequest(invitation_id=native_message.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetRequest]) -> list["InvitationGetRequest"]:
		return [InvitationGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetRequest]) -> "InvitationGetRequest":
		try:
			native_message = await promise
			return InvitationGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, invitation: "Invitation" = None):
		self.invitation: Invitation = invitation

	def _update_content(self, invitation_get_response: InvitationGetResponse) -> None:
		self.invitation: Invitation = invitation_get_response.invitation

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationGetResponse":
		return InvitationGetResponse(invitation=self.invitation._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetResponse) -> "InvitationGetResponse":
		return InvitationGetResponse(invitation=Invitation._from_native(native_message.invitation))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetResponse]) -> list["InvitationGetResponse"]:
		return [InvitationGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetResponse]) -> "InvitationGetResponse":
		try:
			native_message = await promise
			return InvitationGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, invitation_url: str = ""):
		self.invitation_url: str = invitation_url

	def _update_content(self, invitation_new_request: InvitationNewRequest) -> None:
		self.invitation_url: str = invitation_new_request.invitation_url

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationNewRequest":
		return InvitationNewRequest(invitation_url=self.invitation_url)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewRequest) -> "InvitationNewRequest":
		return InvitationNewRequest(invitation_url=native_message.invitation_url)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewRequest]) -> list["InvitationNewRequest"]:
		return [InvitationNewRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewRequest]) -> "InvitationNewRequest":
		try:
			native_message = await promise
			return InvitationNewRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, invitation: "Invitation" = None):
		self.invitation: Invitation = invitation

	def _update_content(self, invitation_new_response: InvitationNewResponse) -> None:
		self.invitation: Invitation = invitation_new_response.invitation

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationNewResponse":
		return InvitationNewResponse(invitation=self.invitation._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewResponse) -> "InvitationNewResponse":
		return InvitationNewResponse(invitation=Invitation._from_native(native_message.invitation))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewResponse]) -> list["InvitationNewResponse"]:
		return [InvitationNewResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewResponse]) -> "InvitationNewResponse":
		try:
			native_message = await promise
			return InvitationNewResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, invitation_id: int = 0):
		self.invitation_id: int = invitation_id

	def _update_content(self, invitation_accept_request: InvitationAcceptRequest) -> None:
		self.invitation_id: int = invitation_accept_request.invitation_id

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationAcceptRequest":
		return InvitationAcceptRequest(invitation_id=self.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptRequest) -> "InvitationAcceptRequest":
		return InvitationAcceptRequest(invitation_id=native_message.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptRequest]) -> list["InvitationAcceptRequest"]:
		return [InvitationAcceptRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptRequest]) -> "InvitationAcceptRequest":
		try:
			native_message = await promise
			return InvitationAcceptRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, invitation_accept_response: InvitationAcceptResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationAcceptResponse":
		return InvitationAcceptResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptResponse) -> "InvitationAcceptResponse":
		return InvitationAcceptResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptResponse]) -> list["InvitationAcceptResponse"]:
		return [InvitationAcceptResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptResponse]) -> "InvitationAcceptResponse":
		try:
			native_message = await promise
			return InvitationAcceptResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, invitation_id: int = 0):
		self.invitation_id: int = invitation_id

	def _update_content(self, invitation_decline_request: InvitationDeclineRequest) -> None:
		self.invitation_id: int = invitation_decline_request.invitation_id

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationDeclineRequest":
		return InvitationDeclineRequest(invitation_id=self.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineRequest) -> "InvitationDeclineRequest":
		return InvitationDeclineRequest(invitation_id=native_message.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineRequest]) -> list["InvitationDeclineRequest"]:
		return [InvitationDeclineRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineRequest]) -> "InvitationDeclineRequest":
		try:
			native_message = await promise
			return InvitationDeclineRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, invitation_decline_response: InvitationDeclineResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationDeclineResponse":
		return InvitationDeclineResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineResponse) -> "InvitationDeclineResponse":
		return InvitationDeclineResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineResponse]) -> list["InvitationDeclineResponse"]:
		return [InvitationDeclineResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineResponse]) -> "InvitationDeclineResponse":
		try:
			native_message = await promise
			return InvitationDeclineResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, invitation_id: int = 0, sas: str = ""):
		self.invitation_id: int = invitation_id
		self.sas: str = sas

	def _update_content(self, invitation_sas_request: InvitationSasRequest) -> None:
		self.invitation_id: int = invitation_sas_request.invitation_id
		self.sas: str = invitation_sas_request.sas

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationSasRequest":
		return InvitationSasRequest(invitation_id=self.invitation_id, sas=self.sas)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasRequest) -> "InvitationSasRequest":
		return InvitationSasRequest(invitation_id=native_message.invitation_id, sas=native_message.sas)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasRequest]) -> list["InvitationSasRequest"]:
		return [InvitationSasRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasRequest]) -> "InvitationSasRequest":
		try:
			native_message = await promise
			return InvitationSasRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, invitation_sas_response: InvitationSasResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationSasResponse":
		return InvitationSasResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasResponse) -> "InvitationSasResponse":
		return InvitationSasResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasResponse]) -> list["InvitationSasResponse"]:
		return [InvitationSasResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasResponse]) -> "InvitationSasResponse":
		try:
			native_message = await promise
			return InvitationSasResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, invitation_id: int = 0):
		self.invitation_id: int = invitation_id

	def _update_content(self, invitation_delete_request: InvitationDeleteRequest) -> None:
		self.invitation_id: int = invitation_delete_request.invitation_id

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationDeleteRequest":
		return InvitationDeleteRequest(invitation_id=self.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteRequest) -> "InvitationDeleteRequest":
		return InvitationDeleteRequest(invitation_id=native_message.invitation_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteRequest]) -> list["InvitationDeleteRequest"]:
		return [InvitationDeleteRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteRequest]) -> "InvitationDeleteRequest":
		try:
			native_message = await promise
			return InvitationDeleteRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, invitation_delete_response: InvitationDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "InvitationDeleteResponse":
		return InvitationDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteResponse) -> "InvitationDeleteResponse":
		return InvitationDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteResponse]) -> list["InvitationDeleteResponse"]:
		return [InvitationDeleteResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteResponse]) -> "InvitationDeleteResponse":
		try:
			native_message = await promise
			return InvitationDeleteResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
class KeycloakBindIdentityRequest:
	def __init__(self, configuration_link: str = ""):
		self.configuration_link: str = configuration_link

	def _update_content(self, keycloak_bind_identity_request: KeycloakBindIdentityRequest) -> None:
		self.configuration_link: str = keycloak_bind_identity_request.configuration_link

	# noinspection PyProtectedMember
	def _clone(self) -> "KeycloakBindIdentityRequest":
		return KeycloakBindIdentityRequest(configuration_link=self.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakBindIdentityRequest) -> "KeycloakBindIdentityRequest":
		return KeycloakBindIdentityRequest(configuration_link=native_message.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakBindIdentityRequest]) -> list["KeycloakBindIdentityRequest"]:
		return [KeycloakBindIdentityRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakBindIdentityRequest]) -> "KeycloakBindIdentityRequest":
		try:
			native_message = await promise
			return KeycloakBindIdentityRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["KeycloakBindIdentityRequest"]):
		if messages is None:
			return []
		return [KeycloakBindIdentityRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["KeycloakBindIdentityRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakBindIdentityRequest(configuration_link=message.configuration_link if message.configuration_link else None)

	def __str__(self):
		s: str = ''
		if self.configuration_link:
			s += f'configuration_link: {self.configuration_link}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, KeycloakBindIdentityRequest):
			return False
		return self.configuration_link == other.configuration_link

	def __bool__(self):
		return self.configuration_link != ""

	def __hash__(self):
		return hash(self.configuration_link)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, KeycloakBindIdentityRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.configuration_link == "" or self.configuration_link == expected.configuration_link, "Invalid value: configuration_link: " + str(expected.configuration_link) + " != " + str(self.configuration_link)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class KeycloakBindIdentityResponse:
	def __init__(self):
		pass

	def _update_content(self, keycloak_bind_identity_response: KeycloakBindIdentityResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "KeycloakBindIdentityResponse":
		return KeycloakBindIdentityResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakBindIdentityResponse) -> "KeycloakBindIdentityResponse":
		return KeycloakBindIdentityResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakBindIdentityResponse]) -> list["KeycloakBindIdentityResponse"]:
		return [KeycloakBindIdentityResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakBindIdentityResponse]) -> "KeycloakBindIdentityResponse":
		try:
			native_message = await promise
			return KeycloakBindIdentityResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["KeycloakBindIdentityResponse"]):
		if messages is None:
			return []
		return [KeycloakBindIdentityResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["KeycloakBindIdentityResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakBindIdentityResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, KeycloakBindIdentityResponse):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, KeycloakBindIdentityResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class KeycloakUnbindIdentityRequest:
	def __init__(self):
		pass

	def _update_content(self, keycloak_unbind_identity_request: KeycloakUnbindIdentityRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "KeycloakUnbindIdentityRequest":
		return KeycloakUnbindIdentityRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUnbindIdentityRequest) -> "KeycloakUnbindIdentityRequest":
		return KeycloakUnbindIdentityRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUnbindIdentityRequest]) -> list["KeycloakUnbindIdentityRequest"]:
		return [KeycloakUnbindIdentityRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUnbindIdentityRequest]) -> "KeycloakUnbindIdentityRequest":
		try:
			native_message = await promise
			return KeycloakUnbindIdentityRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["KeycloakUnbindIdentityRequest"]):
		if messages is None:
			return []
		return [KeycloakUnbindIdentityRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["KeycloakUnbindIdentityRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUnbindIdentityRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, KeycloakUnbindIdentityRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, KeycloakUnbindIdentityRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class KeycloakUnbindIdentityResponse:
	def __init__(self):
		pass

	def _update_content(self, keycloak_unbind_identity_response: KeycloakUnbindIdentityResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "KeycloakUnbindIdentityResponse":
		return KeycloakUnbindIdentityResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUnbindIdentityResponse) -> "KeycloakUnbindIdentityResponse":
		return KeycloakUnbindIdentityResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUnbindIdentityResponse]) -> list["KeycloakUnbindIdentityResponse"]:
		return [KeycloakUnbindIdentityResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUnbindIdentityResponse]) -> "KeycloakUnbindIdentityResponse":
		try:
			native_message = await promise
			return KeycloakUnbindIdentityResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["KeycloakUnbindIdentityResponse"]):
		if messages is None:
			return []
		return [KeycloakUnbindIdentityResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["KeycloakUnbindIdentityResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUnbindIdentityResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, KeycloakUnbindIdentityResponse):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, KeycloakUnbindIdentityResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class KeycloakUserListRequest:
	def __init__(self, filter: "KeycloakUserFilter" = None, last_list_timestamp: int = 0):
		self.filter: KeycloakUserFilter = filter
		self.last_list_timestamp: int = last_list_timestamp

	def _update_content(self, keycloak_user_list_request: KeycloakUserListRequest) -> None:
		self.filter: KeycloakUserFilter = keycloak_user_list_request.filter
		self.last_list_timestamp: int = keycloak_user_list_request.last_list_timestamp

	# noinspection PyProtectedMember
	def _clone(self) -> "KeycloakUserListRequest":
		return KeycloakUserListRequest(filter=self.filter._clone(), last_list_timestamp=self.last_list_timestamp)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUserListRequest) -> "KeycloakUserListRequest":
		return KeycloakUserListRequest(filter=KeycloakUserFilter._from_native(native_message.filter), last_list_timestamp=native_message.last_list_timestamp)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUserListRequest]) -> list["KeycloakUserListRequest"]:
		return [KeycloakUserListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUserListRequest]) -> "KeycloakUserListRequest":
		try:
			native_message = await promise
			return KeycloakUserListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["KeycloakUserListRequest"]):
		if messages is None:
			return []
		return [KeycloakUserListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["KeycloakUserListRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUserListRequest(filter=KeycloakUserFilter._to_native(message.filter if message.filter else None), last_list_timestamp=message.last_list_timestamp if message.last_list_timestamp else None)

	def __str__(self):
		s: str = ''
		if self.filter:
			s += f'filter: ({self.filter}), '
		if self.last_list_timestamp:
			s += f'last_list_timestamp: {self.last_list_timestamp}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, KeycloakUserListRequest):
			return False
		return self.filter == other.filter and self.last_list_timestamp == other.last_list_timestamp

	def __bool__(self):
		return bool(self.filter) or self.last_list_timestamp != 0

	def __hash__(self):
		return hash((self.filter, self.last_list_timestamp))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, KeycloakUserListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		assert expected.last_list_timestamp == 0 or self.last_list_timestamp == expected.last_list_timestamp, "Invalid value: last_list_timestamp: " + str(expected.last_list_timestamp) + " != " + str(self.last_list_timestamp)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class KeycloakUserListResponse:
	def __init__(self, users: "list[KeycloakUser]" = None, last_list_timestamp: int = 0):
		self.users: list[KeycloakUser] = users
		self.last_list_timestamp: int = last_list_timestamp

	def _update_content(self, keycloak_user_list_response: KeycloakUserListResponse) -> None:
		self.users: list[KeycloakUser] = keycloak_user_list_response.users
		self.last_list_timestamp: int = keycloak_user_list_response.last_list_timestamp

	# noinspection PyProtectedMember
	def _clone(self) -> "KeycloakUserListResponse":
		return KeycloakUserListResponse(users=[e._clone() for e in self.users], last_list_timestamp=self.last_list_timestamp)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUserListResponse) -> "KeycloakUserListResponse":
		return KeycloakUserListResponse(users=KeycloakUser._from_native_list(native_message.users), last_list_timestamp=native_message.last_list_timestamp)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUserListResponse]) -> list["KeycloakUserListResponse"]:
		return [KeycloakUserListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUserListResponse]) -> "KeycloakUserListResponse":
		try:
			native_message = await promise
			return KeycloakUserListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["KeycloakUserListResponse"]):
		if messages is None:
			return []
		return [KeycloakUserListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["KeycloakUserListResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUserListResponse(users=KeycloakUser._to_native_list(message.users if message.users else None), last_list_timestamp=message.last_list_timestamp if message.last_list_timestamp else None)

	def __str__(self):
		s: str = ''
		if self.users:
			s += f'users: {[str(el) for el in self.users]}, '
		if self.last_list_timestamp:
			s += f'last_list_timestamp: {self.last_list_timestamp}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, KeycloakUserListResponse):
			return False
		return self.users == other.users and self.last_list_timestamp == other.last_list_timestamp

	def __bool__(self):
		return bool(self.users) or self.last_list_timestamp != 0

	def __hash__(self):
		return hash((tuple(self.users), self.last_list_timestamp))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, KeycloakUserListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field users")
		assert expected.last_list_timestamp == 0 or self.last_list_timestamp == expected.last_list_timestamp, "Invalid value: last_list_timestamp: " + str(expected.last_list_timestamp) + " != " + str(self.last_list_timestamp)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class KeycloakAddUserAsContactRequest:
	def __init__(self, keycloak_id: str = ""):
		self.keycloak_id: str = keycloak_id

	def _update_content(self, keycloak_add_user_as_contact_request: KeycloakAddUserAsContactRequest) -> None:
		self.keycloak_id: str = keycloak_add_user_as_contact_request.keycloak_id

	# noinspection PyProtectedMember
	def _clone(self) -> "KeycloakAddUserAsContactRequest":
		return KeycloakAddUserAsContactRequest(keycloak_id=self.keycloak_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakAddUserAsContactRequest) -> "KeycloakAddUserAsContactRequest":
		return KeycloakAddUserAsContactRequest(keycloak_id=native_message.keycloak_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakAddUserAsContactRequest]) -> list["KeycloakAddUserAsContactRequest"]:
		return [KeycloakAddUserAsContactRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakAddUserAsContactRequest]) -> "KeycloakAddUserAsContactRequest":
		try:
			native_message = await promise
			return KeycloakAddUserAsContactRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["KeycloakAddUserAsContactRequest"]):
		if messages is None:
			return []
		return [KeycloakAddUserAsContactRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["KeycloakAddUserAsContactRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakAddUserAsContactRequest(keycloak_id=message.keycloak_id if message.keycloak_id else None)

	def __str__(self):
		s: str = ''
		if self.keycloak_id:
			s += f'keycloak_id: {self.keycloak_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, KeycloakAddUserAsContactRequest):
			return False
		return self.keycloak_id == other.keycloak_id

	def __bool__(self):
		return self.keycloak_id != ""

	def __hash__(self):
		return hash(self.keycloak_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, KeycloakAddUserAsContactRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.keycloak_id == "" or self.keycloak_id == expected.keycloak_id, "Invalid value: keycloak_id: " + str(expected.keycloak_id) + " != " + str(self.keycloak_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class KeycloakAddUserAsContactResponse:
	def __init__(self):
		pass

	def _update_content(self, keycloak_add_user_as_contact_response: KeycloakAddUserAsContactResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "KeycloakAddUserAsContactResponse":
		return KeycloakAddUserAsContactResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakAddUserAsContactResponse) -> "KeycloakAddUserAsContactResponse":
		return KeycloakAddUserAsContactResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakAddUserAsContactResponse]) -> list["KeycloakAddUserAsContactResponse"]:
		return [KeycloakAddUserAsContactResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakAddUserAsContactResponse]) -> "KeycloakAddUserAsContactResponse":
		try:
			native_message = await promise
			return KeycloakAddUserAsContactResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["KeycloakAddUserAsContactResponse"]):
		if messages is None:
			return []
		return [KeycloakAddUserAsContactResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["KeycloakAddUserAsContactResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakAddUserAsContactResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, KeycloakAddUserAsContactResponse):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, KeycloakAddUserAsContactResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class KeycloakGetApiCredentialsRequest:
	def __init__(self):
		pass

	def _update_content(self, keycloak_get_api_credentials_request: KeycloakGetApiCredentialsRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "KeycloakGetApiCredentialsRequest":
		return KeycloakGetApiCredentialsRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakGetApiCredentialsRequest) -> "KeycloakGetApiCredentialsRequest":
		return KeycloakGetApiCredentialsRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakGetApiCredentialsRequest]) -> list["KeycloakGetApiCredentialsRequest"]:
		return [KeycloakGetApiCredentialsRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakGetApiCredentialsRequest]) -> "KeycloakGetApiCredentialsRequest":
		try:
			native_message = await promise
			return KeycloakGetApiCredentialsRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["KeycloakGetApiCredentialsRequest"]):
		if messages is None:
			return []
		return [KeycloakGetApiCredentialsRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["KeycloakGetApiCredentialsRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakGetApiCredentialsRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, KeycloakGetApiCredentialsRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, KeycloakGetApiCredentialsRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class KeycloakGetApiCredentialsResponse:
	def __init__(self, credentials: "KeycloakApiCredentials" = None):
		self.credentials: KeycloakApiCredentials = credentials

	def _update_content(self, keycloak_get_api_credentials_response: KeycloakGetApiCredentialsResponse) -> None:
		self.credentials: KeycloakApiCredentials = keycloak_get_api_credentials_response.credentials

	# noinspection PyProtectedMember
	def _clone(self) -> "KeycloakGetApiCredentialsResponse":
		return KeycloakGetApiCredentialsResponse(credentials=self.credentials._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakGetApiCredentialsResponse) -> "KeycloakGetApiCredentialsResponse":
		return KeycloakGetApiCredentialsResponse(credentials=KeycloakApiCredentials._from_native(native_message.credentials))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakGetApiCredentialsResponse]) -> list["KeycloakGetApiCredentialsResponse"]:
		return [KeycloakGetApiCredentialsResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakGetApiCredentialsResponse]) -> "KeycloakGetApiCredentialsResponse":
		try:
			native_message = await promise
			return KeycloakGetApiCredentialsResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["KeycloakGetApiCredentialsResponse"]):
		if messages is None:
			return []
		return [KeycloakGetApiCredentialsResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["KeycloakGetApiCredentialsResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakGetApiCredentialsResponse(credentials=KeycloakApiCredentials._to_native(message.credentials if message.credentials else None))

	def __str__(self):
		s: str = ''
		if self.credentials:
			s += f'credentials: ({self.credentials}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, KeycloakGetApiCredentialsResponse):
			return False
		return self.credentials == other.credentials

	def __bool__(self):
		return bool(self.credentials)

	def __hash__(self):
		return hash(self.credentials)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, KeycloakGetApiCredentialsResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.credentials is None or self.credentials._test_assertion(expected.credentials)
		except AssertionError as e:
			raise AssertionError("credentials: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageListRequest:
	def __init__(self, filter: "MessageFilter" = None, unread: bool = False):
		self.filter: MessageFilter = filter
		self.unread: bool = unread

	def _update_content(self, message_list_request: MessageListRequest) -> None:
		self.filter: MessageFilter = message_list_request.filter
		self.unread: bool = message_list_request.unread

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageListRequest":
		return MessageListRequest(filter=self.filter._clone(), unread=self.unread)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageListRequest) -> "MessageListRequest":
		return MessageListRequest(filter=MessageFilter._from_native(native_message.filter), unread=native_message.unread)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageListRequest]) -> list["MessageListRequest"]:
		return [MessageListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageListRequest]) -> "MessageListRequest":
		try:
			native_message = await promise
			return MessageListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, messages: "list[Message]" = None):
		self.messages: list[Message] = messages

	def _update_content(self, message_list_response: MessageListResponse) -> None:
		self.messages: list[Message] = message_list_response.messages

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageListResponse":
		return MessageListResponse(messages=[e._clone() for e in self.messages])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageListResponse) -> "MessageListResponse":
		return MessageListResponse(messages=Message._from_native_list(native_message.messages))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageListResponse]) -> list["MessageListResponse"]:
		return [MessageListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageListResponse]) -> "MessageListResponse":
		try:
			native_message = await promise
			return MessageListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, message_id: "MessageId" = None):
		self.message_id: MessageId = message_id

	def _update_content(self, message_get_request: MessageGetRequest) -> None:
		self.message_id: MessageId = message_get_request.message_id

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageGetRequest":
		return MessageGetRequest(message_id=self.message_id._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageGetRequest) -> "MessageGetRequest":
		return MessageGetRequest(message_id=MessageId._from_native(native_message.message_id))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageGetRequest]) -> list["MessageGetRequest"]:
		return [MessageGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageGetRequest]) -> "MessageGetRequest":
		try:
			native_message = await promise
			return MessageGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, message: "Message" = None):
		self.message: Message = message

	def _update_content(self, message_get_response: MessageGetResponse) -> None:
		self.message: Message = message_get_response.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageGetResponse":
		return MessageGetResponse(message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageGetResponse) -> "MessageGetResponse":
		return MessageGetResponse(message=Message._from_native(native_message.message))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageGetResponse]) -> list["MessageGetResponse"]:
		return [MessageGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageGetResponse]) -> "MessageGetResponse":
		try:
			native_message = await promise
			return MessageGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, message_refresh_request: MessageRefreshRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageRefreshRequest":
		return MessageRefreshRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageRefreshRequest) -> "MessageRefreshRequest":
		return MessageRefreshRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageRefreshRequest]) -> list["MessageRefreshRequest"]:
		return [MessageRefreshRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageRefreshRequest]) -> "MessageRefreshRequest":
		try:
			native_message = await promise
			return MessageRefreshRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self):
		pass

	def _update_content(self, message_refresh_response: MessageRefreshResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageRefreshResponse":
		return MessageRefreshResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageRefreshResponse) -> "MessageRefreshResponse":
		return MessageRefreshResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageRefreshResponse]) -> list["MessageRefreshResponse"]:
		return [MessageRefreshResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageRefreshResponse]) -> "MessageRefreshResponse":
		try:
			native_message = await promise
			return MessageRefreshResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, message_id: "MessageId" = None, delete_everywhere: bool = False):
		self.message_id: MessageId = message_id
		self.delete_everywhere: bool = delete_everywhere

	def _update_content(self, message_delete_request: MessageDeleteRequest) -> None:
		self.message_id: MessageId = message_delete_request.message_id
		self.delete_everywhere: bool = message_delete_request.delete_everywhere

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageDeleteRequest":
		return MessageDeleteRequest(message_id=self.message_id._clone(), delete_everywhere=self.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageDeleteRequest) -> "MessageDeleteRequest":
		return MessageDeleteRequest(message_id=MessageId._from_native(native_message.message_id), delete_everywhere=native_message.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageDeleteRequest]) -> list["MessageDeleteRequest"]:
		return [MessageDeleteRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageDeleteRequest]) -> "MessageDeleteRequest":
		try:
			native_message = await promise
			return MessageDeleteRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, message_delete_response: MessageDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageDeleteResponse":
		return MessageDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageDeleteResponse) -> "MessageDeleteResponse":
		return MessageDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageDeleteResponse]) -> list["MessageDeleteResponse"]:
		return [MessageDeleteResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageDeleteResponse]) -> "MessageDeleteResponse":
		try:
			native_message = await promise
			return MessageDeleteResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, discussion_id: int = 0, body: str = "", reply_id: "MessageId" = None, ephemerality: "MessageEphemerality" = None, disable_link_preview: bool = False):
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
		return MessageSendRequest(discussion_id=self.discussion_id, body=self.body, reply_id=self.reply_id._clone(), ephemerality=self.ephemerality._clone(), disable_link_preview=self.disable_link_preview)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendRequest) -> "MessageSendRequest":
		return MessageSendRequest(discussion_id=native_message.discussion_id, body=native_message.body, reply_id=MessageId._from_native(native_message.reply_id), ephemerality=MessageEphemerality._from_native(native_message.ephemerality), disable_link_preview=native_message.disable_link_preview)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendRequest]) -> list["MessageSendRequest"]:
		return [MessageSendRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendRequest]) -> "MessageSendRequest":
		try:
			native_message = await promise
			return MessageSendRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, message: "Message" = None):
		self.message: Message = message

	def _update_content(self, message_send_response: MessageSendResponse) -> None:
		self.message: Message = message_send_response.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendResponse":
		return MessageSendResponse(message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendResponse) -> "MessageSendResponse":
		return MessageSendResponse(message=Message._from_native(native_message.message))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendResponse]) -> list["MessageSendResponse"]:
		return [MessageSendResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendResponse]) -> "MessageSendResponse":
		try:
			native_message = await promise
			return MessageSendResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, metadata: "MessageSendWithAttachmentsRequestMetadata" = None, payload: bytes = None, file_delimiter: bool = None):
		self.metadata: MessageSendWithAttachmentsRequestMetadata = metadata
		self.payload: bytes = payload
		self.file_delimiter: bool = file_delimiter

	def _update_content(self, message_send_with_attachments_request: MessageSendWithAttachmentsRequest) -> None:
		self.metadata: MessageSendWithAttachmentsRequestMetadata = message_send_with_attachments_request.metadata
		self.payload: bytes = message_send_with_attachments_request.payload
		self.file_delimiter: bool = message_send_with_attachments_request.file_delimiter

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendWithAttachmentsRequest":
		return MessageSendWithAttachmentsRequest(metadata=self.metadata._clone(), payload=self.payload, file_delimiter=self.file_delimiter)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequest) -> "MessageSendWithAttachmentsRequest":
		return MessageSendWithAttachmentsRequest(metadata=MessageSendWithAttachmentsRequestMetadata._from_native(native_message.metadata), payload=native_message.payload, file_delimiter=native_message.file_delimiter)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequest]) -> list["MessageSendWithAttachmentsRequest"]:
		return [MessageSendWithAttachmentsRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequest]) -> "MessageSendWithAttachmentsRequest":
		try:
			native_message = await promise
			return MessageSendWithAttachmentsRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		def __init__(self, filename: str = "", file_size: int = 0):
			self.filename: str = filename
			self.file_size: int = file_size
	
		def _update_content(self, file: MessageSendWithAttachmentsRequestMetadata.File) -> None:
			self.filename: str = file.filename
			self.file_size: int = file.file_size
	
		# noinspection PyProtectedMember
		def _clone(self) -> "MessageSendWithAttachmentsRequestMetadata.File":
			return MessageSendWithAttachmentsRequestMetadata.File(filename=self.filename, file_size=self.file_size)
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
		@staticmethod
		def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata.File) -> "MessageSendWithAttachmentsRequestMetadata.File":
			return MessageSendWithAttachmentsRequestMetadata.File(filename=native_message.filename, file_size=native_message.file_size)
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
		@staticmethod
		def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata.File]) -> list["MessageSendWithAttachmentsRequestMetadata.File"]:
			return [MessageSendWithAttachmentsRequestMetadata.File._from_native(native_message) for native_message in native_message_list]
	
		# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
		@staticmethod
		async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata.File]) -> "MessageSendWithAttachmentsRequestMetadata.File":
			try:
				native_message = await promise
				return MessageSendWithAttachmentsRequestMetadata.File._from_native(native_message)
			except errors.AioRpcError as error:
				raise errors.OlvidError._from_aio_rpc_error(error) from error
	
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

	def __init__(self, discussion_id: int = 0, body: str = "", reply_id: "MessageId" = None, ephemerality: "MessageEphemerality" = None, disable_link_preview: bool = False, files: "list[MessageSendWithAttachmentsRequestMetadata.File]" = None):
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
		return MessageSendWithAttachmentsRequestMetadata(discussion_id=self.discussion_id, body=self.body, reply_id=self.reply_id._clone(), ephemerality=self.ephemerality._clone(), disable_link_preview=self.disable_link_preview, files=[e._clone() for e in self.files])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata) -> "MessageSendWithAttachmentsRequestMetadata":
		return MessageSendWithAttachmentsRequestMetadata(discussion_id=native_message.discussion_id, body=native_message.body, reply_id=MessageId._from_native(native_message.reply_id), ephemerality=MessageEphemerality._from_native(native_message.ephemerality), disable_link_preview=native_message.disable_link_preview, files=MessageSendWithAttachmentsRequestMetadata.File._from_native_list(native_message.files))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata]) -> list["MessageSendWithAttachmentsRequestMetadata"]:
		return [MessageSendWithAttachmentsRequestMetadata._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsRequestMetadata]) -> "MessageSendWithAttachmentsRequestMetadata":
		try:
			native_message = await promise
			return MessageSendWithAttachmentsRequestMetadata._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, message: "Message" = None, attachments: "list[Attachment]" = None):
		self.message: Message = message
		self.attachments: list[Attachment] = attachments

	def _update_content(self, message_send_with_attachments_response: MessageSendWithAttachmentsResponse) -> None:
		self.message: Message = message_send_with_attachments_response.message
		self.attachments: list[Attachment] = message_send_with_attachments_response.attachments

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendWithAttachmentsResponse":
		return MessageSendWithAttachmentsResponse(message=self.message._clone(), attachments=[e._clone() for e in self.attachments])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsResponse) -> "MessageSendWithAttachmentsResponse":
		return MessageSendWithAttachmentsResponse(message=Message._from_native(native_message.message), attachments=Attachment._from_native_list(native_message.attachments))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsResponse]) -> list["MessageSendWithAttachmentsResponse"]:
		return [MessageSendWithAttachmentsResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendWithAttachmentsResponse]) -> "MessageSendWithAttachmentsResponse":
		try:
			native_message = await promise
			return MessageSendWithAttachmentsResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
class MessageSendLocationRequest:
	def __init__(self, discussion_id: int = 0, latitude: float = 0.0, longitude: float = 0.0, altitude: float = 0.0, precision: float = 0.0, address: str = "", preview_filename: str = "", preview_payload: bytes = b"", ephemerality: "MessageEphemerality" = None):
		self.discussion_id: int = discussion_id
		self.latitude: float = latitude
		self.longitude: float = longitude
		self.altitude: float = altitude
		self.precision: float = precision
		self.address: str = address
		self.preview_filename: str = preview_filename
		self.preview_payload: bytes = preview_payload
		self.ephemerality: MessageEphemerality = ephemerality

	def _update_content(self, message_send_location_request: MessageSendLocationRequest) -> None:
		self.discussion_id: int = message_send_location_request.discussion_id
		self.latitude: float = message_send_location_request.latitude
		self.longitude: float = message_send_location_request.longitude
		self.altitude: float = message_send_location_request.altitude
		self.precision: float = message_send_location_request.precision
		self.address: str = message_send_location_request.address
		self.preview_filename: str = message_send_location_request.preview_filename
		self.preview_payload: bytes = message_send_location_request.preview_payload
		self.ephemerality: MessageEphemerality = message_send_location_request.ephemerality

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendLocationRequest":
		return MessageSendLocationRequest(discussion_id=self.discussion_id, latitude=self.latitude, longitude=self.longitude, altitude=self.altitude, precision=self.precision, address=self.address, preview_filename=self.preview_filename, preview_payload=self.preview_payload, ephemerality=self.ephemerality._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendLocationRequest) -> "MessageSendLocationRequest":
		return MessageSendLocationRequest(discussion_id=native_message.discussion_id, latitude=native_message.latitude, longitude=native_message.longitude, altitude=native_message.altitude, precision=native_message.precision, address=native_message.address, preview_filename=native_message.preview_filename, preview_payload=native_message.preview_payload, ephemerality=MessageEphemerality._from_native(native_message.ephemerality))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendLocationRequest]) -> list["MessageSendLocationRequest"]:
		return [MessageSendLocationRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendLocationRequest]) -> "MessageSendLocationRequest":
		try:
			native_message = await promise
			return MessageSendLocationRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageSendLocationRequest"]):
		if messages is None:
			return []
		return [MessageSendLocationRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageSendLocationRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageSendLocationRequest(discussion_id=message.discussion_id if message.discussion_id else None, latitude=message.latitude if message.latitude else None, longitude=message.longitude if message.longitude else None, altitude=message.altitude if message.altitude else None, precision=message.precision if message.precision else None, address=message.address if message.address else None, preview_filename=message.preview_filename if message.preview_filename else None, preview_payload=message.preview_payload if message.preview_payload else None, ephemerality=MessageEphemerality._to_native(message.ephemerality if message.ephemerality else None))

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
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
		if self.preview_filename:
			s += f'preview_filename: {self.preview_filename}, '
		if self.preview_payload:
			s += f'preview_payload: {self.preview_payload}, '
		if self.ephemerality:
			s += f'ephemerality: ({self.ephemerality}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageSendLocationRequest):
			return False
		return self.discussion_id == other.discussion_id and self.latitude == other.latitude and self.longitude == other.longitude and self.altitude == other.altitude and self.precision == other.precision and self.address == other.address and self.preview_filename == other.preview_filename and self.preview_payload == other.preview_payload and self.ephemerality == other.ephemerality

	def __bool__(self):
		return self.discussion_id != 0 or self.latitude != 0.0 or self.longitude != 0.0 or self.altitude != 0.0 or self.precision != 0.0 or self.address != "" or self.preview_filename != "" or self.preview_payload != b"" or bool(self.ephemerality)

	def __hash__(self):
		return hash((self.discussion_id, self.latitude, self.longitude, self.altitude, self.precision, self.address, self.preview_filename, self.preview_payload, self.ephemerality))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageSendLocationRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.latitude == 0.0 or self.latitude == expected.latitude, "Invalid value: latitude: " + str(expected.latitude) + " != " + str(self.latitude)
		assert expected.longitude == 0.0 or self.longitude == expected.longitude, "Invalid value: longitude: " + str(expected.longitude) + " != " + str(self.longitude)
		assert expected.altitude == 0.0 or self.altitude == expected.altitude, "Invalid value: altitude: " + str(expected.altitude) + " != " + str(self.altitude)
		assert expected.precision == 0.0 or self.precision == expected.precision, "Invalid value: precision: " + str(expected.precision) + " != " + str(self.precision)
		assert expected.address == "" or self.address == expected.address, "Invalid value: address: " + str(expected.address) + " != " + str(self.address)
		assert expected.preview_filename == "" or self.preview_filename == expected.preview_filename, "Invalid value: preview_filename: " + str(expected.preview_filename) + " != " + str(self.preview_filename)
		assert expected.preview_payload == b"" or self.preview_payload == expected.preview_payload, "Invalid value: preview_payload: " + str(expected.preview_payload) + " != " + str(self.preview_payload)
		try:
			assert expected.ephemerality is None or self.ephemerality._test_assertion(expected.ephemerality)
		except AssertionError as e:
			raise AssertionError("ephemerality: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageSendLocationResponse:
	def __init__(self, message: "Message" = None):
		self.message: Message = message

	def _update_content(self, message_send_location_response: MessageSendLocationResponse) -> None:
		self.message: Message = message_send_location_response.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageSendLocationResponse":
		return MessageSendLocationResponse(message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageSendLocationResponse) -> "MessageSendLocationResponse":
		return MessageSendLocationResponse(message=Message._from_native(native_message.message))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageSendLocationResponse]) -> list["MessageSendLocationResponse"]:
		return [MessageSendLocationResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageSendLocationResponse]) -> "MessageSendLocationResponse":
		try:
			native_message = await promise
			return MessageSendLocationResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageSendLocationResponse"]):
		if messages is None:
			return []
		return [MessageSendLocationResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageSendLocationResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageSendLocationResponse(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageSendLocationResponse):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageSendLocationResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageStartLocationSharingRequest:
	def __init__(self, discussion_id: int = 0, latitude: float = 0.0, longitude: float = 0.0, altitude: float = 0.0, precision: float = 0.0):
		self.discussion_id: int = discussion_id
		self.latitude: float = latitude
		self.longitude: float = longitude
		self.altitude: float = altitude
		self.precision: float = precision

	def _update_content(self, message_start_location_sharing_request: MessageStartLocationSharingRequest) -> None:
		self.discussion_id: int = message_start_location_sharing_request.discussion_id
		self.latitude: float = message_start_location_sharing_request.latitude
		self.longitude: float = message_start_location_sharing_request.longitude
		self.altitude: float = message_start_location_sharing_request.altitude
		self.precision: float = message_start_location_sharing_request.precision

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageStartLocationSharingRequest":
		return MessageStartLocationSharingRequest(discussion_id=self.discussion_id, latitude=self.latitude, longitude=self.longitude, altitude=self.altitude, precision=self.precision)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageStartLocationSharingRequest) -> "MessageStartLocationSharingRequest":
		return MessageStartLocationSharingRequest(discussion_id=native_message.discussion_id, latitude=native_message.latitude, longitude=native_message.longitude, altitude=native_message.altitude, precision=native_message.precision)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageStartLocationSharingRequest]) -> list["MessageStartLocationSharingRequest"]:
		return [MessageStartLocationSharingRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageStartLocationSharingRequest]) -> "MessageStartLocationSharingRequest":
		try:
			native_message = await promise
			return MessageStartLocationSharingRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageStartLocationSharingRequest"]):
		if messages is None:
			return []
		return [MessageStartLocationSharingRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageStartLocationSharingRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageStartLocationSharingRequest(discussion_id=message.discussion_id if message.discussion_id else None, latitude=message.latitude if message.latitude else None, longitude=message.longitude if message.longitude else None, altitude=message.altitude if message.altitude else None, precision=message.precision if message.precision else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		if self.latitude:
			s += f'latitude: {self.latitude}, '
		if self.longitude:
			s += f'longitude: {self.longitude}, '
		if self.altitude:
			s += f'altitude: {self.altitude}, '
		if self.precision:
			s += f'precision: {self.precision}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageStartLocationSharingRequest):
			return False
		return self.discussion_id == other.discussion_id and self.latitude == other.latitude and self.longitude == other.longitude and self.altitude == other.altitude and self.precision == other.precision

	def __bool__(self):
		return self.discussion_id != 0 or self.latitude != 0.0 or self.longitude != 0.0 or self.altitude != 0.0 or self.precision != 0.0

	def __hash__(self):
		return hash((self.discussion_id, self.latitude, self.longitude, self.altitude, self.precision))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageStartLocationSharingRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		assert expected.latitude == 0.0 or self.latitude == expected.latitude, "Invalid value: latitude: " + str(expected.latitude) + " != " + str(self.latitude)
		assert expected.longitude == 0.0 or self.longitude == expected.longitude, "Invalid value: longitude: " + str(expected.longitude) + " != " + str(self.longitude)
		assert expected.altitude == 0.0 or self.altitude == expected.altitude, "Invalid value: altitude: " + str(expected.altitude) + " != " + str(self.altitude)
		assert expected.precision == 0.0 or self.precision == expected.precision, "Invalid value: precision: " + str(expected.precision) + " != " + str(self.precision)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageStartLocationSharingResponse:
	def __init__(self, message: "Message" = None):
		self.message: Message = message

	def _update_content(self, message_start_location_sharing_response: MessageStartLocationSharingResponse) -> None:
		self.message: Message = message_start_location_sharing_response.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageStartLocationSharingResponse":
		return MessageStartLocationSharingResponse(message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageStartLocationSharingResponse) -> "MessageStartLocationSharingResponse":
		return MessageStartLocationSharingResponse(message=Message._from_native(native_message.message))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageStartLocationSharingResponse]) -> list["MessageStartLocationSharingResponse"]:
		return [MessageStartLocationSharingResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageStartLocationSharingResponse]) -> "MessageStartLocationSharingResponse":
		try:
			native_message = await promise
			return MessageStartLocationSharingResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageStartLocationSharingResponse"]):
		if messages is None:
			return []
		return [MessageStartLocationSharingResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageStartLocationSharingResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageStartLocationSharingResponse(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageStartLocationSharingResponse):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageStartLocationSharingResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageUpdateLocationSharingRequest:
	def __init__(self, message_id: "MessageId" = None, latitude: float = 0.0, longitude: float = 0.0, altitude: float = 0.0, precision: float = 0.0):
		self.message_id: MessageId = message_id
		self.latitude: float = latitude
		self.longitude: float = longitude
		self.altitude: float = altitude
		self.precision: float = precision

	def _update_content(self, message_update_location_sharing_request: MessageUpdateLocationSharingRequest) -> None:
		self.message_id: MessageId = message_update_location_sharing_request.message_id
		self.latitude: float = message_update_location_sharing_request.latitude
		self.longitude: float = message_update_location_sharing_request.longitude
		self.altitude: float = message_update_location_sharing_request.altitude
		self.precision: float = message_update_location_sharing_request.precision

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageUpdateLocationSharingRequest":
		return MessageUpdateLocationSharingRequest(message_id=self.message_id._clone(), latitude=self.latitude, longitude=self.longitude, altitude=self.altitude, precision=self.precision)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageUpdateLocationSharingRequest) -> "MessageUpdateLocationSharingRequest":
		return MessageUpdateLocationSharingRequest(message_id=MessageId._from_native(native_message.message_id), latitude=native_message.latitude, longitude=native_message.longitude, altitude=native_message.altitude, precision=native_message.precision)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageUpdateLocationSharingRequest]) -> list["MessageUpdateLocationSharingRequest"]:
		return [MessageUpdateLocationSharingRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageUpdateLocationSharingRequest]) -> "MessageUpdateLocationSharingRequest":
		try:
			native_message = await promise
			return MessageUpdateLocationSharingRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageUpdateLocationSharingRequest"]):
		if messages is None:
			return []
		return [MessageUpdateLocationSharingRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageUpdateLocationSharingRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageUpdateLocationSharingRequest(message_id=MessageId._to_native(message.message_id if message.message_id else None), latitude=message.latitude if message.latitude else None, longitude=message.longitude if message.longitude else None, altitude=message.altitude if message.altitude else None, precision=message.precision if message.precision else None)

	def __str__(self):
		s: str = ''
		if self.message_id:
			s += f'message_id: ({self.message_id}), '
		if self.latitude:
			s += f'latitude: {self.latitude}, '
		if self.longitude:
			s += f'longitude: {self.longitude}, '
		if self.altitude:
			s += f'altitude: {self.altitude}, '
		if self.precision:
			s += f'precision: {self.precision}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageUpdateLocationSharingRequest):
			return False
		return self.message_id == other.message_id and self.latitude == other.latitude and self.longitude == other.longitude and self.altitude == other.altitude and self.precision == other.precision

	def __bool__(self):
		return bool(self.message_id) or self.latitude != 0.0 or self.longitude != 0.0 or self.altitude != 0.0 or self.precision != 0.0

	def __hash__(self):
		return hash((self.message_id, self.latitude, self.longitude, self.altitude, self.precision))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageUpdateLocationSharingRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message_id is None or self.message_id._test_assertion(expected.message_id)
		except AssertionError as e:
			raise AssertionError("message_id: " + str(e))
		assert expected.latitude == 0.0 or self.latitude == expected.latitude, "Invalid value: latitude: " + str(expected.latitude) + " != " + str(self.latitude)
		assert expected.longitude == 0.0 or self.longitude == expected.longitude, "Invalid value: longitude: " + str(expected.longitude) + " != " + str(self.longitude)
		assert expected.altitude == 0.0 or self.altitude == expected.altitude, "Invalid value: altitude: " + str(expected.altitude) + " != " + str(self.altitude)
		assert expected.precision == 0.0 or self.precision == expected.precision, "Invalid value: precision: " + str(expected.precision) + " != " + str(self.precision)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageUpdateLocationSharingResponse:
	def __init__(self, message: "Message" = None):
		self.message: Message = message

	def _update_content(self, message_update_location_sharing_response: MessageUpdateLocationSharingResponse) -> None:
		self.message: Message = message_update_location_sharing_response.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageUpdateLocationSharingResponse":
		return MessageUpdateLocationSharingResponse(message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageUpdateLocationSharingResponse) -> "MessageUpdateLocationSharingResponse":
		return MessageUpdateLocationSharingResponse(message=Message._from_native(native_message.message))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageUpdateLocationSharingResponse]) -> list["MessageUpdateLocationSharingResponse"]:
		return [MessageUpdateLocationSharingResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageUpdateLocationSharingResponse]) -> "MessageUpdateLocationSharingResponse":
		try:
			native_message = await promise
			return MessageUpdateLocationSharingResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageUpdateLocationSharingResponse"]):
		if messages is None:
			return []
		return [MessageUpdateLocationSharingResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageUpdateLocationSharingResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageUpdateLocationSharingResponse(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageUpdateLocationSharingResponse):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageUpdateLocationSharingResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageEndLocationSharingRequest:
	def __init__(self, message_id: "MessageId" = None):
		self.message_id: MessageId = message_id

	def _update_content(self, message_end_location_sharing_request: MessageEndLocationSharingRequest) -> None:
		self.message_id: MessageId = message_end_location_sharing_request.message_id

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageEndLocationSharingRequest":
		return MessageEndLocationSharingRequest(message_id=self.message_id._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageEndLocationSharingRequest) -> "MessageEndLocationSharingRequest":
		return MessageEndLocationSharingRequest(message_id=MessageId._from_native(native_message.message_id))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageEndLocationSharingRequest]) -> list["MessageEndLocationSharingRequest"]:
		return [MessageEndLocationSharingRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageEndLocationSharingRequest]) -> "MessageEndLocationSharingRequest":
		try:
			native_message = await promise
			return MessageEndLocationSharingRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageEndLocationSharingRequest"]):
		if messages is None:
			return []
		return [MessageEndLocationSharingRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageEndLocationSharingRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageEndLocationSharingRequest(message_id=MessageId._to_native(message.message_id if message.message_id else None))

	def __str__(self):
		s: str = ''
		if self.message_id:
			s += f'message_id: ({self.message_id}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageEndLocationSharingRequest):
			return False
		return self.message_id == other.message_id

	def __bool__(self):
		return bool(self.message_id)

	def __hash__(self):
		return hash(self.message_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageEndLocationSharingRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message_id is None or self.message_id._test_assertion(expected.message_id)
		except AssertionError as e:
			raise AssertionError("message_id: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageEndLocationSharingResponse:
	def __init__(self, message: "Message" = None):
		self.message: Message = message

	def _update_content(self, message_end_location_sharing_response: MessageEndLocationSharingResponse) -> None:
		self.message: Message = message_end_location_sharing_response.message

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageEndLocationSharingResponse":
		return MessageEndLocationSharingResponse(message=self.message._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageEndLocationSharingResponse) -> "MessageEndLocationSharingResponse":
		return MessageEndLocationSharingResponse(message=Message._from_native(native_message.message))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageEndLocationSharingResponse]) -> list["MessageEndLocationSharingResponse"]:
		return [MessageEndLocationSharingResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageEndLocationSharingResponse]) -> "MessageEndLocationSharingResponse":
		try:
			native_message = await promise
			return MessageEndLocationSharingResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["MessageEndLocationSharingResponse"]):
		if messages is None:
			return []
		return [MessageEndLocationSharingResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["MessageEndLocationSharingResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.message_commands_pb2.MessageEndLocationSharingResponse(message=Message._to_native(message.message if message.message else None))

	def __str__(self):
		s: str = ''
		if self.message:
			s += f'message: ({self.message}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, MessageEndLocationSharingResponse):
			return False
		return self.message == other.message

	def __bool__(self):
		return bool(self.message)

	def __hash__(self):
		return hash(self.message)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, MessageEndLocationSharingResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.message is None or self.message._test_assertion(expected.message)
		except AssertionError as e:
			raise AssertionError("message: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class MessageReactRequest:
	def __init__(self, message_id: "MessageId" = None, reaction: str = ""):
		self.message_id: MessageId = message_id
		self.reaction: str = reaction

	def _update_content(self, message_react_request: MessageReactRequest) -> None:
		self.message_id: MessageId = message_react_request.message_id
		self.reaction: str = message_react_request.reaction

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageReactRequest":
		return MessageReactRequest(message_id=self.message_id._clone(), reaction=self.reaction)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageReactRequest) -> "MessageReactRequest":
		return MessageReactRequest(message_id=MessageId._from_native(native_message.message_id), reaction=native_message.reaction)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageReactRequest]) -> list["MessageReactRequest"]:
		return [MessageReactRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageReactRequest]) -> "MessageReactRequest":
		try:
			native_message = await promise
			return MessageReactRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, message_react_response: MessageReactResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageReactResponse":
		return MessageReactResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageReactResponse) -> "MessageReactResponse":
		return MessageReactResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageReactResponse]) -> list["MessageReactResponse"]:
		return [MessageReactResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageReactResponse]) -> "MessageReactResponse":
		try:
			native_message = await promise
			return MessageReactResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
	def __init__(self, message_id: "MessageId" = None, updated_body: str = ""):
		self.message_id: MessageId = message_id
		self.updated_body: str = updated_body

	def _update_content(self, message_update_body_request: MessageUpdateBodyRequest) -> None:
		self.message_id: MessageId = message_update_body_request.message_id
		self.updated_body: str = message_update_body_request.updated_body

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageUpdateBodyRequest":
		return MessageUpdateBodyRequest(message_id=self.message_id._clone(), updated_body=self.updated_body)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyRequest) -> "MessageUpdateBodyRequest":
		return MessageUpdateBodyRequest(message_id=MessageId._from_native(native_message.message_id), updated_body=native_message.updated_body)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyRequest]) -> list["MessageUpdateBodyRequest"]:
		return [MessageUpdateBodyRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyRequest]) -> "MessageUpdateBodyRequest":
		try:
			native_message = await promise
			return MessageUpdateBodyRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self):
		pass

	def _update_content(self, message_update_body_response: MessageUpdateBodyResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "MessageUpdateBodyResponse":
		return MessageUpdateBodyResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyResponse) -> "MessageUpdateBodyResponse":
		return MessageUpdateBodyResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyResponse]) -> list["MessageUpdateBodyResponse"]:
		return [MessageUpdateBodyResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyResponse]) -> "MessageUpdateBodyResponse":
		try:
			native_message = await promise
			return MessageUpdateBodyResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
		return True

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
class SettingsIdentityGetRequest:
	def __init__(self):
		pass

	def _update_content(self, settings_identity_get_request: SettingsIdentityGetRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "SettingsIdentityGetRequest":
		return SettingsIdentityGetRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentityGetRequest) -> "SettingsIdentityGetRequest":
		return SettingsIdentityGetRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentityGetRequest]) -> list["SettingsIdentityGetRequest"]:
		return [SettingsIdentityGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentityGetRequest]) -> "SettingsIdentityGetRequest":
		try:
			native_message = await promise
			return SettingsIdentityGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SettingsIdentityGetRequest"]):
		if messages is None:
			return []
		return [SettingsIdentityGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SettingsIdentityGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentityGetRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SettingsIdentityGetRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SettingsIdentityGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SettingsIdentityGetResponse:
	def __init__(self, identity_settings: "IdentitySettings" = None):
		self.identity_settings: IdentitySettings = identity_settings

	def _update_content(self, settings_identity_get_response: SettingsIdentityGetResponse) -> None:
		self.identity_settings: IdentitySettings = settings_identity_get_response.identity_settings

	# noinspection PyProtectedMember
	def _clone(self) -> "SettingsIdentityGetResponse":
		return SettingsIdentityGetResponse(identity_settings=self.identity_settings._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentityGetResponse) -> "SettingsIdentityGetResponse":
		return SettingsIdentityGetResponse(identity_settings=IdentitySettings._from_native(native_message.identity_settings))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentityGetResponse]) -> list["SettingsIdentityGetResponse"]:
		return [SettingsIdentityGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentityGetResponse]) -> "SettingsIdentityGetResponse":
		try:
			native_message = await promise
			return SettingsIdentityGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SettingsIdentityGetResponse"]):
		if messages is None:
			return []
		return [SettingsIdentityGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SettingsIdentityGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentityGetResponse(identity_settings=IdentitySettings._to_native(message.identity_settings if message.identity_settings else None))

	def __str__(self):
		s: str = ''
		if self.identity_settings:
			s += f'identity_settings: ({self.identity_settings}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SettingsIdentityGetResponse):
			return False
		return self.identity_settings == other.identity_settings

	def __bool__(self):
		return bool(self.identity_settings)

	def __hash__(self):
		return hash(self.identity_settings)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SettingsIdentityGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity_settings is None or self.identity_settings._test_assertion(expected.identity_settings)
		except AssertionError as e:
			raise AssertionError("identity_settings: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SettingsIdentitySetRequest:
	def __init__(self, identity_settings: "IdentitySettings" = None):
		self.identity_settings: IdentitySettings = identity_settings

	def _update_content(self, settings_identity_set_request: SettingsIdentitySetRequest) -> None:
		self.identity_settings: IdentitySettings = settings_identity_set_request.identity_settings

	# noinspection PyProtectedMember
	def _clone(self) -> "SettingsIdentitySetRequest":
		return SettingsIdentitySetRequest(identity_settings=self.identity_settings._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentitySetRequest) -> "SettingsIdentitySetRequest":
		return SettingsIdentitySetRequest(identity_settings=IdentitySettings._from_native(native_message.identity_settings))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentitySetRequest]) -> list["SettingsIdentitySetRequest"]:
		return [SettingsIdentitySetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentitySetRequest]) -> "SettingsIdentitySetRequest":
		try:
			native_message = await promise
			return SettingsIdentitySetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SettingsIdentitySetRequest"]):
		if messages is None:
			return []
		return [SettingsIdentitySetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SettingsIdentitySetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentitySetRequest(identity_settings=IdentitySettings._to_native(message.identity_settings if message.identity_settings else None))

	def __str__(self):
		s: str = ''
		if self.identity_settings:
			s += f'identity_settings: ({self.identity_settings}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SettingsIdentitySetRequest):
			return False
		return self.identity_settings == other.identity_settings

	def __bool__(self):
		return bool(self.identity_settings)

	def __hash__(self):
		return hash(self.identity_settings)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SettingsIdentitySetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity_settings is None or self.identity_settings._test_assertion(expected.identity_settings)
		except AssertionError as e:
			raise AssertionError("identity_settings: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SettingsIdentitySetResponse:
	def __init__(self, identity_settings: "IdentitySettings" = None):
		self.identity_settings: IdentitySettings = identity_settings

	def _update_content(self, settings_identity_set_response: SettingsIdentitySetResponse) -> None:
		self.identity_settings: IdentitySettings = settings_identity_set_response.identity_settings

	# noinspection PyProtectedMember
	def _clone(self) -> "SettingsIdentitySetResponse":
		return SettingsIdentitySetResponse(identity_settings=self.identity_settings._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentitySetResponse) -> "SettingsIdentitySetResponse":
		return SettingsIdentitySetResponse(identity_settings=IdentitySettings._from_native(native_message.identity_settings))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentitySetResponse]) -> list["SettingsIdentitySetResponse"]:
		return [SettingsIdentitySetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentitySetResponse]) -> "SettingsIdentitySetResponse":
		try:
			native_message = await promise
			return SettingsIdentitySetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SettingsIdentitySetResponse"]):
		if messages is None:
			return []
		return [SettingsIdentitySetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SettingsIdentitySetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentitySetResponse(identity_settings=IdentitySettings._to_native(message.identity_settings if message.identity_settings else None))

	def __str__(self):
		s: str = ''
		if self.identity_settings:
			s += f'identity_settings: ({self.identity_settings}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SettingsIdentitySetResponse):
			return False
		return self.identity_settings == other.identity_settings

	def __bool__(self):
		return bool(self.identity_settings)

	def __hash__(self):
		return hash(self.identity_settings)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SettingsIdentitySetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity_settings is None or self.identity_settings._test_assertion(expected.identity_settings)
		except AssertionError as e:
			raise AssertionError("identity_settings: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SettingsDiscussionGetRequest:
	def __init__(self, discussion_id: int = 0):
		self.discussion_id: int = discussion_id

	def _update_content(self, settings_discussion_get_request: SettingsDiscussionGetRequest) -> None:
		self.discussion_id: int = settings_discussion_get_request.discussion_id

	# noinspection PyProtectedMember
	def _clone(self) -> "SettingsDiscussionGetRequest":
		return SettingsDiscussionGetRequest(discussion_id=self.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionGetRequest) -> "SettingsDiscussionGetRequest":
		return SettingsDiscussionGetRequest(discussion_id=native_message.discussion_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionGetRequest]) -> list["SettingsDiscussionGetRequest"]:
		return [SettingsDiscussionGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionGetRequest]) -> "SettingsDiscussionGetRequest":
		try:
			native_message = await promise
			return SettingsDiscussionGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SettingsDiscussionGetRequest"]):
		if messages is None:
			return []
		return [SettingsDiscussionGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SettingsDiscussionGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionGetRequest(discussion_id=message.discussion_id if message.discussion_id else None)

	def __str__(self):
		s: str = ''
		if self.discussion_id:
			s += f'discussion_id: {self.discussion_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SettingsDiscussionGetRequest):
			return False
		return self.discussion_id == other.discussion_id

	def __bool__(self):
		return self.discussion_id != 0

	def __hash__(self):
		return hash(self.discussion_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SettingsDiscussionGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.discussion_id == 0 or self.discussion_id == expected.discussion_id, "Invalid value: discussion_id: " + str(expected.discussion_id) + " != " + str(self.discussion_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SettingsDiscussionGetResponse:
	def __init__(self, discussion_settings: "DiscussionSettings" = None):
		self.discussion_settings: DiscussionSettings = discussion_settings

	def _update_content(self, settings_discussion_get_response: SettingsDiscussionGetResponse) -> None:
		self.discussion_settings: DiscussionSettings = settings_discussion_get_response.discussion_settings

	# noinspection PyProtectedMember
	def _clone(self) -> "SettingsDiscussionGetResponse":
		return SettingsDiscussionGetResponse(discussion_settings=self.discussion_settings._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionGetResponse) -> "SettingsDiscussionGetResponse":
		return SettingsDiscussionGetResponse(discussion_settings=DiscussionSettings._from_native(native_message.discussion_settings))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionGetResponse]) -> list["SettingsDiscussionGetResponse"]:
		return [SettingsDiscussionGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionGetResponse]) -> "SettingsDiscussionGetResponse":
		try:
			native_message = await promise
			return SettingsDiscussionGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SettingsDiscussionGetResponse"]):
		if messages is None:
			return []
		return [SettingsDiscussionGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SettingsDiscussionGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionGetResponse(discussion_settings=DiscussionSettings._to_native(message.discussion_settings if message.discussion_settings else None))

	def __str__(self):
		s: str = ''
		if self.discussion_settings:
			s += f'discussion_settings: ({self.discussion_settings}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SettingsDiscussionGetResponse):
			return False
		return self.discussion_settings == other.discussion_settings

	def __bool__(self):
		return bool(self.discussion_settings)

	def __hash__(self):
		return hash(self.discussion_settings)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SettingsDiscussionGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.discussion_settings is None or self.discussion_settings._test_assertion(expected.discussion_settings)
		except AssertionError as e:
			raise AssertionError("discussion_settings: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SettingsDiscussionSetRequest:
	def __init__(self, discussion_settings: "DiscussionSettings" = None):
		self.discussion_settings: DiscussionSettings = discussion_settings

	def _update_content(self, settings_discussion_set_request: SettingsDiscussionSetRequest) -> None:
		self.discussion_settings: DiscussionSettings = settings_discussion_set_request.discussion_settings

	# noinspection PyProtectedMember
	def _clone(self) -> "SettingsDiscussionSetRequest":
		return SettingsDiscussionSetRequest(discussion_settings=self.discussion_settings._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionSetRequest) -> "SettingsDiscussionSetRequest":
		return SettingsDiscussionSetRequest(discussion_settings=DiscussionSettings._from_native(native_message.discussion_settings))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionSetRequest]) -> list["SettingsDiscussionSetRequest"]:
		return [SettingsDiscussionSetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionSetRequest]) -> "SettingsDiscussionSetRequest":
		try:
			native_message = await promise
			return SettingsDiscussionSetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SettingsDiscussionSetRequest"]):
		if messages is None:
			return []
		return [SettingsDiscussionSetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SettingsDiscussionSetRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionSetRequest(discussion_settings=DiscussionSettings._to_native(message.discussion_settings if message.discussion_settings else None))

	def __str__(self):
		s: str = ''
		if self.discussion_settings:
			s += f'discussion_settings: ({self.discussion_settings}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SettingsDiscussionSetRequest):
			return False
		return self.discussion_settings == other.discussion_settings

	def __bool__(self):
		return bool(self.discussion_settings)

	def __hash__(self):
		return hash(self.discussion_settings)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SettingsDiscussionSetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.discussion_settings is None or self.discussion_settings._test_assertion(expected.discussion_settings)
		except AssertionError as e:
			raise AssertionError("discussion_settings: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class SettingsDiscussionSetResponse:
	def __init__(self, discussion_settings: "DiscussionSettings" = None):
		self.discussion_settings: DiscussionSettings = discussion_settings

	def _update_content(self, settings_discussion_set_response: SettingsDiscussionSetResponse) -> None:
		self.discussion_settings: DiscussionSettings = settings_discussion_set_response.discussion_settings

	# noinspection PyProtectedMember
	def _clone(self) -> "SettingsDiscussionSetResponse":
		return SettingsDiscussionSetResponse(discussion_settings=self.discussion_settings._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionSetResponse) -> "SettingsDiscussionSetResponse":
		return SettingsDiscussionSetResponse(discussion_settings=DiscussionSettings._from_native(native_message.discussion_settings))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionSetResponse]) -> list["SettingsDiscussionSetResponse"]:
		return [SettingsDiscussionSetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionSetResponse]) -> "SettingsDiscussionSetResponse":
		try:
			native_message = await promise
			return SettingsDiscussionSetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["SettingsDiscussionSetResponse"]):
		if messages is None:
			return []
		return [SettingsDiscussionSetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["SettingsDiscussionSetResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionSetResponse(discussion_settings=DiscussionSettings._to_native(message.discussion_settings if message.discussion_settings else None))

	def __str__(self):
		s: str = ''
		if self.discussion_settings:
			s += f'discussion_settings: ({self.discussion_settings}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, SettingsDiscussionSetResponse):
			return False
		return self.discussion_settings == other.discussion_settings

	def __bool__(self):
		return bool(self.discussion_settings)

	def __hash__(self):
		return hash(self.discussion_settings)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, SettingsDiscussionSetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.discussion_settings is None or self.discussion_settings._test_assertion(expected.discussion_settings)
		except AssertionError as e:
			raise AssertionError("discussion_settings: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class StorageListRequest:
	def __init__(self, filter: "StorageElementFilter" = None):
		self.filter: StorageElementFilter = filter

	def _update_content(self, storage_list_request: StorageListRequest) -> None:
		self.filter: StorageElementFilter = storage_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageListRequest":
		return StorageListRequest(filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageListRequest) -> "StorageListRequest":
		return StorageListRequest(filter=StorageElementFilter._from_native(native_message.filter))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageListRequest]) -> list["StorageListRequest"]:
		return [StorageListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageListRequest]) -> "StorageListRequest":
		try:
			native_message = await promise
			return StorageListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, elements: "list[StorageElement]" = None):
		self.elements: list[StorageElement] = elements

	def _update_content(self, storage_list_response: StorageListResponse) -> None:
		self.elements: list[StorageElement] = storage_list_response.elements

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageListResponse":
		return StorageListResponse(elements=[e._clone() for e in self.elements])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageListResponse) -> "StorageListResponse":
		return StorageListResponse(elements=StorageElement._from_native_list(native_message.elements))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageListResponse]) -> list["StorageListResponse"]:
		return [StorageListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageListResponse]) -> "StorageListResponse":
		try:
			native_message = await promise
			return StorageListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, key: str = ""):
		self.key: str = key

	def _update_content(self, storage_get_request: StorageGetRequest) -> None:
		self.key: str = storage_get_request.key

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageGetRequest":
		return StorageGetRequest(key=self.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageGetRequest) -> "StorageGetRequest":
		return StorageGetRequest(key=native_message.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageGetRequest]) -> list["StorageGetRequest"]:
		return [StorageGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageGetRequest]) -> "StorageGetRequest":
		try:
			native_message = await promise
			return StorageGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, value: str = ""):
		self.value: str = value

	def _update_content(self, storage_get_response: StorageGetResponse) -> None:
		self.value: str = storage_get_response.value

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageGetResponse":
		return StorageGetResponse(value=self.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageGetResponse) -> "StorageGetResponse":
		return StorageGetResponse(value=native_message.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageGetResponse]) -> list["StorageGetResponse"]:
		return [StorageGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageGetResponse]) -> "StorageGetResponse":
		try:
			native_message = await promise
			return StorageGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, key: str = "", value: str = ""):
		self.key: str = key
		self.value: str = value

	def _update_content(self, storage_set_request: StorageSetRequest) -> None:
		self.key: str = storage_set_request.key
		self.value: str = storage_set_request.value

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageSetRequest":
		return StorageSetRequest(key=self.key, value=self.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageSetRequest) -> "StorageSetRequest":
		return StorageSetRequest(key=native_message.key, value=native_message.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageSetRequest]) -> list["StorageSetRequest"]:
		return [StorageSetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageSetRequest]) -> "StorageSetRequest":
		try:
			native_message = await promise
			return StorageSetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, previous_value: str = ""):
		self.previous_value: str = previous_value

	def _update_content(self, storage_set_response: StorageSetResponse) -> None:
		self.previous_value: str = storage_set_response.previous_value

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageSetResponse":
		return StorageSetResponse(previous_value=self.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageSetResponse) -> "StorageSetResponse":
		return StorageSetResponse(previous_value=native_message.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageSetResponse]) -> list["StorageSetResponse"]:
		return [StorageSetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageSetResponse]) -> "StorageSetResponse":
		try:
			native_message = await promise
			return StorageSetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, key: str = ""):
		self.key: str = key

	def _update_content(self, storage_unset_request: StorageUnsetRequest) -> None:
		self.key: str = storage_unset_request.key

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageUnsetRequest":
		return StorageUnsetRequest(key=self.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetRequest) -> "StorageUnsetRequest":
		return StorageUnsetRequest(key=native_message.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetRequest]) -> list["StorageUnsetRequest"]:
		return [StorageUnsetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetRequest]) -> "StorageUnsetRequest":
		try:
			native_message = await promise
			return StorageUnsetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, previous_value: str = ""):
		self.previous_value: str = previous_value

	def _update_content(self, storage_unset_response: StorageUnsetResponse) -> None:
		self.previous_value: str = storage_unset_response.previous_value

	# noinspection PyProtectedMember
	def _clone(self) -> "StorageUnsetResponse":
		return StorageUnsetResponse(previous_value=self.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetResponse) -> "StorageUnsetResponse":
		return StorageUnsetResponse(previous_value=native_message.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetResponse]) -> list["StorageUnsetResponse"]:
		return [StorageUnsetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetResponse]) -> "StorageUnsetResponse":
		try:
			native_message = await promise
			return StorageUnsetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussion_id: int = 0, filter: "StorageElementFilter" = None):
		self.discussion_id: int = discussion_id
		self.filter: StorageElementFilter = filter

	def _update_content(self, discussion_storage_list_request: DiscussionStorageListRequest) -> None:
		self.discussion_id: int = discussion_storage_list_request.discussion_id
		self.filter: StorageElementFilter = discussion_storage_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageListRequest":
		return DiscussionStorageListRequest(discussion_id=self.discussion_id, filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListRequest) -> "DiscussionStorageListRequest":
		return DiscussionStorageListRequest(discussion_id=native_message.discussion_id, filter=StorageElementFilter._from_native(native_message.filter))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListRequest]) -> list["DiscussionStorageListRequest"]:
		return [DiscussionStorageListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListRequest]) -> "DiscussionStorageListRequest":
		try:
			native_message = await promise
			return DiscussionStorageListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, elements: "list[StorageElement]" = None):
		self.elements: list[StorageElement] = elements

	def _update_content(self, discussion_storage_list_response: DiscussionStorageListResponse) -> None:
		self.elements: list[StorageElement] = discussion_storage_list_response.elements

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageListResponse":
		return DiscussionStorageListResponse(elements=[e._clone() for e in self.elements])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListResponse) -> "DiscussionStorageListResponse":
		return DiscussionStorageListResponse(elements=StorageElement._from_native_list(native_message.elements))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListResponse]) -> list["DiscussionStorageListResponse"]:
		return [DiscussionStorageListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListResponse]) -> "DiscussionStorageListResponse":
		try:
			native_message = await promise
			return DiscussionStorageListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussion_id: int = 0, key: str = ""):
		self.discussion_id: int = discussion_id
		self.key: str = key

	def _update_content(self, discussion_storage_get_request: DiscussionStorageGetRequest) -> None:
		self.discussion_id: int = discussion_storage_get_request.discussion_id
		self.key: str = discussion_storage_get_request.key

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageGetRequest":
		return DiscussionStorageGetRequest(discussion_id=self.discussion_id, key=self.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetRequest) -> "DiscussionStorageGetRequest":
		return DiscussionStorageGetRequest(discussion_id=native_message.discussion_id, key=native_message.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetRequest]) -> list["DiscussionStorageGetRequest"]:
		return [DiscussionStorageGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetRequest]) -> "DiscussionStorageGetRequest":
		try:
			native_message = await promise
			return DiscussionStorageGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, value: str = ""):
		self.value: str = value

	def _update_content(self, discussion_storage_get_response: DiscussionStorageGetResponse) -> None:
		self.value: str = discussion_storage_get_response.value

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageGetResponse":
		return DiscussionStorageGetResponse(value=self.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetResponse) -> "DiscussionStorageGetResponse":
		return DiscussionStorageGetResponse(value=native_message.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetResponse]) -> list["DiscussionStorageGetResponse"]:
		return [DiscussionStorageGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetResponse]) -> "DiscussionStorageGetResponse":
		try:
			native_message = await promise
			return DiscussionStorageGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussion_id: int = 0, key: str = "", value: str = ""):
		self.discussion_id: int = discussion_id
		self.key: str = key
		self.value: str = value

	def _update_content(self, discussion_storage_set_request: DiscussionStorageSetRequest) -> None:
		self.discussion_id: int = discussion_storage_set_request.discussion_id
		self.key: str = discussion_storage_set_request.key
		self.value: str = discussion_storage_set_request.value

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageSetRequest":
		return DiscussionStorageSetRequest(discussion_id=self.discussion_id, key=self.key, value=self.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetRequest) -> "DiscussionStorageSetRequest":
		return DiscussionStorageSetRequest(discussion_id=native_message.discussion_id, key=native_message.key, value=native_message.value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetRequest]) -> list["DiscussionStorageSetRequest"]:
		return [DiscussionStorageSetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetRequest]) -> "DiscussionStorageSetRequest":
		try:
			native_message = await promise
			return DiscussionStorageSetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, previous_value: str = ""):
		self.previous_value: str = previous_value

	def _update_content(self, discussion_storage_set_response: DiscussionStorageSetResponse) -> None:
		self.previous_value: str = discussion_storage_set_response.previous_value

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageSetResponse":
		return DiscussionStorageSetResponse(previous_value=self.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetResponse) -> "DiscussionStorageSetResponse":
		return DiscussionStorageSetResponse(previous_value=native_message.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetResponse]) -> list["DiscussionStorageSetResponse"]:
		return [DiscussionStorageSetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetResponse]) -> "DiscussionStorageSetResponse":
		try:
			native_message = await promise
			return DiscussionStorageSetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, discussion_id: int = 0, key: str = ""):
		self.discussion_id: int = discussion_id
		self.key: str = key

	def _update_content(self, discussion_storage_unset_request: DiscussionStorageUnsetRequest) -> None:
		self.discussion_id: int = discussion_storage_unset_request.discussion_id
		self.key: str = discussion_storage_unset_request.key

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageUnsetRequest":
		return DiscussionStorageUnsetRequest(discussion_id=self.discussion_id, key=self.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetRequest) -> "DiscussionStorageUnsetRequest":
		return DiscussionStorageUnsetRequest(discussion_id=native_message.discussion_id, key=native_message.key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetRequest]) -> list["DiscussionStorageUnsetRequest"]:
		return [DiscussionStorageUnsetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetRequest]) -> "DiscussionStorageUnsetRequest":
		try:
			native_message = await promise
			return DiscussionStorageUnsetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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
	def __init__(self, previous_value: str = ""):
		self.previous_value: str = previous_value

	def _update_content(self, discussion_storage_unset_response: DiscussionStorageUnsetResponse) -> None:
		self.previous_value: str = discussion_storage_unset_response.previous_value

	# noinspection PyProtectedMember
	def _clone(self) -> "DiscussionStorageUnsetResponse":
		return DiscussionStorageUnsetResponse(previous_value=self.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetResponse) -> "DiscussionStorageUnsetResponse":
		return DiscussionStorageUnsetResponse(previous_value=native_message.previous_value)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetResponse]) -> list["DiscussionStorageUnsetResponse"]:
		return [DiscussionStorageUnsetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetResponse]) -> "DiscussionStorageUnsetResponse":
		try:
			native_message = await promise
			return DiscussionStorageUnsetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

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


# noinspection PyProtectedMember,PyShadowingBuiltins
class PingRequest:
	def __init__(self):
		pass

	def _update_content(self, ping_request: PingRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "PingRequest":
		return PingRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.tool_commands_pb2.PingRequest) -> "PingRequest":
		return PingRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.tool_commands_pb2.PingRequest]) -> list["PingRequest"]:
		return [PingRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.tool_commands_pb2.PingRequest]) -> "PingRequest":
		try:
			native_message = await promise
			return PingRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["PingRequest"]):
		if messages is None:
			return []
		return [PingRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["PingRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.tool_commands_pb2.PingRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, PingRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, PingRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class PingResponse:
	def __init__(self):
		pass

	def _update_content(self, ping_response: PingResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "PingResponse":
		return PingResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.tool_commands_pb2.PingResponse) -> "PingResponse":
		return PingResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.tool_commands_pb2.PingResponse]) -> list["PingResponse"]:
		return [PingResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.tool_commands_pb2.PingResponse]) -> "PingResponse":
		try:
			native_message = await promise
			return PingResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["PingResponse"]):
		if messages is None:
			return []
		return [PingResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["PingResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.tool_commands_pb2.PingResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, PingResponse):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, PingResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DaemonVersionRequest:
	def __init__(self):
		pass

	def _update_content(self, daemon_version_request: DaemonVersionRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "DaemonVersionRequest":
		return DaemonVersionRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.tool_commands_pb2.DaemonVersionRequest) -> "DaemonVersionRequest":
		return DaemonVersionRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.tool_commands_pb2.DaemonVersionRequest]) -> list["DaemonVersionRequest"]:
		return [DaemonVersionRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.tool_commands_pb2.DaemonVersionRequest]) -> "DaemonVersionRequest":
		try:
			native_message = await promise
			return DaemonVersionRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DaemonVersionRequest"]):
		if messages is None:
			return []
		return [DaemonVersionRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DaemonVersionRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.tool_commands_pb2.DaemonVersionRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DaemonVersionRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DaemonVersionRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class DaemonVersionResponse:
	def __init__(self, version: str = ""):
		self.version: str = version

	def _update_content(self, daemon_version_response: DaemonVersionResponse) -> None:
		self.version: str = daemon_version_response.version

	# noinspection PyProtectedMember
	def _clone(self) -> "DaemonVersionResponse":
		return DaemonVersionResponse(version=self.version)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.tool_commands_pb2.DaemonVersionResponse) -> "DaemonVersionResponse":
		return DaemonVersionResponse(version=native_message.version)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.tool_commands_pb2.DaemonVersionResponse]) -> list["DaemonVersionResponse"]:
		return [DaemonVersionResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.tool_commands_pb2.DaemonVersionResponse]) -> "DaemonVersionResponse":
		try:
			native_message = await promise
			return DaemonVersionResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["DaemonVersionResponse"]):
		if messages is None:
			return []
		return [DaemonVersionResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["DaemonVersionResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.tool_commands_pb2.DaemonVersionResponse(version=message.version if message.version else None)

	def __str__(self):
		s: str = ''
		if self.version:
			s += f'version: {self.version}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, DaemonVersionResponse):
			return False
		return self.version == other.version

	def __bool__(self):
		return self.version != ""

	def __hash__(self):
		return hash(self.version)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, DaemonVersionResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.version == "" or self.version == expected.version, "Invalid value: version: " + str(expected.version) + " != " + str(self.version)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AuthenticationTestRequest:
	def __init__(self):
		pass

	def _update_content(self, authentication_test_request: AuthenticationTestRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "AuthenticationTestRequest":
		return AuthenticationTestRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.tool_commands_pb2.AuthenticationTestRequest) -> "AuthenticationTestRequest":
		return AuthenticationTestRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.tool_commands_pb2.AuthenticationTestRequest]) -> list["AuthenticationTestRequest"]:
		return [AuthenticationTestRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.tool_commands_pb2.AuthenticationTestRequest]) -> "AuthenticationTestRequest":
		try:
			native_message = await promise
			return AuthenticationTestRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AuthenticationTestRequest"]):
		if messages is None:
			return []
		return [AuthenticationTestRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AuthenticationTestRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.tool_commands_pb2.AuthenticationTestRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AuthenticationTestRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AuthenticationTestRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AuthenticationTestResponse:
	def __init__(self):
		pass

	def _update_content(self, authentication_test_response: AuthenticationTestResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "AuthenticationTestResponse":
		return AuthenticationTestResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.tool_commands_pb2.AuthenticationTestResponse) -> "AuthenticationTestResponse":
		return AuthenticationTestResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.tool_commands_pb2.AuthenticationTestResponse]) -> list["AuthenticationTestResponse"]:
		return [AuthenticationTestResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.tool_commands_pb2.AuthenticationTestResponse]) -> "AuthenticationTestResponse":
		try:
			native_message = await promise
			return AuthenticationTestResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AuthenticationTestResponse"]):
		if messages is None:
			return []
		return [AuthenticationTestResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AuthenticationTestResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.tool_commands_pb2.AuthenticationTestResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AuthenticationTestResponse):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AuthenticationTestResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AuthenticationAdminTestRequest:
	def __init__(self):
		pass

	def _update_content(self, authentication_admin_test_request: AuthenticationAdminTestRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "AuthenticationAdminTestRequest":
		return AuthenticationAdminTestRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.tool_commands_pb2.AuthenticationAdminTestRequest) -> "AuthenticationAdminTestRequest":
		return AuthenticationAdminTestRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.tool_commands_pb2.AuthenticationAdminTestRequest]) -> list["AuthenticationAdminTestRequest"]:
		return [AuthenticationAdminTestRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.tool_commands_pb2.AuthenticationAdminTestRequest]) -> "AuthenticationAdminTestRequest":
		try:
			native_message = await promise
			return AuthenticationAdminTestRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AuthenticationAdminTestRequest"]):
		if messages is None:
			return []
		return [AuthenticationAdminTestRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AuthenticationAdminTestRequest"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.tool_commands_pb2.AuthenticationAdminTestRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AuthenticationAdminTestRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AuthenticationAdminTestRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class AuthenticationAdminTestResponse:
	def __init__(self):
		pass

	def _update_content(self, authentication_admin_test_response: AuthenticationAdminTestResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "AuthenticationAdminTestResponse":
		return AuthenticationAdminTestResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.command.v1.tool_commands_pb2.AuthenticationAdminTestResponse) -> "AuthenticationAdminTestResponse":
		return AuthenticationAdminTestResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.command.v1.tool_commands_pb2.AuthenticationAdminTestResponse]) -> list["AuthenticationAdminTestResponse"]:
		return [AuthenticationAdminTestResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.command.v1.tool_commands_pb2.AuthenticationAdminTestResponse]) -> "AuthenticationAdminTestResponse":
		try:
			native_message = await promise
			return AuthenticationAdminTestResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["AuthenticationAdminTestResponse"]):
		if messages is None:
			return []
		return [AuthenticationAdminTestResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["AuthenticationAdminTestResponse"]):
		if message is None:
			return None
		return olvid.daemon.command.v1.tool_commands_pb2.AuthenticationAdminTestResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, AuthenticationAdminTestResponse):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, AuthenticationAdminTestResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


class ToolCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.ToolCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.ToolCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def ping(self, ping_request: PingRequest) -> Coroutine[Any, Any, PingResponse]:
		try:
			overlay_object = ping_request
			return PingResponse._from_native_promise(self.__stub.Ping(olvid.daemon.command.v1.tool_commands_pb2.PingRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def daemon_version(self, daemon_version_request: DaemonVersionRequest) -> Coroutine[Any, Any, DaemonVersionResponse]:
		try:
			overlay_object = daemon_version_request
			return DaemonVersionResponse._from_native_promise(self.__stub.DaemonVersion(olvid.daemon.command.v1.tool_commands_pb2.DaemonVersionRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def authentication_test(self, authentication_test_request: AuthenticationTestRequest) -> Coroutine[Any, Any, AuthenticationTestResponse]:
		try:
			overlay_object = authentication_test_request
			return AuthenticationTestResponse._from_native_promise(self.__stub.AuthenticationTest(olvid.daemon.command.v1.tool_commands_pb2.AuthenticationTestRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def authentication_admin_test(self, authentication_admin_test_request: AuthenticationAdminTestRequest) -> Coroutine[Any, Any, AuthenticationAdminTestResponse]:
		try:
			overlay_object = authentication_admin_test_request
			return AuthenticationAdminTestResponse._from_native_promise(self.__stub.AuthenticationAdminTest(olvid.daemon.command.v1.tool_commands_pb2.AuthenticationAdminTestRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class IdentityCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.IdentityCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.IdentityCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_get(self, identity_get_request: IdentityGetRequest) -> Coroutine[Any, Any, IdentityGetResponse]:
		try:
			overlay_object = identity_get_request
			return IdentityGetResponse._from_native_promise(self.__stub.IdentityGet(olvid.daemon.command.v1.identity_commands_pb2.IdentityGetRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_get_bytes_identifier(self, identity_get_bytes_identifier_request: IdentityGetBytesIdentifierRequest) -> Coroutine[Any, Any, IdentityGetBytesIdentifierResponse]:
		try:
			overlay_object = identity_get_bytes_identifier_request
			return IdentityGetBytesIdentifierResponse._from_native_promise(self.__stub.IdentityGetBytesIdentifier(olvid.daemon.command.v1.identity_commands_pb2.IdentityGetBytesIdentifierRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_get_invitation_link(self, identity_get_invitation_link_request: IdentityGetInvitationLinkRequest) -> Coroutine[Any, Any, IdentityGetInvitationLinkResponse]:
		try:
			overlay_object = identity_get_invitation_link_request
			return IdentityGetInvitationLinkResponse._from_native_promise(self.__stub.IdentityGetInvitationLink(olvid.daemon.command.v1.identity_commands_pb2.IdentityGetInvitationLinkRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_update_details(self, identity_update_details_request: IdentityUpdateDetailsRequest) -> Coroutine[Any, Any, IdentityUpdateDetailsResponse]:
		try:
			overlay_object = identity_update_details_request
			return IdentityUpdateDetailsResponse._from_native_promise(self.__stub.IdentityUpdateDetails(olvid.daemon.command.v1.identity_commands_pb2.IdentityUpdateDetailsRequest(new_details=IdentityDetails._to_native(overlay_object.new_details)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_remove_photo(self, identity_remove_photo_request: IdentityRemovePhotoRequest) -> Coroutine[Any, Any, IdentityRemovePhotoResponse]:
		try:
			overlay_object = identity_remove_photo_request
			return IdentityRemovePhotoResponse._from_native_promise(self.__stub.IdentityRemovePhoto(olvid.daemon.command.v1.identity_commands_pb2.IdentityRemovePhotoRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_set_photo(self, identity_set_photo_request_iterator: AsyncIterator[IdentitySetPhotoRequest]) -> Coroutine[Any, Any, IdentitySetPhotoResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember
			async def request_iterator(iterator: AsyncIterator[IdentitySetPhotoRequest]):
				try:
					async for message in iterator.__aiter__():
						yield IdentitySetPhotoRequest._to_native(message)
				except errors.AioRpcError as err:
					raise errors.OlvidError._from_aio_rpc_error(err) from err
			return IdentitySetPhotoResponse._from_native_promise(self.__stub.IdentitySetPhoto(request_iterator(identity_set_photo_request_iterator), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_download_photo(self, identity_download_photo_request: IdentityDownloadPhotoRequest) -> Coroutine[Any, Any, IdentityDownloadPhotoResponse]:
		try:
			overlay_object = identity_download_photo_request
			return IdentityDownloadPhotoResponse._from_native_promise(self.__stub.IdentityDownloadPhoto(olvid.daemon.command.v1.identity_commands_pb2.IdentityDownloadPhotoRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_get_api_key_status(self, identity_get_api_key_status_request: IdentityGetApiKeyStatusRequest) -> Coroutine[Any, Any, IdentityGetApiKeyStatusResponse]:
		try:
			overlay_object = identity_get_api_key_status_request
			return IdentityGetApiKeyStatusResponse._from_native_promise(self.__stub.IdentityGetApiKeyStatus(olvid.daemon.command.v1.identity_commands_pb2.IdentityGetApiKeyStatusRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_set_api_key(self, identity_set_api_key_request: IdentitySetApiKeyRequest) -> Coroutine[Any, Any, IdentitySetApiKeyResponse]:
		try:
			overlay_object = identity_set_api_key_request
			return IdentitySetApiKeyResponse._from_native_promise(self.__stub.IdentitySetApiKey(olvid.daemon.command.v1.identity_commands_pb2.IdentitySetApiKeyRequest(api_key=overlay_object.api_key), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_set_configuration_link(self, identity_set_configuration_link_request: IdentitySetConfigurationLinkRequest) -> Coroutine[Any, Any, IdentitySetConfigurationLinkResponse]:
		try:
			overlay_object = identity_set_configuration_link_request
			return IdentitySetConfigurationLinkResponse._from_native_promise(self.__stub.IdentitySetConfigurationLink(olvid.daemon.command.v1.identity_commands_pb2.IdentitySetConfigurationLinkRequest(configuration_link=overlay_object.configuration_link), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class InvitationCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.InvitationCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.InvitationCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_list(self, invitation_list_request: InvitationListRequest) -> AsyncIterator[InvitationListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.invitation_commands_pb2.InvitationListResponse]) -> AsyncIterator[InvitationListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield InvitationListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = invitation_list_request
			return response_iterator(self.__stub.InvitationList(olvid.daemon.command.v1.invitation_commands_pb2.InvitationListRequest(filter=InvitationFilter._to_native(overlay_object.filter)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_get(self, invitation_get_request: InvitationGetRequest) -> Coroutine[Any, Any, InvitationGetResponse]:
		try:
			overlay_object = invitation_get_request
			return InvitationGetResponse._from_native_promise(self.__stub.InvitationGet(olvid.daemon.command.v1.invitation_commands_pb2.InvitationGetRequest(invitation_id=overlay_object.invitation_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_new(self, invitation_new_request: InvitationNewRequest) -> Coroutine[Any, Any, InvitationNewResponse]:
		try:
			overlay_object = invitation_new_request
			return InvitationNewResponse._from_native_promise(self.__stub.InvitationNew(olvid.daemon.command.v1.invitation_commands_pb2.InvitationNewRequest(invitation_url=overlay_object.invitation_url), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_accept(self, invitation_accept_request: InvitationAcceptRequest) -> Coroutine[Any, Any, InvitationAcceptResponse]:
		try:
			overlay_object = invitation_accept_request
			return InvitationAcceptResponse._from_native_promise(self.__stub.InvitationAccept(olvid.daemon.command.v1.invitation_commands_pb2.InvitationAcceptRequest(invitation_id=overlay_object.invitation_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_decline(self, invitation_decline_request: InvitationDeclineRequest) -> Coroutine[Any, Any, InvitationDeclineResponse]:
		try:
			overlay_object = invitation_decline_request
			return InvitationDeclineResponse._from_native_promise(self.__stub.InvitationDecline(olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeclineRequest(invitation_id=overlay_object.invitation_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_sas(self, invitation_sas_request: InvitationSasRequest) -> Coroutine[Any, Any, InvitationSasResponse]:
		try:
			overlay_object = invitation_sas_request
			return InvitationSasResponse._from_native_promise(self.__stub.InvitationSas(olvid.daemon.command.v1.invitation_commands_pb2.InvitationSasRequest(invitation_id=overlay_object.invitation_id, sas=overlay_object.sas), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def invitation_delete(self, invitation_delete_request: InvitationDeleteRequest) -> Coroutine[Any, Any, InvitationDeleteResponse]:
		try:
			overlay_object = invitation_delete_request
			return InvitationDeleteResponse._from_native_promise(self.__stub.InvitationDelete(olvid.daemon.command.v1.invitation_commands_pb2.InvitationDeleteRequest(invitation_id=overlay_object.invitation_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class ContactCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.ContactCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.ContactCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_list(self, contact_list_request: ContactListRequest) -> AsyncIterator[ContactListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.contact_commands_pb2.ContactListResponse]) -> AsyncIterator[ContactListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield ContactListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = contact_list_request
			return response_iterator(self.__stub.ContactList(olvid.daemon.command.v1.contact_commands_pb2.ContactListRequest(filter=ContactFilter._to_native(overlay_object.filter)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_get(self, contact_get_request: ContactGetRequest) -> Coroutine[Any, Any, ContactGetResponse]:
		try:
			overlay_object = contact_get_request
			return ContactGetResponse._from_native_promise(self.__stub.ContactGet(olvid.daemon.command.v1.contact_commands_pb2.ContactGetRequest(contact_id=overlay_object.contact_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_get_bytes_identifier(self, contact_get_bytes_identifier_request: ContactGetBytesIdentifierRequest) -> Coroutine[Any, Any, ContactGetBytesIdentifierResponse]:
		try:
			overlay_object = contact_get_bytes_identifier_request
			return ContactGetBytesIdentifierResponse._from_native_promise(self.__stub.ContactGetBytesIdentifier(olvid.daemon.command.v1.contact_commands_pb2.ContactGetBytesIdentifierRequest(contact_id=overlay_object.contact_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_get_invitation_link(self, contact_get_invitation_link_request: ContactGetInvitationLinkRequest) -> Coroutine[Any, Any, ContactGetInvitationLinkResponse]:
		try:
			overlay_object = contact_get_invitation_link_request
			return ContactGetInvitationLinkResponse._from_native_promise(self.__stub.ContactGetInvitationLink(olvid.daemon.command.v1.contact_commands_pb2.ContactGetInvitationLinkRequest(contact_id=overlay_object.contact_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_delete(self, contact_delete_request: ContactDeleteRequest) -> Coroutine[Any, Any, ContactDeleteResponse]:
		try:
			overlay_object = contact_delete_request
			return ContactDeleteResponse._from_native_promise(self.__stub.ContactDelete(olvid.daemon.command.v1.contact_commands_pb2.ContactDeleteRequest(contact_id=overlay_object.contact_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_introduction(self, contact_introduction_request: ContactIntroductionRequest) -> Coroutine[Any, Any, ContactIntroductionResponse]:
		try:
			overlay_object = contact_introduction_request
			return ContactIntroductionResponse._from_native_promise(self.__stub.ContactIntroduction(olvid.daemon.command.v1.contact_commands_pb2.ContactIntroductionRequest(first_contact_id=overlay_object.first_contact_id, second_contact_id=overlay_object.second_contact_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_download_photo(self, contact_download_photo_request: ContactDownloadPhotoRequest) -> Coroutine[Any, Any, ContactDownloadPhotoResponse]:
		try:
			overlay_object = contact_download_photo_request
			return ContactDownloadPhotoResponse._from_native_promise(self.__stub.ContactDownloadPhoto(olvid.daemon.command.v1.contact_commands_pb2.ContactDownloadPhotoRequest(contact_id=overlay_object.contact_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_recreate_channels(self, contact_recreate_channels_request: ContactRecreateChannelsRequest) -> Coroutine[Any, Any, ContactRecreateChannelsResponse]:
		try:
			overlay_object = contact_recreate_channels_request
			return ContactRecreateChannelsResponse._from_native_promise(self.__stub.ContactRecreateChannels(olvid.daemon.command.v1.contact_commands_pb2.ContactRecreateChannelsRequest(contact_id=overlay_object.contact_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_invite_to_one_to_one_discussion(self, contact_invite_to_one_to_one_discussion_request: ContactInviteToOneToOneDiscussionRequest) -> Coroutine[Any, Any, ContactInviteToOneToOneDiscussionResponse]:
		try:
			overlay_object = contact_invite_to_one_to_one_discussion_request
			return ContactInviteToOneToOneDiscussionResponse._from_native_promise(self.__stub.ContactInviteToOneToOneDiscussion(olvid.daemon.command.v1.contact_commands_pb2.ContactInviteToOneToOneDiscussionRequest(contact_id=overlay_object.contact_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def contact_downgrade_one_to_one_discussion(self, contact_downgrade_one_to_one_discussion_request: ContactDowngradeOneToOneDiscussionRequest) -> Coroutine[Any, Any, ContactDowngradeOneToOneDiscussionResponse]:
		try:
			overlay_object = contact_downgrade_one_to_one_discussion_request
			return ContactDowngradeOneToOneDiscussionResponse._from_native_promise(self.__stub.ContactDowngradeOneToOneDiscussion(olvid.daemon.command.v1.contact_commands_pb2.ContactDowngradeOneToOneDiscussionRequest(contact_id=overlay_object.contact_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class KeycloakCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.KeycloakCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.KeycloakCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def keycloak_bind_identity(self, keycloak_bind_identity_request: KeycloakBindIdentityRequest) -> Coroutine[Any, Any, KeycloakBindIdentityResponse]:
		try:
			overlay_object = keycloak_bind_identity_request
			return KeycloakBindIdentityResponse._from_native_promise(self.__stub.KeycloakBindIdentity(olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakBindIdentityRequest(configuration_link=overlay_object.configuration_link), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def keycloak_unbind_identity(self, keycloak_unbind_identity_request: KeycloakUnbindIdentityRequest) -> Coroutine[Any, Any, KeycloakUnbindIdentityResponse]:
		try:
			overlay_object = keycloak_unbind_identity_request
			return KeycloakUnbindIdentityResponse._from_native_promise(self.__stub.KeycloakUnbindIdentity(olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUnbindIdentityRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def keycloak_user_list(self, keycloak_user_list_request: KeycloakUserListRequest) -> AsyncIterator[KeycloakUserListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUserListResponse]) -> AsyncIterator[KeycloakUserListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield KeycloakUserListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = keycloak_user_list_request
			return response_iterator(self.__stub.KeycloakUserList(olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakUserListRequest(filter=KeycloakUserFilter._to_native(overlay_object.filter), last_list_timestamp=overlay_object.last_list_timestamp), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def keycloak_add_user_as_contact(self, keycloak_add_user_as_contact_request: KeycloakAddUserAsContactRequest) -> Coroutine[Any, Any, KeycloakAddUserAsContactResponse]:
		try:
			overlay_object = keycloak_add_user_as_contact_request
			return KeycloakAddUserAsContactResponse._from_native_promise(self.__stub.KeycloakAddUserAsContact(olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakAddUserAsContactRequest(keycloak_id=overlay_object.keycloak_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def keycloak_get_api_credentials(self, keycloak_get_api_credentials_request: KeycloakGetApiCredentialsRequest) -> Coroutine[Any, Any, KeycloakGetApiCredentialsResponse]:
		try:
			overlay_object = keycloak_get_api_credentials_request
			return KeycloakGetApiCredentialsResponse._from_native_promise(self.__stub.KeycloakGetApiCredentials(olvid.daemon.command.v1.keycloak_commands_pb2.KeycloakGetApiCredentialsRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class GroupCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.GroupCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.GroupCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_list(self, group_list_request: GroupListRequest) -> AsyncIterator[GroupListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.group_commands_pb2.GroupListResponse]) -> AsyncIterator[GroupListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield GroupListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = group_list_request
			return response_iterator(self.__stub.GroupList(olvid.daemon.command.v1.group_commands_pb2.GroupListRequest(filter=GroupFilter._to_native(overlay_object.filter)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_get(self, group_get_request: GroupGetRequest) -> Coroutine[Any, Any, GroupGetResponse]:
		try:
			overlay_object = group_get_request
			return GroupGetResponse._from_native_promise(self.__stub.GroupGet(olvid.daemon.command.v1.group_commands_pb2.GroupGetRequest(group_id=overlay_object.group_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_get_bytes_identifier(self, group_get_bytes_identifier_request: GroupGetBytesIdentifierRequest) -> Coroutine[Any, Any, GroupGetBytesIdentifierResponse]:
		try:
			overlay_object = group_get_bytes_identifier_request
			return GroupGetBytesIdentifierResponse._from_native_promise(self.__stub.GroupGetBytesIdentifier(olvid.daemon.command.v1.group_commands_pb2.GroupGetBytesIdentifierRequest(group_id=overlay_object.group_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_new_standard_group(self, group_new_standard_group_request: GroupNewStandardGroupRequest) -> Coroutine[Any, Any, GroupNewStandardGroupResponse]:
		try:
			overlay_object = group_new_standard_group_request
			return GroupNewStandardGroupResponse._from_native_promise(self.__stub.GroupNewStandardGroup(olvid.daemon.command.v1.group_commands_pb2.GroupNewStandardGroupRequest(name=overlay_object.name, description=overlay_object.description, admin_contact_ids=overlay_object.admin_contact_ids), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_new_controlled_group(self, group_new_controlled_group_request: GroupNewControlledGroupRequest) -> Coroutine[Any, Any, GroupNewControlledGroupResponse]:
		try:
			overlay_object = group_new_controlled_group_request
			return GroupNewControlledGroupResponse._from_native_promise(self.__stub.GroupNewControlledGroup(olvid.daemon.command.v1.group_commands_pb2.GroupNewControlledGroupRequest(name=overlay_object.name, description=overlay_object.description, admin_contact_ids=overlay_object.admin_contact_ids, contact_ids=overlay_object.contact_ids), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_new_read_only_group(self, group_new_read_only_group_request: GroupNewReadOnlyGroupRequest) -> Coroutine[Any, Any, GroupNewReadOnlyGroupResponse]:
		try:
			overlay_object = group_new_read_only_group_request
			return GroupNewReadOnlyGroupResponse._from_native_promise(self.__stub.GroupNewReadOnlyGroup(olvid.daemon.command.v1.group_commands_pb2.GroupNewReadOnlyGroupRequest(name=overlay_object.name, description=overlay_object.description, admin_contact_ids=overlay_object.admin_contact_ids, contact_ids=overlay_object.contact_ids), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_new_advanced_group(self, group_new_advanced_group_request: GroupNewAdvancedGroupRequest) -> Coroutine[Any, Any, GroupNewAdvancedGroupResponse]:
		try:
			overlay_object = group_new_advanced_group_request
			return GroupNewAdvancedGroupResponse._from_native_promise(self.__stub.GroupNewAdvancedGroup(olvid.daemon.command.v1.group_commands_pb2.GroupNewAdvancedGroupRequest(name=overlay_object.name, description=overlay_object.description, advanced_configuration=Group.AdvancedConfiguration._to_native(overlay_object.advanced_configuration), members=GroupMember._to_native_list(overlay_object.members)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_disband(self, group_disband_request: GroupDisbandRequest) -> Coroutine[Any, Any, GroupDisbandResponse]:
		try:
			overlay_object = group_disband_request
			return GroupDisbandResponse._from_native_promise(self.__stub.GroupDisband(olvid.daemon.command.v1.group_commands_pb2.GroupDisbandRequest(group_id=overlay_object.group_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_leave(self, group_leave_request: GroupLeaveRequest) -> Coroutine[Any, Any, GroupLeaveResponse]:
		try:
			overlay_object = group_leave_request
			return GroupLeaveResponse._from_native_promise(self.__stub.GroupLeave(olvid.daemon.command.v1.group_commands_pb2.GroupLeaveRequest(group_id=overlay_object.group_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_update(self, group_update_request: GroupUpdateRequest) -> Coroutine[Any, Any, GroupUpdateResponse]:
		try:
			overlay_object = group_update_request
			return GroupUpdateResponse._from_native_promise(self.__stub.GroupUpdate(olvid.daemon.command.v1.group_commands_pb2.GroupUpdateRequest(group=Group._to_native(overlay_object.group)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_unset_photo(self, group_unset_photo_request: GroupUnsetPhotoRequest) -> Coroutine[Any, Any, GroupUnsetPhotoResponse]:
		try:
			overlay_object = group_unset_photo_request
			return GroupUnsetPhotoResponse._from_native_promise(self.__stub.GroupUnsetPhoto(olvid.daemon.command.v1.group_commands_pb2.GroupUnsetPhotoRequest(group_id=overlay_object.group_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_set_photo(self, group_set_photo_request_iterator: AsyncIterator[GroupSetPhotoRequest]) -> Coroutine[Any, Any, GroupSetPhotoResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember
			async def request_iterator(iterator: AsyncIterator[GroupSetPhotoRequest]):
				try:
					async for message in iterator.__aiter__():
						yield GroupSetPhotoRequest._to_native(message)
				except errors.AioRpcError as err:
					raise errors.OlvidError._from_aio_rpc_error(err) from err
			return GroupSetPhotoResponse._from_native_promise(self.__stub.GroupSetPhoto(request_iterator(group_set_photo_request_iterator), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def group_download_photo(self, group_download_photo_request: GroupDownloadPhotoRequest) -> Coroutine[Any, Any, GroupDownloadPhotoResponse]:
		try:
			overlay_object = group_download_photo_request
			return GroupDownloadPhotoResponse._from_native_promise(self.__stub.GroupDownloadPhoto(olvid.daemon.command.v1.group_commands_pb2.GroupDownloadPhotoRequest(group_id=overlay_object.group_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class DiscussionCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.DiscussionCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.DiscussionCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_list(self, discussion_list_request: DiscussionListRequest) -> AsyncIterator[DiscussionListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListResponse]) -> AsyncIterator[DiscussionListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield DiscussionListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = discussion_list_request
			return response_iterator(self.__stub.DiscussionList(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionListRequest(filter=DiscussionFilter._to_native(overlay_object.filter)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_get(self, discussion_get_request: DiscussionGetRequest) -> Coroutine[Any, Any, DiscussionGetResponse]:
		try:
			overlay_object = discussion_get_request
			return DiscussionGetResponse._from_native_promise(self.__stub.DiscussionGet(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetRequest(discussion_id=overlay_object.discussion_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_get_bytes_identifier(self, discussion_get_bytes_identifier_request: DiscussionGetBytesIdentifierRequest) -> Coroutine[Any, Any, DiscussionGetBytesIdentifierResponse]:
		try:
			overlay_object = discussion_get_bytes_identifier_request
			return DiscussionGetBytesIdentifierResponse._from_native_promise(self.__stub.DiscussionGetBytesIdentifier(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetBytesIdentifierRequest(discussion_id=overlay_object.discussion_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_get_by_contact(self, discussion_get_by_contact_request: DiscussionGetByContactRequest) -> Coroutine[Any, Any, DiscussionGetByContactResponse]:
		try:
			overlay_object = discussion_get_by_contact_request
			return DiscussionGetByContactResponse._from_native_promise(self.__stub.DiscussionGetByContact(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByContactRequest(contact_id=overlay_object.contact_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_get_by_group(self, discussion_get_by_group_request: DiscussionGetByGroupRequest) -> Coroutine[Any, Any, DiscussionGetByGroupResponse]:
		try:
			overlay_object = discussion_get_by_group_request
			return DiscussionGetByGroupResponse._from_native_promise(self.__stub.DiscussionGetByGroup(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionGetByGroupRequest(group_id=overlay_object.group_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_empty(self, discussion_empty_request: DiscussionEmptyRequest) -> Coroutine[Any, Any, DiscussionEmptyResponse]:
		try:
			overlay_object = discussion_empty_request
			return DiscussionEmptyResponse._from_native_promise(self.__stub.DiscussionEmpty(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionEmptyRequest(discussion_id=overlay_object.discussion_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_download_photo(self, discussion_download_photo_request: DiscussionDownloadPhotoRequest) -> Coroutine[Any, Any, DiscussionDownloadPhotoResponse]:
		try:
			overlay_object = discussion_download_photo_request
			return DiscussionDownloadPhotoResponse._from_native_promise(self.__stub.DiscussionDownloadPhoto(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionDownloadPhotoRequest(discussion_id=overlay_object.discussion_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_locked_list(self, discussion_locked_list_request: DiscussionLockedListRequest) -> AsyncIterator[DiscussionLockedListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListResponse]) -> AsyncIterator[DiscussionLockedListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield DiscussionLockedListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = discussion_locked_list_request
			return response_iterator(self.__stub.DiscussionLockedList(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedListRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_locked_delete(self, discussion_locked_delete_request: DiscussionLockedDeleteRequest) -> Coroutine[Any, Any, DiscussionLockedDeleteResponse]:
		try:
			overlay_object = discussion_locked_delete_request
			return DiscussionLockedDeleteResponse._from_native_promise(self.__stub.DiscussionLockedDelete(olvid.daemon.command.v1.discussion_commands_pb2.DiscussionLockedDeleteRequest(discussion_id=overlay_object.discussion_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class MessageCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.MessageCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.MessageCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_list(self, message_list_request: MessageListRequest) -> AsyncIterator[MessageListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.message_commands_pb2.MessageListResponse]) -> AsyncIterator[MessageListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield MessageListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = message_list_request
			return response_iterator(self.__stub.MessageList(olvid.daemon.command.v1.message_commands_pb2.MessageListRequest(filter=MessageFilter._to_native(overlay_object.filter), unread=overlay_object.unread), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_get(self, message_get_request: MessageGetRequest) -> Coroutine[Any, Any, MessageGetResponse]:
		try:
			overlay_object = message_get_request
			return MessageGetResponse._from_native_promise(self.__stub.MessageGet(olvid.daemon.command.v1.message_commands_pb2.MessageGetRequest(message_id=MessageId._to_native(overlay_object.message_id)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_refresh(self, message_refresh_request: MessageRefreshRequest) -> Coroutine[Any, Any, MessageRefreshResponse]:
		try:
			overlay_object = message_refresh_request
			return MessageRefreshResponse._from_native_promise(self.__stub.MessageRefresh(olvid.daemon.command.v1.message_commands_pb2.MessageRefreshRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_delete(self, message_delete_request: MessageDeleteRequest) -> Coroutine[Any, Any, MessageDeleteResponse]:
		try:
			overlay_object = message_delete_request
			return MessageDeleteResponse._from_native_promise(self.__stub.MessageDelete(olvid.daemon.command.v1.message_commands_pb2.MessageDeleteRequest(message_id=MessageId._to_native(overlay_object.message_id), delete_everywhere=overlay_object.delete_everywhere), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_send(self, message_send_request: MessageSendRequest) -> Coroutine[Any, Any, MessageSendResponse]:
		try:
			overlay_object = message_send_request
			return MessageSendResponse._from_native_promise(self.__stub.MessageSend(olvid.daemon.command.v1.message_commands_pb2.MessageSendRequest(discussion_id=overlay_object.discussion_id, body=overlay_object.body, reply_id=MessageId._to_native(overlay_object.reply_id), ephemerality=MessageEphemerality._to_native(overlay_object.ephemerality), disable_link_preview=overlay_object.disable_link_preview), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_send_with_attachments(self, message_send_with_attachments_request_iterator: AsyncIterator[MessageSendWithAttachmentsRequest]) -> Coroutine[Any, Any, MessageSendWithAttachmentsResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember
			async def request_iterator(iterator: AsyncIterator[MessageSendWithAttachmentsRequest]):
				try:
					async for message in iterator.__aiter__():
						yield MessageSendWithAttachmentsRequest._to_native(message)
				except errors.AioRpcError as err:
					raise errors.OlvidError._from_aio_rpc_error(err) from err
			return MessageSendWithAttachmentsResponse._from_native_promise(self.__stub.MessageSendWithAttachments(request_iterator(message_send_with_attachments_request_iterator), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_send_location(self, message_send_location_request: MessageSendLocationRequest) -> Coroutine[Any, Any, MessageSendLocationResponse]:
		try:
			overlay_object = message_send_location_request
			return MessageSendLocationResponse._from_native_promise(self.__stub.MessageSendLocation(olvid.daemon.command.v1.message_commands_pb2.MessageSendLocationRequest(discussion_id=overlay_object.discussion_id, latitude=overlay_object.latitude, longitude=overlay_object.longitude, altitude=overlay_object.altitude, precision=overlay_object.precision, address=overlay_object.address, preview_filename=overlay_object.preview_filename, preview_payload=overlay_object.preview_payload, ephemerality=MessageEphemerality._to_native(overlay_object.ephemerality)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_start_location_sharing(self, message_start_location_sharing_request: MessageStartLocationSharingRequest) -> Coroutine[Any, Any, MessageStartLocationSharingResponse]:
		try:
			overlay_object = message_start_location_sharing_request
			return MessageStartLocationSharingResponse._from_native_promise(self.__stub.MessageStartLocationSharing(olvid.daemon.command.v1.message_commands_pb2.MessageStartLocationSharingRequest(discussion_id=overlay_object.discussion_id, latitude=overlay_object.latitude, longitude=overlay_object.longitude, altitude=overlay_object.altitude, precision=overlay_object.precision), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_update_location_sharing(self, message_update_location_sharing_request: MessageUpdateLocationSharingRequest) -> Coroutine[Any, Any, MessageUpdateLocationSharingResponse]:
		try:
			overlay_object = message_update_location_sharing_request
			return MessageUpdateLocationSharingResponse._from_native_promise(self.__stub.MessageUpdateLocationSharing(olvid.daemon.command.v1.message_commands_pb2.MessageUpdateLocationSharingRequest(message_id=MessageId._to_native(overlay_object.message_id), latitude=overlay_object.latitude, longitude=overlay_object.longitude, altitude=overlay_object.altitude, precision=overlay_object.precision), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_end_location_sharing(self, message_end_location_sharing_request: MessageEndLocationSharingRequest) -> Coroutine[Any, Any, MessageEndLocationSharingResponse]:
		try:
			overlay_object = message_end_location_sharing_request
			return MessageEndLocationSharingResponse._from_native_promise(self.__stub.MessageEndLocationSharing(olvid.daemon.command.v1.message_commands_pb2.MessageEndLocationSharingRequest(message_id=MessageId._to_native(overlay_object.message_id)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_react(self, message_react_request: MessageReactRequest) -> Coroutine[Any, Any, MessageReactResponse]:
		try:
			overlay_object = message_react_request
			return MessageReactResponse._from_native_promise(self.__stub.MessageReact(olvid.daemon.command.v1.message_commands_pb2.MessageReactRequest(message_id=MessageId._to_native(overlay_object.message_id), reaction=overlay_object.reaction), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def message_update_body(self, message_update_body_request: MessageUpdateBodyRequest) -> Coroutine[Any, Any, MessageUpdateBodyResponse]:
		try:
			overlay_object = message_update_body_request
			return MessageUpdateBodyResponse._from_native_promise(self.__stub.MessageUpdateBody(olvid.daemon.command.v1.message_commands_pb2.MessageUpdateBodyRequest(message_id=MessageId._to_native(overlay_object.message_id), updated_body=overlay_object.updated_body), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class AttachmentCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.AttachmentCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.AttachmentCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def attachment_list(self, attachment_list_request: AttachmentListRequest) -> AsyncIterator[AttachmentListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListResponse]) -> AsyncIterator[AttachmentListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield AttachmentListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = attachment_list_request
			return response_iterator(self.__stub.AttachmentList(olvid.daemon.command.v1.attachment_commands_pb2.AttachmentListRequest(filter=AttachmentFilter._to_native(overlay_object.filter)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def attachment_get(self, attachment_get_request: AttachmentGetRequest) -> Coroutine[Any, Any, AttachmentGetResponse]:
		try:
			overlay_object = attachment_get_request
			return AttachmentGetResponse._from_native_promise(self.__stub.AttachmentGet(olvid.daemon.command.v1.attachment_commands_pb2.AttachmentGetRequest(attachment_id=AttachmentId._to_native(overlay_object.attachment_id)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def attachment_delete(self, attachment_delete_request: AttachmentDeleteRequest) -> Coroutine[Any, Any, AttachmentDeleteResponse]:
		try:
			overlay_object = attachment_delete_request
			return AttachmentDeleteResponse._from_native_promise(self.__stub.AttachmentDelete(olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDeleteRequest(attachment_id=AttachmentId._to_native(overlay_object.attachment_id), delete_everywhere=overlay_object.delete_everywhere), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def attachment_download(self, attachment_download_request: AttachmentDownloadRequest) -> AsyncIterator[AttachmentDownloadResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadResponse]) -> AsyncIterator[AttachmentDownloadResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield AttachmentDownloadResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = attachment_download_request
			return response_iterator(self.__stub.AttachmentDownload(olvid.daemon.command.v1.attachment_commands_pb2.AttachmentDownloadRequest(attachment_id=AttachmentId._to_native(overlay_object.attachment_id)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class StorageCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.StorageCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.StorageCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def storage_list(self, storage_list_request: StorageListRequest) -> AsyncIterator[StorageListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.storage_commands_pb2.StorageListResponse]) -> AsyncIterator[StorageListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield StorageListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = storage_list_request
			return response_iterator(self.__stub.StorageList(olvid.daemon.command.v1.storage_commands_pb2.StorageListRequest(filter=StorageElementFilter._to_native(overlay_object.filter)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def storage_get(self, storage_get_request: StorageGetRequest) -> Coroutine[Any, Any, StorageGetResponse]:
		try:
			overlay_object = storage_get_request
			return StorageGetResponse._from_native_promise(self.__stub.StorageGet(olvid.daemon.command.v1.storage_commands_pb2.StorageGetRequest(key=overlay_object.key), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def storage_set(self, storage_set_request: StorageSetRequest) -> Coroutine[Any, Any, StorageSetResponse]:
		try:
			overlay_object = storage_set_request
			return StorageSetResponse._from_native_promise(self.__stub.StorageSet(olvid.daemon.command.v1.storage_commands_pb2.StorageSetRequest(key=overlay_object.key, value=overlay_object.value), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def storage_unset(self, storage_unset_request: StorageUnsetRequest) -> Coroutine[Any, Any, StorageUnsetResponse]:
		try:
			overlay_object = storage_unset_request
			return StorageUnsetResponse._from_native_promise(self.__stub.StorageUnset(olvid.daemon.command.v1.storage_commands_pb2.StorageUnsetRequest(key=overlay_object.key), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class DiscussionStorageCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.DiscussionStorageCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.DiscussionStorageCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_storage_list(self, discussion_storage_list_request: DiscussionStorageListRequest) -> AsyncIterator[DiscussionStorageListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListResponse]) -> AsyncIterator[DiscussionStorageListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield DiscussionStorageListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = discussion_storage_list_request
			return response_iterator(self.__stub.DiscussionStorageList(olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageListRequest(discussion_id=overlay_object.discussion_id, filter=StorageElementFilter._to_native(overlay_object.filter)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_storage_get(self, discussion_storage_get_request: DiscussionStorageGetRequest) -> Coroutine[Any, Any, DiscussionStorageGetResponse]:
		try:
			overlay_object = discussion_storage_get_request
			return DiscussionStorageGetResponse._from_native_promise(self.__stub.DiscussionStorageGet(olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageGetRequest(discussion_id=overlay_object.discussion_id, key=overlay_object.key), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_storage_set(self, discussion_storage_set_request: DiscussionStorageSetRequest) -> Coroutine[Any, Any, DiscussionStorageSetResponse]:
		try:
			overlay_object = discussion_storage_set_request
			return DiscussionStorageSetResponse._from_native_promise(self.__stub.DiscussionStorageSet(olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageSetRequest(discussion_id=overlay_object.discussion_id, key=overlay_object.key, value=overlay_object.value), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def discussion_storage_unset(self, discussion_storage_unset_request: DiscussionStorageUnsetRequest) -> Coroutine[Any, Any, DiscussionStorageUnsetResponse]:
		try:
			overlay_object = discussion_storage_unset_request
			return DiscussionStorageUnsetResponse._from_native_promise(self.__stub.DiscussionStorageUnset(olvid.daemon.command.v1.storage_commands_pb2.DiscussionStorageUnsetRequest(discussion_id=overlay_object.discussion_id, key=overlay_object.key), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class CallCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.CallCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.CallCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def call_start_discussion_call(self, call_start_discussion_call_request: CallStartDiscussionCallRequest) -> Coroutine[Any, Any, CallStartDiscussionCallResponse]:
		try:
			overlay_object = call_start_discussion_call_request
			return CallStartDiscussionCallResponse._from_native_promise(self.__stub.CallStartDiscussionCall(olvid.daemon.command.v1.call_commands_pb2.CallStartDiscussionCallRequest(discussion_id=overlay_object.discussion_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def call_start_custom_call(self, call_start_custom_call_request: CallStartCustomCallRequest) -> Coroutine[Any, Any, CallStartCustomCallResponse]:
		try:
			overlay_object = call_start_custom_call_request
			return CallStartCustomCallResponse._from_native_promise(self.__stub.CallStartCustomCall(olvid.daemon.command.v1.call_commands_pb2.CallStartCustomCallRequest(contact_ids=overlay_object.contact_ids, discussion_id=overlay_object.discussion_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class SettingsCommandServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.command_service_pb2_grpc.SettingsCommandServiceStub = olvid.daemon.services.v1.command_service_pb2_grpc.SettingsCommandServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def settings_identity_get(self, settings_identity_get_request: SettingsIdentityGetRequest) -> Coroutine[Any, Any, SettingsIdentityGetResponse]:
		try:
			overlay_object = settings_identity_get_request
			return SettingsIdentityGetResponse._from_native_promise(self.__stub.SettingsIdentityGet(olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentityGetRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def settings_identity_set(self, settings_identity_set_request: SettingsIdentitySetRequest) -> Coroutine[Any, Any, SettingsIdentitySetResponse]:
		try:
			overlay_object = settings_identity_set_request
			return SettingsIdentitySetResponse._from_native_promise(self.__stub.SettingsIdentitySet(olvid.daemon.command.v1.settings_commands_pb2.SettingsIdentitySetRequest(identity_settings=IdentitySettings._to_native(overlay_object.identity_settings)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def settings_discussion_get(self, settings_discussion_get_request: SettingsDiscussionGetRequest) -> Coroutine[Any, Any, SettingsDiscussionGetResponse]:
		try:
			overlay_object = settings_discussion_get_request
			return SettingsDiscussionGetResponse._from_native_promise(self.__stub.SettingsDiscussionGet(olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionGetRequest(discussion_id=overlay_object.discussion_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def settings_discussion_set(self, settings_discussion_set_request: SettingsDiscussionSetRequest) -> Coroutine[Any, Any, SettingsDiscussionSetResponse]:
		try:
			overlay_object = settings_discussion_set_request
			return SettingsDiscussionSetResponse._from_native_promise(self.__stub.SettingsDiscussionSet(olvid.daemon.command.v1.settings_commands_pb2.SettingsDiscussionSetRequest(discussion_settings=DiscussionSettings._to_native(overlay_object.discussion_settings)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e
