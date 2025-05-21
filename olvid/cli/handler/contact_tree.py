import os
from google.protobuf.json_format import Parse, ParseError

from ..interactive_tree import interactive_tree

from ..tools.cli_tools import *
from ..tools.click_wrappers import WrapperGroup
from ..tools.interactive_actions import contact_new

#####
# contact
#####
@interactive_tree.group("contact", help="manage your contacts", cls=WrapperGroup)
def contact_tree():
	pass


#####
# contact new
#####
# noinspection PyProtectedMember
@contact_tree.command("new", help="interactively add a  contact")
async def contact_new_cmd():
	if ClientSingleton.is_script_mode_enabled():
		raise click.UsageError("Cannot run contact new in script mode")
	prompt: str = "contact new"
	fg_color: str = "bright_green"

	try:
		discussion: datatypes.Discussion = await contact_new(ClientSingleton.get_client().current_identity_id, prompt=prompt, fg_color=fg_color)
		if discussion:
			print(f"You can now send messages to {discussion.title} in discussion {discussion.id}")
		else:
			print("Invitation process finished")
	except click.exceptions.Abort:
		pass

#####
# contact get
#####
# noinspection PyProtectedMember
@contact_tree.command("get", help="list current identity contacts")
@click.option("-a", "--all", "get_all", is_flag=True)
@click.option("-l", "--link", "show_invitation_link", is_flag=True)
@click.option("-i", "--identifier", "show_contact_identifier", is_flag=True)
@click.argument("contact_ids", nargs=-1, type=click.INT)
@click.option("-f", "--fields", "fields", type=str)
@click.option("--filter", "filter_", type=str)
async def contact_get(get_all, show_invitation_link: bool, show_contact_identifier: bool, contact_ids, fields: str, filter_: str = ""):
	# build filter
	contact_filter: datatypes.ContactFilter = datatypes.ContactFilter()
	if filter_:
		try:
			parsed_message = Parse(filter_, datatypes.ContactFilter()._to_native(contact_filter))
			contact_filter = datatypes.ContactFilter._from_native(parsed_message)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	if get_all or not contact_ids:
		contacts: list[datatypes.Contact] = [c async for c in ClientSingleton.get_client().contact_list(filter=contact_filter)]
	else:
		contacts = [await ClientSingleton.get_client().contact_get(contact_id) for contact_id in contact_ids]

	for contact in contacts:
		if show_invitation_link:
			print(f"{contact.id}: {await ClientSingleton.get_client().contact_get_invitation_link(contact_id=contact.id)}")
		elif show_contact_identifier:
			print(f"{contact.id}: {await ClientSingleton.get_client().contact_get_bytes_identifier(contact_id=contact.id)}")
		else:
			filter_fields_and_print_normal_message(contact, fields)


#####
# contact rm
#####
@contact_tree.command("rm", help="delete contacts")
@click.argument("contact_ids", nargs=-1, type=click.INT)
@click.option("-a", "--all", "delete_all", is_flag=True)
async def contact_delete(delete_all: bool, contact_ids: tuple[int]):
	if (not len(contact_ids) and not delete_all):
		raise click.exceptions.BadArgumentUsage("Specify contact id")

	if delete_all:
		contact_ids = [c.id async for c in ClientSingleton.get_client().contact_list()]
		if not contact_ids:
			raise click.exceptions.BadArgumentUsage("No contact to delete")

	for contact_id in contact_ids:
		await ClientSingleton.get_client().contact_delete(contact_id)
		print_command_result(f"contact deleted: {contact_id}", contact_id)


#####
# contact introduce
#####
@contact_tree.command("introduce", help="present a contact to other contacts")
@click.argument("introduced_contact_id", nargs=1, type=click.INT, required=True)
@click.argument("contact_ids", nargs=-1, type=click.INT, required=True)
async def contact_introduce(introduced_contact_id: int, contact_ids: tuple[int]):
	for contact_id in contact_ids:
		await ClientSingleton.get_client().contact_introduction(introduced_contact_id, contact_id)
		print_command_result(f"Introduced contact {introduced_contact_id} to {contact_id}")


#####
# contact invite
#####
@contact_tree.command("invite", help="invite contacts in one to one discussion")
@click.argument("contact_ids", nargs=-1, type=click.INT, required=True)
async def contact_invite(contact_ids: tuple[int]):
	for contact_id in contact_ids:
		invitation: datatypes.Invitation = await ClientSingleton.get_client().contact_invite_to_one_to_one_discussion(contact_id)
		print_normal_message(invitation, invitation.id)


@contact_tree.command("downgrade", help="downgrade contacts and remove their one to one discussion")
@click.argument("contact_ids", nargs=-1, type=click.INT, required=True)
async def contact_downgrade(contact_ids: tuple[int]):
	for contact_id in contact_ids:
		await ClientSingleton.get_client().contact_downgrade_one_to_one_discussion(contact_id)
		print_command_result(f"Contact downgraded: {contact_id}")


#####
# contact photo
#####
@contact_tree.group("photo", help="get contact photos", cls=WrapperGroup)
def contact_photo_tree():
	pass


#####
# contact photo save
#####
@contact_photo_tree.command("save", help="Save contact photos to local files.")
@click.argument("contact_ids", required=False, nargs=-1, type=click.INT)
@click.option("-a", "--all", "save_all", is_flag=True, help="Save all contact photos")
@click.option("-p", "--path", "path", help="directory to store downloaded photo (default: ./photos)", nargs=1, type=click.STRING, required=False)
@click.option("-f", "--filename", "filename", help="specify file name to use (ignored if saving more than one image)", nargs=1, type=click.STRING, required=False)
async def contact_photo_set(path: str, filename: str, save_all: bool, contact_ids: list[int]):
	# use default save directory if necessary
	if not path:
		path = "./photos"
	# create save directory
	os.makedirs(path, exist_ok=True)

	if not contact_ids or save_all:
		contact_ids = [g.id async for g in ClientSingleton.get_client().contact_list()]

	# save every requested photo
	for contact_id in contact_ids:
		photo_bytes: bytes = await ClientSingleton.get_client().contact_download_photo(contact_id=contact_id)

		# specified filename flag
		if len(contact_ids) == 1 and filename:
			filepath: str = os.path.join(path, filename)
		# default filename
		else:
			filepath: str = os.path.join(path, f"contact_{contact_id}.jpeg")
		with open(filepath, "wb") as photo:
			photo.write(photo_bytes)
		print_normal_message(f"Photo saved in: {filepath}", filepath)


#####
# contact kc
#####
@contact_tree.group("kc", help="manage keycloak contacts", cls=WrapperGroup)
def contact_kc_tree():
	pass


#####
# contact kc get
#####
@contact_kc_tree.command("get", help="list keycloak users")
@click.option("-t", "--timestamp", type=int, default=0, help="last list user timestamp")
@click.option("-f", "--fields", "fields", type=str)
@click.option("--filter", "filter_", type=str)
async def contact_kc_get(filter_: str, fields: str, timestamp: int):
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
# contact kc add
#####
@contact_kc_tree.command("add", help="add a keycloak user as a contact")
@click.argument("user_id", nargs=1, required=True, type=click.STRING)
async def contact_kc_get(user_id: str):
	await ClientSingleton.get_client().keycloak_add_user_as_contact(keycloak_id=user_id)
	print_normal_message("Added contact", "")


#####
# contact reset
#####
@contact_tree.command("reset", help="Recreate secure channels")
@click.option("-a", "--all", "reset_all", is_flag=True, help="Re-create secure channels for every contact")
@click.argument("contact_ids", nargs=-1, type=click.INT)
async def contact_reset(reset_all: bool, contact_ids: tuple[int]):
	if (not len(contact_ids) and not reset_all):
		raise click.exceptions.BadArgumentUsage("Specify contact id")

	if reset_all:
		contact_ids = [c.id async for c in ClientSingleton.get_client().contact_list()]
		if not contact_ids:
			raise click.exceptions.BadArgumentUsage("No contacts found")

	for contact_id in contact_ids:
		await ClientSingleton.get_client().contact_recreate_channels(contact_id=contact_id)
		print_command_result(f"Recreating channels: {contact_id}", contact_id)
