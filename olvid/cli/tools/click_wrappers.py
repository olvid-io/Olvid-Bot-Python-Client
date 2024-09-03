import traceback
import typing
import typing as t

import asyncclick as click
import grpc
from asyncclick import Context

from .cli_tools import print_error_message


class WrappedCommand(click.Command):
	async def invoke(self, ctx: click.Context):
		try:
			await super(WrappedCommand, self).invoke(ctx)
		except grpc.aio.AioRpcError as e:
			if e.code() == grpc.StatusCode.UNAVAILABLE:
				print_error_message("Server unavailable")
			else:
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
