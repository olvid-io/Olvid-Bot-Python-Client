import asyncio
import secrets
from typing import Coroutine, Callable, Optional, Union, Any

# for compatibility with python 3.10
from typing import TypeVar
# noinspection PyTypeHints
Self = TypeVar("ChatBot")


from .logger import tools_logger

from .. import datatypes
from ..core.OlvidClient import OlvidClient
from ..core.OlvidBot import OlvidBot
from ..listeners.Command import Command
from ..listeners.ListenersImplementation import MessageReceivedListener, DiscussionNewListener


####
# This class helps to implements a basic chat bot that can send a welcome message when it enters a new discussion.
# It also add an help command and send help every time a user send a message in a one to one discussion.
# All these behavior can be modified after creation using help_... and welcome_... methods.
####
class ChatBot(OlvidBot):
	WELCOME_MESSAGE_FACTORY: type = Callable[[datatypes.Discussion], Union[Optional[str], Coroutine[Any, Any, Optional[str]]]]
	HELP_MESSAGE_FACTORY: type = Callable[[int], Union[Optional[str], Coroutine[Any, Any, Optional[str]]]]

	def __init__(self, parent_client: OlvidClient = None):
		super().__init__(parent_client=parent_client)
		# welcome message
		self._welcome_message: Optional[str] = None
		self._welcome_message_factory: Optional[ChatBot.WELCOME_MESSAGE_FACTORY] = None
		self._welcome_send_help: bool = True
		self._welcome_send_in_one_to_one: bool = True
		self._welcome_send_in_groups: bool = True

		# help message
		self._help_message: Optional[str] = None
		self._help_message_factory: Optional[ChatBot.HELP_MESSAGE_FACTORY] = None
		self._help_always_send_in_to_one: bool = True
		self._help_always_send_in_group: bool = False
		self._help_command_prefix: Optional[str] = None

		# help command
		self._help_command: Optional[Command] = Command(regexp_filter="!?help", handler=self._help_command_handler)
		self.add_command(self._help_command)
		self._on_message_listener: MessageReceivedListener = MessageReceivedListener(handler=self._message_received_handler)
		self.add_listener(self._on_message_listener)

		# various
		self.add_listener(DiscussionNewListener(handler=self._discussion_new_handler))

	#####
	# Help configuration
	#####
	def help_set_message(self, help_message: str) -> Self:
		self._help_message = help_message
		self._help_message_factory = None
		return self

	def help_set_message_factory(self, factory: HELP_MESSAGE_FACTORY) -> Self:
		self._help_message = None
		self._help_message_factory = factory
		return self

	def help_disable_command(self) -> Self:
		self.remove_command(command=self._help_command)
		self._help_command = None
		return self

	def help_send_on_invalid_command(self, command_prefix: str = "!") -> Self:
		self._help_command_prefix = command_prefix
		return self

	def help_always_send_in_groups(self) -> Self:
		self._help_always_send_in_group = True
		return self

	def help_do_not_always_send_in_one_to_one(self) -> Self:
		self._help_always_send_in_to_one = False
		return self

	def help_add_custom_checker(self, checker: MessageReceivedListener.CheckerType) -> Self:
		self._on_message_listener.add_checker(checker)
		self._help_command.add_checker(checker)
		return self

	async def _message_received_handler(self, message: datatypes.Message):
		# if message is a valid command do nothing
		if self.tool_is_message_a_valid_command(message):
			return

		# check if we send help on invalid command, and if this was supposed to be a command
		if self._help_command_prefix and message.body.startswith(self._help_command_prefix):
			await self.send_help_message(message.discussion_id)

		discussion: datatypes.Discussion = await self.discussion_get(discussion_id=message.discussion_id)
		if discussion.contact_id and self._help_always_send_in_to_one:
			await self.send_help_message(message.discussion_id)
		elif discussion.group_id and self._help_always_send_in_group:
			await self.send_help_message(message.discussion_id)

	#####
	# Welcome configuration
	#####
	def welcome_set_message(self, welcome_message: str) -> Self:
		self._welcome_message = welcome_message
		self._welcome_message_factory = None
		return self

	def welcome_set_message_factory(self, factory: WELCOME_MESSAGE_FACTORY) -> Self:
		self._welcome_message = None
		self._welcome_message_factory = factory
		return self

	def welcome_do_not_send_in_one_to_one(self) -> Self:
		self._welcome_send_in_one_to_one = False
		return self

	def welcome_do_not_send_in_groups(self) -> Self:
		self._welcome_send_in_groups = False
		return self

	def welcome_do_not_send_help(self) -> Self:
		self._welcome_send_help = False
		return self

	#####
	# Help section
	#####
	# This can be overwritten to build more complex help message
	async def send_help_message(self, discussion_id: int):
		if self._help_message:
			await self.message_send(discussion_id=discussion_id, body=self._help_message)
		elif self._help_message_factory:
			promise = self._help_message_factory(discussion_id)
			if asyncio.iscoroutine(promise):
				help_message: str = await promise
			else:
				help_message: str = promise
			if help_message:
				await self.message_send(discussion_id=discussion_id, body=help_message)

	async def _help_command_handler(self, message: datatypes.Message):
		await self.send_help_message(message.discussion_id)

	#####
	# Welcome section
	#####
	# This can be overwritten to build more complex welcome message
	async def send_welcome_message(self, discussion: datatypes.Discussion):
		if self._welcome_message:
			await discussion.post_message(body=self._welcome_message)
		elif self._welcome_message_factory:
			promise = self._welcome_message_factory(discussion)
			if asyncio.iscoroutine(promise):
				welcome_message: str = await promise
			else:
				welcome_message: str = promise
			if welcome_message:
				await discussion.post_message(body=welcome_message)
			if self._welcome_send_help:
				await self.send_help_message(discussion.id)

	# On discussion creation, create a webhook and post it in discussion
	async def _discussion_new_handler(self, discussion: datatypes.Discussion):
		# handle new groups (we do not need to wait to post in a group)
		if discussion.group_id != 0:
			await self.send_welcome_message(discussion)
			return

		# handle the new contact case
		if discussion.contact_id == 0:
			return

		# check if contact have channels to post a message
		contact = await self.contact_get(contact_id=discussion.contact_id)
		if contact.established_channel_count != 0:
			await self.send_welcome_message(discussion)
			return

		# if contact has no channel a background task that will try to post the welcome message later
		self.add_background_task(self._post_welcome_message_task(discussion), name=f"welcome_bot_{contact.id}")
		tools_logger.info(f"WelcomeBot: waiting for channel establishment, contact_id: {contact.id}")

	# if there are no channel create a task that will wait for up to 10 seconds to post the message
	async def _post_welcome_message_task(self, discussion: datatypes.Discussion):
		count = 0
		max_count = 1000
		while count < max_count:
			await asyncio.sleep(1)
			c = await self.contact_get(contact_id=discussion.contact_id)
			if c.established_channel_count > 0:
				await self.send_welcome_message(discussion)
				return
			tools_logger.info(f"WelcomeBot: still waiting for contact channel: {count + 1}/{max_count}")
			count += 1

	####
	#  tools
	####
	# send a randomized greeting in a discussion
	async def tool_basic_welcome_factory(self, discussion: datatypes.Discussion):
		name: str
		if discussion.contact_id:
			contact: datatypes.Contact = await self.contact_get(contact_id=discussion.contact_id)
			name = contact.details.first_name if contact.details.first_name else contact.display_name
		else:
			group: datatypes.Group = await self.group_get(group_id=discussion.group_id)
			if group.members == 1:
				contact: datatypes.Contact = await self.contact_get(contact_id=group.members[0].contact_id)
				name = contact.details.first_name if contact.details.first_name else contact.display_name
			else:
				name = "everyone"
		greetings: str = secrets.choice(["Hi", "Hello", "Hey"])
		return f"""
{greetings} {name} 👋
		""".strip()

	@staticmethod
	async def tool_ignore_location_message_checker(message: datatypes.Message):
		return message.message_location.type == datatypes.MessageLocation.LocationType.LOCATION_TYPE_UNSPECIFIED

	def tool_is_message_a_valid_command(self, message: datatypes.Message):
		return any([isinstance(listener, Command) and listener.match(message) for listener in self._listeners_set])
