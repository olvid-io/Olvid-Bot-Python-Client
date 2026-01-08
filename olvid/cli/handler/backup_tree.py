import asyncclick as click
from datetime import datetime

from olvid import datatypes
from ..interactive_tree import interactive_tree
from ..tools.ClientSingleton import ClientSingleton
from ..tools.cli_tools import print_normal_message, print_command_result, print_error_message
from ..tools.click_wrappers import WrapperGroup


#####
# backup
#####
@interactive_tree.group("backup", short_help="manage your daemon backups", cls=WrapperGroup)
async def backup_tree():
	pass

#####
# backup get
#####
@backup_tree.command("get", help="list backed up profiles and available snapshots")
@click.argument("backup_key", required=True, type=str)
async def backup_get(backup_key: str):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage backups when impersonating a non admin key")
		return

	backup: datatypes.Backup = await ClientSingleton.get_client().admin_backup_get(backup_key=backup_key)
	print(f"=== Admin backup ===")
	print(f"admin_client_key_count: {backup.admin_backup.admin_client_key_count}")
	print(f"storage_elements_count: {backup.admin_backup.storage_elements_count}")

	for backup_profile in backup.profile_backups:
		print(f"=== {backup_profile.profile_display_name} (can be restored: {'❌' if backup_profile.already_exists_locally else '✅'}) {'(keycloak managed)'if backup_profile.keycloak_managed else ''} ===")
		snapshots: list[str] = []
		for snapshot in backup_profile.snapshots:
			snapshots.append(f"""  id: {snapshot.id}
  contact_count: {snapshot.contact_count}
  group_count: {snapshot.group_count}
  client_key_count: {snapshot.client_key_count}
  storage_elements_count: {snapshot.storage_elements_count}
  settings: {snapshot.identity_settings}
  timestamp: {datetime.fromtimestamp(snapshot.timestamp/1000).isoformat()}""")
		print("\n  -----\n".join(snapshots))

#####
# backup now
#####
@backup_tree.command("now", help="start a full backup now")
async def backup_now():
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage backups when impersonating a non admin key")
		return

	await ClientSingleton.get_client().admin_backup_now()
	print_command_result(f"Finished backup", "")

#####
# backup restore
#####
@backup_tree.group("restore", short_help="restore an entire backup on a new daemon or only specific parts", cls=WrapperGroup)
async def backup_restore_tree():
	pass

#####
# backup restore daemon
#####
@backup_restore_tree.command("daemon", help="restore an entire backup on blank daemon instance")
@click.argument("backup_key", required=True, type=str)
@click.option("-n", "--device-name", "device_name", default=None, type=click.STRING, help="Specify this new daemon instance name")
async def backup_restore_daemon(backup_key: str, device_name: str):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage backups when impersonating a non admin key")
		return

	response = await ClientSingleton.get_client().admin_backup_restore_daemon(backup_key=backup_key, new_device_name=device_name)

	full_result: str = f"Restored identities:\n" + "\n".join([str(i) for i in response.restored_identities]) + "\n"
	full_result += f"Restored admin client keys:\n" + "\n".join(f"- {c.name}" for c in response.restored_admin_client_keys) + "\n"
	full_result += f"Restored client keys:\n" + "\n".join(f"- {c.name}" for c in response.restored_client_keys)

	script_result: str = "\n".join([str(i.id) for i in response.restored_identities])

	print_command_result(full_result, script_result)

#####
# backup restore admin
#####
@backup_restore_tree.command("admin", help="restore admin backup only (admin client keys and storage)")
@click.argument("backup_key", required=True, type=str)
async def backup_restore_admin(backup_key: str):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage backups when impersonating a non admin key")
		return

	restored_admin_client_keys: list[datatypes.ClientKey] = await ClientSingleton.get_client().admin_backup_restore_admin_backup(backup_key=backup_key)
	print_command_result(f"Restored admin client keys:\n" + "\n".join(f"- {c.name}" for c in restored_admin_client_keys), str(len(restored_admin_client_keys)))

#####
# backup restore profile
#####
@backup_restore_tree.command("profile", help="restore a specific profile snapshot")
@click.argument("backup_key", required=True, type=str)
@click.argument("snapshot_id", required=True, type=str)
async def backup_restore_profile(backup_key: str, snapshot_id: str):
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage backups when impersonating a non admin key")
		return

	response = await ClientSingleton.get_client().admin_backup_restore_profile_snapshot(backup_key=backup_key, id=snapshot_id)
	print_command_result(f"Restored identity: {response.restored_identity}", str(response.restored_identity.id))

#####
# backup key
#####
@backup_tree.group("key", short_help="manage your daemon backup key", cls=WrapperGroup)
async def backup_key_tree():
	pass

#####
# backup key get
#####
@backup_key_tree.command("get", help="get current backup key (this key is common for every identity on this daemon)")
async def backup_key_get():
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage backups when impersonating a non admin key")
		return

	backup_key: str = await ClientSingleton.get_client().admin_backup_key_get()
	print_normal_message(backup_key, backup_key)

#####
# backup key renew
#####
@backup_key_tree.command("renew", help="revoke current backup key and generate a new one")
async def backup_key_renew():
	if not ClientSingleton.is_client_admin():
		print_error_message("Cannot manage backups when impersonating a non admin key")
		return

	backup_key: str = await ClientSingleton.get_client().admin_backup_key_renew()
	print_normal_message(backup_key, backup_key)
