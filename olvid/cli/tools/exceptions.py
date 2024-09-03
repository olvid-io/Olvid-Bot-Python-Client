import asyncclick as click


# Cancel a command with not specific messages
class CancelCommandError(click.ClickException):
	def __init__(self):
		pass
