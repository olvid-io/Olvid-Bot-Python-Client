import asyncio
import sys
import traceback

import asyncclick as click

from .cli.tools.ClientSingleton import ClientSingleton
from .cli.interactive_tree import interactive_tree
from .cli.root_tree import root_tree
from .cli.tools.cli_tools import print_error_message

from .core import errors

# import logging
# logging.basicConfig(level=logging.INFO, format="[%(levelname)5s]: %(message)s", filename="cli.log")
# logging.info("Level set to file")


async def async_main():
	# initialize connection to server
	try:
		# initialize connection to server
		await ClientSingleton.init()
	except ValueError as e:
		click.echo(click.style(e, fg="red"))
		exit(1)
	except errors.AioRpcError as e:
		click.echo(click.style(e.details(), fg="red"))
		exit(1)

	try:
		try:
			for arg in sys.argv[1:]:
				if not arg.startswith("-"):
					break
				if arg == "--help":
					raise click.exceptions.ClickException("")

			async with await root_tree.make_context("olvid-cli", list(sys.argv[1:])) as ctx:
				await root_tree.invoke(ctx)
		except (click.UsageError, click.ClickException) as e:
			if e.format_message():
				click.echo(click.style(e.format_message(), fg="red"))
			interactive_tree.params.extend(root_tree.params)
			interactive_tree.commands.update(root_tree.commands)
			print(interactive_tree.get_help(interactive_tree.context_class(interactive_tree)))
		except click.exceptions.Exit:
			pass
	except Exception:
		print_error_message("Unexpected exception caught in main_tree")
		traceback.print_exc()


def main():
	try:
		asyncio.set_event_loop(asyncio.new_event_loop())
		asyncio.get_event_loop().run_until_complete(async_main())
	except KeyboardInterrupt:
		pass


if __name__ == "__main__":
	main()