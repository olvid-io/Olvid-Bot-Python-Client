import asyncio
import base64
from warnings import warn
import os
from typing import Callable, Optional, Coroutine, Union, Any, AsyncIterator, TYPE_CHECKING

if TYPE_CHECKING:
	from ..core.OlvidClient import OlvidClient

from ..core.logger import core_logger
from .Notifications import NOTIFICATIONS
from ..internal import types


class GenericNotificationListener:
	"""
	GenericNotificationListener a basic notification listener to use within OlvidClient and other subclasses.

	A listener is a method called every time a notification is triggered. When you add a listener to an OlvidClient it will
	automatically register to this notification and handler will be called every time a notification is sent by daemon.

	We do not recommend that you use GenericNotificationListener directly. Instead, you should use one of the provided
	listeners in the ListenersImplementation file.
	You can access them like this:
	```
	from olvid import listeners
	listeners.MessageReceivedListener(handler=lambda m: a)
	```
	Like this you won't need to specify the notification you want to listen to.
	Also, you won't need to use protobuf Notification messages, message are already un-wrapped and handler ill receive notification content.
	For example MessageReceivedListener.handler will receive a datatypes.Message item, not a MessageReceivedNotification
	as a GenericNotificationListener will receive if listening to MessageReceivedNotification.
	"""
	NotificationHandlerType = Callable[[types.NotificationMessageType], Optional[Coroutine]]
	CheckerType = Callable[[types.NotificationMessageType], Union[bool, Coroutine[Any, Any, bool]]]

	def __init__(self, notification_type: NOTIFICATIONS, handler: NotificationHandlerType, checkers: list[CheckerType] = None, count: int = -1, priority: int = 0):
		self._notification_type: NOTIFICATIONS = notification_type
		self._handler = handler
		self._checkers = checkers if checkers else []
		if checkers:
			warn("Listener.checkers will be deprecated in future release", PendingDeprecationWarning, stacklevel=10)
		self._count: int = count
		# we consider that 0 and -1 are endless listeners, -1 for legacy reasons and 0 because it will be normal value in future (notification filtering feature)
		self._endless: bool = count <= 0
		self._priority: int = priority
		self._finished: bool = False

		self._iterator_args: dict = {}

		# we compute listener key after end of init to let child classes fill iterator args
		self._listener_key: Optional[str] = None

	@property
	def notification_type(self) -> NOTIFICATIONS:
		return self._notification_type

	@property
	def priority(self) -> int:
		return self._priority

	@property
	def listener_key(self) -> str:
		if self._listener_key is None:
			self._listener_key = self._generate_listener_key()
		return self._listener_key

	@property
	def count(self) -> int:
		return self._count

	def add_checker(self, checker: CheckerType):
		self._checkers.append(checker)

	@property
	def is_finished(self) -> bool:
		return self._finished

	def mark_as_finished(self):
		self._finished = True

	async def handle_notification(self, notification_message: types.NotificationMessageType, remove_listener_callback: Callable[[
		"GenericNotificationListener"], None]):
		for checker in self._checkers:
			ret = checker(notification_message)
			if asyncio.iscoroutine(ret):
				ret = await ret
			if not ret:
				return

		# check this was not marked as finished before start (not supposed to happen)
		if self._finished:
			return

		try:
			res = self._handler(notification_message)
			if asyncio.iscoroutine(res):
				await res
		except Exception:
			core_logger.exception(f"{self.__class__.__name__}: unexpected exception: {self}")
		finally:
			if not self._endless:
				if self._count > 0:
					self._count -= 1
				if self._count == 0:
					self.mark_as_finished()
					remove_listener_callback(self)

	def _create_iterator(self, client: "OlvidClient") -> AsyncIterator:
		return getattr(client, f"_notif_{self.notification_type.name.lower()}")(**self._iterator_args)

	def _generate_listener_key(self) -> str:
		key: str = f"{self.notification_type.name}"
		# if listener have iterator args (we ignore count arg) we create a unique key (daemon response stream might differ even with same parameters, for example if a count parameter is set)
		if self._iterator_args.get("count") or len(self._iterator_args) > 1:
			for k, v in self._iterator_args.items():
				key += f"_{k}-{v}"
			key += f"_{base64.b64encode(os.urandom(12))}"
		return key

	def __str__(self):
		return f"{self.listener_key}: {self._handler.__name__} (count: {self.count})"

	def __repr__(self):
		return self.__str__()
