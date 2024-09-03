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
class ClientKeyListRequest:
	def __init__(self, client: OlvidClient = None, filter: "ClientKeyFilter" = None):
		self._client: OlvidClient = client
		self.filter: ClientKeyFilter = filter

	def _update_content(self, client_key_list_request: ClientKeyListRequest) -> None:
		self.filter: ClientKeyFilter = client_key_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyListRequest":
		return ClientKeyListRequest(client=self._client, filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListRequest, client: OlvidClient = None) -> "ClientKeyListRequest":
		return ClientKeyListRequest(client, filter=ClientKeyFilter._from_native(native_message.filter, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListRequest], client: OlvidClient = None) -> list["ClientKeyListRequest"]:
		return [ClientKeyListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListRequest], client: OlvidClient = None) -> "ClientKeyListRequest":
		native_message = await promise
		return ClientKeyListRequest._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None, client_keys: "list[ClientKey]" = None):
		self._client: OlvidClient = client
		self.client_keys: list[ClientKey] = client_keys

	def _update_content(self, client_key_list_response: ClientKeyListResponse) -> None:
		self.client_keys: list[ClientKey] = client_key_list_response.client_keys

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyListResponse":
		return ClientKeyListResponse(client=self._client, client_keys=[e._clone() for e in self.client_keys])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListResponse, client: OlvidClient = None) -> "ClientKeyListResponse":
		return ClientKeyListResponse(client, client_keys=ClientKey._from_native_list(native_message.client_keys, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListResponse], client: OlvidClient = None) -> list["ClientKeyListResponse"]:
		return [ClientKeyListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListResponse], client: OlvidClient = None) -> "ClientKeyListResponse":
		native_message = await promise
		return ClientKeyListResponse._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None, client_key: str = ""):
		self._client: OlvidClient = client
		self.client_key: str = client_key

	def _update_content(self, client_key_get_request: ClientKeyGetRequest) -> None:
		self.client_key: str = client_key_get_request.client_key

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyGetRequest":
		return ClientKeyGetRequest(client=self._client, client_key=self.client_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetRequest, client: OlvidClient = None) -> "ClientKeyGetRequest":
		return ClientKeyGetRequest(client, client_key=native_message.client_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetRequest], client: OlvidClient = None) -> list["ClientKeyGetRequest"]:
		return [ClientKeyGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetRequest], client: OlvidClient = None) -> "ClientKeyGetRequest":
		native_message = await promise
		return ClientKeyGetRequest._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None, client_key: "ClientKey" = None):
		self._client: OlvidClient = client
		self.client_key: ClientKey = client_key

	def _update_content(self, client_key_get_response: ClientKeyGetResponse) -> None:
		self.client_key: ClientKey = client_key_get_response.client_key

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyGetResponse":
		return ClientKeyGetResponse(client=self._client, client_key=self.client_key._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetResponse, client: OlvidClient = None) -> "ClientKeyGetResponse":
		return ClientKeyGetResponse(client, client_key=ClientKey._from_native(native_message.client_key, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetResponse], client: OlvidClient = None) -> list["ClientKeyGetResponse"]:
		return [ClientKeyGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetResponse], client: OlvidClient = None) -> "ClientKeyGetResponse":
		native_message = await promise
		return ClientKeyGetResponse._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None, name: str = "", identity_id: int = 0):
		self._client: OlvidClient = client
		self.name: str = name
		self.identity_id: int = identity_id

	def _update_content(self, client_key_new_request: ClientKeyNewRequest) -> None:
		self.name: str = client_key_new_request.name
		self.identity_id: int = client_key_new_request.identity_id

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyNewRequest":
		return ClientKeyNewRequest(client=self._client, name=self.name, identity_id=self.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewRequest, client: OlvidClient = None) -> "ClientKeyNewRequest":
		return ClientKeyNewRequest(client, name=native_message.name, identity_id=native_message.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewRequest], client: OlvidClient = None) -> list["ClientKeyNewRequest"]:
		return [ClientKeyNewRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewRequest], client: OlvidClient = None) -> "ClientKeyNewRequest":
		native_message = await promise
		return ClientKeyNewRequest._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None, client_key: "ClientKey" = None):
		self._client: OlvidClient = client
		self.client_key: ClientKey = client_key

	def _update_content(self, client_key_new_response: ClientKeyNewResponse) -> None:
		self.client_key: ClientKey = client_key_new_response.client_key

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyNewResponse":
		return ClientKeyNewResponse(client=self._client, client_key=self.client_key._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewResponse, client: OlvidClient = None) -> "ClientKeyNewResponse":
		return ClientKeyNewResponse(client, client_key=ClientKey._from_native(native_message.client_key, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewResponse], client: OlvidClient = None) -> list["ClientKeyNewResponse"]:
		return [ClientKeyNewResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewResponse], client: OlvidClient = None) -> "ClientKeyNewResponse":
		native_message = await promise
		return ClientKeyNewResponse._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None, client_key: str = ""):
		self._client: OlvidClient = client
		self.client_key: str = client_key

	def _update_content(self, client_key_delete_request: ClientKeyDeleteRequest) -> None:
		self.client_key: str = client_key_delete_request.client_key

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyDeleteRequest":
		return ClientKeyDeleteRequest(client=self._client, client_key=self.client_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteRequest, client: OlvidClient = None) -> "ClientKeyDeleteRequest":
		return ClientKeyDeleteRequest(client, client_key=native_message.client_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteRequest], client: OlvidClient = None) -> list["ClientKeyDeleteRequest"]:
		return [ClientKeyDeleteRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteRequest], client: OlvidClient = None) -> "ClientKeyDeleteRequest":
		native_message = await promise
		return ClientKeyDeleteRequest._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, client_key_delete_response: ClientKeyDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "ClientKeyDeleteResponse":
		return ClientKeyDeleteResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteResponse, client: OlvidClient = None) -> "ClientKeyDeleteResponse":
		return ClientKeyDeleteResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteResponse], client: OlvidClient = None) -> list["ClientKeyDeleteResponse"]:
		return [ClientKeyDeleteResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteResponse], client: OlvidClient = None) -> "ClientKeyDeleteResponse":
		native_message = await promise
		return ClientKeyDeleteResponse._from_native(native_message, client=client)

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
		return 

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
	def __init__(self, client: OlvidClient = None, filter: "IdentityFilter" = None):
		self._client: OlvidClient = client
		self.filter: IdentityFilter = filter

	def _update_content(self, identity_list_request: IdentityListRequest) -> None:
		self.filter: IdentityFilter = identity_list_request.filter

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityListRequest":
		return IdentityListRequest(client=self._client, filter=self.filter._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityListRequest, client: OlvidClient = None) -> "IdentityListRequest":
		return IdentityListRequest(client, filter=IdentityFilter._from_native(native_message.filter, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityListRequest], client: OlvidClient = None) -> list["IdentityListRequest"]:
		return [IdentityListRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityListRequest], client: OlvidClient = None) -> "IdentityListRequest":
		native_message = await promise
		return IdentityListRequest._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None, identities: "list[Identity]" = None):
		self._client: OlvidClient = client
		self.identities: list[Identity] = identities

	def _update_content(self, identity_list_response: IdentityListResponse) -> None:
		self.identities: list[Identity] = identity_list_response.identities

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityListResponse":
		return IdentityListResponse(client=self._client, identities=[e._clone() for e in self.identities])

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityListResponse, client: OlvidClient = None) -> "IdentityListResponse":
		return IdentityListResponse(client, identities=Identity._from_native_list(native_message.identities, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityListResponse], client: OlvidClient = None) -> list["IdentityListResponse"]:
		return [IdentityListResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityListResponse], client: OlvidClient = None) -> "IdentityListResponse":
		native_message = await promise
		return IdentityListResponse._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None, identity_id: int = 0):
		self._client: OlvidClient = client
		self.identity_id: int = identity_id

	def _update_content(self, identity_admin_get_request: IdentityAdminGetRequest) -> None:
		self.identity_id: int = identity_admin_get_request.identity_id

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityAdminGetRequest":
		return IdentityAdminGetRequest(client=self._client, identity_id=self.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetRequest, client: OlvidClient = None) -> "IdentityAdminGetRequest":
		return IdentityAdminGetRequest(client, identity_id=native_message.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetRequest], client: OlvidClient = None) -> list["IdentityAdminGetRequest"]:
		return [IdentityAdminGetRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetRequest], client: OlvidClient = None) -> "IdentityAdminGetRequest":
		native_message = await promise
		return IdentityAdminGetRequest._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None, identity: "Identity" = None):
		self._client: OlvidClient = client
		self.identity: Identity = identity

	def _update_content(self, identity_admin_get_response: IdentityAdminGetResponse) -> None:
		self.identity: Identity = identity_admin_get_response.identity

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityAdminGetResponse":
		return IdentityAdminGetResponse(client=self._client, identity=self.identity._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetResponse, client: OlvidClient = None) -> "IdentityAdminGetResponse":
		return IdentityAdminGetResponse(client, identity=Identity._from_native(native_message.identity, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetResponse], client: OlvidClient = None) -> list["IdentityAdminGetResponse"]:
		return [IdentityAdminGetResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetResponse], client: OlvidClient = None) -> "IdentityAdminGetResponse":
		native_message = await promise
		return IdentityAdminGetResponse._from_native(native_message, client=client)

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
class IdentityNewRequest:
	def __init__(self, client: OlvidClient = None, identity_details: "IdentityDetails" = None, server_url: str = "", api_key: str = ""):
		self._client: OlvidClient = client
		self.identity_details: IdentityDetails = identity_details
		self.server_url: str = server_url
		self.api_key: str = api_key

	def _update_content(self, identity_new_request: IdentityNewRequest) -> None:
		self.identity_details: IdentityDetails = identity_new_request.identity_details
		self.server_url: str = identity_new_request.server_url
		self.api_key: str = identity_new_request.api_key

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityNewRequest":
		return IdentityNewRequest(client=self._client, identity_details=self.identity_details._clone(), server_url=self.server_url, api_key=self.api_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewRequest, client: OlvidClient = None) -> "IdentityNewRequest":
		return IdentityNewRequest(client, identity_details=IdentityDetails._from_native(native_message.identity_details, client=client), server_url=native_message.server_url, api_key=native_message.api_key)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewRequest], client: OlvidClient = None) -> list["IdentityNewRequest"]:
		return [IdentityNewRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewRequest], client: OlvidClient = None) -> "IdentityNewRequest":
		native_message = await promise
		return IdentityNewRequest._from_native(native_message, client=client)

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
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewRequest(identity_details=IdentityDetails._to_native(message.identity_details if message.identity_details else None), server_url=message.server_url if message.server_url else None, api_key=message.api_key if message.api_key else None)

	def __str__(self):
		s: str = ''
		if self.identity_details:
			s += f'identity_details: ({self.identity_details}), '
		if self.server_url:
			s += f'server_url: {self.server_url}, '
		if self.api_key:
			s += f'api_key: {self.api_key}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityNewRequest):
			return False
		return self.identity_details == other.identity_details and self.server_url == other.server_url and self.api_key == other.api_key

	def __bool__(self):
		return bool(self.identity_details) or self.server_url != "" or self.api_key != ""

	def __hash__(self):
		return hash((self.identity_details, self.server_url, self.api_key))

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
		assert expected.api_key == "" or self.api_key == expected.api_key, "Invalid value: api_key: " + str(expected.api_key) + " != " + str(self.api_key)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityNewResponse:
	def __init__(self, client: OlvidClient = None, identity: "Identity" = None):
		self._client: OlvidClient = client
		self.identity: Identity = identity

	def _update_content(self, identity_new_response: IdentityNewResponse) -> None:
		self.identity: Identity = identity_new_response.identity

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityNewResponse":
		return IdentityNewResponse(client=self._client, identity=self.identity._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewResponse, client: OlvidClient = None) -> "IdentityNewResponse":
		return IdentityNewResponse(client, identity=Identity._from_native(native_message.identity, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewResponse], client: OlvidClient = None) -> list["IdentityNewResponse"]:
		return [IdentityNewResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewResponse], client: OlvidClient = None) -> "IdentityNewResponse":
		native_message = await promise
		return IdentityNewResponse._from_native(native_message, client=client)

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
class IdentityDeleteRequest:
	def __init__(self, client: OlvidClient = None, identity_id: int = 0):
		self._client: OlvidClient = client
		self.identity_id: int = identity_id

	def _update_content(self, identity_delete_request: IdentityDeleteRequest) -> None:
		self.identity_id: int = identity_delete_request.identity_id

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityDeleteRequest":
		return IdentityDeleteRequest(client=self._client, identity_id=self.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteRequest, client: OlvidClient = None) -> "IdentityDeleteRequest":
		return IdentityDeleteRequest(client, identity_id=native_message.identity_id)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteRequest], client: OlvidClient = None) -> list["IdentityDeleteRequest"]:
		return [IdentityDeleteRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteRequest], client: OlvidClient = None) -> "IdentityDeleteRequest":
		native_message = await promise
		return IdentityDeleteRequest._from_native(native_message, client=client)

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
		return olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteRequest(identity_id=message.identity_id if message.identity_id else None)

	def __str__(self):
		s: str = ''
		if self.identity_id:
			s += f'identity_id: {self.identity_id}, '
		return s.removesuffix(', ')

	def __eq__(self, other):
		if not isinstance(other, IdentityDeleteRequest):
			return False
		return self.identity_id == other.identity_id

	def __bool__(self):
		return self.identity_id != 0

	def __hash__(self):
		return hash(self.identity_id)

	# For tests routines
	# noinspection DuplicatedCode,PyProtectedMember
	def _test_assertion(self, expected):
		if not isinstance(expected, IdentityDeleteRequest):
			assert False, "Invalid type: " + str(type(expected).__name__) + " != " + str(type(self).__name__)
		assert expected.identity_id == 0 or self.identity_id == expected.identity_id, "Invalid value: identity_id: " + str(expected.identity_id) + " != " + str(self.identity_id)
		return True


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityDeleteResponse:
	def __init__(self, client: OlvidClient = None):
		self._client: OlvidClient = client

	def _update_content(self, identity_delete_response: IdentityDeleteResponse) -> None:
		pass

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityDeleteResponse":
		return IdentityDeleteResponse(client=self._client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteResponse, client: OlvidClient = None) -> "IdentityDeleteResponse":
		return IdentityDeleteResponse(client)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteResponse], client: OlvidClient = None) -> list["IdentityDeleteResponse"]:
		return [IdentityDeleteResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteResponse], client: OlvidClient = None) -> "IdentityDeleteResponse":
		native_message = await promise
		return IdentityDeleteResponse._from_native(native_message, client=client)

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
		return 

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


# noinspection PyProtectedMember,PyShadowingBuiltins
class IdentityKeycloakNewRequest:
	def __init__(self, client: OlvidClient = None, configuration_link: str = ""):
		self._client: OlvidClient = client
		self.configuration_link: str = configuration_link

	def _update_content(self, identity_keycloak_new_request: IdentityKeycloakNewRequest) -> None:
		self.configuration_link: str = identity_keycloak_new_request.configuration_link

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityKeycloakNewRequest":
		return IdentityKeycloakNewRequest(client=self._client, configuration_link=self.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewRequest, client: OlvidClient = None) -> "IdentityKeycloakNewRequest":
		return IdentityKeycloakNewRequest(client, configuration_link=native_message.configuration_link)

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewRequest], client: OlvidClient = None) -> list["IdentityKeycloakNewRequest"]:
		return [IdentityKeycloakNewRequest._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewRequest], client: OlvidClient = None) -> "IdentityKeycloakNewRequest":
		native_message = await promise
		return IdentityKeycloakNewRequest._from_native(native_message, client=client)

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
	def __init__(self, client: OlvidClient = None, identity: "Identity" = None):
		self._client: OlvidClient = client
		self.identity: Identity = identity

	def _update_content(self, identity_keycloak_new_response: IdentityKeycloakNewResponse) -> None:
		self.identity: Identity = identity_keycloak_new_response.identity

	# noinspection PyProtectedMember
	def _clone(self) -> "IdentityKeycloakNewResponse":
		return IdentityKeycloakNewResponse(client=self._client, identity=self.identity._clone())

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native(native_message: olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewResponse, client: OlvidClient = None) -> "IdentityKeycloakNewResponse":
		return IdentityKeycloakNewResponse(client, identity=Identity._from_native(native_message.identity, client=client))

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	def _from_native_list(native_message_list: list[olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewResponse], client: OlvidClient = None) -> list["IdentityKeycloakNewResponse"]:
		return [IdentityKeycloakNewResponse._from_native(native_message, client=client) for native_message in native_message_list]

	# noinspection PyUnresolvedReferences,PyUnusedLocal,PyProtectedMember
	@staticmethod
	async def _from_native_promise(promise: Coroutine[Any, Any, olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewResponse], client: OlvidClient = None) -> "IdentityKeycloakNewResponse":
		native_message = await promise
		return IdentityKeycloakNewResponse._from_native(native_message, client=client)

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


class ClientKeyAdminServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.admin_service_pb2_grpc.ClientKeyAdminServiceStub = olvid.daemon.services.v1.admin_service_pb2_grpc.ClientKeyAdminServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def client_key_list(self, client_key_list_request: ClientKeyListRequest) -> AsyncIterator[ClientKeyListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListResponse]) -> AsyncIterator[ClientKeyListResponse]:
			async for native_message in iterator.__aiter__():
				yield ClientKeyListResponse._from_native(native_message, client=self._client)
		overlay_object = client_key_list_request
		return response_iterator(self.__stub.ClientKeyList(olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyListRequest(filter=ClientKeyFilter._to_native(overlay_object.filter)), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def client_key_get(self, client_key_get_request: ClientKeyGetRequest) -> Coroutine[Any, Any, ClientKeyGetResponse]:
		overlay_object = client_key_get_request
		return ClientKeyGetResponse._from_native_promise(self.__stub.ClientKeyGet(olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyGetRequest(client_key=overlay_object.client_key), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def client_key_new(self, client_key_new_request: ClientKeyNewRequest) -> Coroutine[Any, Any, ClientKeyNewResponse]:
		overlay_object = client_key_new_request
		return ClientKeyNewResponse._from_native_promise(self.__stub.ClientKeyNew(olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyNewRequest(name=overlay_object.name, identity_id=overlay_object.identity_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def client_key_delete(self, client_key_delete_request: ClientKeyDeleteRequest) -> Coroutine[Any, Any, ClientKeyDeleteResponse]:
		overlay_object = client_key_delete_request
		return ClientKeyDeleteResponse._from_native_promise(self.__stub.ClientKeyDelete(olvid.daemon.admin.v1.client_key_admin_pb2.ClientKeyDeleteRequest(client_key=overlay_object.client_key), metadata=self._client.grpc_metadata), client=self._client)


class IdentityAdminServiceStub:
	def __init__(self, client: OlvidClient, channel: grpc.Channel):
		self.__stub: olvid.daemon.services.v1.admin_service_pb2_grpc.IdentityAdminServiceStub = olvid.daemon.services.v1.admin_service_pb2_grpc.IdentityAdminServiceStub(channel=channel)
		self._client: OlvidClient = client

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_list(self, identity_list_request: IdentityListRequest) -> AsyncIterator[IdentityListResponse]:
		# noinspection PyUnresolvedReferences,PyProtectedMember
		async def response_iterator(iterator: AsyncIterator[olvid.daemon.admin.v1.identity_admin_pb2.IdentityListResponse]) -> AsyncIterator[IdentityListResponse]:
			async for native_message in iterator.__aiter__():
				yield IdentityListResponse._from_native(native_message, client=self._client)
		overlay_object = identity_list_request
		return response_iterator(self.__stub.IdentityList(olvid.daemon.admin.v1.identity_admin_pb2.IdentityListRequest(filter=IdentityFilter._to_native(overlay_object.filter)), metadata=self._client.grpc_metadata))

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_admin_get(self, identity_admin_get_request: IdentityAdminGetRequest) -> Coroutine[Any, Any, IdentityAdminGetResponse]:
		overlay_object = identity_admin_get_request
		return IdentityAdminGetResponse._from_native_promise(self.__stub.IdentityAdminGet(olvid.daemon.admin.v1.identity_admin_pb2.IdentityAdminGetRequest(identity_id=overlay_object.identity_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_delete(self, identity_delete_request: IdentityDeleteRequest) -> Coroutine[Any, Any, IdentityDeleteResponse]:
		overlay_object = identity_delete_request
		return IdentityDeleteResponse._from_native_promise(self.__stub.IdentityDelete(olvid.daemon.admin.v1.identity_admin_pb2.IdentityDeleteRequest(identity_id=overlay_object.identity_id), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_new(self, identity_new_request: IdentityNewRequest) -> Coroutine[Any, Any, IdentityNewResponse]:
		overlay_object = identity_new_request
		return IdentityNewResponse._from_native_promise(self.__stub.IdentityNew(olvid.daemon.admin.v1.identity_admin_pb2.IdentityNewRequest(identity_details=IdentityDetails._to_native(overlay_object.identity_details), server_url=overlay_object.server_url, api_key=overlay_object.api_key), metadata=self._client.grpc_metadata), client=self._client)

	# noinspection PyUnresolvedReferences,PyProtectedMember,PyUnusedLocal
	def identity_keycloak_new(self, identity_keycloak_new_request: IdentityKeycloakNewRequest) -> Coroutine[Any, Any, IdentityKeycloakNewResponse]:
		overlay_object = identity_keycloak_new_request
		return IdentityKeycloakNewResponse._from_native_promise(self.__stub.IdentityKeycloakNew(olvid.daemon.admin.v1.identity_admin_pb2.IdentityKeycloakNewRequest(configuration_link=overlay_object.configuration_link), metadata=self._client.grpc_metadata), client=self._client)
