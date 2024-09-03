import os
from google.protobuf.json_format import Parse, ParseError

from ..interactive_tree import interactive_tree
from ..tools.cli_tools import *
from ..tools.click_wrappers import WrapperGroup


#####
# attachment
#####
@interactive_tree.group("attachment", help="list and save your attachments", cls=WrapperGroup)
def attachment_tree():
	pass


#####
# attachment get
#####
# noinspection PyProtectedMember
@attachment_tree.command("get", help="list current identity attachments")
@click.option("-a", "--all", "get_all", is_flag=True, help="get attachments for current owned identity")
@click.option("-m", "--message", "message_id", type=click.STRING, help="get attachments associated to a message id")
@click.argument("attachment_ids", nargs=-1, required=False, type=click.STRING)
@click.option("--filter", "filter_", type=str)
@click.option("-f", "--fields", "fields", type=str)
async def attachment_get(get_all: bool, message_id: str, attachment_ids: tuple[str], fields: str, filter_: str = ""):
	# build filter
	attachment_filter: datatypes.AttachmentFilter = datatypes.AttachmentFilter()
	if filter_:
		try:
			parsed_attachment = Parse(filter_, datatypes.AttachmentFilter()._to_native(attachment_filter))
			attachment_filter = datatypes.AttachmentFilter._from_native(parsed_attachment)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	if message_id:
		async for attachment in ClientSingleton.get_client().attachment_message_list(message_id=string_to_message_id(message_id)):
			filter_fields_and_print_normal_message(attachment, fields)
	elif get_all or not attachment_ids:
		async for attachment in ClientSingleton.get_client().attachment_list(filter=attachment_filter):
			filter_fields_and_print_normal_message(attachment, fields)
	else:
		for attachment_id in attachment_ids:
			attachment = await ClientSingleton.get_client().attachment_get(attachment_id=string_to_attachment_id(attachment_id))
			filter_fields_and_print_normal_message(attachment, fields)


#####
# attachment rm
#####
@attachment_tree.command("rm", help="delete attachments")
@click.argument("attachment_ids", nargs=-1, type=click.STRING, required=True)
async def attachment_rm(attachment_ids: tuple[str]):
	for attachment_id in attachment_ids:
		await ClientSingleton.get_client().attachment_delete(string_to_attachment_id(attachment_id))
		print_command_result(f"attachment deleted: {attachment_id}")


#####
# attachment save
#####
@attachment_tree.command("save", help="download an attachment file and save it in your filesystem")
@click.argument("attachment_id", nargs=1, type=click.STRING)
@click.option("-p", "--path", "path", help="directory to store downloaded attachment", nargs=1, type=click.STRING, required=False)
@click.option("-f", "--filename", "filename", help="override original file name", nargs=1, type=click.STRING, required=False)
async def attachment_save(attachment_id: str, path: str, filename: str):
	# ues the default path to store attachments (and create dir if needed)
	if not path:
		path = "./attachments"
		if not os.path.isdir(path):
			os.mkdir(path)
	# check the path exists
	elif not os.path.isdir:
		raise click.exceptions.FileError("{}: no such directory".format(path))

	if not filename:
		attachment = await ClientSingleton.get_client().attachment_get(attachment_id=string_to_attachment_id(attachment_id))
		filename = attachment.file_name
	try:
		# create file
		with open(os.path.join(path, filename), "wb") as fd:
			async for chunk in ClientSingleton.get_client().attachment_download(attachment_id=string_to_attachment_id(attachment_id)):
				fd.write(chunk)
		print_success_message(f"Attachment downloaded at: {os.path.join(path, filename)}", f"{os.path.join(path, filename)}")
	except Exception as e:
		raise click.exceptions.BadArgumentUsage("Unable to download file: " + str(e))
