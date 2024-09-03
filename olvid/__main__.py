import asyncio
import sys
import traceback

import asyncclick as click
import grpc.aio

from .cli.tools.ClientSingleton import ClientSingleton
from .cli.interactive_tree import interactive_tree
from .cli.root_tree import root_tree

from .cli.tools.cli_tools import print_error_message

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
	except grpc.aio.AioRpcError as e:
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
	# This is supposed to improve performances, and it fix and exception when running cli in docker (not sure why)
	import uvloop
	asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
	asyncio.run(async_main())


if __name__ == "__main__":
	main()