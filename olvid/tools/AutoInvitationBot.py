from grpc.aio import AioRpcError

from .logger import tools_logger
from ..core.OlvidClient import OlvidClient
from .. import datatypes


class AutoInvitationBot(OlvidClient):
	def __init__(self, parent_client: OlvidClient = None, accept_group_invitations: bool = True, accept_introductions: bool = True, accept_one_to_one_invitations: bool = True, accept_sas_invitations: bool = True):
		super().__init__(parent_client=parent_client)
		self.accept_group_invitations = accept_group_invitations
		self.accept_introductions = accept_introductions
		self.accept_one_to_one_invitations = accept_one_to_one_invitations
		self.accept_sas_invitations = accept_sas_invitations

		# accept pending invitations (need a background task)
		async def accept_invitations_task():
			try:
				async for invitation in self.invitation_list():
					await self.accept_invitation_if_necessary(invitation)
			except AioRpcError as rpc_error:
				tools_logger.error(f"{self.__class__.__name__}: accept invitation on start task: {rpc_error.code()}: {rpc_error.details()}")
			except Exception:
				tools_logger.exception(f"{self.__class__.__name__}: accept invitation on start task: unexpected error")

		self.add_background_task(coroutine=accept_invitations_task(), name=f"{self.__class__.__name__}-accept_invitations_task")

	async def on_invitation_received(self, invitation: datatypes.Invitation):
		await self.accept_invitation_if_necessary(invitation=invitation)

	async def accept_invitation_if_necessary(self, invitation: datatypes.Invitation):
		# introductions
		if invitation.status == datatypes.Invitation.Status.STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT:
			if self.accept_introductions:
				tools_logger.info(f"{self.__class__.__name__}: introduction accepted: {invitation.id}: {invitation.status}")
				await self.invitation_accept(invitation_id=invitation.id)

		# sas invitation
		elif invitation.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_TO_ACCEPT:
			if self.accept_sas_invitations:
				tools_logger.info(f"{self.__class__.__name__}: sas invitation accepted: {invitation.id}: {invitation.status}")
				await self.invitation_accept(invitation_id=invitation.id)

		# group
		elif invitation.status == datatypes.Invitation.Status.STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT:
			if self.accept_group_invitations:
				tools_logger.info(f"{self.__class__.__name__}: group invitation accepted: {invitation.id}: {invitation.status}")
				await self.invitation_accept(invitation_id=invitation.id)
			else:
				tools_logger.info(f"{self.__class__.__name__}: group invitation declined: {invitation.id}: {invitation.status}")
				await self.invitation_decline(invitation_id=invitation.id)

		# one to one
		elif invitation.status == datatypes.Invitation.Status.STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT:
			if self.accept_one_to_one_invitations:
				tools_logger.info(f"{self.__class__.__name__}: one to one invitation accepted: {invitation.id}: {invitation.status}")
				await self.invitation_accept(invitation_id=invitation.id)
			else:
				tools_logger.info(f"{self.__class__.__name__}: one to one invitation declined: {invitation.id}: {invitation.status}")
				await self.invitation_accept(invitation_id=invitation.id)
