from typing import Optional, AsyncIterator

from .OlvidClient import OlvidClient
from .. import datatypes
from ..internal import admin

from .logger import command_logger


class OlvidAdminClient(OlvidClient):
	"""
	OlvidAdminClient: OlvidClient extended to add access to gRPC admin methods.

	As OlvidAdminClient extends OlvidClient it has the same constraints, for example it needs to find a valid client_key to
	connect to a daemon (see OlvidClient for more information).
	An admin client needs to use an admin_client_key (a key not associated to an identity, with an identity_id equal to 0).
	It uses same mechanism as OlvidBot to look for an admin client key except that the key file is named *.admin_client_key*
	and environment variable name is OLVID_ADMIN_CLIENT_KEY.

	As in OlvidClient OlvidAdminClient implements gRPC methods as python methods.
	You can find methods using the same name as in gRPC but using snake case.

	If an admin client wants to use normal command and notification api you will need to specify the identity you want to use.
	Use the current_identity_id property to specify the identity you want to use. It will persist for any future api call.
	"""
	_KEY_ENV_VARIABLE_NAME = "OLVID_ADMIN_CLIENT_KEY"
	_KEY_FILE_PATH = ".admin_client_key"

	def __init__(self, identity_id: int, client_key: Optional[str] = None, server_target: Optional[str] = None, parent_client: Optional['OlvidClient'] = None):
		try:
			super().__init__(client_key, server_target, parent_client)
		except ValueError:
			raise ValueError("Admin client key not found")

		# overwrite parent client type
		self._parent_client: Optional["OlvidAdminClient"] = parent_client

		# admin client need to specify an identity id in all requests metadata
		self._current_identity_id: int = identity_id

		# generate admin stubs
		self._stubs.create_admin_stubs()

	#####
	# current identity property
	#####
	@property
	def current_identity_id(self) -> int:
		return self._current_identity_id

	@current_identity_id.setter
	def current_identity_id(self, identity_id: int) -> None:
		self._current_identity_id = identity_id

	async def get_current_identity_details(self) -> Optional[datatypes.IdentityDetails]:
		return (await self.admin_identity_admin_get(identity_id=self._current_identity_id)).details

	#####
	# override grpc metadata property, to add identity id
	#####
	@property
	def grpc_metadata(self) -> list[tuple[str, str]]:
		return [
			("daemon-client-key", self._client_key),
			("daemon-identity-id", str(self.current_identity_id))
		]

	####################################################################################################################
	##### WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_olvid_client_code.py
	####################################################################################################################
	# ClientKeyAdminService
	def admin_client_key_list(self, filter: datatypes.ClientKeyFilter = None) -> AsyncIterator[datatypes.ClientKey]:
		command_logger.info(f'{self.__class__.__name__}: command: ClientKeyList')
	
		async def iterator(message_iterator: AsyncIterator[admin.ClientKeyListResponse]) -> AsyncIterator[datatypes.ClientKey]:
			async for message in message_iterator:
				for element in message.client_keys:
					yield element
		return iterator(self._stubs.clientKeyAdminStub.client_key_list(admin.ClientKeyListRequest(client=self, filter=filter)))
	
	async def admin_client_key_get(self, client_key: str) -> datatypes.ClientKey:
		command_logger.info(f'{self.__class__.__name__}: command: ClientKeyGet')
		response: admin.ClientKeyGetResponse = await self._stubs.clientKeyAdminStub.client_key_get(admin.ClientKeyGetRequest(client=self, client_key=client_key))
		return response.client_key
	
	async def admin_client_key_new(self, name: str, identity_id: int) -> datatypes.ClientKey:
		command_logger.info(f'{self.__class__.__name__}: command: ClientKeyNew')
		response: admin.ClientKeyNewResponse = await self._stubs.clientKeyAdminStub.client_key_new(admin.ClientKeyNewRequest(client=self, name=name, identity_id=identity_id))
		return response.client_key
	
	async def admin_client_key_delete(self, client_key: str) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: ClientKeyDelete')
		await self._stubs.clientKeyAdminStub.client_key_delete(admin.ClientKeyDeleteRequest(client=self, client_key=client_key))
	
	# IdentityAdminService
	def admin_identity_list(self, filter: datatypes.IdentityFilter = None) -> AsyncIterator[datatypes.Identity]:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityList')
	
		async def iterator(message_iterator: AsyncIterator[admin.IdentityListResponse]) -> AsyncIterator[datatypes.Identity]:
			async for message in message_iterator:
				for element in message.identities:
					yield element
		return iterator(self._stubs.identityAdminStub.identity_list(admin.IdentityListRequest(client=self, filter=filter)))
	
	async def admin_identity_admin_get(self, identity_id: int) -> datatypes.Identity:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityAdminGet')
		response: admin.IdentityAdminGetResponse = await self._stubs.identityAdminStub.identity_admin_get(admin.IdentityAdminGetRequest(client=self, identity_id=identity_id))
		return response.identity
	
	async def admin_identity_delete(self, identity_id: int) -> None:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityDelete')
		await self._stubs.identityAdminStub.identity_delete(admin.IdentityDeleteRequest(client=self, identity_id=identity_id))
	
	async def admin_identity_new(self, identity_details: datatypes.IdentityDetails, server_url: str = "", api_key: str = "") -> datatypes.Identity:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityNew')
		response: admin.IdentityNewResponse = await self._stubs.identityAdminStub.identity_new(admin.IdentityNewRequest(client=self, identity_details=identity_details, server_url=server_url, api_key=api_key))
		return response.identity
	
	async def admin_identity_keycloak_new(self, configuration_link: str) -> datatypes.Identity:
		command_logger.info(f'{self.__class__.__name__}: command: IdentityKeycloakNew')
		response: admin.IdentityKeycloakNewResponse = await self._stubs.identityAdminStub.identity_keycloak_new(admin.IdentityKeycloakNewRequest(client=self, configuration_link=configuration_link))
		return response.identity
	
	