from typing import Callable
import asyncclick as click
from google.protobuf.json_format import Parse, ParseError

from olvid import OlvidAdminClient, OlvidClient, datatypes, listeners, errors
from olvid.cli.tools.cli_tools import print_error_message


async def listen(identity_id: int = 0, quiet: bool = False, notifications_to_listen: str = "", filter_=None, count=0):
	admin_client: OlvidAdminClient = OlvidAdminClient(identity_id=0)
	# create clients, one per identity
	clients: list[OlvidClient] = []
	try:
		if identity_id <= 0:
			async for identity in admin_client.admin_identity_list():
				clients.append(OlvidAdminClient(identity_id=identity.id))
		else:
			clients.append(OlvidAdminClient(identity_id=identity_id))
	except errors.AioRpcError as e:
		print(e.details())
		return

	# determine notifications to listen to
	if not notifications_to_listen:
		notifications: list[listeners.NOTIFICATIONS] = [notification for notification in listeners.NOTIFICATIONS]
	else:
		notifications: list[listeners.NOTIFICATIONS] = []
		for notif_name in notifications_to_listen.split(","):
			try:
				notifications.append(getattr(listeners.NOTIFICATIONS, notif_name))
			except AttributeError:
				raise click.exceptions.BadOptionUsage("-n", f"Invalid notification name: {notif_name}")

	# build filter
	protobuf_filter = None
	if filter_:
		# check we only listen for one kind of notification
		if len(set([n.name.split("_")[0] for n in notifications])) != 1:
			raise click.exceptions.BadArgumentUsage("Cannot filter if listening for different notifications kind (message, attachments, ...)")
		# determine attachment filter class

		entity_name: str = notifications[0].name.split("_")[0].capitalize()
		entity_filter = getattr(datatypes, f"{entity_name}Filter")

		protobuf_filter = entity_filter()
		try:
			parsed_filter = Parse(filter_, entity_filter()._to_native(protobuf_filter))
			protobuf_filter = entity_filter._from_native(parsed_filter)
		except ParseError as e:
			print_error_message(f"Cannot parse filter: {e}")
			return

	# add listeners
	for client in clients:
		identity: datatypes.Identity = await client.identity_get()
		for notification in notifications:
			listener_class_name = f"{''.join(s.title() for s in notification.name.split('_'))}Listener"
			listener_class = getattr(listeners, listener_class_name)
			if protobuf_filter:
				client.add_listener(listener_class(handler=await get_notification_handler(identity, notification, quiet), filter=protobuf_filter, count=count))
			else:
				client.add_listener(listener_class(handler=await get_notification_handler(identity, notification, quiet), count=count))

	for client in clients:
		await client.wait_for_listeners_end()


async def get_notification_handler(identity: datatypes.Identity, notification_type: listeners.NOTIFICATIONS, quiet: bool) -> Callable:
	def notification_handler(*fields):
		if quiet:
			print(f"{identity.id:2}: {notification_type.name}")
		else:
			print(f"{identity.id:2}: {notification_type.name:20}: {', '.join([field_to_str(field) for field in fields])}")
	return notification_handler


def field_to_str(field) -> str:
	if isinstance(field, datatypes.Message):
		id_str = f"{'O' if field.id.type == datatypes.MessageId.Type.TYPE_OUTBOUND else 'I'}{field.id.id}"
		return f"({id_str}) {field.body}"
	elif isinstance(field, datatypes.Attachment):
		id_str = f"{'O' if field.id.type == datatypes.AttachmentId.Type.TYPE_OUTBOUND else 'I'}{field.id.id})"
		return f"({id_str}) {field.file_name}"
	elif isinstance(field, datatypes.Group):
		return f"({field.id}) {field.name}"
	elif isinstance(field, datatypes.Discussion):
		return f"({field.id}) {field.title}"
	elif isinstance(field, datatypes.Contact):
		return f"({field.id}) {field.display_name}"
	elif isinstance(field, datatypes.Invitation):
		return f"({field.id}) {field.display_name} {field.status.name}"
	else:
		return f"{field}"
