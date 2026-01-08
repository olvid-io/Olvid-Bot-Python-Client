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
class BackupKeyGetRequest:
	def __init__(self):
		pass

	def _update_content(self, backup_key_get_request: BackupKeyGetRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupKeyGetRequest":
		return BackupKeyGetRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyGetRequest) -> "BackupKeyGetRequest":
		return BackupKeyGetRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyGetRequest]) -> list["BackupKeyGetRequest"]:
		return [BackupKeyGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyGetRequest]) -> "BackupKeyGetRequest":
		try:
			native_message = await promise
			return BackupKeyGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupKeyGetRequest"]):
		if messages is None:
			return []
		return [BackupKeyGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupKeyGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyGetRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupKeyGetRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupKeyGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupKeyGetResponse:
	def __init__(self, backup_key: str = ""):
		self.backup_key: str = backup_key

	def _update_content(self, backup_key_get_response: BackupKeyGetResponse) -> None:
		self.backup_key: str = backup_key_get_response.backup_key

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupKeyGetResponse":
		return BackupKeyGetResponse(backup_key=self.backup_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyGetResponse) -> "BackupKeyGetResponse":
		return BackupKeyGetResponse(backup_key=native_message.backup_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyGetResponse]) -> list["BackupKeyGetResponse"]:
		return [BackupKeyGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyGetResponse]) -> "BackupKeyGetResponse":
		try:
			native_message = await promise
			return BackupKeyGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupKeyGetResponse"]):
		if messages is None:
			return []
		return [BackupKeyGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupKeyGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyGetResponse(backup_key=message.backup_key if message.backup_key else None)

	def __str__(self):
		s: str = ''
		if self.backup_key:
			s += f'backup_key: {self.backup_key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupKeyGetResponse):
			return False
		return self.backup_key == other.backup_key

	def __bool__(self):
		return self.backup_key != ""

	def __hash__(self):
		return hash(self.backup_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupKeyGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.backup_key == "" or self.backup_key == expected.backup_key, "Invalid value: backup_key: " + str(expected.backup_key) + " != " + str(self.backup_key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupKeyRenewRequest:
	def __init__(self):
		pass

	def _update_content(self, backup_key_renew_request: BackupKeyRenewRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupKeyRenewRequest":
		return BackupKeyRenewRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyRenewRequest) -> "BackupKeyRenewRequest":
		return BackupKeyRenewRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyRenewRequest]) -> list["BackupKeyRenewRequest"]:
		return [BackupKeyRenewRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyRenewRequest]) -> "BackupKeyRenewRequest":
		try:
			native_message = await promise
			return BackupKeyRenewRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupKeyRenewRequest"]):
		if messages is None:
			return []
		return [BackupKeyRenewRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupKeyRenewRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyRenewRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupKeyRenewRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupKeyRenewRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupKeyRenewResponse:
	def __init__(self, backup_key: str = ""):
		self.backup_key: str = backup_key

	def _update_content(self, backup_key_renew_response: BackupKeyRenewResponse) -> None:
		self.backup_key: str = backup_key_renew_response.backup_key

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupKeyRenewResponse":
		return BackupKeyRenewResponse(backup_key=self.backup_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyRenewResponse) -> "BackupKeyRenewResponse":
		return BackupKeyRenewResponse(backup_key=native_message.backup_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyRenewResponse]) -> list["BackupKeyRenewResponse"]:
		return [BackupKeyRenewResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyRenewResponse]) -> "BackupKeyRenewResponse":
		try:
			native_message = await promise
			return BackupKeyRenewResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupKeyRenewResponse"]):
		if messages is None:
			return []
		return [BackupKeyRenewResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupKeyRenewResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyRenewResponse(backup_key=message.backup_key if message.backup_key else None)

	def __str__(self):
		s: str = ''
		if self.backup_key:
			s += f'backup_key: {self.backup_key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupKeyRenewResponse):
			return False
		return self.backup_key == other.backup_key

	def __bool__(self):
		return self.backup_key != ""

	def __hash__(self):
		return hash(self.backup_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupKeyRenewResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.backup_key == "" or self.backup_key == expected.backup_key, "Invalid value: backup_key: " + str(expected.backup_key) + " != " + str(self.backup_key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupGetRequest:
	def __init__(self, backup_key: str = ""):
		self.backup_key: str = backup_key

	def _update_content(self, backup_get_request: BackupGetRequest) -> None:
		self.backup_key: str = backup_get_request.backup_key

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupGetRequest":
		return BackupGetRequest(backup_key=self.backup_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupGetRequest) -> "BackupGetRequest":
		return BackupGetRequest(backup_key=native_message.backup_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupGetRequest]) -> list["BackupGetRequest"]:
		return [BackupGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupGetRequest]) -> "BackupGetRequest":
		try:
			native_message = await promise
			return BackupGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupGetRequest"]):
		if messages is None:
			return []
		return [BackupGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupGetRequest(backup_key=message.backup_key if message.backup_key else None)

	def __str__(self):
		s: str = ''
		if self.backup_key:
			s += f'backup_key: {self.backup_key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupGetRequest):
			return False
		return self.backup_key == other.backup_key

	def __bool__(self):
		return self.backup_key != ""

	def __hash__(self):
		return hash(self.backup_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.backup_key == "" or self.backup_key == expected.backup_key, "Invalid value: backup_key: " + str(expected.backup_key) + " != " + str(self.backup_key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupGetResponse:
	def __init__(self, backup: "Backup" = None):
		self.backup: Backup = backup

	def _update_content(self, backup_get_response: BackupGetResponse) -> None:
		self.backup: Backup = backup_get_response.backup

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupGetResponse":
		return BackupGetResponse(backup=self.backup._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupGetResponse) -> "BackupGetResponse":
		return BackupGetResponse(backup=Backup._from_native(native_message.backup))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupGetResponse]) -> list["BackupGetResponse"]:
		return [BackupGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupGetResponse]) -> "BackupGetResponse":
		try:
			native_message = await promise
			return BackupGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupGetResponse"]):
		if messages is None:
			return []
		return [BackupGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupGetResponse(backup=Backup._to_native(message.backup if message.backup else None))

	def __str__(self):
		s: str = ''
		if self.backup:
			s += f'backup: ({self.backup}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupGetResponse):
			return False
		return self.backup == other.backup

	def __bool__(self):
		return bool(self.backup)

	def __hash__(self):
		return hash(self.backup)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.backup is None or self.backup._test_assertion(expected.backup)
		except AssertionError as e:
			raise AssertionError("backup: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupNowRequest:
	def __init__(self):
		pass

	def _update_content(self, backup_now_request: BackupNowRequest) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupNowRequest":
		return BackupNowRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupNowRequest) -> "BackupNowRequest":
		return BackupNowRequest()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupNowRequest]) -> list["BackupNowRequest"]:
		return [BackupNowRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupNowRequest]) -> "BackupNowRequest":
		try:
			native_message = await promise
			return BackupNowRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupNowRequest"]):
		if messages is None:
			return []
		return [BackupNowRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupNowRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupNowRequest()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupNowRequest):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupNowRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupNowResponse:
	def __init__(self):
		pass

	def _update_content(self, backup_now_response: BackupNowResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupNowResponse":
		return BackupNowResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupNowResponse) -> "BackupNowResponse":
		return BackupNowResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupNowResponse]) -> list["BackupNowResponse"]:
		return [BackupNowResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupNowResponse]) -> "BackupNowResponse":
		try:
			native_message = await promise
			return BackupNowResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupNowResponse"]):
		if messages is None:
			return []
		return [BackupNowResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupNowResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupNowResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupNowResponse):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupNowResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupRestoreDaemonRequest:
	def __init__(self, backup_key: str = "", new_device_name: str = ""):
		self.backup_key: str = backup_key
		self.new_device_name: str = new_device_name

	def _update_content(self, backup_restore_daemon_request: BackupRestoreDaemonRequest) -> None:
		self.backup_key: str = backup_restore_daemon_request.backup_key
		self.new_device_name: str = backup_restore_daemon_request.new_device_name

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupRestoreDaemonRequest":
		return BackupRestoreDaemonRequest(backup_key=self.backup_key, new_device_name=self.new_device_name)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreDaemonRequest) -> "BackupRestoreDaemonRequest":
		return BackupRestoreDaemonRequest(backup_key=native_message.backup_key, new_device_name=native_message.new_device_name)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreDaemonRequest]) -> list["BackupRestoreDaemonRequest"]:
		return [BackupRestoreDaemonRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreDaemonRequest]) -> "BackupRestoreDaemonRequest":
		try:
			native_message = await promise
			return BackupRestoreDaemonRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupRestoreDaemonRequest"]):
		if messages is None:
			return []
		return [BackupRestoreDaemonRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupRestoreDaemonRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreDaemonRequest(backup_key=message.backup_key if message.backup_key else None, new_device_name=message.new_device_name if message.new_device_name else None)

	def __str__(self):
		s: str = ''
		if self.backup_key:
			s += f'backup_key: {self.backup_key}, '
		if self.new_device_name:
			s += f'new_device_name: {self.new_device_name}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupRestoreDaemonRequest):
			return False
		return self.backup_key == other.backup_key and self.new_device_name == other.new_device_name

	def __bool__(self):
		return self.backup_key != "" or self.new_device_name != ""

	def __hash__(self):
		return hash((self.backup_key, self.new_device_name))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupRestoreDaemonRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.backup_key == "" or self.backup_key == expected.backup_key, "Invalid value: backup_key: " + str(expected.backup_key) + " != " + str(self.backup_key)
		assert expected.new_device_name == "" or self.new_device_name == expected.new_device_name, "Invalid value: new_device_name: " + str(expected.new_device_name) + " != " + str(self.new_device_name)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupRestoreDaemonResponse:
	def __init__(self, restored_identities: "list[Identity]" = None, restored_admin_client_keys: "list[ClientKey]" = None, restored_client_keys: "list[ClientKey]" = None):
		self.restored_identities: list[Identity] = restored_identities
		self.restored_admin_client_keys: list[ClientKey] = restored_admin_client_keys
		self.restored_client_keys: list[ClientKey] = restored_client_keys

	def _update_content(self, backup_restore_daemon_response: BackupRestoreDaemonResponse) -> None:
		self.restored_identities: list[Identity] = backup_restore_daemon_response.restored_identities
		self.restored_admin_client_keys: list[ClientKey] = backup_restore_daemon_response.restored_admin_client_keys
		self.restored_client_keys: list[ClientKey] = backup_restore_daemon_response.restored_client_keys

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupRestoreDaemonResponse":
		return BackupRestoreDaemonResponse(restored_identities=[e._clone() for e in self.restored_identities], restored_admin_client_keys=[e._clone() for e in self.restored_admin_client_keys], restored_client_keys=[e._clone() for e in self.restored_client_keys])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreDaemonResponse) -> "BackupRestoreDaemonResponse":
		return BackupRestoreDaemonResponse(restored_identities=Identity._from_native_list(native_message.restored_identities), restored_admin_client_keys=ClientKey._from_native_list(native_message.restored_admin_client_keys), restored_client_keys=ClientKey._from_native_list(native_message.restored_client_keys))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreDaemonResponse]) -> list["BackupRestoreDaemonResponse"]:
		return [BackupRestoreDaemonResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreDaemonResponse]) -> "BackupRestoreDaemonResponse":
		try:
			native_message = await promise
			return BackupRestoreDaemonResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupRestoreDaemonResponse"]):
		if messages is None:
			return []
		return [BackupRestoreDaemonResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupRestoreDaemonResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreDaemonResponse(restored_identities=Identity._to_native_list(message.restored_identities if message.restored_identities else None), restored_admin_client_keys=ClientKey._to_native_list(message.restored_admin_client_keys if message.restored_admin_client_keys else None), restored_client_keys=ClientKey._to_native_list(message.restored_client_keys if message.restored_client_keys else None))

	def __str__(self):
		s: str = ''
		if self.restored_identities:
			s += f'restored_identities: {[str(el) for el in self.restored_identities]}, '
		if self.restored_admin_client_keys:
			s += f'restored_admin_client_keys: {[str(el) for el in self.restored_admin_client_keys]}, '
		if self.restored_client_keys:
			s += f'restored_client_keys: {[str(el) for el in self.restored_client_keys]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupRestoreDaemonResponse):
			return False
		return self.restored_identities == other.restored_identities and self.restored_admin_client_keys == other.restored_admin_client_keys and self.restored_client_keys == other.restored_client_keys

	def __bool__(self):
		return bool(self.restored_identities) or bool(self.restored_admin_client_keys) or bool(self.restored_client_keys)

	def __hash__(self):
		return hash((tuple(self.restored_identities), tuple(self.restored_admin_client_keys), tuple(self.restored_client_keys)))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupRestoreDaemonResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field restored_identities")
		pass  # print("Warning: test_assertion: skipped a list field restored_admin_client_keys")
		pass  # print("Warning: test_assertion: skipped a list field restored_client_keys")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupRestoreAdminBackupRequest:
	def __init__(self, backup_key: str = ""):
		self.backup_key: str = backup_key

	def _update_content(self, backup_restore_admin_backup_request: BackupRestoreAdminBackupRequest) -> None:
		self.backup_key: str = backup_restore_admin_backup_request.backup_key

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupRestoreAdminBackupRequest":
		return BackupRestoreAdminBackupRequest(backup_key=self.backup_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreAdminBackupRequest) -> "BackupRestoreAdminBackupRequest":
		return BackupRestoreAdminBackupRequest(backup_key=native_message.backup_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreAdminBackupRequest]) -> list["BackupRestoreAdminBackupRequest"]:
		return [BackupRestoreAdminBackupRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreAdminBackupRequest]) -> "BackupRestoreAdminBackupRequest":
		try:
			native_message = await promise
			return BackupRestoreAdminBackupRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupRestoreAdminBackupRequest"]):
		if messages is None:
			return []
		return [BackupRestoreAdminBackupRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupRestoreAdminBackupRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreAdminBackupRequest(backup_key=message.backup_key if message.backup_key else None)

	def __str__(self):
		s: str = ''
		if self.backup_key:
			s += f'backup_key: {self.backup_key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupRestoreAdminBackupRequest):
			return False
		return self.backup_key == other.backup_key

	def __bool__(self):
		return self.backup_key != ""

	def __hash__(self):
		return hash(self.backup_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupRestoreAdminBackupRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.backup_key == "" or self.backup_key == expected.backup_key, "Invalid value: backup_key: " + str(expected.backup_key) + " != " + str(self.backup_key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupRestoreAdminBackupResponse:
	def __init__(self, restored_admin_client_keys: "list[ClientKey]" = None):
		self.restored_admin_client_keys: list[ClientKey] = restored_admin_client_keys

	def _update_content(self, backup_restore_admin_backup_response: BackupRestoreAdminBackupResponse) -> None:
		self.restored_admin_client_keys: list[ClientKey] = backup_restore_admin_backup_response.restored_admin_client_keys

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupRestoreAdminBackupResponse":
		return BackupRestoreAdminBackupResponse(restored_admin_client_keys=[e._clone() for e in self.restored_admin_client_keys])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreAdminBackupResponse) -> "BackupRestoreAdminBackupResponse":
		return BackupRestoreAdminBackupResponse(restored_admin_client_keys=ClientKey._from_native_list(native_message.restored_admin_client_keys))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreAdminBackupResponse]) -> list["BackupRestoreAdminBackupResponse"]:
		return [BackupRestoreAdminBackupResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreAdminBackupResponse]) -> "BackupRestoreAdminBackupResponse":
		try:
			native_message = await promise
			return BackupRestoreAdminBackupResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupRestoreAdminBackupResponse"]):
		if messages is None:
			return []
		return [BackupRestoreAdminBackupResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupRestoreAdminBackupResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreAdminBackupResponse(restored_admin_client_keys=ClientKey._to_native_list(message.restored_admin_client_keys if message.restored_admin_client_keys else None))

	def __str__(self):
		s: str = ''
		if self.restored_admin_client_keys:
			s += f'restored_admin_client_keys: {[str(el) for el in self.restored_admin_client_keys]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupRestoreAdminBackupResponse):
			return False
		return self.restored_admin_client_keys == other.restored_admin_client_keys

	def __bool__(self):
		return bool(self.restored_admin_client_keys)

	def __hash__(self):
		return hash(tuple(self.restored_admin_client_keys))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupRestoreAdminBackupResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field restored_admin_client_keys")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupRestoreProfileSnapshotRequest:
	def __init__(self, backup_key: str = "", id: str = "", new_device_name: str = ""):
		self.backup_key: str = backup_key
		self.id: str = id
		self.new_device_name: str = new_device_name

	def _update_content(self, backup_restore_profile_snapshot_request: BackupRestoreProfileSnapshotRequest) -> None:
		self.backup_key: str = backup_restore_profile_snapshot_request.backup_key
		self.id: str = backup_restore_profile_snapshot_request.id
		self.new_device_name: str = backup_restore_profile_snapshot_request.new_device_name

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupRestoreProfileSnapshotRequest":
		return BackupRestoreProfileSnapshotRequest(backup_key=self.backup_key, id=self.id, new_device_name=self.new_device_name)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreProfileSnapshotRequest) -> "BackupRestoreProfileSnapshotRequest":
		return BackupRestoreProfileSnapshotRequest(backup_key=native_message.backup_key, id=native_message.id, new_device_name=native_message.new_device_name)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreProfileSnapshotRequest]) -> list["BackupRestoreProfileSnapshotRequest"]:
		return [BackupRestoreProfileSnapshotRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreProfileSnapshotRequest]) -> "BackupRestoreProfileSnapshotRequest":
		try:
			native_message = await promise
			return BackupRestoreProfileSnapshotRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupRestoreProfileSnapshotRequest"]):
		if messages is None:
			return []
		return [BackupRestoreProfileSnapshotRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupRestoreProfileSnapshotRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreProfileSnapshotRequest(backup_key=message.backup_key if message.backup_key else None, id=message.id if message.id else None, new_device_name=message.new_device_name if message.new_device_name else None)

	def __str__(self):
		s: str = ''
		if self.backup_key:
			s += f'backup_key: {self.backup_key}, '
		if self.id:
			s += f'id: {self.id}, '
		if self.new_device_name:
			s += f'new_device_name: {self.new_device_name}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupRestoreProfileSnapshotRequest):
			return False
		return self.backup_key == other.backup_key and self.id == other.id and self.new_device_name == other.new_device_name

	def __bool__(self):
		return self.backup_key != "" or self.id != "" or self.new_device_name != ""

	def __hash__(self):
		return hash((self.backup_key, self.id, self.new_device_name))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupRestoreProfileSnapshotRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.backup_key == "" or self.backup_key == expected.backup_key, "Invalid value: backup_key: " + str(expected.backup_key) + " != " + str(self.backup_key)
		assert expected.id == "" or self.id == expected.id, "Invalid value: id: " + str(expected.id) + " != " + str(self.id)
		assert expected.new_device_name == "" or self.new_device_name == expected.new_device_name, "Invalid value: new_device_name: " + str(expected.new_device_name) + " != " + str(self.new_device_name)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class BackupRestoreProfileSnapshotResponse:
	def __init__(self, restored_identity: "Identity" = None, restored_client_keys: "list[ClientKey]" = None):
		self.restored_identity: Identity = restored_identity
		self.restored_client_keys: list[ClientKey] = restored_client_keys

	def _update_content(self, backup_restore_profile_snapshot_response: BackupRestoreProfileSnapshotResponse) -> None:
		self.restored_identity: Identity = backup_restore_profile_snapshot_response.restored_identity
		self.restored_client_keys: list[ClientKey] = backup_restore_profile_snapshot_response.restored_client_keys

	# noinspection PyProtectedMember
	def _clone(self) -> "BackupRestoreProfileSnapshotResponse":
		return BackupRestoreProfileSnapshotResponse(restored_identity=self.restored_identity._clone(), restored_client_keys=[e._clone() for e in self.restored_client_keys])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreProfileSnapshotResponse) -> "BackupRestoreProfileSnapshotResponse":
		return BackupRestoreProfileSnapshotResponse(restored_identity=Identity._from_native(native_message.restored_identity), restored_client_keys=ClientKey._from_native_list(native_message.restored_client_keys))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreProfileSnapshotResponse]) -> list["BackupRestoreProfileSnapshotResponse"]:
		return [BackupRestoreProfileSnapshotResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreProfileSnapshotResponse]) -> "BackupRestoreProfileSnapshotResponse":
		try:
			native_message = await promise
			return BackupRestoreProfileSnapshotResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["BackupRestoreProfileSnapshotResponse"]):
		if messages is None:
			return []
		return [BackupRestoreProfileSnapshotResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["BackupRestoreProfileSnapshotResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreProfileSnapshotResponse(restored_identity=Identity._to_native(message.restored_identity if message.restored_identity else None), restored_client_keys=ClientKey._to_native_list(message.restored_client_keys if message.restored_client_keys else None))

	def __str__(self):
		s: str = ''
		if self.restored_identity:
			s += f'restored_identity: ({self.restored_identity}), '
		if self.restored_client_keys:
			s += f'restored_client_keys: {[str(el) for el in self.restored_client_keys]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, BackupRestoreProfileSnapshotResponse):
			return False
		return self.restored_identity == other.restored_identity and self.restored_client_keys == other.restored_client_keys

	def __bool__(self):
		return bool(self.restored_identity) or bool(self.restored_client_keys)

	def __hash__(self):
		return hash((self.restored_identity, tuple(self.restored_client_keys)))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, BackupRestoreProfileSnapshotResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.restored_identity is None or self.restored_identity._test_assertion(expected.restored_identity)
		except AssertionError as e:
			raise AssertionError("restored_identity: " + str(e))
		pass  # print("Warning: test_assertion: skipped a list field restored_client_keys")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ClientKeyListRequest:
	def __init__(self, filter: "ClientKeyFilter" = None):
		self.filter: ClientKeyFilter = filter

	def _update_content(self, client_key_list_request: ClientKeyListRequest) -> None:
		self.filter: ClientKeyFilter = client_key_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyListRequest":
		return ClientKeyListRequest(filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListRequest) -> "ClientKeyListRequest":
		return ClientKeyListRequest(filter=ClientKeyFilter._from_native(native_message.filter))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListRequest]) -> list["ClientKeyListRequest"]:
		return [ClientKeyListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListRequest]) -> "ClientKeyListRequest":
		try:
			native_message = await promise
			return ClientKeyListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ClientKeyListRequest"]):
		if messages is None:
			return []
		return [ClientKeyListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ClientKeyListRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListRequest(filter=ClientKeyFilter._to_native(message.filter if message.filter else None))

	def __str__(self):
		s: str = ''
		if self.filter:
			s += f'filter: ({self.filter}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ClientKeyListRequest):
			return False
		return self.filter == other.filter

	def __bool__(self):
		return bool(self.filter)

	def __hash__(self):
		return hash(self.filter)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ClientKeyListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ClientKeyListResponse:
	def __init__(self, client_keys: "list[ClientKey]" = None):
		self.client_keys: list[ClientKey] = client_keys

	def _update_content(self, client_key_list_response: ClientKeyListResponse) -> None:
		self.client_keys: list[ClientKey] = client_key_list_response.client_keys

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyListResponse":
		return ClientKeyListResponse(client_keys=[e._clone() for e in self.client_keys])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListResponse) -> "ClientKeyListResponse":
		return ClientKeyListResponse(client_keys=ClientKey._from_native_list(native_message.client_keys))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListResponse]) -> list["ClientKeyListResponse"]:
		return [ClientKeyListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListResponse]) -> "ClientKeyListResponse":
		try:
			native_message = await promise
			return ClientKeyListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ClientKeyListResponse"]):
		if messages is None:
			return []
		return [ClientKeyListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ClientKeyListResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListResponse(client_keys=ClientKey._to_native_list(message.client_keys if message.client_keys else None))

	def __str__(self):
		s: str = ''
		if self.client_keys:
			s += f'client_keys: {[str(el) for el in self.client_keys]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ClientKeyListResponse):
			return False
		return self.client_keys == other.client_keys

	def __bool__(self):
		return bool(self.client_keys)

	def __hash__(self):
		return hash(tuple(self.client_keys))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ClientKeyListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field client_keys")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ClientKeyGetRequest:
	def __init__(self, client_key: str = ""):
		self.client_key: str = client_key

	def _update_content(self, client_key_get_request: ClientKeyGetRequest) -> None:
		self.client_key: str = client_key_get_request.client_key

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyGetRequest":
		return ClientKeyGetRequest(client_key=self.client_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetRequest) -> "ClientKeyGetRequest":
		return ClientKeyGetRequest(client_key=native_message.client_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetRequest]) -> list["ClientKeyGetRequest"]:
		return [ClientKeyGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetRequest]) -> "ClientKeyGetRequest":
		try:
			native_message = await promise
			return ClientKeyGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ClientKeyGetRequest"]):
		if messages is None:
			return []
		return [ClientKeyGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ClientKeyGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetRequest(client_key=message.client_key if message.client_key else None)

	def __str__(self):
		s: str = ''
		if self.client_key:
			s += f'client_key: {self.client_key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ClientKeyGetRequest):
			return False
		return self.client_key == other.client_key

	def __bool__(self):
		return self.client_key != ""

	def __hash__(self):
		return hash(self.client_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ClientKeyGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.client_key == "" or self.client_key == expected.client_key, "Invalid value: client_key: " + str(expected.client_key) + " != " + str(self.client_key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ClientKeyGetResponse:
	def __init__(self, client_key: "ClientKey" = None):
		self.client_key: ClientKey = client_key

	def _update_content(self, client_key_get_response: ClientKeyGetResponse) -> None:
		self.client_key: ClientKey = client_key_get_response.client_key

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyGetResponse":
		return ClientKeyGetResponse(client_key=self.client_key._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetResponse) -> "ClientKeyGetResponse":
		return ClientKeyGetResponse(client_key=ClientKey._from_native(native_message.client_key))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetResponse]) -> list["ClientKeyGetResponse"]:
		return [ClientKeyGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetResponse]) -> "ClientKeyGetResponse":
		try:
			native_message = await promise
			return ClientKeyGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ClientKeyGetResponse"]):
		if messages is None:
			return []
		return [ClientKeyGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ClientKeyGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetResponse(client_key=ClientKey._to_native(message.client_key if message.client_key else None))

	def __str__(self):
		s: str = ''
		if self.client_key:
			s += f'client_key: ({self.client_key}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ClientKeyGetResponse):
			return False
		return self.client_key == other.client_key

	def __bool__(self):
		return bool(self.client_key)

	def __hash__(self):
		return hash(self.client_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ClientKeyGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.client_key is None or self.client_key._test_assertion(expected.client_key)
		except AssertionError as e:
			raise AssertionError("client_key: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ClientKeyNewRequest:
	def __init__(self, name: str = "", identity_id: int = 0):
		self.name: str = name
		self.identity_id: int = identity_id

	def _update_content(self, client_key_new_request: ClientKeyNewRequest) -> None:
		self.name: str = client_key_new_request.name
		self.identity_id: int = client_key_new_request.identity_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyNewRequest":
		return ClientKeyNewRequest(name=self.name, identity_id=self.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewRequest) -> "ClientKeyNewRequest":
		return ClientKeyNewRequest(name=native_message.name, identity_id=native_message.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewRequest]) -> list["ClientKeyNewRequest"]:
		return [ClientKeyNewRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewRequest]) -> "ClientKeyNewRequest":
		try:
			native_message = await promise
			return ClientKeyNewRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ClientKeyNewRequest"]):
		if messages is None:
			return []
		return [ClientKeyNewRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ClientKeyNewRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewRequest(name=message.name if message.name else None, identity_id=message.identity_id if message.identity_id else None)

	def __str__(self):
		s: str = ''
		if self.name:
			s += f'name: {self.name}, '
		if self.identity_id:
			s += f'identity_id: {self.identity_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ClientKeyNewRequest):
			return False
		return self.name == other.name and self.identity_id == other.identity_id

	def __bool__(self):
		return self.name != "" or self.identity_id != 0

	def __hash__(self):
		return hash((self.name, self.identity_id))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ClientKeyNewRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.name == "" or self.name == expected.name, "Invalid value: name: " + str(expected.name) + " != " + str(self.name)
		assert expected.identity_id == 0 or self.identity_id == expected.identity_id, "Invalid value: identity_id: " + str(expected.identity_id) + " != " + str(self.identity_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ClientKeyNewResponse:
	def __init__(self, client_key: "ClientKey" = None):
		self.client_key: ClientKey = client_key

	def _update_content(self, client_key_new_response: ClientKeyNewResponse) -> None:
		self.client_key: ClientKey = client_key_new_response.client_key

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyNewResponse":
		return ClientKeyNewResponse(client_key=self.client_key._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewResponse) -> "ClientKeyNewResponse":
		return ClientKeyNewResponse(client_key=ClientKey._from_native(native_message.client_key))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewResponse]) -> list["ClientKeyNewResponse"]:
		return [ClientKeyNewResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewResponse]) -> "ClientKeyNewResponse":
		try:
			native_message = await promise
			return ClientKeyNewResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ClientKeyNewResponse"]):
		if messages is None:
			return []
		return [ClientKeyNewResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ClientKeyNewResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewResponse(client_key=ClientKey._to_native(message.client_key if message.client_key else None))

	def __str__(self):
		s: str = ''
		if self.client_key:
			s += f'client_key: ({self.client_key}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ClientKeyNewResponse):
			return False
		return self.client_key == other.client_key

	def __bool__(self):
		return bool(self.client_key)

	def __hash__(self):
		return hash(self.client_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ClientKeyNewResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.client_key is None or self.client_key._test_assertion(expected.client_key)
		except AssertionError as e:
			raise AssertionError("client_key: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ClientKeyDeleteRequest:
	def __init__(self, client_key: str = ""):
		self.client_key: str = client_key

	def _update_content(self, client_key_delete_request: ClientKeyDeleteRequest) -> None:
		self.client_key: str = client_key_delete_request.client_key

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyDeleteRequest":
		return ClientKeyDeleteRequest(client_key=self.client_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteRequest) -> "ClientKeyDeleteRequest":
		return ClientKeyDeleteRequest(client_key=native_message.client_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteRequest]) -> list["ClientKeyDeleteRequest"]:
		return [ClientKeyDeleteRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteRequest]) -> "ClientKeyDeleteRequest":
		try:
			native_message = await promise
			return ClientKeyDeleteRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ClientKeyDeleteRequest"]):
		if messages is None:
			return []
		return [ClientKeyDeleteRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ClientKeyDeleteRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteRequest(client_key=message.client_key if message.client_key else None)

	def __str__(self):
		s: str = ''
		if self.client_key:
			s += f'client_key: {self.client_key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ClientKeyDeleteRequest):
			return False
		return self.client_key == other.client_key

	def __bool__(self):
		return self.client_key != ""

	def __hash__(self):
		return hash(self.client_key)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ClientKeyDeleteRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.client_key == "" or self.client_key == expected.client_key, "Invalid value: client_key: " + str(expected.client_key) + " != " + str(self.client_key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class ClientKeyDeleteResponse:
	def __init__(self):
		pass

	def _update_content(self, client_key_delete_response: ClientKeyDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyDeleteResponse":
		return ClientKeyDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteResponse) -> "ClientKeyDeleteResponse":
		return ClientKeyDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteResponse]) -> list["ClientKeyDeleteResponse"]:
		return [ClientKeyDeleteResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteResponse]) -> "ClientKeyDeleteResponse":
		try:
			native_message = await promise
			return ClientKeyDeleteResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["ClientKeyDeleteResponse"]):
		if messages is None:
			return []
		return [ClientKeyDeleteResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["ClientKeyDeleteResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, ClientKeyDeleteResponse):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, ClientKeyDeleteResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityListRequest:
	def __init__(self, filter: "IdentityFilter" = None):
		self.filter: IdentityFilter = filter

	def _update_content(self, identity_list_request: IdentityListRequest) -> None:
		self.filter: IdentityFilter = identity_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityListRequest":
		return IdentityListRequest(filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityListRequest) -> "IdentityListRequest":
		return IdentityListRequest(filter=IdentityFilter._from_native(native_message.filter))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityListRequest]) -> list["IdentityListRequest"]:
		return [IdentityListRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityListRequest]) -> "IdentityListRequest":
		try:
			native_message = await promise
			return IdentityListRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityListRequest"]):
		if messages is None:
			return []
		return [IdentityListRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityListRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityListRequest(filter=IdentityFilter._to_native(message.filter if message.filter else None))

	def __str__(self):
		s: str = ''
		if self.filter:
			s += f'filter: ({self.filter}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityListRequest):
			return False
		return self.filter == other.filter

	def __bool__(self):
		return bool(self.filter)

	def __hash__(self):
		return hash(self.filter)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityListRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.filter is None or self.filter._test_assertion(expected.filter)
		except AssertionError as e:
			raise AssertionError("filter: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityListResponse:
	def __init__(self, identities: "list[Identity]" = None):
		self.identities: list[Identity] = identities

	def _update_content(self, identity_list_response: IdentityListResponse) -> None:
		self.identities: list[Identity] = identity_list_response.identities

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityListResponse":
		return IdentityListResponse(identities=[e._clone() for e in self.identities])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityListResponse) -> "IdentityListResponse":
		return IdentityListResponse(identities=Identity._from_native_list(native_message.identities))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityListResponse]) -> list["IdentityListResponse"]:
		return [IdentityListResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityListResponse]) -> "IdentityListResponse":
		try:
			native_message = await promise
			return IdentityListResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityListResponse"]):
		if messages is None:
			return []
		return [IdentityListResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityListResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityListResponse(identities=Identity._to_native_list(message.identities if message.identities else None))

	def __str__(self):
		s: str = ''
		if self.identities:
			s += f'identities: {[str(el) for el in self.identities]}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityListResponse):
			return False
		return self.identities == other.identities

	def __bool__(self):
		return bool(self.identities)

	def __hash__(self):
		return hash(tuple(self.identities))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityListResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		pass  # print("Warning: test_assertion: skipped a list field identities")
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityAdminGetRequest:
	def __init__(self, identity_id: int = 0):
		self.identity_id: int = identity_id

	def _update_content(self, identity_admin_get_request: IdentityAdminGetRequest) -> None:
		self.identity_id: int = identity_admin_get_request.identity_id

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityAdminGetRequest":
		return IdentityAdminGetRequest(identity_id=self.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetRequest) -> "IdentityAdminGetRequest":
		return IdentityAdminGetRequest(identity_id=native_message.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetRequest]) -> list["IdentityAdminGetRequest"]:
		return [IdentityAdminGetRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetRequest]) -> "IdentityAdminGetRequest":
		try:
			native_message = await promise
			return IdentityAdminGetRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityAdminGetRequest"]):
		if messages is None:
			return []
		return [IdentityAdminGetRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityAdminGetRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetRequest(identity_id=message.identity_id if message.identity_id else None)

	def __str__(self):
		s: str = ''
		if self.identity_id:
			s += f'identity_id: {self.identity_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityAdminGetRequest):
			return False
		return self.identity_id == other.identity_id

	def __bool__(self):
		return self.identity_id != 0

	def __hash__(self):
		return hash(self.identity_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityAdminGetRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identity_id == 0 or self.identity_id == expected.identity_id, "Invalid value: identity_id: " + str(expected.identity_id) + " != " + str(self.identity_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityAdminGetResponse:
	def __init__(self, identity: "Identity" = None):
		self.identity: Identity = identity

	def _update_content(self, identity_admin_get_response: IdentityAdminGetResponse) -> None:
		self.identity: Identity = identity_admin_get_response.identity

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityAdminGetResponse":
		return IdentityAdminGetResponse(identity=self.identity._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetResponse) -> "IdentityAdminGetResponse":
		return IdentityAdminGetResponse(identity=Identity._from_native(native_message.identity))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetResponse]) -> list["IdentityAdminGetResponse"]:
		return [IdentityAdminGetResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetResponse]) -> "IdentityAdminGetResponse":
		try:
			native_message = await promise
			return IdentityAdminGetResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityAdminGetResponse"]):
		if messages is None:
			return []
		return [IdentityAdminGetResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityAdminGetResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetResponse(identity=Identity._to_native(message.identity if message.identity else None))

	def __str__(self):
		s: str = ''
		if self.identity:
			s += f'identity: ({self.identity}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityAdminGetResponse):
			return False
		return self.identity == other.identity

	def __bool__(self):
		return bool(self.identity)

	def __hash__(self):
		return hash(self.identity)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityAdminGetResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity is None or self.identity._test_assertion(expected.identity)
		except AssertionError as e:
			raise AssertionError("identity: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityAdminGetBytesIdentifierRequest:
	def __init__(self, identity_id: int = 0):
		self.identity_id: int = identity_id

	def _update_content(self, identity_admin_get_bytes_identifier_request: IdentityAdminGetBytesIdentifierRequest) -> None:
		self.identity_id: int = identity_admin_get_bytes_identifier_request.identity_id

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityAdminGetBytesIdentifierRequest":
		return IdentityAdminGetBytesIdentifierRequest(identity_id=self.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetBytesIdentifierRequest) -> "IdentityAdminGetBytesIdentifierRequest":
		return IdentityAdminGetBytesIdentifierRequest(identity_id=native_message.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetBytesIdentifierRequest]) -> list["IdentityAdminGetBytesIdentifierRequest"]:
		return [IdentityAdminGetBytesIdentifierRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetBytesIdentifierRequest]) -> "IdentityAdminGetBytesIdentifierRequest":
		try:
			native_message = await promise
			return IdentityAdminGetBytesIdentifierRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityAdminGetBytesIdentifierRequest"]):
		if messages is None:
			return []
		return [IdentityAdminGetBytesIdentifierRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityAdminGetBytesIdentifierRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetBytesIdentifierRequest(identity_id=message.identity_id if message.identity_id else None)

	def __str__(self):
		s: str = ''
		if self.identity_id:
			s += f'identity_id: {self.identity_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityAdminGetBytesIdentifierRequest):
			return False
		return self.identity_id == other.identity_id

	def __bool__(self):
		return self.identity_id != 0

	def __hash__(self):
		return hash(self.identity_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityAdminGetBytesIdentifierRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identity_id == 0 or self.identity_id == expected.identity_id, "Invalid value: identity_id: " + str(expected.identity_id) + " != " + str(self.identity_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityAdminGetBytesIdentifierResponse:
	def __init__(self, identifier: bytes = b""):
		self.identifier: bytes = identifier

	def _update_content(self, identity_admin_get_bytes_identifier_response: IdentityAdminGetBytesIdentifierResponse) -> None:
		self.identifier: bytes = identity_admin_get_bytes_identifier_response.identifier

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityAdminGetBytesIdentifierResponse":
		return IdentityAdminGetBytesIdentifierResponse(identifier=self.identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetBytesIdentifierResponse) -> "IdentityAdminGetBytesIdentifierResponse":
		return IdentityAdminGetBytesIdentifierResponse(identifier=native_message.identifier)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetBytesIdentifierResponse]) -> list["IdentityAdminGetBytesIdentifierResponse"]:
		return [IdentityAdminGetBytesIdentifierResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetBytesIdentifierResponse]) -> "IdentityAdminGetBytesIdentifierResponse":
		try:
			native_message = await promise
			return IdentityAdminGetBytesIdentifierResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityAdminGetBytesIdentifierResponse"]):
		if messages is None:
			return []
		return [IdentityAdminGetBytesIdentifierResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityAdminGetBytesIdentifierResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetBytesIdentifierResponse(identifier=message.identifier if message.identifier else None)

	def __str__(self):
		s: str = ''
		if self.identifier:
			s += f'identifier: {self.identifier}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityAdminGetBytesIdentifierResponse):
			return False
		return self.identifier == other.identifier

	def __bool__(self):
		return self.identifier != b""

	def __hash__(self):
		return hash(self.identifier)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityAdminGetBytesIdentifierResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identifier == b"" or self.identifier == expected.identifier, "Invalid value: identifier: " + str(expected.identifier) + " != " + str(self.identifier)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityAdminGetInvitationLinkRequest:
	def __init__(self, identity_id: int = 0):
		self.identity_id: int = identity_id

	def _update_content(self, identity_admin_get_invitation_link_request: IdentityAdminGetInvitationLinkRequest) -> None:
		self.identity_id: int = identity_admin_get_invitation_link_request.identity_id

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityAdminGetInvitationLinkRequest":
		return IdentityAdminGetInvitationLinkRequest(identity_id=self.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetInvitationLinkRequest) -> "IdentityAdminGetInvitationLinkRequest":
		return IdentityAdminGetInvitationLinkRequest(identity_id=native_message.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetInvitationLinkRequest]) -> list["IdentityAdminGetInvitationLinkRequest"]:
		return [IdentityAdminGetInvitationLinkRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetInvitationLinkRequest]) -> "IdentityAdminGetInvitationLinkRequest":
		try:
			native_message = await promise
			return IdentityAdminGetInvitationLinkRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityAdminGetInvitationLinkRequest"]):
		if messages is None:
			return []
		return [IdentityAdminGetInvitationLinkRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityAdminGetInvitationLinkRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetInvitationLinkRequest(identity_id=message.identity_id if message.identity_id else None)

	def __str__(self):
		s: str = ''
		if self.identity_id:
			s += f'identity_id: {self.identity_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityAdminGetInvitationLinkRequest):
			return False
		return self.identity_id == other.identity_id

	def __bool__(self):
		return self.identity_id != 0

	def __hash__(self):
		return hash(self.identity_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityAdminGetInvitationLinkRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identity_id == 0 or self.identity_id == expected.identity_id, "Invalid value: identity_id: " + str(expected.identity_id) + " != " + str(self.identity_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityAdminGetInvitationLinkResponse:
	def __init__(self, invitation_link: str = ""):
		self.invitation_link: str = invitation_link

	def _update_content(self, identity_admin_get_invitation_link_response: IdentityAdminGetInvitationLinkResponse) -> None:
		self.invitation_link: str = identity_admin_get_invitation_link_response.invitation_link

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityAdminGetInvitationLinkResponse":
		return IdentityAdminGetInvitationLinkResponse(invitation_link=self.invitation_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetInvitationLinkResponse) -> "IdentityAdminGetInvitationLinkResponse":
		return IdentityAdminGetInvitationLinkResponse(invitation_link=native_message.invitation_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetInvitationLinkResponse]) -> list["IdentityAdminGetInvitationLinkResponse"]:
		return [IdentityAdminGetInvitationLinkResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetInvitationLinkResponse]) -> "IdentityAdminGetInvitationLinkResponse":
		try:
			native_message = await promise
			return IdentityAdminGetInvitationLinkResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityAdminGetInvitationLinkResponse"]):
		if messages is None:
			return []
		return [IdentityAdminGetInvitationLinkResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityAdminGetInvitationLinkResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetInvitationLinkResponse(invitation_link=message.invitation_link if message.invitation_link else None)

	def __str__(self):
		s: str = ''
		if self.invitation_link:
			s += f'invitation_link: {self.invitation_link}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityAdminGetInvitationLinkResponse):
			return False
		return self.invitation_link == other.invitation_link

	def __bool__(self):
		return self.invitation_link != ""

	def __hash__(self):
		return hash(self.invitation_link)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityAdminGetInvitationLinkResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.invitation_link == "" or self.invitation_link == expected.invitation_link, "Invalid value: invitation_link: " + str(expected.invitation_link) + " != " + str(self.invitation_link)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityAdminDownloadPhotoRequest:
	def __init__(self, identity_id: int = 0):
		self.identity_id: int = identity_id

	def _update_content(self, identity_admin_download_photo_request: IdentityAdminDownloadPhotoRequest) -> None:
		self.identity_id: int = identity_admin_download_photo_request.identity_id

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityAdminDownloadPhotoRequest":
		return IdentityAdminDownloadPhotoRequest(identity_id=self.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminDownloadPhotoRequest) -> "IdentityAdminDownloadPhotoRequest":
		return IdentityAdminDownloadPhotoRequest(identity_id=native_message.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminDownloadPhotoRequest]) -> list["IdentityAdminDownloadPhotoRequest"]:
		return [IdentityAdminDownloadPhotoRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminDownloadPhotoRequest]) -> "IdentityAdminDownloadPhotoRequest":
		try:
			native_message = await promise
			return IdentityAdminDownloadPhotoRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityAdminDownloadPhotoRequest"]):
		if messages is None:
			return []
		return [IdentityAdminDownloadPhotoRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityAdminDownloadPhotoRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminDownloadPhotoRequest(identity_id=message.identity_id if message.identity_id else None)

	def __str__(self):
		s: str = ''
		if self.identity_id:
			s += f'identity_id: {self.identity_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityAdminDownloadPhotoRequest):
			return False
		return self.identity_id == other.identity_id

	def __bool__(self):
		return self.identity_id != 0

	def __hash__(self):
		return hash(self.identity_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityAdminDownloadPhotoRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identity_id == 0 or self.identity_id == expected.identity_id, "Invalid value: identity_id: " + str(expected.identity_id) + " != " + str(self.identity_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityAdminDownloadPhotoResponse:
	def __init__(self, photo: bytes = b""):
		self.photo: bytes = photo

	def _update_content(self, identity_admin_download_photo_response: IdentityAdminDownloadPhotoResponse) -> None:
		self.photo: bytes = identity_admin_download_photo_response.photo

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityAdminDownloadPhotoResponse":
		return IdentityAdminDownloadPhotoResponse(photo=self.photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminDownloadPhotoResponse) -> "IdentityAdminDownloadPhotoResponse":
		return IdentityAdminDownloadPhotoResponse(photo=native_message.photo)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminDownloadPhotoResponse]) -> list["IdentityAdminDownloadPhotoResponse"]:
		return [IdentityAdminDownloadPhotoResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminDownloadPhotoResponse]) -> "IdentityAdminDownloadPhotoResponse":
		try:
			native_message = await promise
			return IdentityAdminDownloadPhotoResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityAdminDownloadPhotoResponse"]):
		if messages is None:
			return []
		return [IdentityAdminDownloadPhotoResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityAdminDownloadPhotoResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminDownloadPhotoResponse(photo=message.photo if message.photo else None)

	def __str__(self):
		s: str = ''
		if self.photo:
			s += f'photo: {self.photo}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityAdminDownloadPhotoResponse):
			return False
		return self.photo == other.photo

	def __bool__(self):
		return self.photo != b""

	def __hash__(self):
		return hash(self.photo)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityAdminDownloadPhotoResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.photo == b"" or self.photo == expected.photo, "Invalid value: photo: " + str(expected.photo) + " != " + str(self.photo)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityNewRequest:
	def __init__(self, identity_details: "IdentityDetails" = None, server_url: str = ""):
		self.identity_details: IdentityDetails = identity_details
		self.server_url: str = server_url

	def _update_content(self, identity_new_request: IdentityNewRequest) -> None:
		self.identity_details: IdentityDetails = identity_new_request.identity_details
		self.server_url: str = identity_new_request.server_url

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityNewRequest":
		return IdentityNewRequest(identity_details=self.identity_details._clone(), server_url=self.server_url)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewRequest) -> "IdentityNewRequest":
		return IdentityNewRequest(identity_details=IdentityDetails._from_native(native_message.identity_details), server_url=native_message.server_url)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewRequest]) -> list["IdentityNewRequest"]:
		return [IdentityNewRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewRequest]) -> "IdentityNewRequest":
		try:
			native_message = await promise
			return IdentityNewRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityNewRequest"]):
		if messages is None:
			return []
		return [IdentityNewRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityNewRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewRequest(identity_details=IdentityDetails._to_native(message.identity_details if message.identity_details else None), server_url=message.server_url if message.server_url else None)

	def __str__(self):
		s: str = ''
		if self.identity_details:
			s += f'identity_details: ({self.identity_details}), '
		if self.server_url:
			s += f'server_url: {self.server_url}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityNewRequest):
			return False
		return self.identity_details == other.identity_details and self.server_url == other.server_url

	def __bool__(self):
		return bool(self.identity_details) or self.server_url != ""

	def __hash__(self):
		return hash((self.identity_details, self.server_url))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityNewRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity_details is None or self.identity_details._test_assertion(expected.identity_details)
		except AssertionError as e:
			raise AssertionError("identity_details: " + str(e))
		assert expected.server_url == "" or self.server_url == expected.server_url, "Invalid value: server_url: " + str(expected.server_url) + " != " + str(self.server_url)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityNewResponse:
	def __init__(self, identity: "Identity" = None):
		self.identity: Identity = identity

	def _update_content(self, identity_new_response: IdentityNewResponse) -> None:
		self.identity: Identity = identity_new_response.identity

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityNewResponse":
		return IdentityNewResponse(identity=self.identity._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewResponse) -> "IdentityNewResponse":
		return IdentityNewResponse(identity=Identity._from_native(native_message.identity))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewResponse]) -> list["IdentityNewResponse"]:
		return [IdentityNewResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewResponse]) -> "IdentityNewResponse":
		try:
			native_message = await promise
			return IdentityNewResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityNewResponse"]):
		if messages is None:
			return []
		return [IdentityNewResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityNewResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewResponse(identity=Identity._to_native(message.identity if message.identity else None))

	def __str__(self):
		s: str = ''
		if self.identity:
			s += f'identity: ({self.identity}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityNewResponse):
			return False
		return self.identity == other.identity

	def __bool__(self):
		return bool(self.identity)

	def __hash__(self):
		return hash(self.identity)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityNewResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity is None or self.identity._test_assertion(expected.identity)
		except AssertionError as e:
			raise AssertionError("identity: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityKeycloakNewRequest:
	def __init__(self, configuration_link: str = ""):
		self.configuration_link: str = configuration_link

	def _update_content(self, identity_keycloak_new_request: IdentityKeycloakNewRequest) -> None:
		self.configuration_link: str = identity_keycloak_new_request.configuration_link

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityKeycloakNewRequest":
		return IdentityKeycloakNewRequest(configuration_link=self.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewRequest) -> "IdentityKeycloakNewRequest":
		return IdentityKeycloakNewRequest(configuration_link=native_message.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewRequest]) -> list["IdentityKeycloakNewRequest"]:
		return [IdentityKeycloakNewRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewRequest]) -> "IdentityKeycloakNewRequest":
		try:
			native_message = await promise
			return IdentityKeycloakNewRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityKeycloakNewRequest"]):
		if messages is None:
			return []
		return [IdentityKeycloakNewRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityKeycloakNewRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewRequest(configuration_link=message.configuration_link if message.configuration_link else None)

	def __str__(self):
		s: str = ''
		if self.configuration_link:
			s += f'configuration_link: {self.configuration_link}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityKeycloakNewRequest):
			return False
		return self.configuration_link == other.configuration_link

	def __bool__(self):
		return self.configuration_link != ""

	def __hash__(self):
		return hash(self.configuration_link)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityKeycloakNewRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.configuration_link == "" or self.configuration_link == expected.configuration_link, "Invalid value: configuration_link: " + str(expected.configuration_link) + " != " + str(self.configuration_link)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityKeycloakNewResponse:
	def __init__(self, identity: "Identity" = None):
		self.identity: Identity = identity

	def _update_content(self, identity_keycloak_new_response: IdentityKeycloakNewResponse) -> None:
		self.identity: Identity = identity_keycloak_new_response.identity

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityKeycloakNewResponse":
		return IdentityKeycloakNewResponse(identity=self.identity._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewResponse) -> "IdentityKeycloakNewResponse":
		return IdentityKeycloakNewResponse(identity=Identity._from_native(native_message.identity))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewResponse]) -> list["IdentityKeycloakNewResponse"]:
		return [IdentityKeycloakNewResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewResponse]) -> "IdentityKeycloakNewResponse":
		try:
			native_message = await promise
			return IdentityKeycloakNewResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityKeycloakNewResponse"]):
		if messages is None:
			return []
		return [IdentityKeycloakNewResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityKeycloakNewResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewResponse(identity=Identity._to_native(message.identity if message.identity else None))

	def __str__(self):
		s: str = ''
		if self.identity:
			s += f'identity: ({self.identity}), '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityKeycloakNewResponse):
			return False
		return self.identity == other.identity

	def __bool__(self):
		return bool(self.identity)

	def __hash__(self):
		return hash(self.identity)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityKeycloakNewResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		try:
			assert expected.identity is None or self.identity._test_assertion(expected.identity)
		except AssertionError as e:
			raise AssertionError("identity: " + str(e))
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityDeleteRequest:
	def __init__(self, identity_id: int = 0, delete_everywhere: bool = False):
		self.identity_id: int = identity_id
		self.delete_everywhere: bool = delete_everywhere

	def _update_content(self, identity_delete_request: IdentityDeleteRequest) -> None:
		self.identity_id: int = identity_delete_request.identity_id
		self.delete_everywhere: bool = identity_delete_request.delete_everywhere

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityDeleteRequest":
		return IdentityDeleteRequest(identity_id=self.identity_id, delete_everywhere=self.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteRequest) -> "IdentityDeleteRequest":
		return IdentityDeleteRequest(identity_id=native_message.identity_id, delete_everywhere=native_message.delete_everywhere)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteRequest]) -> list["IdentityDeleteRequest"]:
		return [IdentityDeleteRequest._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteRequest]) -> "IdentityDeleteRequest":
		try:
			native_message = await promise
			return IdentityDeleteRequest._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityDeleteRequest"]):
		if messages is None:
			return []
		return [IdentityDeleteRequest._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityDeleteRequest"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteRequest(identity_id=message.identity_id if message.identity_id else None, delete_everywhere=message.delete_everywhere if message.delete_everywhere else None)

	def __str__(self):
		s: str = ''
		if self.identity_id:
			s += f'identity_id: {self.identity_id}, '
		if self.delete_everywhere:
			s += f'delete_everywhere: {self.delete_everywhere}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityDeleteRequest):
			return False
		return self.identity_id == other.identity_id and self.delete_everywhere == other.delete_everywhere

	def __bool__(self):
		return self.identity_id != 0 or self.delete_everywhere

	def __hash__(self):
		return hash((self.identity_id, self.delete_everywhere))

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityDeleteRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identity_id == 0 or self.identity_id == expected.identity_id, "Invalid value: identity_id: " + str(expected.identity_id) + " != " + str(self.identity_id)
		assert expected.delete_everywhere is False or self.delete_everywhere == expected.delete_everywhere, "Invalid value: delete_everywhere: " + str(expected.delete_everywhere) + " != " + str(self.delete_everywhere)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityDeleteResponse:
	def __init__(self):
		pass

	def _update_content(self, identity_delete_response: IdentityDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityDeleteResponse":
		return IdentityDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteResponse) -> "IdentityDeleteResponse":
		return IdentityDeleteResponse()

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteResponse]) -> list["IdentityDeleteResponse"]:
		return [IdentityDeleteResponse._from_native(native_message) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember,PyTypeHints
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteResponse]) -> "IdentityDeleteResponse":
		try:
			native_message = await promise
			return IdentityDeleteResponse._from_native(native_message)
		except errors.AioRpcError as error:
			raise errors.OlvidError._from_aio_rpc_error(error) from error

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native_list(messages: list["IdentityDeleteResponse"]):
		if messages is None:
			return []
		return [IdentityDeleteResponse._to_native(message) for message in messages]

	# noinspection PyUnresolvedReferences,PyProtectedMember
	@staticmethod
	def _to_native(message: Optional["IdentityDeleteResponse"]):
		if message is None:
			return None
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteResponse()

	def __str__(self):
		s: str = ''
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityDeleteResponse):
			return False
		return True

	def __bool__(self):
		return False

	def __hash__(self):
		return hash(())

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityDeleteResponse):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)

		return True


class ClientKeyAdminServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.admin_service_pb2_grpc.ClientKeyAdminServiceStub = olvid.daemon.services.v1.admin_service_pb2_grpc.ClientKeyAdminServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def client_key_list(self, client_key_list_request: ClientKeyListRequest) -> AsyncIterator[ClientKeyListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListResponse]) -> AsyncIterator[ClientKeyListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield ClientKeyListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = client_key_list_request
			return response_iterator(self.__stub.ClientKeyList(olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListRequest(filter=ClientKeyFilter._to_native(overlay_object.filter)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def client_key_get(self, client_key_get_request: ClientKeyGetRequest) -> Coroutine[Any, Any, ClientKeyGetResponse]:
		try:
			overlay_object = client_key_get_request
			return ClientKeyGetResponse._from_native_promise(self.__stub.ClientKeyGet(olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetRequest(client_key=overlay_object.client_key), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def client_key_new(self, client_key_new_request: ClientKeyNewRequest) -> Coroutine[Any, Any, ClientKeyNewResponse]:
		try:
			overlay_object = client_key_new_request
			return ClientKeyNewResponse._from_native_promise(self.__stub.ClientKeyNew(olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewRequest(name=overlay_object.name, identity_id=overlay_object.identity_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def client_key_delete(self, client_key_delete_request: ClientKeyDeleteRequest) -> Coroutine[Any, Any, ClientKeyDeleteResponse]:
		try:
			overlay_object = client_key_delete_request
			return ClientKeyDeleteResponse._from_native_promise(self.__stub.ClientKeyDelete(olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteRequest(client_key=overlay_object.client_key), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class IdentityAdminServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.admin_service_pb2_grpc.IdentityAdminServiceStub = olvid.daemon.services.v1.admin_service_pb2_grpc.IdentityAdminServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_list(self, identity_list_request: IdentityListRequest) -> AsyncIterator[IdentityListResponse]:
		try:
			# noinspection PyUnresolvedReferences,PyProtectedMember,PyTypeHints
			async def response_iterator(iterator: AsyncIterator[olvid.daemon.admin.v1.identity_admin_pb2.IdentityListResponse]) -> AsyncIterator[IdentityListResponse]:
				try:
					async for native_message in iterator.__aiter__():
						yield IdentityListResponse._from_native(native_message)
				except errors.AioRpcError as er:
					raise errors.OlvidError._from_aio_rpc_error(er) from er
			overlay_object = identity_list_request
			return response_iterator(self.__stub.IdentityList(olvid.daemon.admin.v1.identity_admin_pb2.IdentityListRequest(filter=IdentityFilter._to_native(overlay_object.filter)), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_admin_get(self, identity_admin_get_request: IdentityAdminGetRequest) -> Coroutine[Any, Any, IdentityAdminGetResponse]:
		try:
			overlay_object = identity_admin_get_request
			return IdentityAdminGetResponse._from_native_promise(self.__stub.IdentityAdminGet(olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetRequest(identity_id=overlay_object.identity_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_admin_get_bytes_identifier(self, identity_admin_get_bytes_identifier_request: IdentityAdminGetBytesIdentifierRequest) -> Coroutine[Any, Any, IdentityAdminGetBytesIdentifierResponse]:
		try:
			overlay_object = identity_admin_get_bytes_identifier_request
			return IdentityAdminGetBytesIdentifierResponse._from_native_promise(self.__stub.IdentityAdminGetBytesIdentifier(olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetBytesIdentifierRequest(identity_id=overlay_object.identity_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_admin_get_invitation_link(self, identity_admin_get_invitation_link_request: IdentityAdminGetInvitationLinkRequest) -> Coroutine[Any, Any, IdentityAdminGetInvitationLinkResponse]:
		try:
			overlay_object = identity_admin_get_invitation_link_request
			return IdentityAdminGetInvitationLinkResponse._from_native_promise(self.__stub.IdentityAdminGetInvitationLink(olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetInvitationLinkRequest(identity_id=overlay_object.identity_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_admin_download_photo(self, identity_admin_download_photo_request: IdentityAdminDownloadPhotoRequest) -> Coroutine[Any, Any, IdentityAdminDownloadPhotoResponse]:
		try:
			overlay_object = identity_admin_download_photo_request
			return IdentityAdminDownloadPhotoResponse._from_native_promise(self.__stub.IdentityAdminDownloadPhoto(olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminDownloadPhotoRequest(identity_id=overlay_object.identity_id), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_delete(self, identity_delete_request: IdentityDeleteRequest) -> Coroutine[Any, Any, IdentityDeleteResponse]:
		try:
			overlay_object = identity_delete_request
			return IdentityDeleteResponse._from_native_promise(self.__stub.IdentityDelete(olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteRequest(identity_id=overlay_object.identity_id, delete_everywhere=overlay_object.delete_everywhere), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_new(self, identity_new_request: IdentityNewRequest) -> Coroutine[Any, Any, IdentityNewResponse]:
		try:
			overlay_object = identity_new_request
			return IdentityNewResponse._from_native_promise(self.__stub.IdentityNew(olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewRequest(identity_details=IdentityDetails._to_native(overlay_object.identity_details), server_url=overlay_object.server_url), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_keycloak_new(self, identity_keycloak_new_request: IdentityKeycloakNewRequest) -> Coroutine[Any, Any, IdentityKeycloakNewResponse]:
		try:
			overlay_object = identity_keycloak_new_request
			return IdentityKeycloakNewResponse._from_native_promise(self.__stub.IdentityKeycloakNew(olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewRequest(configuration_link=overlay_object.configuration_link), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e


class BackupAdminServiceStub:
	def __init__(self, get_grpc_metadata: Callable[[], list[tuple[str, str]]], channel: Channel):
		self.__stub: olvid.daemon.services.v1.admin_service_pb2_grpc.BackupAdminServiceStub = olvid.daemon.services.v1.admin_service_pb2_grpc.BackupAdminServiceStub(channel=channel)
		self.__get_grpc_metadata: Callable[[], list[tuple[str, str]]] = get_grpc_metadata

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def backup_key_get(self, backup_key_get_request: BackupKeyGetRequest) -> Coroutine[Any, Any, BackupKeyGetResponse]:
		try:
			overlay_object = backup_key_get_request
			return BackupKeyGetResponse._from_native_promise(self.__stub.BackupKeyGet(olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyGetRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def backup_key_renew(self, backup_key_renew_request: BackupKeyRenewRequest) -> Coroutine[Any, Any, BackupKeyRenewResponse]:
		try:
			overlay_object = backup_key_renew_request
			return BackupKeyRenewResponse._from_native_promise(self.__stub.BackupKeyRenew(olvid.daemon.admin.v1.backup_admin_pb2.BackupKeyRenewRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def backup_get(self, backup_get_request: BackupGetRequest) -> Coroutine[Any, Any, BackupGetResponse]:
		try:
			overlay_object = backup_get_request
			return BackupGetResponse._from_native_promise(self.__stub.BackupGet(olvid.daemon.admin.v1.backup_admin_pb2.BackupGetRequest(backup_key=overlay_object.backup_key), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def backup_now(self, backup_now_request: BackupNowRequest) -> Coroutine[Any, Any, BackupNowResponse]:
		try:
			overlay_object = backup_now_request
			return BackupNowResponse._from_native_promise(self.__stub.BackupNow(olvid.daemon.admin.v1.backup_admin_pb2.BackupNowRequest(), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def backup_restore_daemon(self, backup_restore_daemon_request: BackupRestoreDaemonRequest) -> Coroutine[Any, Any, BackupRestoreDaemonResponse]:
		try:
			overlay_object = backup_restore_daemon_request
			return BackupRestoreDaemonResponse._from_native_promise(self.__stub.BackupRestoreDaemon(olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreDaemonRequest(backup_key=overlay_object.backup_key, new_device_name=overlay_object.new_device_name), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def backup_restore_admin_backup(self, backup_restore_admin_backup_request: BackupRestoreAdminBackupRequest) -> Coroutine[Any, Any, BackupRestoreAdminBackupResponse]:
		try:
			overlay_object = backup_restore_admin_backup_request
			return BackupRestoreAdminBackupResponse._from_native_promise(self.__stub.BackupRestoreAdminBackup(olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreAdminBackupRequest(backup_key=overlay_object.backup_key), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def backup_restore_profile_snapshot(self, backup_restore_profile_snapshot_request: BackupRestoreProfileSnapshotRequest) -> Coroutine[Any, Any, BackupRestoreProfileSnapshotResponse]:
		try:
			overlay_object = backup_restore_profile_snapshot_request
			return BackupRestoreProfileSnapshotResponse._from_native_promise(self.__stub.BackupRestoreProfileSnapshot(olvid.daemon.admin.v1.backup_admin_pb2.BackupRestoreProfileSnapshotRequest(backup_key=overlay_object.backup_key, id=overlay_object.id, new_device_name=overlay_object.new_device_name), metadata=self.__get_grpc_metadata()))
		except errors.AioRpcError as e:
			raise errors.OlvidError._from_aio_rpc_error(e) from e
