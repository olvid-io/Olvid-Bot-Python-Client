from asyncio import iscoroutine
from typing import Callable, Coroutine, Union, Any

from grpc.aio import AioRpcError

from .logger import tools_logger
from ..core.OlvidClient import OlvidClient
from .. import datatypes
from ..listeners.ListenersImplementation import MessageReceivedListener, MessageSentListener, AttachmentUploadedListener, MessageUploadedListener


class SelfCleaningBot(OlvidClient):
	# with no parameters we clean in and out messages
	# if you specify is_message_for_cleaning parameter we disable in and out clean,
	# we only use is_message_for_cleaning method (so be sure to cover every case).
	def __init__(self, parent_client: OlvidClient = None, clean_inbound_messages: bool = None, clean_outbound_messages: bool = None, is_message_for_cleaning: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]] = None):
		super().__init__(parent_client=parent_client)

		# keep original messages (sent by message_sent notification)
		# then we decrement attachment_number field every time an attachment had been uploaded
		# when every attachment had been sent we delete message and attachment
		self._pending_outbound_messages_by_id: dict[int, datatypes.Message] = {}

		self.is_message_for_cleaning: Callable[[datatypes.Message], Union[Coroutine[Any, Any, bool]]] = self._is_message_for_cleaning_wrapper(is_message_for_cleaning) if is_message_for_cleaning else None
		if self.is_message_for_cleaning and (clean_inbound_messages is not None or clean_outbound_messages is not None):
			raise ValueError("Cannot set is_message_for_cleaning and clean_inbound_messages or clean_outbound_messages")
		self.clean_inbound_messages: bool = clean_inbound_messages if clean_inbound_messages is not None else True if not is_message_for_cleaning else False
		self.clean_outbound_messages: bool = clean_outbound_messages if clean_outbound_messages is not None else True if not is_message_for_cleaning else False

		self.add_listener(listener=MessageReceivedListener(handler=self.message_received_handler))
		self.add_listener(listener=MessageSentListener(handler=self.message_sent_handler))
		self.add_listener(listener=MessageUploadedListener(handler=self.message_uploaded_handler))
		self.add_listener(listener=AttachmentUploadedListener(handler=self.attachment_uploaded_handler))

		# clean on every start
		self.add_background_task(self.clean_on_start_task(client=self, clean_inbound_messages=self.clean_inbound_messages, clean_outbound_messages=self.clean_outbound_messages, is_message_for_cleaning=self.is_message_for_cleaning))

	# this is static to use it even if we do not need a full SelfCleaningBot
	@staticmethod
	async def clean_on_start_task(client: OlvidClient, clean_inbound_messages: bool = None, clean_outbound_messages: bool = None, is_message_for_cleaning: Callable[[datatypes.Message], Union[Coroutine[Any, Any, bool]]] = None):
		try:
			# delete every messages
			deleted_messages_count = 0
			async for message in client.message_list():
				if is_message_for_cleaning:
					if await is_message_for_cleaning(message):
						await client.message_delete(message_id=message.id)
						deleted_messages_count += 1
				elif clean_inbound_messages and message.is_inbound():
					await client.message_delete(message_id=message.id)
					deleted_messages_count += 1
				elif clean_outbound_messages and message.is_outbound():
					await client.message_delete(message_id=message.id)
					deleted_messages_count += 1

			tools_logger.debug(f"{client.__class__.__name__}: start clean: deleted {deleted_messages_count} messages")
		except AioRpcError as rpc_error:
			tools_logger.error(f"{client.__class__.__name__}: clean on start: {rpc_error.code()}: {rpc_error.details()}")
		except Exception:
			tools_logger.exception(f"{client.__class__.__name__}: clean on start: unexpected error")

	# delete every received messages
	async def message_received_handler(self, message: datatypes.Message):
		if self.clean_inbound_messages or (self.is_message_for_cleaning and await self.is_message_for_cleaning(message)):
			try:
				await self.message_delete(message_id=message.id)
			except Exception:
				tools_logger.exception(f"{self.__class__.__name__}: on_message_received: unexpected exception")

	# delete outbound messages when they arrive or when all attachments have been uploaded
	async def message_sent_handler(self, message: datatypes.Message):
		if self.clean_outbound_messages or (self.is_message_for_cleaning and await self.is_message_for_cleaning(message)):
			self._pending_outbound_messages_by_id[message.id.id] = message

	async def message_uploaded_handler(self, message: datatypes.Message):
		try:
			message = self._pending_outbound_messages_by_id.get(message.id.id)
			if not message:
				return
			# wait for attachments to be uploaded before deletion
			if message.attachments_count > 0:
				return

			await self.message_delete(message_id=message.id)
			self._pending_outbound_messages_by_id.pop(message.id.id)
		except Exception:
			tools_logger.exception(f"{self.__class__.__name__}: on_message_uploaded: unexpected exception")

	async def attachment_uploaded_handler(self, attachment: datatypes.Attachment):
		try:
			message = self._pending_outbound_messages_by_id.get(attachment.message_id.id)
			if not message:
				return
			message.attachments_count -= 1

			# all attachments have been uploaded, we can delete the message.
			if message.attachments_count == 0:
				await self.message_delete(message_id=message.id)
				self._pending_outbound_messages_by_id.pop(message.id.id)
		except Exception:
			tools_logger.exception(f"{self.__class__.__name__}: on_attachment_uploaded: unexpected exception")

	@staticmethod
	def _is_message_for_cleaning_wrapper(is_message_for_cleaning: Callable[[datatypes.Message], Union[bool, Coroutine[Any, Any, bool]]]) -> Callable[[datatypes.Message], Union[Coroutine[Any, Any, bool]]]:
		async def wrapper(message: datatypes.Message):
			res = is_message_for_cleaning(message)
			if iscoroutine(res):
				res = await res
			return res
		return wrapper

	####
	# tools
	####
	# use this just after sending a message to manually add it to
	def delete_message_when_uploaded(self, message: datatypes.Message):
		self._pending_outbound_messages_by_id[message.id.id] = message
