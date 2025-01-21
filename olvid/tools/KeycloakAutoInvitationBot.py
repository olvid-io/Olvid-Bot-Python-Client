import asyncio

from ..core.OlvidClient import OlvidClient
from .. import datatypes
from .logger import tools_logger


class KeycloakAutoInvitationBot(OlvidClient):
	LAST_LIST_TIMESTAMP_STORAGE_KEY = "keycloak-auto-invitation-bot-last-list-timestamp"

	def __init__(self, parent_client: OlvidClient = None, cron_interval_min: int = 5):
		super().__init__(parent_client=parent_client)

		self.add_background_task(self._cron_task(cron_interval_min))

	async def add_every_new_keycloak_member(self):
		last_list_timestamp_str: str = await self.storage_get(self.LAST_LIST_TIMESTAMP_STORAGE_KEY)
		last_list_timestamp: Optional[int] = int(last_list_timestamp_str) if last_list_timestamp_str else None

		# request all / new keycloak users that are not already contacts
		new_last_list_timestamp = last_list_timestamp
		tools_logger.info(f"{self.__class__.__name__}: last list timestamp: {last_list_timestamp}")
		async for users, new_last_list_timestamp in self.keycloak_user_list(last_list_timestamp=last_list_timestamp if last_list_timestamp else None, filter=datatypes.KeycloakUserFilter(contact=datatypes.KeycloakUserFilter.Contact.CONTACT_IS_NOT)):
			for user in users:
				user: datatypes.KeycloakUser
				tools_logger.info(f"{self.__class__.__name__}: new keycloak user: {user.display_name}")
				await self.keycloak_add_user_as_contact(keycloak_id=user.keycloak_id)

		# update last_list_timestamp in storage
		await self.storage_set(self.LAST_LIST_TIMESTAMP_STORAGE_KEY, str(new_last_list_timestamp))

	async def _cron_task(self, interval_min: int):
		while True:
			tools_logger.info(f"{self.__class__.__name__}: _cron_task: start cron task")
			try:
				await self.add_every_new_keycloak_member()
			except Exception:
				tools_logger.exception(f"{self.__class__.__name__}: _cron_task")
			await asyncio.sleep(interval_min * 60)
