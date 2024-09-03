import asyncclick as click
from google.protobuf.json_format import Parse, ParseError

from olvid import datatypes
from ..interactive_tree import interactive_tree
from ..tools.ClientSingleton import ClientSingleton
from ..tools.cli_tools import filter_fields_and_print_normal_message, print_error_message
from ..tools.click_wrappers import WrapperGroup

# default permissions
DEFAULT_ADMIN_PERMISSIONS = datatypes.GroupMemberPermissions(admin=True, remote_delete_anything=True,
																edit_or_remote_delete_own_messages=True,
																change_settings=True,
																send_message=True)
DEFAULT_MEMBER_PERMISSIONS = datatypes.GroupMemberPermissions(admin=False, remote_delete_anything=True,
																edit_or_remote_delete_own_messages=True,
																change_settings=False, send_message=True)


#####
# group
#####
@interactive_tree.group("group", help="manage current identity groups", cls=WrapperGroup)
def group_tree():
	pass


#####
# group get
#####
# noinspection PyProtectedMember
@group_tree.command("get", help="list current identity groups")
@click.option("-a", "--all", "get_all", is_flag=True)
@click.argument("group_ids", nargs=-1, type=click.INT)
@click.option("-f", "--fields", "fields", type=str)
@click.option("--filter", "filter_", type=str)
async def group_get(get_all: bool, group_ids: list[int], fields: str, filter_: str = ""):
	# build filter
	group_filter: datatypes.GroupFilter = datatypes.GroupFilter()
	if filter_:
		try:
			parsed_message = Parse(filter_, datatypes.GroupFilter()._to_native(group_filter))
			group_filter = datatypes.GroupFilter._from_native(parsed_message)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	groups: list[datatypes.Group]
	if not group_ids or get_all:
		groups = [group async for group in ClientSingleton.get_client().group_list(filter=group_filter)]
	else:
		groups = [await ClientSingleton.get_client().group_get(group_id=group_id) for group_id in group_ids]

	group_as_strings: list[str] = []
	for group in groups:
		if fields:
			group_as_strings.append(filter_fields_and_print_normal_message(group, fields))
		else:
			group_as_strings.append(await group_to_string(group))

	print(("-" * 20 + "\n").join(group_as_strings))


#####
# group new
#####
@group_tree.group("new", help="create new groups", cls=WrapperGroup)
def group_new_tree():
	pass


#####
# group new standard
#####
@group_new_tree.command("standard", help="create a standard group, where everyone have admin rights")
@click.option("-n", "--name", "group_name", default="")
@click.option("-d", "--description", "group_description", default="")
@click.argument("admin_contact_ids", nargs=-1, type=click.INT, required=False)
async def group_new_standard(admin_contact_ids: tuple[int], group_name: str, group_description: str = "", ):
	group = await ClientSingleton.get_client().group_new_standard_group(
		name=group_name,
		description=group_description,
		admin_contact_ids=list(admin_contact_ids)
	)
	print(await group_to_string(group))


#####
# group new controlled
#####
@group_new_tree.command("controlled", help="create a controlled group with admin and regular members")
@click.option("-n", "--name", "group_name")
@click.option("-d", "--description", "group_description", default="")
@click.argument("contacts_id", nargs=-1, type=click.INT, required=False)
@click.option("-a", "--admin", "admin_contact_ids", multiple=True, type=click.INT)
async def group_new_controlled(contacts_id: tuple[int], admin_contact_ids: tuple[int], group_name: str, group_description: str = "", ):
	group = await ClientSingleton.get_client().group_new_controlled_group(
		name=group_name,
		description=group_description,
		contact_ids=list(contacts_id),
		admin_contact_ids=list(admin_contact_ids)
	)
	print(await group_to_string(group))


#####
# group new read-only
#####
@group_new_tree.command("read-only", help="create a read-only group where only admin members can post messages")
@click.option("-n", "--name", "group_name")
@click.option("-d", "--description", "group_description", default="")
@click.option("-a", "--admin", "admin_contact_ids", multiple=True, type=click.INT)
@click.argument("contacts_id", nargs=-1, type=click.INT, required=False)
async def group_new_read_only(contacts_id: tuple[int], admin_contact_ids: tuple[int], group_name: str, group_description: str = "", ):
	group = await ClientSingleton.get_client().group_new_read_only_group(
		name=group_name,
		description=group_description,
		contact_ids=list(contacts_id),
		admin_contact_ids=list(admin_contact_ids)
	)
	print(await group_to_string(group))


#####
# group new advanced
#####
@group_new_tree.command("advanced", help="create an advanced group with custom permissions for members (not recommended)")
@click.option("-n", "--name", "group_name")
@click.option("-d", "--description", "group_description", default="")
@click.argument("contacts_id", nargs=-1, type=click.INT, required=False)
@click.option("--read-only", "read_only", is_flag=True, help="By default new members won't have the send_message permission")
@click.option("--do-not-remote-delete", "do_not_remote_delete", is_flag=True, help="By default do not give remote delete permission to future members")
@click.option("--remote-delete-admins", "remote_delete_admins", is_flag=True, help="By default give future admins remote delete permission")
@click.option("--remote-delete-everyone", "remote_delete_everyone", is_flag=True, help="By default give future member remote delete permission")
@click.option("-a", "--admin", "admin", is_flag=True, help="Set members as admin")
@click.option("-s", "--send-message", "send_message", is_flag=True, help="Let members send message")
@click.option("-e", "--edit", "edit", is_flag=True, help="Let members edit or delete their messages")
@click.option("-r", "--remote-delete", "remote_delete", is_flag=True, help="Let members remote delete every messages")
@click.option("-c", "--change-settings", "change_settings", is_flag=True, help="Let members change discussion settings")
async def group_new_advanced(contacts_id: tuple[int], read_only: bool, do_not_remote_delete: bool, remote_delete_admins: bool, remote_delete_everyone: bool, group_name: str, group_description: str, admin: bool, send_message: bool, edit: bool, remote_delete: bool, change_settings: bool):
	if (do_not_remote_delete and (remote_delete_admins or remote_delete_everyone)) or (remote_delete_admins and remote_delete_everyone):
		print_error_message("Can only pass one global remote delete parameter option")
		return

	rd = datatypes.Group.AdvancedConfiguration.RemoteDelete
	global_remote_delete: rd = rd.REMOTE_DELETE_UNSPECIFIED
	if do_not_remote_delete:
		global_remote_delete = rd.REMOTE_DELETE_NOBODY
	elif remote_delete_admins:
		global_remote_delete = rd.REMOTE_DELETE_ADMINS
	elif remote_delete_everyone:
		global_remote_delete = rd.REMOTE_DELETE_EVERYONE

	advanced_configuration: datatypes.Group.AdvancedConfiguration = datatypes.Group.AdvancedConfiguration(
		read_only=read_only,
		remote_delete=global_remote_delete
	)

	members: list[datatypes.GroupMember] = []
	for cid in contacts_id:
		members.append(datatypes.GroupMember(contact_id=cid, permissions=datatypes.GroupMemberPermissions(
			admin=admin,
			send_message=send_message,
			remote_delete_anything=edit,
			edit_or_remote_delete_own_messages=remote_delete,
			change_settings=change_settings
		)))

	group = await ClientSingleton.get_client().group_new_advanced_group(
		name=group_name,
		description=group_description,
		advanced_configuration=advanced_configuration,
		members=members,
	)
	print(await group_to_string(group))


#####
# group disband
#####
@group_tree.command("disband", help="disband a group where you have admin permissions")
@click.argument("group_id", type=click.INT)
async def group_disband(group_id):
	group = await ClientSingleton.get_client().group_disband(group_id)
	print(await group_to_string(group))


#####
# group leave
#####
@group_tree.command("leave", help="leave a group")
@click.argument("group_id", type=click.INT)
async def group_leave(group_id):
	group = await ClientSingleton.get_client().group_leave(group_id)
	print(await group_to_string(group))


#####
# group update
#####
@group_tree.command("update", help="update group details and/or members (advanced command)")
@click.option("-n", "--name", "group_name", type=str, default="")
@click.option("-d", "--description", "group_description", type=str, default="")
@click.option("-am", "--add-member", "add_members", multiple=True, type=click.INT)
@click.option("-aam", "--add-admin-member", "add_admin_members", multiple=True, type=click.INT)
@click.option("-dm", "--delete-member", "delete_members", multiple=True, type=click.INT)
@click.argument("group_id", type=click.INT, required=True)
async def group_update(group_id: int, group_name: str, group_description: str, add_admin_members: tuple[int],
						add_members: tuple[int], delete_members: tuple[int]):
	group = await ClientSingleton.get_client().group_get(group_id=group_id)
	if group_name:
		group.name = group_name
	if group_description:
		group.description = group_description

	# add admin members
	for member_id in add_admin_members:
		group.members.append(datatypes.GroupMember(contact_id=member_id, permissions=DEFAULT_ADMIN_PERMISSIONS))

	# add members
	for member_id in add_members:
		group.members.append(datatypes.GroupMember(contact_id=member_id, permissions=DEFAULT_MEMBER_PERMISSIONS))

	# remove members
	group.members = list(filter(lambda m: m.contact_id not in delete_members, group.members))

	updated_group = await ClientSingleton.get_client().group_update(group=group)
	print(await group_to_string(updated_group))


#####
# group admin
#####
@group_tree.command("admin", help="manage group admins")
@click.option("-pa", "--promote-admin", "admins_to_add", multiple=True, type=click.INT)
@click.option("-da", "--demote-admin", "admins_to_remove", multiple=True, type=click.INT)
@click.option("-ppa", "--pending-promote-admin", "pending_admins_to_add", multiple=True, type=click.INT)
@click.option("-pda", "--pending-demote-admin", "pending_admins_to_remove", multiple=True, type=click.INT)
@click.argument("group_id", type=click.INT, required=True)
async def group_update(group_id: int, admins_to_add: tuple[int], admins_to_remove: tuple[int],
						pending_admins_to_add: tuple[int], pending_admins_to_remove: tuple[int]):
	group = await ClientSingleton.get_client().group_get(group_id=group_id)

	for member in group.members:
		if member.contact_id in admins_to_add:
			member.permissions = DEFAULT_ADMIN_PERMISSIONS
		if member.contact_id in admins_to_remove:
			member.permissions = DEFAULT_MEMBER_PERMISSIONS

	for pending in group.pending_members:
		if pending.pending_member_id in pending_admins_to_add:
			pending.permissions = DEFAULT_ADMIN_PERMISSIONS
		if pending.pending_member_id in pending_admins_to_remove:
			pending.permissions = DEFAULT_MEMBER_PERMISSIONS

	updated_group = await ClientSingleton.get_client().group_update(group=group)
	print(await group_to_string(updated_group))


#####
# group permissions
#####
@group_tree.command("permissions", help="manage a group member permissions")
@click.option("-a", "--admin", type=bool)
@click.option("-rda", "--remote-delete-anything", "remote_delete_anything", type=bool, default=False)
@click.option("-erm", "--edit-or-remote-delete-own-messages", "edit_or_remote_delete_own_messages", type=bool,
				default=False)
@click.option("-cs", "--change-settings", "change_settings", type=bool, default=False)
@click.option("-sm", "--send-message", "send_message", type=bool, default=False)
@click.argument("group_id", type=click.INT, required=True)
@click.argument("contact_id", type=click.INT, required=True)
async def group_update(group_id: int, contact_id: int, admin: bool, remote_delete_anything: bool,
						edit_or_remote_delete_own_messages: bool, change_settings: bool, send_message: bool):
	group = await ClientSingleton.get_client().group_get(group_id=group_id)

	found = False
	for member in group.members:
		if member.contact_id == contact_id:
			member.permissions = datatypes.GroupMemberPermissions(
				admin=admin, remote_delete_anything=remote_delete_anything,
				edit_or_remote_delete_own_messages=edit_or_remote_delete_own_messages,
				change_settings=change_settings, send_message=send_message)
			found = True

	if not found:
		raise click.exceptions.BadArgumentUsage("Member not found")

	updated_group = await ClientSingleton.get_client().group_update(group=group)
	print(await group_to_string(updated_group))


#####
# group photo
#####
@group_tree.group("photo", help="get/update group photos", cls=WrapperGroup)
def group_photo_tree():
	pass


#####
# group photo set
#####
@group_photo_tree.command("set")
@click.argument("group_id", required=True, type=click.INT)
@click.argument("photo_path", required=True, type=click.STRING)
async def group_photo_set(group_id: int, photo_path: str):
	try:
		open(photo_path, "rb")
	except IOError:
		raise click.exceptions.FileError("File not found: " + photo_path)

	updated_group = await ClientSingleton.get_client().group_set_photo(group_id, photo_path)
	print(await group_to_string(updated_group))


#####
# group photo unset
#####
@group_photo_tree.command("unset")
@click.argument("group_id", required=True, type=click.INT)
async def group_photo_unset(group_id: int):
	updated_group = await ClientSingleton.get_client().group_unset_photo(group_id=group_id)
	print(await group_to_string(updated_group))


#####
# tools
#####
async def group_to_string(group: datatypes.Group) -> str:
	def permission_to_string(permission: datatypes.GroupMemberPermissions) -> str:
		permissions: list[str] = []
		if permission.admin:
			permissions.append("admin")
		if permission.send_message:
			permissions.append("send-message")
		if permission.edit_or_remote_delete_own_messages:
			permissions.append("edit-or-remote-delete-own")
		if permission.remote_delete_anything:
			permissions.append("remote-delete-anything")
		if permission.change_settings:
			permissions.append("change-settings")
		return "(" + ", ".join(permissions) + ")"
	s = f"{group.id}:{' ' + group.name if group.name else ''} (type: {group.type.name}){' (has a photo)' if group.has_a_photo else ''}\n"
	s += str(group.advanced_configuration) + "\n" if group.type == datatypes.Group.Type.TYPE_ADVANCED else ''
	s += f"{group.description}\n" if group.description else ""
	s += f"(has photo)\n" if group.has_a_photo else ""
	s += f"permissions: {permission_to_string(group.own_permissions)}\n"
	if group.members:
		s += "Members:\n"
	for member in group.members:
		# noinspection PyProtectedMember
		s += f"\t{member.contact_id}: {(await group._client.contact_get(contact_id=member.contact_id)).display_name}: {permission_to_string(member.permissions)}\n"
	if group.pending_members:
		s += "Pending Members:\n"
	for pending_member in group.pending_members:
		s += f"\t{pending_member.contact_id}: {pending_member.display_name}: {permission_to_string(pending_member.permissions)}\n"
	return s
