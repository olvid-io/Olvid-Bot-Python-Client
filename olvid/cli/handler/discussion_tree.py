from google.protobuf.json_format import Parse, ParseError

from ..interactive_tree import interactive_tree
from ..tools.cli_tools import *
from ..tools.click_wrappers import WrapperGroup


#####
# discussion
#####
@interactive_tree.group("discussion", help="manage your discussions", cls=WrapperGroup)
def discussion_tree():
	pass


#####
# discussion get
#####
# noinspection PyProtectedMember
@discussion_tree.command("get", help="list current identity discussions")
@click.option("-a", "--all", "get_all", is_flag=True)
@click.option("-c", "--contact", "by_contact", is_flag=True)
@click.option("-g", "--group", "by_group", is_flag=True)
@click.argument("discussion_ids", nargs=-1, type=click.INT)
@click.option("-f", "--fields", "fields", type=str)
@click.option("--filter", "filter_", type=str)
async def discussion_get(get_all, by_contact: bool, by_group: bool, discussion_ids, fields: str, filter_: str = ""):
	# build filter
	discussion_filter: datatypes.DiscussionFilter = datatypes.DiscussionFilter()
	if filter_:
		try:
			parsed_message = Parse(filter_, datatypes.DiscussionFilter()._to_native(discussion_filter))
			discussion_filter = datatypes.DiscussionFilter._from_native(parsed_message)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	discussions: list[datatypes.Discussion]
	if get_all or not discussion_ids:
		discussions = [d async for d in ClientSingleton.get_client().discussion_list(filter=discussion_filter)]
	elif by_contact:
		discussions = [await ClientSingleton.get_client().discussion_get_by_contact(did) for did in discussion_ids]
	elif by_group:
		discussions = [await ClientSingleton.get_client().discussion_get_by_group(did) for did in discussion_ids]
	else:
		discussions = [await ClientSingleton.get_client().discussion_get(did) for did in discussion_ids]
	for discussion in discussions:
		filter_fields_and_print_normal_message(discussion, fields)


#####
# discussion rm
#####
@discussion_tree.command("empty", help="delete all messages in a discussion")
@click.argument("discussion_ids", nargs=-1, type=click.INT, required=True)
@click.option("-e", "--everywhere", "delete_everywhere", is_flag=True, default=False)
async def discussion_rm(discussion_ids: tuple[int], delete_everywhere: bool = False):
	for discussion_id in discussion_ids:
		await ClientSingleton.get_client().discussion_empty(discussion_id=discussion_id,
															delete_everywhere=delete_everywhere)
		print_command_result(f"Discussion emptied: {discussion_id}")


#####
# discussion settings
#####
@discussion_tree.group("settings", help="manage discussion settings", cls=WrapperGroup)
def settings_tree():
	pass


#####
# discussion settings get
#####
@settings_tree.command("get", help="get a ")
@click.argument("discussion_id", nargs=1, type=click.INT, required=True)
@click.option("-f", "--fields", "fields", type=str)
async def discussion_settings_get(discussion_id: int, fields: str):
	settings = await ClientSingleton.get_client().discussion_settings_get(discussion_id=discussion_id)
	filter_fields_and_print_normal_message(settings, fields)


#####
# discussion settings set
#####
@settings_tree.command("set")
@click.option("-o", "--once", "read_once", is_flag=True)
@click.option("-e", "--existence", "existence_duration", type=click.INT, default=0)
@click.option("-v", "--visibility", "visibility_duration", type=click.INT, default=0)
@click.argument("discussion_id", nargs=1, type=click.INT)
async def discussion_settings_set(discussion_id: int, read_once: bool, existence_duration: int,
									visibility_duration: int):
	settings = datatypes.DiscussionSettings(discussion_id=discussion_id,
											read_once=read_once,
											existence_duration=existence_duration,
											visibility_duration=visibility_duration)
	new_settings = await ClientSingleton.get_client().discussion_settings_set(settings=settings)
	print_normal_message(new_settings, new_settings)


#####
# discussion locked
#####
@discussion_tree.group("locked", help="manage locked discussion", cls=WrapperGroup)
def locked_tree():
	pass


#####
# discussion locked get
#####
@locked_tree.command("get", help="list locked discussions")
@click.option("-f", "--fields", "fields", type=str)
async def discussion_locked_get(fields: str):
	async for discussion in ClientSingleton.get_client().discussion_locked_list():
		filter_fields_and_print_normal_message(discussion, fields)


#####
# discussion locked rm
#####
@locked_tree.command("rm", help="delete locked discussion")
@click.argument("discussion_ids", nargs=-1, type=click.INT, required=True)
async def discussion_rm(discussion_ids: tuple[int]):
	for discussion_id in discussion_ids:
		await ClientSingleton.get_client().discussion_locked_delete(discussion_id=discussion_id)
		print_command_result(f"Locked discussion deleted: {discussion_id}")
