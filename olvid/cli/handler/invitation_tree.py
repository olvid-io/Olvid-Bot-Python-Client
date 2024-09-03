from google.protobuf.json_format import Parse, ParseError

from ..interactive_tree import interactive_tree
from ..tools.cli_tools import *
from ..tools.click_wrappers import WrapperGroup
from ..tools.interactive_actions import ask_question_with_context, invitation_new

#####
# invitation
#####
@interactive_tree.group("invitation", help="send and answer invitations", cls=WrapperGroup)
def invitation_tree():
	pass


#####
# invitation send
#####
@invitation_tree.command("send", help="send a new invitation using an olvid invitation url")
@click.argument("invitation_url", required=True, type=click.STRING)
async def invitation_send(invitation_url: str):
	invitation: datatypes.Invitation = await ClientSingleton.get_client().invitation_new(invitation_url)

	if ClientSingleton.is_script_mode_enabled():
		print(invitation.id)
		return

	prompt: str = "invitation send"
	fg_color: str = "bright_yellow"

	try:
		if not ask_question_with_context("Do you want to complete invitation process interactively ?", prompt=prompt, fg_color=fg_color):
			print(invitation)
			return

		discussion: datatypes.Discussion = await invitation_new(identity_id=ClientSingleton.get_current_identity_id(), invitation=invitation, prompt=prompt, fg_color=fg_color)
		if discussion:
			print(f"You can now send messages to {discussion.title} in discussion {discussion.id}")
		else:
			print("Invitation process finished")
	except click.exceptions.Abort:
		pass


#####
# invitation get
#####
# noinspection PyProtectedMember
@invitation_tree.command("get", help="list current identity invitations")
@click.option("-a", "--all", "get_all", is_flag=True)
@click.argument("invitation_ids", nargs=-1, type=click.INT)
@click.option("-f", "--fields", "fields", type=str)
@click.option("--filter", "filter_", type=str)
async def invitation_get(get_all: bool, invitation_ids: tuple[int], fields: str, filter_: str = ""):
	# build filter
	invitation_filter: datatypes.InvitationFilter = datatypes.InvitationFilter()
	if filter_:
		try:
			parsed_message = Parse(filter_, datatypes.InvitationFilter()._to_native(invitation_filter))
			invitation_filter = datatypes.InvitationFilter._from_native(parsed_message)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	if get_all or not invitation_ids:
		async for invitation in ClientSingleton.get_client().invitation_list(filter=invitation_filter):
			filter_fields_and_print_normal_message(invitation, fields)
	else:
		for invitation_id in invitation_ids:
			invitation = await ClientSingleton.get_client().invitation_get(invitation_id)
			filter_fields_and_print_normal_message(invitation, fields)


#####
# invitation accept
#####
@invitation_tree.command("accept", help="accept an invitation")
@click.argument("invitation_id", required=True, type=click.INT)
async def invitation_accept(invitation_id: int):
	await ClientSingleton.get_client().invitation_accept(invitation_id=invitation_id)
	print_command_result("Invitation accepted")


#####
# invitation decline
#####
@invitation_tree.command("decline", help="decline an invitation")
@click.argument("invitation_id", required=True, type=click.INT)
async def invitation_decline(invitation_id: int):
	await ClientSingleton.get_client().invitation_decline(invitation_id=invitation_id)
	print_command_result("Invitation declined")


#####
# invitation sas
#####
@invitation_tree.command("sas", help="set your future contact sas code")
@click.argument("invitation_id", required=True, type=click.INT)
@click.argument("sas_code", required=True, type=click.STRING)
async def invitation_sas(invitation_id: int, sas_code: str):
	if (len(sas_code) != 4 or not sas_code.isnumeric()):
		raise click.exceptions.BadArgumentUsage("Invalid sas code format")
	await ClientSingleton.get_client().invitation_sas(invitation_id, sas_code)


#####
# invitation rm
#####
@invitation_tree.command("rm", help="delete an invitation")
@click.option("-a", "--all", "delete_all", is_flag=True)
@click.argument("invitation_ids", nargs=-1, type=click.INT)
async def invitation_delete(invitation_ids: tuple[int], delete_all: bool):
	invitation_ids = list(invitation_ids)  # convert tuple to list
	if (not len(invitation_ids) and not delete_all):
		raise click.exceptions.BadArgumentUsage("Specify invitation id")

	if delete_all:
		async for invitation in ClientSingleton.get_client().invitation_list():
			await ClientSingleton.get_client().invitation_delete(invitation_id=invitation.id)
			print_command_result(f"Invitation deleted: {invitation.id}")
	else:
		for invitation_id in invitation_ids:
			await ClientSingleton.get_client().invitation_delete(invitation_id=invitation_id)
			print_command_result(f"Invitation deleted: {invitation_id}")
