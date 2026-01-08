import os

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
async def discussion_rm(discussion_ids: tuple[int]):
	for discussion_id in discussion_ids:
		await ClientSingleton.get_client().discussion_empty(discussion_id=discussion_id)
		print_command_result(f"Discussion emptied: {discussion_id}")


#####
# discussion photo
#####
@discussion_tree.group("photo", help="get discussion photos", cls=WrapperGroup)
def discussion_photo_tree():
	pass

#####
# discussion photo save
#####
@discussion_photo_tree.command("save", help="Save discussion photos to local files.")
@click.argument("discussion_ids", required=False, nargs=-1, type=click.INT)
@click.option("-a", "--all", "save_all", is_flag=True, help="Save all discussion photos")
@click.option("-p", "--path", "path", help="directory to store downloaded photo (default: ./photos)", nargs=1, type=click.STRING, required=False)
@click.option("-f", "--filename", "filename", help="specify file name to use (ignored if saving more than one image)", nargs=1, type=click.STRING, required=False)
async def discussion_photo_set(path: str, filename: str, save_all: bool, discussion_ids: list[int]):
	# use default save directory if necessary
	if not path:
		path = "./photos"
	# create save directory
	os.makedirs(path, exist_ok=True)

	if not discussion_ids or save_all:
		discussion_ids = [g.id async for g in ClientSingleton.get_client().discussion_list()]

	# save every requested photo
	for discussion_id in discussion_ids:
		photo_bytes: bytes = await ClientSingleton.get_client().discussion_download_photo(discussion_id=discussion_id)

		# specified filename flag
		if len(discussion_ids) == 1 and filename:
			filepath: str = os.path.join(path, filename)
		# default filename
		else:
			filepath: str = os.path.join(path, f"discussion_{discussion_id}.jpeg")
		with open(filepath, "wb") as photo:
			photo.write(photo_bytes)
		print_normal_message(f"Photo saved in: {filepath}", filepath)

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
