from typing import Callable

import grpc
from olvid import OlvidAdminClient, OlvidClient, datatypes, listeners


async def listen(identity_id: int = 0, quiet: bool = False, notifications_to_listen: str = ""):
	admin_client: OlvidAdminClient = OlvidAdminClient(identity_id=0)
	# create clients, one per identity
	clients: list[OlvidClient] = []
	try:
		if identity_id <= 0:
			async for identity in admin_client.admin_identity_list():
				clients.append(OlvidAdminClient(identity_id=identity.id))
		else:
			clients.append(OlvidAdminClient(identity_id=identity_id))
	except grpc.aio.AioRpcError as e:
		print(e.details())
		return

	# determine notifications to listen to
	if not notifications_to_listen:
		notifications: list[listeners.NOTIFICATIONS] = [notification for notification in listeners.NOTIFICATIONS]
	else:
		notifications: list[listeners.NOTIFICATIONS] = [getattr(listeners.NOTIFICATIONS, notif_name) for notif_name in notifications_to_listen.split(",")]

	# add listeners
	for client in clients:
		identity: datatypes.Identity = await client.identity_get()
		for notification in notifications:
			listener_class_name = f"{''.join(s.title() for s in notification.name.split('_'))}Listener"
			listener_class = getattr(listeners, listener_class_name)
			client.add_listener(listener_class(handler=await get_notification_handler(identity, notification, quiet)))

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
