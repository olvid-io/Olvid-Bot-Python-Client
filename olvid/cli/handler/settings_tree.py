from ..interactive_tree import interactive_tree
from ..tools.cli_tools import *
from ..tools.click_wrappers import WrapperGroup

#####
# settings
#####
@interactive_tree.group("settings", help="manage your settings", cls=WrapperGroup)
def settings_tree():
	pass

#####
# settings identity
#####
@settings_tree.group("identity", help="manage identity settings", cls=WrapperGroup)
def settings_identity_tree():
	pass


#####
# settings identity invitation
#####
@settings_identity_tree.group("invitation")
def settings_identity_invitation_tree():
	pass


#####
# settings identity invitation get
#####
@settings_identity_invitation_tree.command("get")
@click.option("-f", "--fields", "fields", type=str)
async def identity_settings_invitation_get(fields: str):
	settings = await ClientSingleton.get_client().settings_identity_get()
	if fields:
		filter_fields_and_print_normal_message(settings.invitation, fields)
	else:
		print_normal_message(settings_invitation_to_string(settings.invitation), settings.invitation)

#####
# settings identity invitation set
#####
@settings_identity_invitation_tree.command("set")
@click.option("-a", "--all", "all_opt", is_flag=True)
@click.option("-n", "--none", "none_opt", is_flag=True)
@click.option("-i", "--invitation", "invitation", is_flag=True)
@click.option("-t", "--introduction", "introduction", is_flag=True)
@click.option("-o", "--one-to-one", "one_to_one", is_flag=True)
@click.option("-g", "--group", "group", is_flag=True)
async def identity_settings_invitation_set(all_opt: bool, none_opt: bool, invitation: bool, introduction: bool, one_to_one: bool, group: bool):
	identity_settings: datatypes.IdentitySettings = await ClientSingleton.get_client().settings_identity_get()

	if all_opt:
		invitation: datatypes.IdentitySettings.AutoAcceptInvitation = datatypes.IdentitySettings.AutoAcceptInvitation(
			auto_accept_invitation=True,
			auto_accept_introduction=True,
			auto_accept_one_to_one=True,
			auto_accept_group=True
		)
	elif none_opt:
		invitation: datatypes.IdentitySettings.AutoAcceptInvitation = datatypes.IdentitySettings.AutoAcceptInvitation()
	elif invitation or introduction or one_to_one or group:
		invitation: datatypes.IdentitySettings.AutoAcceptInvitation = datatypes.IdentitySettings.AutoAcceptInvitation(
			auto_accept_invitation=invitation,
			auto_accept_introduction=introduction,
			auto_accept_one_to_one=one_to_one,
			auto_accept_group=group
		)
	else:
		raise click.UsageError("Specify at least one option")

	identity_settings.invitation = invitation

	new_settings = await ClientSingleton.get_client().settings_identity_set(identity_settings=identity_settings)
	print_normal_message(settings_invitation_to_string(new_settings.invitation), new_settings.invitation)

#####
# settings identity keycloak
#####
@settings_identity_tree.group("keycloak")
def settings_identity_keycloak_tree():
	pass


#####
# settings identity keycloak get
#####
@settings_identity_keycloak_tree.command("get")
@click.option("-f", "--fields", "fields", type=str)
async def identity_settings_keycloak_get(fields: str):
	settings = await ClientSingleton.get_client().settings_identity_get()
	if fields:
		filter_fields_and_print_normal_message(settings.keycloak, fields)
	else:
		print_normal_message(settings_keycloak_to_string(settings.keycloak), settings.keycloak)

#####
# settings identity keycloak set
#####
@settings_identity_keycloak_tree.command("set")
@click.option("--auto-invite", "auto_invite", is_flag=True)
async def identity_settings_keycloak_set(auto_invite: bool):
	identity_settings: datatypes.IdentitySettings = await ClientSingleton.get_client().settings_identity_get()

	keycloak: datatypes.IdentitySettings.Keycloak = datatypes.IdentitySettings.Keycloak(
		auto_invite_new_members=auto_invite
	)
	identity_settings.keycloak = keycloak

	new_settings = await ClientSingleton.get_client().settings_identity_set(identity_settings=identity_settings)
	print_normal_message(settings_keycloak_to_string(new_settings.keycloak), new_settings.keycloak)

#####
# settings identity message
#####
@settings_identity_tree.group("message")
def settings_identity_message_tree():
	pass


#####
# settings identity message get
#####
@settings_identity_message_tree.command("get")
@click.option("-f", "--fields", "fields", type=str)
async def identity_settings_message_get(fields: str):
	settings = await ClientSingleton.get_client().settings_identity_get()
	if fields:
		filter_fields_and_print_normal_message(settings.message_retention, fields)
	else:
		print_normal_message(settings_message_to_string(settings.message_retention), settings.message_retention)

#####
# settings identity message set
#####
@settings_identity_message_tree.command("set")
@click.option("-d", "--discussion-count", "discussion_count", help="Set a maximum number of messages to keep in each discussion", type=click.INT, default=0)
@click.option("-g", "--global-count", "global_count", help="Set a maximum number of messages to keep globally", type=click.INT, default=0)
@click.option("-t", "--duration", help="Set a duration after messages are deleted (in seconds)", type=click.INT, default=0)
@click.option("-l", "--locked", help="Delete message in locked discussions", is_flag=True)
@click.option("-p", "--preserve-location", help="Do not delete non-finished location sharing messages", is_flag=True)
@click.option("-n", "--none", "none_opt", is_flag=True)
async def identity_settings_message_set(discussion_count: int, global_count: int, duration: int, locked: bool, preserve_location: bool, none_opt: bool):
	if discussion_count or global_count or duration or locked or preserve_location:
		message_retention: datatypes.IdentitySettings.MessageRetention = datatypes.IdentitySettings.MessageRetention(
			existence_duration=duration,
			discussion_count=discussion_count,
			global_count=global_count,
			clean_locked_discussions=locked,
			preserve_is_sharing_location_messages=preserve_location
		)
	elif none_opt:
		message_retention: datatypes.IdentitySettings.MessageRetention = datatypes.IdentitySettings.MessageRetention()
	else:
		raise click.UsageError("Specify at least one option")

	identity_settings: datatypes.IdentitySettings = await ClientSingleton.get_client().settings_identity_get()
	identity_settings.message_retention = message_retention

	new_settings = await ClientSingleton.get_client().settings_identity_set(identity_settings=identity_settings)
	print_normal_message(settings_message_to_string(new_settings.message_retention), new_settings.message_retention)


#####
# settings discussion
#####
@settings_tree.group("discussion", help="manage discussion settings", cls=WrapperGroup)
def settings_discussion_tree():
	pass


#####
# settings discussion get
#####
@settings_discussion_tree.command("get")
@click.argument("discussion_id", nargs=1, type=click.INT, required=True)
@click.option("-f", "--fields", "fields", type=str)
async def discussion_settings_get(discussion_id: int, fields: str):
	settings = await ClientSingleton.get_client().settings_discussion_get(discussion_id=discussion_id)
	filter_fields_and_print_normal_message(settings, fields)


#####
# settings discussion set
#####
@settings_discussion_tree.command("set")
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
	new_settings = await ClientSingleton.get_client().settings_discussion_set(discussion_settings=settings)
	print_normal_message(new_settings, new_settings)

def settings_invitation_to_string(invitation: datatypes.IdentitySettings.AutoAcceptInvitation):
	return f"""
auto_accept_invitation: {invitation.auto_accept_invitation}
auto_accept_introduction: {invitation.auto_accept_introduction}
auto_accept_group: {invitation.auto_accept_group}
auto_accept_one_to_one: {invitation.auto_accept_one_to_one}
""".strip()

def settings_keycloak_to_string(keycloak: datatypes.IdentitySettings.Keycloak):
	return f"""
auto_invite_new_members: {keycloak.auto_invite_new_members}
""".strip()

def settings_message_to_string(message: datatypes.IdentitySettings.MessageRetention):
	return f"""
discussion_count: {message.discussion_count}
global_count: {message.global_count}
existence_duration: {message.existence_duration}
clean_locked_discussions: {message.clean_locked_discussions}
preserve_is_sharing_location_messages: {message.preserve_is_sharing_location_messages}
""".strip()
