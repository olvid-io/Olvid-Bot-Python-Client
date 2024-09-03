import grpc.aio
from google.protobuf.json_format import Parse, ParseError

from ..interactive_tree import interactive_tree
from ..tools.cli_tools import *
from ..tools.click_wrappers import WrapperGroup


#####
# key
#####
@interactive_tree.group("key", short_help="(admin) manage your identities client keys", cls=WrapperGroup)
def key_tree():
	pass


#####
# key new
#####
@key_tree.command("new", help="create a new client key associated with an identity")
@click.argument("key_name", required=True, type=str)
@click.argument("identity_id", required=True, type=int)
async def key_new(key_name: str, identity_id: int):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage client keys when impersonating a non admin key")
		return

	client_key = await ClientSingleton.get_client().admin_client_key_new(name=key_name, identity_id=identity_id)
	print_normal_message(f"Client key created: {client_key.key}", client_key.key)


#####
# key rm
#####
@key_tree.command("rm", help="delete a client key")
@click.argument("client_keys", nargs=-1, required=True, type=click.STRING)
async def key_delete(client_keys: tuple[str]):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage client keys when impersonating a non admin key")
		return

	for key in client_keys:
		await ClientSingleton.get_client().admin_client_key_delete(key)
		print_command_result(f"Key deleted: {key}")


#####
# key get
#####
# noinspection PyProtectedMember
@key_tree.command("get", help="list existing client keys")
@click.option("-a", "--all", "get_all", is_flag=True)
@click.argument("keys", nargs=-1, type=click.STRING)
@click.option("-f", "--fields", "fields", type=str)
@click.option("--filter", "filter_", type=str)
async def key_get(get_all: bool, keys: tuple[str], fields: str, filter_: str = ""):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage client keys when impersonating a non admin key")
		return

	# build filter
	key_filter: datatypes.ClientKeyFilter = datatypes.ClientKeyFilter()
	if filter_:
		try:
			parsed_message = Parse(filter_, datatypes.ClientKeyFilter()._to_native(key_filter))
			key_filter = datatypes.ClientKeyFilter._from_native(parsed_message)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	if get_all or not keys:
		async for client_key in ClientSingleton.get_client().admin_client_key_list(filter=key_filter):
			filter_fields_and_print_normal_message(client_key, fields)
	else:
		for client_key in list(keys):
			client_key = await ClientSingleton.get_client().admin_client_key_get(client_key)
			filter_fields_and_print_normal_message(client_key, fields)


#####
# identity impersonate
#####
@key_tree.command("impersonate", help="connect the cli to daemon using a specific client key (necessary to access storage api)")
@click.argument("client_key", required=False, type=click.STRING, default="")
async def key_impersonate(client_key: str):
	if client_key:
		# if not currently on admin client swap to default admin client to create a new client
		if not ClientSingleton.is_client_admin():
			await ClientSingleton.use_default_client()
		try:
			key = await ClientSingleton.get_client().admin_client_key_get(client_key=client_key)
		except grpc.aio.AioRpcError:
			print_error_message("Client key not found")
			return
		await ClientSingleton.impersonate_client_key(client_key=key)
		print_normal_message(f"Impersonating: {key.name}: {key.identity_id}", f"{key.identity_id}")
	# swap to default admin client
	else:
		if ClientSingleton.is_default_client():
			print_normal_message("Already using default key", "")
		else:
			print_normal_message("Back to default key", "")
			await ClientSingleton.use_default_client()
