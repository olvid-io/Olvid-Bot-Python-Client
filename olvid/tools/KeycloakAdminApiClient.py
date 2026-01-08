import json
from .. import datatypes

try:
	import aiohttp
	_has_aio_http = True
except ImportError:
	aiohttp = None
	_has_aio_http = False

# this class must be used with a keycloak managed identity and bot must have a valid role on keycloak
# !! required aiohttp module !!
class KeycloakAdminApiClient:
	def __init__(self, keycloak_credentials: datatypes.KeycloakApiCredentials):
		"""requires aiohttp to be installed"""
		if not _has_aio_http:
			raise ImportError('aiohttp must be installed to use KeycloakAdminApiClient, use pip3 install \'olvid-bot[keycloak]\'')

		self.credentials: datatypes.KeycloakApiCredentials = keycloak_credentials

	async def get_your_realm_name(self):
		# parse server url to extract realm name
		return [s for s in self.credentials.server_url.split("/") if s][-1]

	# return a list of realms: {"realmList":[{"name": str, "admin": bool, "olvid": bool, [...]}]}
	async def list_realms(self, only_olvid_realms: bool = False, only_admin_realms: bool = False) -> list[dict]:
		payload: dict = {"q": 3}
		response = await self._admin_api_request(payload)
		realmList = response.get("data").get("realmList")
		if only_olvid_realms:
			return [realm for realm in realmList if realm.get("olvid")]
		elif only_admin_realms:
			return [realm for realm in realmList if realm.get("admin")]
		else:
			return realmList

	# return new bot configuration link
	# possible roles: "admin", "editor", "viewer", "none"
	async def create_bot(self, realmName: str, username: str, identity_details: datatypes.IdentityDetails, role: str = "none") -> str:
		payload: dict = {
		  "q": 19,
		  "realmName": realmName,
		  "username": username,
		  "firstname": identity_details.first_name,
		  "lastname": identity_details.last_name,
		  "position": identity_details.position,
		  "company": identity_details.company,
		  "role": role
		}
		return await self._admin_api_request(payload)

	# return {"usersList": [{"id":str,"username":str,"email":str,"firstname":str,"lastname":str,"position":str,"company":str,[...]}]}
	async def get_user_by_username(self, realm_name: str, username: str) -> dict:
		payload: dict = {
		  "q": 25,
		  "realmName": realm_name,
		  "usersUsernameList": [username],
		}
		return (await self._admin_api_request(payload)).get("data")

	# return password
	async def create_user(self, realmName: str, username: str, password: str, identity_details: datatypes.IdentityDetails, email: str = "") -> str:
		payload: dict = {
			"q": 24,
			"realmName": realmName,
			"isNoPassword": False,
			"user": {
				"email": email,
				"username": username,
				"firstname": identity_details.first_name,
				"lastname": identity_details.last_name,
				"position": identity_details.position,
				"company": identity_details.company,
				"password": password
			}
		}
		return (await self._admin_api_request(payload)).get("data").get("password")

	async def delete_user(self, realmName: str, username: str) -> str:
		payload: dict = {
			"q": 39,
			"realmName": realmName,
			"usersUsernameList": [username],
			"revocationType": 1
		}
		return (await self._admin_api_request(payload)).get("data").get("password")

	# return a realm dict: {"configLink":str,"writeAllowed":bool,"enableBotsManagement":bool,[...]}
	async def get_realm_settings(self, realm_name: str) -> dict:
		payload: dict = {"q": 43, "realmName": realm_name}
		return (await self._admin_api_request(payload)).get("data")

	# return a response dict: {"created":[{"link":str, "id":str, "tag":str, [...]}], "errors":[]}
	async def create_external_link(self, realm_name: str, tags: list[str]) -> dict:
		payload: dict = {"q": 58, "realmName": realm_name, "dataArray": tags}
		return (await self._admin_api_request(payload)).get("data")

	async def _admin_api_request(self, payload: dict):
		async with aiohttp.ClientSession() as session:
			headers = {
				"Content-Type": "application/json;charset=UTF-8",
				"direct-auth-username": self.credentials.username,
				"direct-auth-token": self.credentials.direct_auth_token,
			}
			async with session.post(url=self.credentials.server_url.rstrip("/") + "/olvid-rest/configuration", headers=headers, data=json.dumps(payload)) as resp:
				json_response = await resp.json()
				if type(json_response) is dict and json_response.get("error"):
					raise Exception(f"{json_response['message']} [code: {json_response.get('error')}]" if json_response.get("message") else str(json_response["error"]))
				return json_response
