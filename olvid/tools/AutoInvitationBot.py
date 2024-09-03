from grpc.aio import AioRpcError

from .logger import tools_logger
from ..core.OlvidClient import OlvidClient
from ..core.OlvidBot import OlvidBot
from .. import datatypes


class AutoInvitationBot(OlvidBot):
	def __init__(self, parent_client: OlvidClient = None):
		super().__init__(parent_client=parent_client)

		# accept pending invitations (need a background task)
		async def accept_invitations_task():
			try:
				async for invitation in self.invitation_list():
					await self.accept_invitation(invitation)
			except AioRpcError as rpc_error:
				tools_logger.error(f"{self.name}: accept invitation on start task: {rpc_error.code()}: {rpc_error.details()}")
			except Exception:
				tools_logger.exception(f"{self.name}: accept invitation on start task: unexpected error")

		self.add_background_task(coroutine=accept_invitations_task(), name=f"{self.__class__.__name__}-accept_invitations_task")

	async def on_invitation_received(self, invitation: datatypes.Invitation):
		await self.accept_invitation(invitation=invitation)

	async def accept_invitation(self, invitation: datatypes.Invitation):
		if invitation.status in [
			datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_TO_ACCEPT,
			datatypes.Invitation.Status.STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT,
			datatypes.Invitation.Status.STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT,
			datatypes.Invitation.Status.STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT]:
			tools_logger.info(f"{self.__class__.__name__}: invitation accepted: {invitation.id}: {invitation.status}")
			await self.invitation_accept(invitation_id=invitation.id)
