import asyncclick as click

from .interactive_main import interactive_main
from .interactive_tree import interactive_tree
from .tools.ClientSingleton import ClientSingleton
from .tools.click_wrappers import WrapperGroup


@click.group(invoke_without_command=True, cls=WrapperGroup)
@click.option("-i", "--identity", "identity", default=-1, type=click.INT, help="Id of the identity you want to use")
@click.option("-e", "--foreach", "for_each", is_flag=True, help="Run this command for each identity (ignored if -i is set)")
@click.option("-k", "--key", "client_key", default="", type=click.STRING, help="Impersonate a client key on start")
@click.option("-v", "--version", "version", is_flag=True, help="Show program version and exit")
@click.argument("arguments", required=False, nargs=-1, type=click.UNPROCESSED)
async def root_tree(arguments: list[str], identity: int = 0, client_key: str = "", for_each: bool = False, version: bool = False):
	if version:
		from olvid import __version__
		print(__version__)
		return
	# global options to interactive and non-interactive
	if identity != -1:
		ClientSingleton.set_current_identity_id(identity_id=identity)
	if client_key:
		key = await ClientSingleton.get_client().admin_client_key_get(client_key=client_key)
		await ClientSingleton.impersonate_client_key(key)

	# start interactive mode
	if not arguments:
		await interactive_main()
		return

	# enable script mode
	ClientSingleton.enable_script_mode()

	# non interactive mode
	try:
		# add root tree commands to this tree
		interactive_tree.commands.update(root_tree.commands)

		# set identity (or run for_each)
		identity_ids: list[int] = [i.id async for i in ClientSingleton.get_client().admin_identity_list()] if for_each and identity == -1 else [identity]
		for identity_id in identity_ids:
			if not client_key:
				ClientSingleton.set_current_identity_id(identity_id)

			# parse command
			async with await interactive_tree.make_context(info_name="olvid-cli", args=list(arguments)) as ctx:
				# run command
				await interactive_tree.invoke(ctx)
	except click.UsageError as e:
		click.echo(click.style(e.format_message(), fg="red"))
		if e.ctx is not None:
			print(e.ctx.get_help())
	# raised in some conditions for invalid commands (for example when you call a command group: `cli identity`)
	except click.exceptions.Exit:
		pass
	except Exception as e:
		click.echo(click.style(f"Unexpected exception: {e}", fg="red"))
		raise e
