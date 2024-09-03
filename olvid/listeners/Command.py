from __future__ import annotations
from typing import TYPE_CHECKING

import re
import inspect

from .ListenersImplementation import MessageReceivedListener

if TYPE_CHECKING:
	from typing import Callable, Optional, Coroutine
	from .. import datatypes


class Command(MessageReceivedListener):
	"""
	Command: a specific MessageReceivedListener associated with a regexp that will determine if it's called or not.

	The most convenient way to add a command is to use the `OlvidBot.command` decorator, like this command are automatically
	added to an OlvidBot instance.
	Examples of possible way to add commands to a bot:

	```
	class Bot(OlvidBot):
		# use decorator in you bot class declaration
		@OlvidBot.command(regexp_filter="^!help")
		async def help_cmd(self, message: datatypes.Message):
			await message.reply("help message")

	bot = OlvidBot()

	# use decorator to to an existing bot instance
	@bot.command(regexp_filter="!second")
	async def second_command(message: datatypes.Message):
		print("Second command")

	# use add_command method
	bot.add_command(Command(regexp_filter="^!cmd", handler=lambda message: print(message)))
	```

	Command attributes:
	- regexp_filter (mandatory): the regexp that will determine if this command is called or not
	- ignore_case: bool (optional) (default= True): regexp ignore case
	- name: str (optional): can be used to create help messages
	- usage: str (optional): can be used to create help messages
	"""
	def __init__(self, regexp_filter: str, handler: Callable[[datatypes.Message], Optional[Coroutine]], name: str = None, usage: str = None, ignore_case: bool = True):
		super().__init__(handler=self._handler_wrapper(handler), checkers=[self.match], count=-1)

		self._regexp_filter: str = regexp_filter
		self._original_handler: Callable[[datatypes.Message], Optional[Coroutine]] = handler
		self._name = name if name is not None else regexp_filter
		self._usage: Optional[str] = usage
		self._ignore_case = ignore_case

	def match(self, message: datatypes.Message) -> bool:
		return self.match_str(message.body)

	def match_str(self, message_body: str) -> bool:
		return re.match(self._regexp_filter, message_body, re.IGNORECASE if self._ignore_case else 0) is not None

	def _handler_wrapper(self, original_handler) -> Callable[[datatypes.Message], Optional[Coroutine]]:
		async def wrapped_command_handler(message: datatypes.Message):
			signature = inspect.signature(original_handler)
			if len(signature.parameters) == 1:
				ret = original_handler(message)
			else:
				match_body = re.match(self._regexp_filter, message.body, re.IGNORECASE if self._ignore_case else 0)
				ret = original_handler(message, match_body.group())
			if inspect.iscoroutine(ret):
				await ret
		return wrapped_command_handler

	@property
	def regexp_filter(self) -> str:
		return self._regexp_filter

	@property
	def name(self) -> str:
		return self._name

	@property
	def usage(self) -> str:
		return self._usage

	@staticmethod
	def get_default_regexp(name: str):
		return f"^!{name}"

	def __str__(self):
		return f"{self._name}{': ' + self.usage if self.usage else ''}"


#####
# Decorator section
#####
# Abstract class, contains __call__ method to create a decorator to add commands to a bot.
# This class have two implementations:
# - ClassCommandDecorator: embed it at class level, to annotate methods in class definition.
# it will store method names that you want to add as commands. Then on bot instance creation it will
# retrieve all these methods (using their names), create appropriated Command instances and add it as listeners.
# We need to use method instead of functions that's why we store function names and then resolve methods using getattr when bot is instantiated.
# - InstanceCommandDecorator: this is supposed to override the class attribute containing ClassCommandDecorator when a bot
# is instantiated. On decorator use it will create a new Command and add it to bot listeners.
# this is valid decorator usage: @command, @command(), @command("regexp"), @command("regexp", "usage"),
#   @command(regexp="regexp", usage="usage"), @command(usage="usage")
class CommandDecorator:
	def __call__(self, *args, regexp_filter: str = None, usage: str = None, name: str = None, ignore_case: bool = None):
		## handle @command call: store command using function name as command name, and return function
		if args and callable(args[0]):
			function = args[0]
			regexp_filter = Command.get_default_regexp(function.__name__)
			self._add_command(function=function, regexp_filter=regexp_filter)
			return function

		####
		# handle @command() call: expect to return a decorator, so create a decorator that will create the command using initial wrapper optional arguments
		####
		# if there are no named arguments try to determine arguments
		if regexp_filter is None and usage is None and name is None:
			if len(args) == 3:
				regexp_filter = args[0]
				usage = args[1]
				name = args[2]
			elif len(args) == 2:
				regexp_filter = args[0]
				usage = args[1]
			elif len(args) == 1:
				regexp_filter = args[0]
			elif len(args) == 0:
				regexp_filter = ""
			else:
				raise TypeError(f"invalid number of parameters: {len(args)}")
		else:
			regexp_filter = regexp_filter

		# check argument types
		if regexp_filter is None or type(regexp_filter) is not str:
			raise ValueError("Command: regexp_filter is required and must be a string")
		if usage is not None and type(usage) is not str:
			raise ValueError("Command: usage must be a string")
		if name is not None and type(name) is not str:
			raise ValueError("Command: name must be a string")
		if ignore_case is not None and type(ignore_case) is not bool:
			raise ValueError("Command: ignore_case must be a boolean")

		# handle @command() call: expect to return a decorator, so create a decorator that will create the command using initial wrapper optional arguments
		def decorator(func):
			# add command (handle @command() with no arguments)
			if not regexp_filter:
				self._add_command(function=func, regexp_filter=Command.get_default_regexp(func.__name__), usage=usage, name=name, ignore_case=ignore_case)
			else:
				self._add_command(function=func, regexp_filter=regexp_filter, usage=usage, name=name, ignore_case=ignore_case)
			return func
		return decorator

	# method to override by implementations
	def _add_command(self, function: callable, regexp_filter: str, usage: str = None, name: str = None, ignore_case: bool = None):
		pass

	# method to override by implementations
	def get_commands(self, instance: "CommandHolder") -> list[Command]:
		pass


class ClassCommandDecorator(CommandDecorator):
	def __init__(self):
		# We use a dict to store commands by class name. This allows computing commands inherited from parents.
		# We store every command by name to allow command overriding.
		# For every command, we store constructor params because we will only create Command on Bot creation to use instance
		# methods as handlers.
		# Data structure: dict: bot class_name -> dict2
		# dict2: regexp_filter -> (class_method_name, usage, name)
		self._command_elements_by_name_by_class_name: dict[str, dict[str, (str, str, str, bool)]] = {}

	# add command to the global OlvidBot command holder
	def _add_command(self, function: callable, regexp_filter: str, usage: str = None, name: str = None, ignore_case: bool = None):
		class_name = function.__qualname__.removesuffix(f".{function.__name__}")

		if not self._command_elements_by_name_by_class_name.get(class_name):
			self._command_elements_by_name_by_class_name[class_name] = {}
		self._command_elements_by_name_by_class_name[class_name][regexp_filter] = (function.__name__, usage, name, ignore_case)

	def get_commands(self, instance: "CommandHolder") -> list[Command]:
		commands_dict: dict[str, Command] = {}
		for class_ in reversed(instance.__class__.mro()):
			if class_ == object:
				continue
			if self._command_elements_by_name_by_class_name.get(class_.__name__):
				for regexp, (command_handler_name, usage, name, ignore_case) in self._command_elements_by_name_by_class_name.get(class_.__name__).items():
					command_constructor_params = {
						"regexp_filter": regexp,
						"handler": getattr(instance, command_handler_name),
					}
					if name is not None:
						command_constructor_params["name"] = name
					if usage is not None:
						command_constructor_params["usage"] = usage
					if ignore_case is not None:
						command_constructor_params["ignore_case"] = ignore_case
					commands_dict[regexp] = Command(**command_constructor_params)
		return list(commands_dict.values())


#####
# Abstract class to implement to have a command decorator.
# It will add a class attribute for command decorator. This will store the commands for this class and its child classes.
# When you instantiate this class it will override previous command attribute. The new InstanceCommandDecorator determine
# commands associated to this instance browsing ClassCommandDecorator registered commands using instance __bases__.
# When new decorator is called it will directly create Command and add it to bot listener.
#####
class CommandHolder:
	command: CommandDecorator = ClassCommandDecorator()

	def __init__(self):
		for c in self.__class__.command.get_commands(self):
			self.add_command(c)
		self.command = InstanceCommandDecorator(self)

	def add_command(self, command: Command):
		raise NotImplementedError(f"{self.__class__.__name__}: CommandHolder: add_command not implemented")

	def remove_command(self, command: Command):
		raise NotImplementedError(f"{self.__class__.__name__}: CommandHolder: remove_command not implemented")


class InstanceCommandDecorator(CommandDecorator):
	def __init__(self, instance: CommandHolder):
		super(CommandDecorator, self).__init__()
		# retrieve commands from ClassLevel command decorator
		self._holder_instance: CommandHolder = instance
		self._command_list: list[Command] = self._holder_instance.__class__.command.get_commands(
			self._holder_instance)

	# method to override by implementations
	def _add_command(self, function: callable, regexp_filter: str, usage: str = None, name: str = None, ignore_case: bool = None):
		command_constructor_params = {
			"regexp_filter": regexp_filter,
			"handler": function,
		}
		if name is not None:
			command_constructor_params["name"] = name
		if usage is not None:
			command_constructor_params["usage"] = usage
		if ignore_case is not None:
			command_constructor_params["ignore_case"] = ignore_case
		new_command = Command(**command_constructor_params)
		# check if a command is already registered with this regexp_filter
		filtered_commands: list[Command] = list(filter(lambda c: c.regexp_filter == regexp_filter, self._command_list))

		if not filtered_commands:
			self._command_list.append(new_command)
			self._holder_instance.add_command(new_command)
		# overriding existing command
		else:
			previous_command = filtered_commands[0]
			self._command_list.remove(previous_command)
			self._holder_instance.remove_command(previous_command)
			self._holder_instance.add_command(new_command)

	def get_commands(self, instance: "CommandHolder") -> list[Command]:
		return self._command_list
