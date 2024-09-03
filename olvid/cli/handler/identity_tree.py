import asyncio

import grpc.aio
from google.protobuf.json_format import Parse, ParseError

from ..interactive_tree import interactive_tree
from ..tools.cli_tools import *
from olvid import datatypes
from ..tools.click_wrappers import WrapperGroup
from ..tools.interactive_actions import ask_question_with_context, contact_new, print_with_context


#####
# identity
#####
@interactive_tree.group("identity", help="select current identity, (admin) manage olvid identities", cls=WrapperGroup)
def identity_tree():
	pass


#####
# identity current
#####
@identity_tree.command("current", help="get or update identity currently used for your commands")
@click.argument("identity_id", nargs=1, type=click.INT, required=False)
async def identity_current(identity_id: int):
	# If no arguments show current identity
	if (not identity_id):
		if not ClientSingleton.get_current_identity_id():
			print_command_result("No current identity")
		else:
			identity = await ClientSingleton.get_client().identity_get()
			print_command_result("Identity currently used: {}".format(identity.details))
		return

	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot change current identity when impersonating a non admin key")
		return

	# unset current identity
	if identity_id == 0:
		ClientSingleton.set_current_identity_id(0)
		print_command_result("Unselected current identity")
		return

	# change current identity index (save previous version)
	previous_identity_id = ClientSingleton.get_current_identity_id()
	ClientSingleton.set_current_identity_id(identity_id)

	try:
		# check if identity exists
		identity = await ClientSingleton.get_client().identity_get()
		# hide invitation url and show result
		identity.invitation_url = ""
		print_normal_message(identity, identity.id)
	except grpc.aio.AioRpcError as e:
		# identity does not exist, restore previous id
		if e.code() == grpc.StatusCode.NOT_FOUND:
			ClientSingleton.set_current_identity_id(previous_identity_id)
		raise e


#####
# identity new
#####
@identity_tree.command("new", help="create a new identity")
@click.option("-f", "--first", "first_opt", default="", help="first name")
@click.option("-l", "--last", "last_opt", default="", help="last name")
@click.option("-p", "--position", "position_opt", default="", help="position")
@click.option("-c", "--company", "company_opt", default="", help="company")
@click.option("-s", "--server", "server_url", default="", help="custom server url (optional)")
@click.option("-k", "--api-key", "api_key", default="", help="custom api key (optional)")
@click.argument("firstName", required=False)
@click.argument("lastName", required=False)
@click.argument("position", required=False)
@click.argument("company", required=False)
async def identity_new(first_opt: str, last_opt: str, position_opt: str, company_opt: str, firstname: str, lastname: str, position: str, company: str, server_url: str, api_key: str):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot create an identity when impersonating a non admin key")
		return

	identity_details = datatypes.IdentityDetails()
	if (first_opt or firstname):
		identity_details.first_name = first_opt if first_opt else firstname
	if (last_opt or lastname):
		identity_details.last_name = last_opt if last_opt else lastname
	if (company_opt or company):
		identity_details.company = company_opt if company_opt else company
	if (position_opt or position):
		identity_details.position = position_opt if position_opt else position

	identity = await ClientSingleton.get_client().admin_identity_new(identity_details=identity_details, server_url=server_url, api_key=api_key)

	if ClientSingleton.is_script_mode_enabled():
		print(identity.id)
		return

	prompt: str = "identity creation"
	fg_color: str = "bright_blue"

	print_command_result(f"identity created with id: {identity.id}")

	try:
		# create associated client key
		client_key: datatypes.ClientKey = await ClientSingleton.get_client().admin_client_key_new(name=f"identity-new-key-{identity.id}", identity_id=identity.id)
		print_with_context(f"Here is your client key to connect to daemon with this identity:\n{click.style(client_key.key, underline=True)}", prompt=prompt, fg_color=fg_color)
		await asyncio.sleep(0.5)
		while not ask_question_with_context("Did you saved your client key ?", prompt=prompt, fg_color=fg_color):
			continue

		# ask to add this new identity as a contact
		if not ask_question_with_context("Do you want to add this identity to your contacts ?", prompt=prompt, fg_color=fg_color):
			ClientSingleton.set_current_identity_id(identity.id)
			click.secho(f"Now using identity: {ClientSingleton.get_current_identity_id()}", fg="green")
			return

		# add this new identity as a contact
		discussion: datatypes.Discussion = await contact_new(identity_id=identity.id, prompt=prompt, fg_color=fg_color)

		ClientSingleton.set_current_identity_id(identity.id)
		click.secho(f"Now using identity: {ClientSingleton.get_current_identity_id()}", fg="green")

		if discussion:
			print(f"You can now send messages to {discussion.title} in discussion {discussion.id}")
		else:
			print("Invitation process finished")
	except click.exceptions.Abort:
		pass


#####
# identity get
#####
# noinspection PyProtectedMember
@identity_tree.command("get", help="list identities on this daemon")
@click.option("-a", "--all", "get_all", is_flag=True)
# @click.option("-l", "--link", "show_invitation_link", is_flag=True)
@click.option("-f", "--fields", "fields", type=str)
@click.argument("identity_ids", nargs=-1, type=click.INT)
@click.option("--filter", "filter_", type=str)
async def identity_get(get_all: bool, identity_ids: tuple[int], fields: str, filter_: str = ""):
	if ClientSingleton.is_client_admin():
		# build filter
		identity_filter: datatypes.IdentityFilter = datatypes.IdentityFilter()
		if filter_:
			try:
				parsed_message = Parse(filter_, datatypes.IdentityFilter()._to_native(identity_filter))
				identity_filter = datatypes.IdentityFilter._from_native(parsed_message)
			except ParseError as e:
				print_error_message(f"Cannot parse filter: {e}")
				return

		if get_all or not identity_ids:
			async for identity in ClientSingleton.get_client().admin_identity_list(filter=identity_filter):
				# hide invitation link
				# if not show_invitation_link:
				# 	identity.invitation_url = ""
				filter_fields_and_print_normal_message(identity, fields)
		else:
			for identity_id in identity_ids:
				identity = await ClientSingleton.get_client().admin_identity_admin_get(identity_id=identity_id)
				# hide invitation link
				# if not show_invitation_link:
				# 	identity.invitation_url = ""
				filter_fields_and_print_normal_message(identity, fields)
	else:
		if identity_ids:
			print_error_message("Cannot list identities when impersonating a non admin key")
			return
		identity = await ClientSingleton.get_client().identity_get()
		# hide invitation link
		# if not show_invitation_link:
		# 	identity.invitation_url = ""
		filter_fields_and_print_normal_message(identity, fields)


#####
# identity rm
#####
@identity_tree.command("rm", help="delete identities")
@click.option("-a", "--all", "delete_all", is_flag=True)
@click.argument("identity_ids", nargs=-1, type=click.INT)
async def identity_delete(delete_all: bool, identity_ids: tuple[int]):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot delete an identity when impersonating a non admin key")
		return

	identity_ids = list(identity_ids)  # convert tuple to list
	if (not len(identity_ids) and not delete_all):
		raise click.exceptions.BadArgumentUsage("Specify identity id")

	if delete_all:
		identity_ids = [i.id async for i in ClientSingleton.get_client().admin_identity_list()]
		if not identity_ids:
			raise click.exceptions.BadArgumentUsage("No identity to delete")

	for identity_id in identity_ids:
		await ClientSingleton.get_client().admin_identity_delete(identity_id)
		print_command_result(f"Identity deleted: {identity_id}", identity_ids)


#####
# identity update
#####
@identity_tree.command("update", help="update your current identity details (name, position, ...)")
@click.option("-f", "--first", "first_opt", default="")
@click.option("-l", "--last", "last_opt", default="")
@click.option("-p", "--position", "position_opt", default="")
@click.option("-c", "--company", "company_opt", default="")
@click.argument("firstName", required=False)
@click.argument("lastName", required=False)
@click.argument("position", required=False)
@click.argument("company", required=False)
async def identity_update_details(first_opt: str, last_opt: str, position_opt: str, company_opt: str, firstname: str, lastname: str, position: str, company: str):
	identity_details = datatypes.IdentityDetails()
	if (first_opt or firstname):
		identity_details.first_name = first_opt if first_opt else firstname
	if (last_opt or lastname):
		identity_details.last_name = last_opt if last_opt else lastname
	if (company_opt or company):
		identity_details.company = company_opt if company_opt else company
	if (position_opt or position):
		identity_details.position = position_opt if position_opt else position

	if not identity_details.first_name and not identity_details.last_name:
		raise click.exceptions.BadArgumentUsage("Specify at least first or last name")

	await ClientSingleton.get_client().identity_update_details(identity_details)
	print_command_result("Identity updated")


#####
# identity key
#####
@identity_tree.command("key", help="set api key for current identity")
@click.argument("apiKey", nargs=1, required=True)
@click.option("-c", "--configuration", is_flag=True, required=False, help="Use a configuration link instead of a raw api key")
async def identity_apikey(configuration: bool, apikey: str):
	if configuration:
		result = await ClientSingleton.get_client().identity_set_configuration_link(configuration_link=apikey)
	else:
		result = await ClientSingleton.get_client().identity_set_api_key(api_key=apikey)
	print_command_result(f"Api key set up, new permissions: {result}")


#####
# identity photo
#####
@identity_tree.group("photo", help="manage current identity photo", cls=WrapperGroup)
def identity_photo_tree():
	pass


#####
# identity photo set
#####
@identity_photo_tree.command("set", help="set current identity photo")
@click.argument("photo_path", required=True, type=click.STRING)
async def identity_photo_set(photo_path):
	try:
		await ClientSingleton.get_client().identity_set_photo(photo_path)
		print_command_result("Identity photo set")
	except IOError as e:
		raise click.exceptions.BadArgumentUsage(str(e))


#####
# identity photo unset
#####
@identity_photo_tree.command("unset", help="remove current identity photo")
async def identity_photo_unset():
	await ClientSingleton.get_client().identity_remove_photo()
	print_command_result("Identity photo unset")


#####
# identity kc
#####
@identity_tree.group("kc", help="manage keycloak server for identities", cls=WrapperGroup)
def identity_kc_tree():
	pass


#####
# identity kc new
#####
@identity_kc_tree.command("new", help="create a new identity using a keycloak bot configuration link")
@click.argument("configuration_link", required=True, type=click.STRING)
async def identity_kc_new(configuration_link):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot create a new identity when impersonating a non admin key")
		return

	identity = await ClientSingleton.get_client().admin_identity_keycloak_new(configuration_link=configuration_link)

	if ClientSingleton.is_script_mode_enabled():
		print(identity.id)
		return

	prompt: str = "identity creation"
	fg_color: str = "bright_blue"

	print_command_result(f"identity created with id: {identity.id}")

	try:
		# create associated client key
		client_key: datatypes.ClientKey = await ClientSingleton.get_client().admin_client_key_new(name=f"identity-new-key-{identity.id}", identity_id=identity.id)
		print_with_context(f"Here is your client key to connect to daemon with this identity:\n{click.style(client_key.key, underline=True)}", prompt=prompt, fg_color=fg_color)
		await asyncio.sleep(0.5)
		while not ask_question_with_context("Did you saved your client key ?", prompt=prompt, fg_color=fg_color):
			continue

		ClientSingleton.set_current_identity_id(identity.id)
		click.secho(f"Now using identity: {ClientSingleton.get_current_identity_id()}", fg="green")
	except click.exceptions.Abort:
		pass



#####
# identity kc bind
#####
@identity_kc_tree.command("bind", help="attach your current identity to a keycloak server using a keycloak bot configuration link")
@click.argument("configuration_link", required=True, type=click.STRING)
async def identity_kc_bind(configuration_link):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage identities when impersonating a non admin key")
		return

	await ClientSingleton.get_client().identity_keycloak_bind(configuration_link=configuration_link)
	print_command_result(f"Identity now linked to keycloak")


#####
# identity kc unbind
#####
@identity_kc_tree.command("unbind", help="remove keycloak server for current identity")
async def identity_kc_unbind():
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage identities when impersonating a non admin key")
		return

	await ClientSingleton.get_client().identity_keycloak_unbind()
	print_command_result(f"Identity is not linked to keycloak anymore")
