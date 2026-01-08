import asyncio
import base64
import os
from typing import Callable, Optional, Coroutine, AsyncIterator, TYPE_CHECKING

if TYPE_CHECKING:
	from ..core.OlvidClient import OlvidClient
	from ..internal.types import NotificationMessageType

from ..core.logger import core_logger
from .Notifications import NOTIFICATIONS


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
	def __init__(self, notification_type: NOTIFICATIONS, handler: Callable[[type["NotificationMessageType"]], Optional[Coroutine]], iterator_args: dict = None):
		self._notification_type: NOTIFICATIONS = notification_type
		self._handler = handler

		self._iterator_args: dict = iterator_args if iterator_args else {}

		# we compute listener key after end of init to let child classes fill iterator args
		self._listener_key: Optional[str] = None

	@property
	def notification_type(self) -> NOTIFICATIONS:
		return self._notification_type

	@property
	def listener_key(self) -> str:
		if self._listener_key is None:
			self._listener_key = self._generate_listener_key()
		return self._listener_key

	async def handle_notification(self, notification_message: type["NotificationMessageType"]):
		try:
			res = self._handler(notification_message)
			if asyncio.iscoroutine(res):
				await res
		except Exception:
			core_logger.exception(f"{self.__class__.__name__}: unexpected exception: {self}")

	def _create_iterator(self, client: "OlvidClient") -> AsyncIterator:
		return getattr(client, f"_notif_{self.notification_type.name.lower()}")(**self._iterator_args)

	def _generate_listener_key(self) -> str:
		key: str = f"{self.notification_type.name}"
		# if listener have iterator args we create a unique key (daemon response stream might differ even with same parameters, for example if a count parameter is set)
		if len(self._iterator_args) >= 1:
			for k, v in self._iterator_args.items():
				key += f"_{k}-{v}"
			key += f"_{base64.b64encode(os.urandom(12))}"
		return key

	def __str__(self):
		return f"{self.listener_key}: {self._handler.__name__} (arguments: {self._iterator_args})"

	def __repr__(self):
		return self.__str__()
