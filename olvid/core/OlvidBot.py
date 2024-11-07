import sys
from typing import Optional

from .OlvidClient import OlvidClient
from .GrpcTlsConfiguration import GrpcTlsConfiguration


class OlvidBot(OlvidClient):
	"""

	OlvidBot implements a set of method named on_something. There is one method for each gRPC notification method.
	On instantiation overwritten methods will automatically be subscribed as notification listener.
	For example:

	class Bot(OlvidBot)
		async def on_message_received(self, message: datatypes.Message):
			print(message)

	Every time Bot class is instantiated it will add a listener to message_received notification with the method as handler.

	OlvidBot can also add Command objects with add_command method. Command are specific listeners.
	They subclass listeners.MessageReceivedListener, and they are created with a regexp filter that will filter notifications.
	Only messages that match the regexp will raise a notification.
	Commands can be added using OlvidBot.command decorator:
	For example:

	class Bot(OlvidBot)
		@OlvidBot.command(regexp_filter="^!help")
		async def on_message_received(self, message: datatypes.Message):
			await message.reply("Help message")
	"""
	def __init__(self, bot_name: str = None, client_key: Optional[str] = None, server_target: Optional[str] = None,
				parent_client: Optional['OlvidClient'] = None, tls_configuration: GrpcTlsConfiguration = None):
		OlvidClient.__init__(self, client_key=client_key, server_target=server_target, parent_client=parent_client, tls_configuration=tls_configuration)
		self._name = bot_name if bot_name is not None else self.__class__.__name__

		print("WARNING: OlvidBot is marked as deprecated since v1.1.0 and will be removed in future release\nUse OlvidClient instead.", file=sys.stderr)

	# read only properties
	@property
	def name(self) -> str:
		return self._name

	#####
	# Common methods
	#####
	def __str__(self) -> str:
		current_listeners = [f"{listener.listener_key}: (finished: {listener.is_finished})" for listener in self._listeners_set]
		return f"{self.name}: {', '.join(current_listeners)}"

	#####
	# tools
	#####
	def print(self, *args, **kwargs):
		print(f"{self._name}:", *args, **kwargs)
