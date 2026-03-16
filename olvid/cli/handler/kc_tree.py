from google.protobuf.json_format import Parse, ParseError

from ..interactive_tree import interactive_tree
from ..tools.cli_tools import *
from ..tools.click_wrappers import WrapperGroup
from ...datatypes import datatypes


#####
# identity
#####
@interactive_tree.group("kc", help="interact with your keycloak server", cls=WrapperGroup)
def kc_tree():
	pass


#####
# kc bind
#####
@kc_tree.command("bind", help="attach your current identity to a keycloak server using a keycloak bot configuration link")
@click.argument("configuration_link", required=True, type=click.STRING)
async def kc_bind(configuration_link):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage identities when impersonating a non admin key")
		return

	await ClientSingleton.get_client().keycloak_bind_identity(configuration_link=configuration_link)
	print_command_result(f"Identity now linked to keycloak")


#####
# kc unbind
#####
@kc_tree.command("unbind", help="remove keycloak server for current identity")
async def kc_unbind():
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage identities when impersonating a non admin key")
		return

	await ClientSingleton.get_client().keycloak_unbind_identity()
	print_command_result(f"Identity is not linked to keycloak anymore")

#####
# kc contact
#####
@kc_tree.group("contact", help="manage keycloak contacts", cls=WrapperGroup)
def kc_contact_tree():
	pass

#####
# kc contact get
#####
@kc_contact_tree.command("get", help="list keycloak users")
@click.option("-t", "--timestamp", type=int, default=0, help="last list user timestamp")
@click.option("-f", "--fields", "fields", type=str)
@click.option("--filter", "filter_", type=str)
async def kc_contact_get(filter_: str, fields: str, timestamp: int):
	# build filter
	keycloak_user_filter: datatypes.KeycloakUserFilter = datatypes.KeycloakUserFilter()
	if filter_:
		try:
			parsed_message = Parse(filter_, datatypes.KeycloakUserFilter()._to_native(keycloak_user_filter))
			keycloak_user_filter = datatypes.KeycloakUserFilter._from_native(parsed_message)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	last_list_timestamp = 0
	async for users, last_list_timestamp in ClientSingleton.get_client().keycloak_user_list(filter=keycloak_user_filter, last_list_timestamp=timestamp if timestamp else None):
		for user in users:
			filter_fields_and_print_normal_message(user, fields)
	print_normal_message(f"Last list timestamp: {last_list_timestamp}", last_list_timestamp)


#####
# kc contact add
#####
@kc_contact_tree.command("add", help="add a keycloak user as a contact")
@click.argument("user_id", nargs=1, required=True, type=click.STRING)
async def kc_contact_add(user_id: str):
	await ClientSingleton.get_client().keycloak_add_user_as_contact(keycloak_id=user_id)
	print_normal_message("Added contact", "")
