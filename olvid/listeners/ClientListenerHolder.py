from __future__ import annotations

from typing import TYPE_CHECKING

import asyncio
import grpc.aio

from ..core.logger import core_logger, notification_logger

if TYPE_CHECKING:
	from typing import Optional, Set, AsyncIterator, Dict
	from ..internal import types
	from .Notifications import NOTIFICATIONS
	from .GenericNotificationListener import GenericNotificationListener
	from ..core.OlvidClient import OlvidClient


class ClientListenerHolder:
	def __init__(self, client: "OlvidClient"):
		self._client: "OlvidClient" = client

		self._registered_listeners: Dict[str, Set[GenericNotificationListener]] = {}
		self._iterators_tasks: Dict[str, asyncio.Task] = {}
		self._listener_removed_event: asyncio.Event = asyncio.Event()

		self._stream_listener_task: Optional[asyncio.Task] = None

	#####
	# Public api
	#####
	async def await_task(self):
		if self._stream_listener_task is not None:
			await self._stream_listener_task

	async def wait_for_listener_removed_event(self):
		await self._listener_removed_event.wait()

	async def stop(self):
		# cancel every background task
		for notif in self._iterators_tasks.keys():
			self._iterators_tasks.get(notif).cancel()
		# cancel listening task
		if self._stream_listener_task:
			self._stream_listener_task.cancel()
		# wait for listening task end
		if self._stream_listener_task:
			await self._stream_listener_task

	def add_listener(self, listener: GenericNotificationListener):
		# check listener count is valid (if count == 0 on start it will stay active forever)
		if listener.count == 0:
			print(f"adding listener: {listener}")
			return

		# add listener to registered_listeners
		if not self._registered_listeners.get(listener.listener_key):
			self._registered_listeners[listener.listener_key] = set()
		self._registered_listeners[listener.listener_key].add(listener)

		# create an iterator if needed
		if not self._iterators_tasks.get(listener.listener_key):
			self._add_iterator(listener)

	def remove_listener(self, listener: GenericNotificationListener):
		# remove listener from registered_listeners
		if self._registered_listeners.get(listener.listener_key) \
					and listener in self._registered_listeners.get(listener.listener_key):
			self._registered_listeners[listener.listener_key].remove(listener)
			# mark listener as finished
			listener.mark_as_finished()
			# notify any waiting client that a listener finished, they will check if their listeners list was updated
			# we set and clear event because we only need to wake up methods waiting for this event, and this event might be used multiple times
			self._listener_removed_event.set()
			self._listener_removed_event.clear()

		# remove iterator if it's not used anymore
		if not self._registered_listeners.get(listener.listener_key):
			self._remove_iterator(listener.listener_key)

	def get_listeners_count(self) -> int:
		count = 0
		for listeners_list in self._registered_listeners.values():
			count += len(listeners_list)
		return count

	#####
	# notifications iterators aggregation
	#####
	def _add_iterator(self, listener: GenericNotificationListener):
		# if iterator already exists skip
		if self._iterators_tasks.get(listener.listener_key):
			return
		# create a notification channel for given notification type
		# noinspection PyProtectedMember
		notification_iterator = listener._create_iterator(self._client)

		# create a task listening to the notification iterator
		task = asyncio.get_event_loop().create_task(self._iterator_wrapper(listener.listener_key, listener.notification_type, notification_iterator))
		self._iterators_tasks[listener.listener_key] = task

	def _remove_iterator(self, listener_key: str):
		task = self._iterators_tasks.get(listener_key)

		# no iterator to remove
		if not task:
			return

		# cancel current iterator and remove it from tasks
		task.cancel()
		self._iterators_tasks.pop(listener_key)

		# if there are no more iterators stop listening task
		if len(self._iterators_tasks) == 0 and self._stream_listener_task:
			self._stream_listener_task.cancel()

	async def _iterator_wrapper(self, listener_key: str, notification_type: NOTIFICATIONS, async_iterator: AsyncIterator):
		try:
			async for notification_message in async_iterator:
				self._dispatch_notification(listener_key, notification_message)
		except asyncio.CancelledError:
			raise
		except grpc.aio.AioRpcError as e:
			if e.code() == e.code().UNAVAILABLE:
				if e.details() == "Socket closed":
					core_logger.error(f"{self.__class__.__name__}: {notification_type}: connection lost")
				else:
					core_logger.error(f"{self.__class__.__name__}: {notification_type}: server error: {e.details()}")
			else:
				core_logger.error(f"{self.__class__.__name__}: {notification_type}: grpc error: {e.code()} {e.details()}")
		except Exception as e:
			core_logger.exception(f"{self.__class__.__name__}: {notification_type}: unexpected exception: {e}")

		# unregister notifications listener ...
		listeners = self._registered_listeners.get(listener_key).copy()
		for listener in listeners:
			self.remove_listener(listener)

	def _dispatch_notification(self, listener_key: str, notification_message: types.NotificationMessageType):
		if not self._registered_listeners.get(listener_key):
			return
		registered_listeners = list(self._registered_listeners.get(listener_key))
		notification_logger.info(f"{self._client.__class__.__name__}: notification received: {listener_key}")
		notification_logger.debug(f"{self._client.__class__.__name__}: notification content:  {listener_key}: {notification_message}")
		# sort by priority higher priority first
		registered_listeners.sort(key=lambda listen: listen.priority, reverse=True)
		for listener in registered_listeners:
			try:
				# clone original notification else a listener can modify notification content for next listeners ...
				# noinspection PyProtectedMember
				self._client.add_background_task(listener.handle_notification(notification_message._clone(), self.remove_listener))
			except Exception as e:
				core_logger.exception(f"ClientListenerHolder: cannot create listener task (this is not supposed to happen !!): {e}")
