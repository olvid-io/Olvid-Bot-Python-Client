import logging
import sys

import asyncclick as click

from olvid import tools, OlvidAdminClient
from ..listen import listen
from ..interactive_tree import interactive_tree
from ..tools.ClientSingleton import ClientSingleton
from ..tools.auto_invitation import auto_invite
from ..tools.cli_tools import print_error_message
from ..tools.click_wrappers import WrapperGroup


#####
# tools
#####
@interactive_tree.group("tools", short_help="advanced commands to debug and manage daemon", cls=WrapperGroup)
def tools_tree():
	pass


#####
# tools listen
#####
@tools_tree.command(name="listen", help="listen notifications received for a specific or every notifications")
@click.option("-i", "--identity", "identity_id", default=-1, type=click.INT, help="Specify a specific identity to listen")
@click.option("-q", "--quiet", "quiet", is_flag=True, help="Hide notification content")
@click.option("-n", "--notifications", "notifications", type=str, help="Coma separated list of notifications to listen (upper snake case: MESSAGE_SEND,MESSAGE_RECEIVED)")
async def listen_cmd(identity_id: int = -1, quiet: bool = False, notifications: str = ""):
	if identity_id == -1:
		identity_id = ClientSingleton.get_current_identity_id()
	await listen(identity_id, quiet=quiet, notifications_to_listen=notifications)
	exit(0)


#####
# tools auto-invite
#####
@tools_tree.command(name="auto-invite", help="add every other identity on this daemon as a contact")
@click.option("-i", "--identity", "identity_id", default=-1, type=click.INT, help="Specify a specific identity to use")
@click.option("-f", "--full", "full", is_flag=True, help="Present every identity in the server to each other (else it only present current identity to others)")
async def auto_invite_cmd(full: bool, identity_id: int = -1):
	if identity_id == -1:
		identity_id = ClientSingleton.get_current_identity_id()
	if not full and identity_id <= 0:
		print_error_message("Specify identity to use or --full flag")
		return
	await auto_invite(identity_id, ClientSingleton.get_client(), full=full)


#####
# tools auto-accept
#####
@tools_tree.command(name="auto-accept", help="accept every pending and incoming invitations")
@click.option("-i", "--identity", "identity_id", default=-1, type=click.INT, help="Specify a specific identity to use")
@click.option("-f", "--full", "full", is_flag=True, help="Accept every invitation for every identity")
async def auto_accept_cmd(identity_id: int, full: bool):
	# redirect autoInvitationBot logging to stdout
	handler = logging.StreamHandler(sys.stdout)
	handler.setLevel(logging.INFO)
	tools_logger = logging.getLogger(tools.__package__)
	tools_logger.setLevel(logging.INFO)
	tools_logger.addHandler(handler)

	if identity_id == -1:
		identity_id = ClientSingleton.get_current_identity_id()
	if not full and identity_id <= 0:
		print_error_message("Specify identity to use or --full flag")
		return
	if full:
		bots: list[tools.AutoInvitationBot] = []
		async for identity in ClientSingleton.get_client().admin_identity_list():
			bots.append(tools.AutoInvitationBot(parent_client=OlvidAdminClient(identity_id=identity.id)))
		for bot in bots:
			await bot.wait_for_listeners_end()
	else:
		ClientSingleton.set_current_identity_id(identity_id)
		bot = tools.AutoInvitationBot(parent_client=ClientSingleton.get_client())
		await bot.wait_for_listeners_end()
