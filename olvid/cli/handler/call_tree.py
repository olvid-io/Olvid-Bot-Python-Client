from ..interactive_tree import interactive_tree

from ..tools.cli_tools import *

#####
# call
#####
@interactive_tree.group("call", short_help="Manage your calls")
def call_tree():
	pass

#####
# call start
#####
@call_tree.command("start", short_help="start a new call in a discussion")
@click.option("-d", "--discussion", "discussion_id", type=int, default=None, help="Use passed id as discussion id")
@click.argument("contact_ids", nargs=-1, type=click.INT)
async def call_start(contact_ids: list[int], discussion_id: int):
	if contact_ids:
		call_identifier = await ClientSingleton.get_client().call_start_custom_call(contact_ids=contact_ids, discussion_id=discussion_id)
	else:
		call_identifier = await ClientSingleton.get_client().call_start_discussion_call(discussion_id=discussion_id)
	print_success_message(f"Call started: {call_identifier}", call_identifier)
