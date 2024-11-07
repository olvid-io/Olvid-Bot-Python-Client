import asyncio
import sys
import threading

import asyncclick as click

from .interactive_tree import interactive_tree
from .tools.ClientSingleton import ClientSingleton
from .tools.cli_tools import print_error_message
from .tools.exceptions import CancelCommandError
from ..core import errors


def tokenize_command_line(cmd_line: str) -> list[str]:
	tokens: list[str] = []
	current_token: str = ''
	in_quote: str = "" # contains current quoting character
	escape_next: bool = False

	for char in cmd_line:
		if char == '\\' and in_quote != '\'':
			# Handle escaping the next character
			escape_next = True
		elif char in ['"', "'"] and not (in_quote and char != in_quote):
			# Toggle quote mode
			in_quote = "" if in_quote else char
			if not in_quote:
				tokens.append(current_token)
				current_token = ''
		# Add the escaped character to the current token
		elif escape_next or in_quote:
			current_token += char
			escape_next = False
		elif char == ' ' and not in_quote and not escape_next:
			if current_token:
				tokens.append(current_token)
				current_token = ''
		else:
			current_token += char

	if current_token:
		tokens.append(current_token)

	return tokens


class InputThread(threading.Thread):
	def __init__(self, loop: asyncio.AbstractEventLoop):
		super().__init__()
		self.loop: asyncio.AbstractEventLoop = loop
		# event set when main wants InputThread to start input
		self.read_event: threading.Event = threading.Event()
		# Allow the thread to exit when the main program finishes
		self.daemon = True
		self.stop: bool = False
		self.queue = asyncio.Queue()

	async def read_main(self):
		while not self.stop:
			try:
				self.read_event.wait()
				self.read_event.clear()
				self.loop.call_soon_threadsafe(self.queue.put_nowait, input(f"{ClientSingleton.get_current_identity_id()} > "))
			except EOFError:
				self.stop = True
				self.loop.call_soon_threadsafe(self.queue.put_nowait, None)
				break
			except KeyboardInterrupt:
				self.loop.call_soon_threadsafe(self.queue.put_nowait, None)

	def run(self):
		asyncio.set_event_loop(asyncio.new_event_loop())
		asyncio.get_event_loop().run_until_complete(self.read_main())


async def interactive_main():
	# this import is important to enable the command line edition in interactive mode
	import readline

	# add exit command
	interactive_tree.add_command(click.Command("exit", callback=lambda *args, **kwargs: sys.exit(0)))
	interactive_tree.add_command(click.Command("quit", callback=lambda *args, **kwargs: sys.exit(0), hidden=True))

	# setup history
	try:
		readline.read_history_file("./.cli_history")
	except FileNotFoundError:
		pass
	except Exception:
		print_error_message("Cannot load cli history")
	readline.set_history_length(200)
	readline.set_auto_history(True)
	# auto select current identity if not specified in options
	try:
		if not ClientSingleton.get_current_identity_id():
			await ClientSingleton.auto_select_identity()
	except errors.UnavailableError:
		print_error_message(f"Cannot connect to server: {ClientSingleton.get_client().server_target}")
		return
	except errors.AioRpcError as e:
		print_error_message(e.details())
		return

	try:
		input_thread = InputThread(asyncio.get_event_loop())
		input_thread.start()

		while not input_thread.stop:
			try:
				input_thread.read_event.set()
				line = await input_thread.queue.get()
				if line is None:
					continue
				# line = await asyncio.to_thread(input, f"{ClientSingleton.get_current_identity_id()} > ")
				# print("post input")
				tokens: list[str] = tokenize_command_line(line)

				# shortcut for current identity
				if tokens and tokens[0].isdigit():
					# no command, just change current identity
					if len(tokens) == 1:
						ClientSingleton.set_current_identity_id(identity_id=int(tokens[0]))
						click.secho(f"Now using identity: {ClientSingleton.get_current_identity_id()}", fg="green")
					# execute command as specified identity
					else:
						previous_identity: int = ClientSingleton.get_current_identity_id()
						ClientSingleton.set_current_identity_id(identity_id=int(tokens[0]))
						try:
							click.secho(f"Executing command as {ClientSingleton.get_current_identity_id()}", fg="green")
							await interactive_tree.main(tokens[1:], prog_name="olvid-cli", standalone_mode=False)
						finally:
							ClientSingleton.set_current_identity_id(previous_identity)
					continue
				# normal case
				else:
					await interactive_tree.main(tokens, prog_name="olvid-cli", standalone_mode=False)
			except CancelCommandError:
				continue
			except click.UsageError as e:
				click.echo(click.style(e.format_message(), fg="red"))
				if e.ctx is not None:
					print(e.ctx.get_help())
			# clean line on ctrl + c
			except (KeyboardInterrupt, asyncio.CancelledError) as e:
				break
			# handle ctrl + d
			except EOFError:
				break
			except ValueError:
				break
	finally:
		# save history
		readline.write_history_file("./.cli_history")
