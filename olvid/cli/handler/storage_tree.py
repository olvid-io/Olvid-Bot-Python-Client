from google.protobuf.json_format import Parse, ParseError

from ..interactive_tree import interactive_tree
from ..tools.cli_tools import *
from ..tools.click_wrappers import WrapperGroup


#####
# storage
#####
@interactive_tree.group("storage", short_help="(advanced) access a client key associated storage", cls=WrapperGroup)
def storage_tree():
	pass


#####
# storage get
#####
# noinspection PyProtectedMember
@storage_tree.command("get")
@click.option("-a", "--all", "get_all", is_flag=True)
@click.option("-d", "discussion_id", nargs=1, type=click.INT, default=0)
@click.argument("keys", nargs=-1, type=click.STRING)
@click.option("--filter", "filter_", type=str)
@click.option("-f", "--fields", "fields", type=str)
async def storage_get(get_all: bool, keys: tuple[str], discussion_id: int, fields: str, filter_: str = ""):
	# build filter
	storage_filter: datatypes.StorageElementFilter = datatypes.StorageElementFilter()
	if filter_:
		try:
			parsed_message = Parse(filter_, datatypes.StorageElementFilter()._to_native(storage_filter))
			storage_filter = datatypes.StorageElementFilter._from_native(parsed_message)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	if get_all:
		# global storage
		elements = [element async for element in ClientSingleton.get_client().storage_list(filter=storage_filter)]
		if elements:
			print_normal_message("Global storage:", "")
		for element in elements:
			filter_fields_and_print_normal_message(element, fields)

		# discussion storage
		async for discussion in ClientSingleton.get_client().discussion_list():
			elements = [element async for element in ClientSingleton.get_client().discussion_storage_list(discussion_id=discussion.id, filter=storage_filter)]
			if elements:
				print_normal_message(f"Discussion id: {discussion.id}", "")
				for element in elements:
					filter_fields_and_print_normal_message(element, fields)

	elif not keys:
		if discussion_id:
			async for element in ClientSingleton.get_client().discussion_storage_list(discussion_id=discussion_id, filter=storage_filter):
				print_normal_message(f"{element.key}: {element.value}", f"{element.key}: {element.value}")
		else:
			async for element in ClientSingleton.get_client().storage_list(filter=storage_filter):
				print_normal_message(f"{element.key}: {element.value}", f"{element.key}: {element.value}")

	# get all storage entries
	else:
		for key in keys:
			if discussion_id:
				value = await ClientSingleton.get_client().discussion_storage_get(key=key, discussion_id=discussion_id)
			else:
				value = await ClientSingleton.get_client().storage_get(key)
			print_normal_message(f"{key}: {value}", f"{value}")


#####
# storage set
#####
@storage_tree.command("set")
@click.argument("key", nargs=1, required=True, type=click.STRING)
@click.option("-d", "discussion_id", nargs=1, type=click.INT, default=0)
@click.argument("value", nargs=1, required=True, type=click.STRING)
async def storage_set(key: str, value: str, discussion_id: int):
	if discussion_id:
		await ClientSingleton.get_client().discussion_storage_set(key=key, value=value, discussion_id=discussion_id)
	else:
		await ClientSingleton.get_client().storage_set(key=key, value=value)
	print_command_result("Element successfully set")


#####
# storage rm
#####
@storage_tree.command("rm")
@click.option("-a", "--all", "delete_all", is_flag=True)
@click.option("-d", "discussion_id", nargs=1, type=click.INT, default=0)
@click.argument("keys", nargs=-1, type=click.STRING)
async def storage_delete(delete_all: bool, discussion_id: int, keys: tuple[str]):
	if delete_all:
		element_deleted = False
		if discussion_id:
			async for element in ClientSingleton.get_client().discussion_storage_list(discussion_id=discussion_id):
				element_deleted = True
				await ClientSingleton.get_client().discussion_storage_unset(key=element.key, discussion_id=discussion_id)
				print_command_result(f"Deleted element: {element.key}={element.value}")
			if not element_deleted:
				print_warning_message("No element to delete")
		else:
			async for element in ClientSingleton.get_client().storage_list():
				element_deleted = True
				await ClientSingleton.get_client().storage_unset(element.key)
				print_command_result(f"Deleted element: {element.key}={element.value}")
			if not element_deleted:
				print_warning_message("No element to delete")
		return

	for key in keys:
		if discussion_id:
			previous_value = await ClientSingleton.get_client().discussion_storage_unset(discussion_id=discussion_id, key=key)
			print_command_result(f"Element deleted: {key}: {previous_value}")
		else:
			previous_value = await ClientSingleton.get_client().storage_unset(key)
			print_command_result(f"Element deleted: {key}: {previous_value}")
