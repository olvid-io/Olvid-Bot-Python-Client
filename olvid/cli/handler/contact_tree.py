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
@click.argument("contact_ids", nargs=-1, type=click.INT)
@click.option("-f", "--fields", "fields", type=str)
@click.option("--filter", "filter_", type=str)
async def contact_get(get_all, contact_ids, fields: str, filter_: str = ""):
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
		async for contact in ClientSingleton.get_client().contact_list(filter=contact_filter):
			filter_fields_and_print_normal_message(contact, fields)
	else:
		for contact_id in contact_ids:
			contact = await ClientSingleton.get_client().contact_get(contact_id)
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
