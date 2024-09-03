import datetime
from typing import Optional

from ..core.OlvidBot import OlvidBot
from ..listeners.ListenersImplementation import MessageReceivedListener, MessageSentListener
from .. import datatypes


class DiscussionRetentionPolicyBot(OlvidBot):
	def __init__(self, retention_delay_s: int = None, discussion_retention_number: int = None, global_retention_number: int = None):
		super().__init__()

		self.retention_delay_s: Optional[int] = retention_delay_s
		self.discussion_retention_number: Optional[int] = discussion_retention_number
		self.global_retention_number: Optional[int] = global_retention_number

		self.add_listener(listener=MessageReceivedListener(handler=self.message_received_handler))
		self.add_listener(listener=MessageSentListener(handler=self.message_sent_handler))

		# on start clean everything
		async def start_task():
			await self._clean_globally()
			async for d in self.discussion_list():
				await self._clean_discussion_messages(d.id)

		self.add_background_task(start_task())

	# delete every received messages
	async def message_received_handler(self, message: datatypes.Message):
		if self.retention_delay_s or self.discussion_retention_number:
			await self._clean_discussion_messages(message.discussion_id)
		if self.global_retention_number:
			await self._clean_globally()

	async def message_sent_handler(self, message: datatypes.Message):
		if self.retention_delay_s or self.discussion_retention_number:
			await self._clean_discussion_messages(message.discussion_id)
		if self.global_retention_number:
			await self._clean_globally()

	async def _clean_discussion_messages(self, discussion_id: int):
		discussion_messages: list[datatypes.Message] = [m async for m in self.message_list(filter=datatypes.MessageFilter(discussion_id=discussion_id))]
		messages_to_delete: set[datatypes.Message] = set()

		if self.retention_delay_s is not None:
			now_ms: int = round(datetime.datetime.now().timestamp() * 1000)
			for message in discussion_messages:
				if message.timestamp < now_ms - self.retention_delay_s * 1000:
					messages_to_delete.add(message)

		if self.discussion_retention_number is not None:
			if len(discussion_messages) > self.discussion_retention_number:
				messages_to_delete.update(discussion_messages[:-self.discussion_retention_number])

		for message_to_delete in messages_to_delete:
			await self.message_delete(message_id=message_to_delete.id)

	async def _clean_globally(self):
		all_messages: list[datatypes.Message] = [m async for m in self.message_list()]

		if self.global_retention_number:
			if len(all_messages) > self.global_retention_number:
				for message_to_delete in all_messages[:-self.global_retention_number]:
					await self.message_delete(message_id=message_to_delete.id)
