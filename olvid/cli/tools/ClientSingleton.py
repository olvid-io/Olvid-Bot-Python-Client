import asyncclick as click

from olvid import OlvidClient, OlvidAdminClient, datatypes


class ClientSingleton():
	__client: OlvidClient = None
	__is_current_client_admin: bool = True
	__script_mode: bool = False
	__current_identity_id: int = 0
	__default_admin_client: OlvidAdminClient = None

	@staticmethod
	async def init(identity_id: int = 0):
		ClientSingleton.__current_identity_id = identity_id
		ClientSingleton.__default_admin_client = OlvidAdminClient(identity_id=identity_id)
		ClientSingleton.__client = ClientSingleton.__default_admin_client

	@staticmethod
	async def auto_select_identity():
		if ClientSingleton.is_client_admin():
			async for identity in ClientSingleton.get_client().admin_identity_list():
				ClientSingleton.set_current_identity_id(identity_id=identity.id)
				click.secho("{}".format(f"Currently using identity: {identity.id}"), fg="green")
				return
		else:
			click.secho("ClientSingleton: cannot auto select identity for a non admin client", fg="red", err=True)

	####
	# change current client api
	####
	@staticmethod
	async def impersonate_client_key(client_key: datatypes.ClientKey):
		if client_key.identity_id == 0:
			ClientSingleton.__is_current_client_admin = True
			ClientSingleton.__client = OlvidAdminClient(client_key=client_key.key, identity_id=ClientSingleton.__default_admin_client.current_identity_id)
		else:
			ClientSingleton.__is_current_client_admin = False
			if not ClientSingleton.is_default_client():
				await ClientSingleton.__client.stop()
			ClientSingleton.__client = OlvidClient(client_key=client_key.key)
			ClientSingleton.__current_identity_id = client_key.identity_id

	@staticmethod
	async def use_default_client():
		ClientSingleton.__client = ClientSingleton.__default_admin_client
		ClientSingleton.__is_current_client_admin = True
		ClientSingleton.__current_identity_id = ClientSingleton.__default_admin_client.current_identity_id

	####
	# Access current client and properties
	####
	@staticmethod
	def is_client_admin() -> bool:
		return ClientSingleton.__is_current_client_admin

	@staticmethod
	def is_default_client() -> bool:
		return ClientSingleton.__client == ClientSingleton.__default_admin_client

	@staticmethod
	def get_client() -> OlvidAdminClient:
		if not ClientSingleton.__client:
			raise Exception("ClientSingleton was not initialized")
		return ClientSingleton.__client

	@staticmethod
	def get_current_identity_id():
		return ClientSingleton.__current_identity_id

	@staticmethod
	def set_current_identity_id(identity_id: int):
		if ClientSingleton.is_client_admin():
			client: OlvidAdminClient = ClientSingleton.__client
			client.current_identity_id = identity_id
			ClientSingleton.__current_identity_id = identity_id
		else:
			click.secho("Cannot change current identity for non admin clients", fg="red", err=True)

	####
	# Script mode property
	####
	@staticmethod
	def is_script_mode_enabled():
		return ClientSingleton.__script_mode

	@staticmethod
	def enable_script_mode():
		ClientSingleton.__script_mode = True
