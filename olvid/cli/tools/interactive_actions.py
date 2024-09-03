import asyncio
from typing import Optional

import readline
import asyncclick as click
import grpc.aio

from .ClientSingleton import ClientSingleton
from ...core.OlvidAdminClient import OlvidAdminClient
from ...datatypes import datatypes
from ...listeners import ListenersImplementation as listeners
from .cli_tools import print_warning_message

def interactive_command(func):
	def wrapper(*args, **kwargs):
		if ClientSingleton.is_script_mode_enabled():
			print_warning_message("WARNING: launching interactive command in script mode")
		try:
			# disable history in interactive mode
			readline.set_auto_history(False)
			return func(*args, **kwargs)
		finally:
			# re-enable history in interactive mode
			readline.set_auto_history(True)
	return wrapper


# raise AbortException
@interactive_command
def ask_question_with_context(question: str, prompt: str = None, fg_color: str = None, bg_color: str = None) -> bool:
	if prompt:
		prompt += " > "
	if prompt and (fg_color or bg_color):
		prompt = click.style(prompt, fg=fg_color, bg=bg_color)
	return click.prompt(prompt + question, type=bool, prompt_suffix=" (y/N)\n>")


@interactive_command
def prompt_with_context(question: str, prompt: str = None, fg_color: str = None, bg_color: str = None) -> str:
	if prompt:
		prompt += " > "
	if prompt and (fg_color or bg_color):
		prompt = click.style(prompt, fg=fg_color, bg=bg_color)
	return click.prompt(prompt + question, type=str, prompt_suffix="\n>")


def print_with_context(text: str, prompt: str = None, fg_color: str = None, bg_color: str = None):
	if prompt:
		prompt += " > "
	if prompt and (fg_color or bg_color):
		prompt = click.style(prompt, fg=fg_color, bg=bg_color)
	print(prompt + text)


# return new discussion
async def contact_new(identity_id: int, prompt: str = None, fg_color: str = None, bg_color: str = None) -> Optional[datatypes.Discussion]:
	identity: datatypes.Identity = await ClientSingleton.get_client().admin_identity_admin_get(identity_id=identity_id)
	print_with_context(f"Send an invitation to this invitation link: {identity.invitation_url}", prompt=prompt, fg_color=fg_color, bg_color=bg_color)

	# create invitation received listener
	client: OlvidAdminClient = OlvidAdminClient(identity_id=identity_id)
	invitations: list[datatypes.Invitation] = []
	client.add_listener(listeners.InvitationReceivedListener(handler=lambda i: invitations.append(i), count=1, checkers=[lambda i: i.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_TO_ACCEPT]))

	# create discussion new listener
	discussion_new_client = OlvidAdminClient(identity_id=identity_id)
	discussions: list[datatypes.Discussion] = []
	discussion_new_client.add_listener(listeners.DiscussionNewListener(handler=lambda i: discussions.append(i), count=1))

	# wait for invitation to arrive
	await client.wait_for_listeners_end()
	invitation: datatypes.Invitation = invitations[0]
	await client.invitation_accept(invitation_id=invitation.id)
	invitation = await invitation.wait_for(listener_class=listeners.InvitationUpdatedListener, extra_checker=lambda i, s: i.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE)

	# enter other device sas
	while True:
		sas_code: str = prompt_with_context("Please enter sas code displayed on the other device", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
		try:
			await client.invitation_sas(invitation_id=invitation.id, sas=sas_code)
		except grpc.aio.AioRpcError:
			print_with_context("Invalid sas code", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
			continue

		await asyncio.sleep(0.1)
		invitation = await client.invitation_get(invitation_id=invitation.id)
		if invitation.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE:
			prompt_with_context("Invalid sas code", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
		else:
			break

	# show your sas and wait for invitation deletion
	print_with_context(f"Please enter this sas code on the other device: {invitation.sas}", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
	await invitation.wait_for(listeners.InvitationDeletedListener)

	await discussion_new_client.stop()
	if discussions:
		return discussions[0]
	else:
		return None


async def invitation_new(identity_id: int, invitation: datatypes.Invitation, prompt: str = None, fg_color: str = None, bg_color: str = None) -> Optional[datatypes.Discussion]:
	client: OlvidAdminClient = OlvidAdminClient(identity_id=identity_id)

	# create discussion new listener
	discussion_new_client = OlvidAdminClient(identity_id=identity_id)
	discussions: list[datatypes.Discussion] = []
	discussion_new_client.add_listener(listeners.DiscussionNewListener(handler=lambda i: discussions.append(i), count=1))

	# wait for other identity to accept
	print_with_context("Waiting for other device to accept invitation ...", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
	invitation = await invitation.wait_for(listener_class=listeners.InvitationUpdatedListener, extra_checker=lambda i, s: i.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE)

	# set other identity sas
	while True:
		sas_code: str = prompt_with_context("Please enter sas code displayed on the other device", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
		try:
			await client.invitation_sas(invitation_id=invitation.id, sas=sas_code)
		except grpc.aio.AioRpcError:
			print_with_context("Invalid sas code", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
			continue

		await asyncio.sleep(0.1)
		invitation = await client.invitation_get(invitation_id=invitation.id)
		if invitation.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE:
			prompt_with_context("Invalid sas code", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
		else:
			break

	# show your sas and wait for invitation deletion
	print_with_context(f"Please enter this sas code on the other device: {invitation.sas}", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
	await invitation.wait_for(listeners.InvitationDeletedListener)

	await discussion_new_client.stop()
	if discussions:
		return discussions[0]
	else:
		return None
