import traceback
import typing
import typing as t

import asyncclick as click
from asyncclick import Context

from .cli_tools import print_error_message
from .ClientSingleton import ClientSingleton
from ...core import errors

class WrappedCommand(click.Command):
	async def invoke(self, ctx: click.Context):
		try:
			await super(WrappedCommand, self).invoke(ctx)
		except errors.UnavailableError:
			print_error_message(f"Cannot connect to server: {ClientSingleton.get_client().server_target}")
		except errors.AioRpcError as e:
			click.echo(click.style(f"{e.code().name}: {e.details()}", fg="red"))
		except click.exceptions.ClickException as e:
			# pass exceptions to upper level (to get correct return value)
			raise e
		except Exception as e:
			click.echo(click.style(f"Unexpected exception during command: {e}", fg="magenta"))
			traceback.print_exc()


class WrapperGroup(click.Group):
	def __init__(self, **attrs: typing.Any):
		super().__init__(**attrs)
		self.command_class = WrappedCommand
		self.group_class = WrapperGroup

	# override this method not to sort command by alphabetic order in usage message, we use the added order
	def list_commands(self, ctx: Context) -> t.List[str]:
		return list(self.commands)
