import asyncio
from typing import Optional

import readline
import asyncclick as click

from .ClientSingleton import ClientSingleton
from ...core.OlvidAdminClient import OlvidAdminClient
from ...datatypes import datatypes
from ...listeners import ListenersImplementation as listeners
from ...core import errors
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
async def ask_question_with_context(question: str, prompt: str = None, fg_color: str = None, bg_color: str = None) -> bool:
	if prompt:
		prompt += " > "
	if prompt and (fg_color or bg_color):
		prompt = click.style(prompt, fg=fg_color, bg=bg_color)
	return await click.prompt(prompt + question, type=bool, prompt_suffix=" (y/N)\n>")


@interactive_command
async def prompt_with_context(question: str, prompt: str = None, fg_color: str = None, bg_color: str = None) -> str:
	if prompt:
		prompt += " > "
	if prompt and (fg_color or bg_color):
		prompt = click.style(prompt, fg=fg_color, bg=bg_color)
	return await click.prompt(prompt + question, type=str, prompt_suffix="\n>")


def print_with_context(text: str, prompt: str = None, fg_color: str = None, bg_color: str = None):
	if prompt:
		prompt += " > "
	if prompt and (fg_color or bg_color):
		prompt = click.style(prompt, fg=fg_color, bg=bg_color)
	print(prompt + text)


# show invitation link and wait for an invitation to arrive to complete it interactively
async def contact_new(identity_id: int, prompt: str = None, fg_color: str = None, bg_color: str = None) -> Optional[datatypes.Discussion]:
	identity: datatypes.Identity = await ClientSingleton.get_client().admin_identity_admin_get(identity_id=identity_id)
	print_with_context(f"Send an invitation to this invitation link: {identity.invitation_url}", prompt=prompt, fg_color=fg_color, bg_color=bg_color)

	# create invitation received listener
	client: OlvidAdminClient = OlvidAdminClient(identity_id=identity_id)
	invitations: list[datatypes.Invitation] = []
	client.add_listener(listeners.InvitationReceivedListener(handler=lambda i: invitations.append(i), count=1, filter=datatypes.InvitationFilter(status=datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_TO_ACCEPT)))
	await client.wait_for_listeners_end()

	return await handle_invitation_interactively(client=client, invitation=invitations[0], prompt=prompt, fg_color=fg_color, bg_color=bg_color)


# send an invitation and complete it interactively
async def invitation_new(identity_id: int, invitation: datatypes.Invitation, prompt: str = None, fg_color: str = None, bg_color: str = None) -> Optional[datatypes.Discussion]:
	client: OlvidAdminClient = OlvidAdminClient(identity_id=identity_id)
	return await handle_invitation_interactively(client=client, invitation=invitation, prompt=prompt, fg_color=fg_color, bg_color=bg_color)


# a loop to complete interactively an invitation process
async def handle_invitation_interactively(client: OlvidAdminClient, invitation: datatypes.Invitation, prompt: str = None, fg_color: str = None, bg_color: str = None) -> Optional[datatypes.Discussion]:
	# create discussion new listener
	discussion_new_client = OlvidAdminClient(identity_id=client.current_identity_id)
	discussions: list[datatypes.Discussion] = []
	discussion_new_client.add_listener(listeners.DiscussionNewListener(handler=lambda i: discussions.append(i), count=1))

	first_sas: bool = True
	while True:
		# refresh invitation, stop loop if invitation was deleted
		try:
			invitation = await client.invitation_get(invitation_id=invitation.id)
		except errors.NotFoundError:
			break
		if invitation.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_TO_ACCEPT:
			await client.invitation_accept(invitation_id=invitation.id)
			await asyncio.sleep(0.1)
		elif invitation.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_IT_TO_ACCEPT:
			print_with_context("Waiting for other device to accept invitation ...", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
			invitation = await invitation.wait_for_update(client=client)
		elif invitation.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_IT_FOR_SAS_EXCHANGE:
			print_with_context(f"Please enter this code on the other device: {invitation.sas}", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
			update_or_delete_client = OlvidAdminClient(identity_id=client.current_identity_id)
			update_or_delete_client.add_listener(listeners.InvitationUpdatedListener(handler=lambda i, pi: update_or_delete_client.stop(), invitation_ids=[invitation.id]))
			update_or_delete_client.add_listener(listeners.InvitationDeletedListener(handler=lambda i: update_or_delete_client.stop(), invitation_ids=[invitation.id]))
			await update_or_delete_client.wait_for_listeners_end()
		elif invitation.status == datatypes.Invitation.Status.STATUS_INVITATION_STATUS_IN_PROGRESS:
			invitation = await invitation.wait_for_update(client=client)
		elif invitation.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE:
			if not first_sas:
				print_with_context("Invalid sas code", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
			if invitation.sas:
				print_with_context(f"Your code: {invitation.sas}", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
			sas_code: str = await prompt_with_context("Please enter code displayed on the other device", prompt=prompt, fg_color=fg_color, bg_color=bg_color)
			try:
				await client.invitation_sas(invitation_id=invitation.id, sas=sas_code)
			except errors.AioRpcError:
				pass
			first_sas = False
			await asyncio.sleep(0.1)

	await discussion_new_client.stop()
	return discussions[0] if discussions else None
