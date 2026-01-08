
import asyncclick as click

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
@click.option("--filter", "filter_", type=str)
@click.option("--count", "-c", "count", type=int, default=0)
@click.option("-i", "--identity", "identity_id", default=-1, type=click.INT, help="Specify a specific identity to listen")
@click.option("-q", "--quiet", "quiet", is_flag=True, help="Hide notification content")
@click.option("-v", "--verbose", "verbose", is_flag=True, help="Show notification full content")
@click.option("-n", "--notifications", "notifications", type=str, help="Coma separated list of notifications to listen (upper snake case: MESSAGE_SEND,MESSAGE_RECEIVED)")
async def listen_cmd(identity_id: int = -1, verbose: bool = False, quiet: bool = False, notifications: str = "", filter_=None, count=0):
	if identity_id == -1:
		identity_id = ClientSingleton.get_current_identity_id()
	await listen(identity_id, verbose=verbose, quiet=quiet, notifications_to_listen=notifications, filter_=filter_, count=count)
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
# tools daemon-version
#####
@tools_tree.command(name="daemon-version", help="show daemon version")
async def auto_accept_cmd():
	print(await ClientSingleton.get_client().daemon_version())
