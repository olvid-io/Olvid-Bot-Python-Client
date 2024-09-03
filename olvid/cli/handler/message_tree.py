import os.path
from google.protobuf.json_format import Parse, ParseError

from ..interactive_tree import interactive_tree

from ..tools.cli_tools import *
from ..tools.click_wrappers import WrapperGroup


#####
# message
#####
@interactive_tree.group("message", help="send and manage messages", cls=WrapperGroup)
def message_tree():
	pass


#####
# message get
#####
# noinspection PyProtectedMember
@message_tree.command("get", help="list current identity messages")
@click.option("-d", "--discussion", type=int, help="get all messages in given discussion id")
@click.option("-u", "--unread", "unread", is_flag=True, help="get only unread messages")
@click.argument("message_ids", required=False, nargs=-1, type=click.STRING)
@click.option("--filter", "filter_", type=str)
@click.option("-f", "--fields", "fields", type=str)
async def message_get(message_ids: tuple[str], fields: str, discussion: int = 0, filter_: str = "", unread: bool = False):
	# build filter
	message_filter: datatypes.MessageFilter = datatypes.MessageFilter()
	if filter_:
		try:
			parsed_message = Parse(filter_, datatypes.MessageFilter()._to_native(message_filter))
			message_filter = datatypes.MessageFilter._from_native(parsed_message)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	# all messages for identity
	messages = []
	if message_ids:
		for message_id in message_ids:
			messages.append(await ClientSingleton.get_client().message_get(string_to_message_id(message_id)))
	elif discussion:
		message_filter.discussion_id = discussion
		async for message in ClientSingleton.get_client().message_list(filter=message_filter, unread=unread):
			messages.append(message)
	else:
		async for message in ClientSingleton.get_client().message_list(filter=message_filter, unread=unread):
			messages.append(message)
	for message in messages:
		filter_fields_and_print_normal_message(message, fields)


#####
# message rm
#####
# noinspection PyProtectedMember
@message_tree.command("rm", help="delete messages")
@click.option("-d", "--discussion", "discussion_id", type=int, help="delete all messages in given discussion id")
@click.option("-a", "--all", "all_opt", type=bool, is_flag=True, help="delete all messages for given identity id")
@click.option("-e", "--everywhere", type=bool, is_flag=True, help="Delete messages everywhere")
@click.option("--filter", "filter_", type=str)
@click.argument("message_ids", nargs=-1, type=click.STRING)
async def message_delete(message_ids: tuple[str], discussion_id: int, all_opt: bool, everywhere: bool, filter_: str = ""):
	# build filter
	message_filter: datatypes.MessageFilter = datatypes.MessageFilter()
	if filter_:
		try:
			parsed_message = Parse(filter_, datatypes.MessageFilter()._to_native(message_filter))
			message_filter = datatypes.MessageFilter._from_native(parsed_message)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	if (message_ids):
		for message_id in message_ids:
			await ClientSingleton.get_client().message_delete(message_id=string_to_message_id(message_id), delete_everywhere=everywhere)
			print_command_result(f"Message deleted: {message_id}")
	elif discussion_id:
		await ClientSingleton.get_client().discussion_empty(discussion_id=discussion_id, delete_everywhere=everywhere)
		print_command_result(f"Emptied discussion: {discussion_id}")
	elif (all_opt):
		async for message in ClientSingleton.get_client().message_list(filter=message_filter):
			await ClientSingleton.get_client().message_delete(message_id=message.id, delete_everywhere=everywhere)
			print_command_result(f"Message deleted: {message.id}")
	else:
		raise click.exceptions.UsageError("")


#####
# message send
#####
@message_tree.command("send", help="send text message in a given discussion")
@click.option("-c", "--contact", "use_contact", is_flag=True, help="Use passed id as a contact id")
@click.option("-g", "--group", "use_group", is_flag=True, help="Use passed id as a group id")
@click.option("-r", "--reply", "reply_id", type=click.STRING, default=None)
@click.option("-o", "--once", "read_once", is_flag=True)
@click.option("-e", "--existence", "existence_duration", type=click.INT, default=0)
@click.option("-v", "--visibility", "visibility_duration", type=click.INT, default=0)
@click.option("-a", "--attachment", "attachment_paths", type=str, default=(), multiple=True)
@click.argument("discussion_id", nargs=1, type=click.INT)
@click.argument("body", nargs=-1, type=click.STRING, required=False)
async def message_send(discussion_id: int, use_contact: bool, use_group: bool, body: tuple[str], attachment_paths: tuple[str], reply_id: str, read_once: bool, existence_duration: int, visibility_duration: int):
	# check options consistency
	if use_contact and use_group:
		print_error_message("You cannot use --contact and --group simultaneously")
		print_normal_message(click.get_current_context().get_help(), "")
		return
	if not body and not attachment_paths:
		print_error_message("You must specify at least a body or an attachment path")
		print_normal_message(click.get_current_context().get_help(), "")
		return

	# check attachment existence
	for path in attachment_paths:
		if not os.path.isfile(path):
			print_error_message(f"File not found: {path}")
			return
		if not os.access(path, os.R_OK):
			print_error_message(f"Cannot read file: {path}")
			return

	ephemerality = datatypes.MessageEphemerality(
		read_once=read_once,
		visibility_duration=visibility_duration,
		existence_duration=existence_duration
	)
	if use_contact:
		discussion_id = (await ClientSingleton.get_client().discussion_get_by_contact(contact_id=discussion_id)).id
	elif use_group:
		discussion_id = (await ClientSingleton.get_client().discussion_get_by_group(group_id=discussion_id)).id

	message, attachments = await ClientSingleton.get_client().message_send_with_attachments_files(
		discussion_id=discussion_id,
		body=" ".join(body),
		reply_id=string_to_message_id(reply_id) if reply_id is not None else None,
		ephemerality=ephemerality,
		file_paths=list(attachment_paths)
	)
	print_normal_message(message, message.id)
	for attachment in attachments:
		print_normal_message(attachment, attachment.id)


#####
# message update
#####
@message_tree.command("update", help="Update a message text body")
@click.argument("message_id", nargs=1, type=click.STRING)
@click.argument("new_body", nargs=-1, type=click.STRING, required=True)
async def message_send(message_id: str, new_body: tuple[str]):
	new_body = " ".join(new_body)
	await ClientSingleton.get_client().message_update_body(string_to_message_id(message_id), new_body)
	print_command_result("Message updated")


#####
# message react
#####
@message_tree.command("react", help="react to a given message")
@click.argument("message_id", nargs=1, type=click.STRING)
@click.argument("reaction", nargs=1, required=False, type=click.STRING)
async def message_send_reaction(message_id: str, reaction: str):
	await ClientSingleton.get_client().message_react(string_to_message_id(message_id), reaction)
	print_command_result("Reaction sent")


#####
# message voip
#####
@message_tree.command("voip", help="start a fake call in a discussion")
@click.argument("discussion_id", nargs=1, type=click.INT)
async def message_send_voip(discussion_id: int):
	await ClientSingleton.get_client().message_send_voip(discussion_id=discussion_id)
	print_command_result("Fake call sent")


#####
# message refresh
#####
@message_tree.command("refresh", help="fore downloading last messages from server")
async def message_update():
	await ClientSingleton.get_client().message_refresh()
	print_command_result("Refreshed messages")
