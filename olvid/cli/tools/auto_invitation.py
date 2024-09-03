import asyncio

from olvid import datatypes, OlvidAdminClient, listeners


# noinspection PyProtectedMember
async def invitation_task(identity_1: datatypes.Identity, identity_2: datatypes.Identity):
	global count, total_count

	client_1: OlvidAdminClient = OlvidAdminClient(identity_id=identity_1.id)
	client_2: OlvidAdminClient = OlvidAdminClient(identity_id=identity_2.id)
	# check if identity is already a contact
	details_search: datatypes.IdentityDetails = identity_2.details._clone()
	details_search.first_name = f"^{details_search.first_name}$"
	details_search.last_name = f"^{details_search.last_name}$"
	details_search.position = f"^{details_search.position}$"
	details_search.company = f"^{details_search.company}$"
	if [c async for c in client_1.contact_list(filter=datatypes.ContactFilter(details_search=details_search))]:
		count += 1
		print(f"{count:3} / {total_count:3} skipped: {identity_1.id} -> {identity_2.id}")
		return

	print(f"Processing: {identity_1.id} -> {identity_2.id}")

	# send invitation
	invitation_1: datatypes.Invitation = await client_1.invitation_new(identity_2.invitation_url)

	# wait for invitation to arrive
	invitation_store_2: list[datatypes.Invitation] = []
	listener = listeners.InvitationReceivedListener(lambda i: invitation_store_2.append(i), checkers=[lambda i: i.display_name == identity_1.display_name], count=1)
	client_2.add_listener(listener)
	await client_2.wait_for_listeners_end()
	invitation_2: datatypes.Invitation = invitation_store_2[0]

	# accept invitation 2
	await client_2.invitation_accept(invitation_id=invitation_2.id)

	# wait for invitation to be ready to set sas
	invitation_store_1: list[datatypes.Invitation] = []
	listener_1 = listeners.InvitationUpdatedListener(handler=lambda i, p: invitation_store_1.append(i), checkers=[lambda i, p: i.id == invitation_1.id and i.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE], count=1)
	client_1.add_listener(listener_1)

	invitation_store_2: list[datatypes.Invitation] = []
	listener_2 = listeners.InvitationUpdatedListener(handler=lambda i, p: invitation_store_2.append(i), checkers=[lambda i, p: i.id == invitation_2.id and i.status == datatypes.Invitation.Status.STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE], count=1)
	client_2.add_listener(listener_2)

	await client_1.wait_for_listeners_end()
	await client_2.wait_for_listeners_end()

	invitation_1 = invitation_store_1[0]
	invitation_2 = invitation_store_2[0]

	# set sas
	await client_1.invitation_sas(invitation_id=invitation_1.id, sas=invitation_2.sas)
	await client_2.invitation_sas(invitation_id=invitation_2.id, sas=invitation_1.sas)

	count += 1
	print(f"{count:3} / {total_count:3}: finished: {identity_1.id} -> {identity_2.id}")


count: int = 0
total_count: int = 0


async def auto_invite(identity_id: int, admin_client: OlvidAdminClient, full: bool = False):
	global total_count, count
	identities: list[datatypes.Identity] = [i async for i in admin_client.admin_identity_list()]
	len_identities: int = len(identities)
	count = 0
	if full:
		total_count = round(len_identities * ((len_identities - 1) / 2))
	else:
		total_count = len_identities - 1

	tasks = []

	# full mode
	if full:
		total_count = round(len_identities * ((len_identities - 1) / 2))
		for i in range(len(identities)):
			identity_1: datatypes.Identity = identities[i]
			for j in range(i, len_identities):
				identity_2: datatypes.Identity = identities[j]
				if identity_1.id == identity_2.id:
					continue

				tasks.append(admin_client.add_background_task(invitation_task(identities[i], identities[j])))
	else:
		current_identity: datatypes.Identity = await admin_client.admin_identity_admin_get(identity_id=identity_id)
		for i in range(len(identities)):
			identity_1: datatypes.Identity = identities[i]
			if identity_1.id == current_identity.id:
				continue
			tasks.append(admin_client.add_background_task(invitation_task(current_identity, identities[i])))

	print(f"Queued {len(tasks)} tasks")
	await asyncio.gather(*tasks)
