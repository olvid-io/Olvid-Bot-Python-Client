import asyncclick as click

from .ClientSingleton import ClientSingleton
from typing import Any

from olvid import datatypes

from ..tools.exceptions import CancelCommandError


def _recursive_get_attr(item: object, attributes: list[str]):
	if not attributes:
		return item
	return _recursive_get_attr(getattr(item, attributes[0]), attributes[1:])


def filter_fields_and_print_normal_message(item: object, fields: str):
	if not fields:
		print_normal_message(item, item)
	else:
		try:
			field_names = fields.split(",")
			if len(field_names) == 1:
				attr = _recursive_get_attr(item, field_names[0].split('.'))
				if type(attr) in [tuple, list]:
					attr = ",".join([f"({a})" for a in attr])
				normal_str: str = f"{attr}"
				script_str: str = f"{attr}"
			else:
				normal_str: str = ""
				script_str: str = ""
				for field_name in field_names:
					attr = _recursive_get_attr(item, field_name.split('.'))
					if type(attr) in [tuple, list]:
						attr = ",".join([f"({a})" for a in attr])
					script_str += f"{attr},"
					normal_str += f"{field_name}: {attr},"
				normal_str = normal_str.strip().removesuffix(",")
				script_str = script_str.strip().removesuffix(",")
			print_normal_message(normal_str, script_str)
		except AttributeError as e:
			print_error_message(f"Invalid fields filter: {fields}")
			print_error_message(e)
			raise CancelCommandError()


# print a red message on stderr
def print_error_message(message: Any):
	click.secho("{}".format(message), fg="red", err=True)


# print a yellow message on stderr
def print_warning_message(message: Any):
	click.secho("{}".format(message), fg="yellow", err=True)


# print a message if not in script mode
def print_command_result(message: Any, script_message: Any = None):
	if not ClientSingleton.is_script_mode_enabled():
		click.secho("{}".format(message), fg="cyan")
	elif script_message:
		click.secho(str(script_message))


def print_debug_message(message: Any, script_version: Any):
	if ClientSingleton.is_script_mode_enabled():
		if script_version:
			click.secho("{}".format(script_version), fg="magenta", err=True)
	else:
		click.secho("{}".format(message), fg="magenta", err=True)


def print_success_message(message: Any, script_version: Any):
	if ClientSingleton.is_script_mode_enabled():
		if script_version:
			click.secho("{}".format(script_version), fg="green")
	else:
		click.secho("{}".format(message), fg="green")


def print_normal_message(message: Any, script_version: Any):
	if ClientSingleton.is_script_mode_enabled():
		if script_version:
			click.secho("{}".format(script_version))
	else:
		click.secho("{}".format(message))


def string_to_message_id(message_id: str) -> datatypes.MessageId:
	if len(message_id) <= 1:
		raise click.exceptions.NoSuchOption(f"Invalid message id: {message_id}")
	try:
		int_id = int(message_id[1:])
	except ValueError:
		raise click.exceptions.NoSuchOption(f"Invalid message id: {message_id}")

	if message_id[0].upper() == "I":
		return datatypes.MessageId(type=datatypes.MessageId.Type.TYPE_INBOUND, id=int_id)
	elif message_id[0].upper() == "O":
		return datatypes.MessageId(type=datatypes.MessageId.Type.TYPE_OUTBOUND, id=int_id)
	raise click.exceptions.NoSuchOption(f"Invalid message id: {message_id}")


def string_to_attachment_id(attachment_id: str) -> datatypes.AttachmentId:
	if len(attachment_id) <= 1:
		raise click.exceptions.NoSuchOption(f"Invalid attachment id: {attachment_id}")
	try:
		int_id = int(attachment_id[1:])
	except ValueError:
		raise click.exceptions.NoSuchOption(f"Invalid attachment id: {attachment_id}")

	if attachment_id[0].upper() == "I":
		return datatypes.AttachmentId(type=datatypes.AttachmentId.Type.TYPE_INBOUND, id=int_id)
	elif attachment_id[0].upper() == "O":
		return datatypes.AttachmentId(type=datatypes.AttachmentId.Type.TYPE_OUTBOUND, id=int_id)
	raise click.exceptions.NoSuchOption(f"Invalid attachment id: {attachment_id}")


def message_id_to_string(message_id: datatypes.MessageId):
	return f"{message_id.type.name[0]}{message_id.id}"


def attachment_id_to_string(attachment_id: datatypes.AttachmentId):
	return f"{attachment_id.type.name[0]}{attachment_id.id}"
