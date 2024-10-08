####
# WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_listeners_module.py
####

from enum import Enum


class NOTIFICATIONS(Enum):
	# InvitationNotificationService
	INVITATION_RECEIVED = 0
	INVITATION_SENT = 1
	INVITATION_DELETED = 2
	INVITATION_UPDATED = 3

	# ContactNotificationService
	CONTACT_NEW = 4
	CONTACT_DELETED = 5
	CONTACT_DETAILS_UPDATED = 6

	# GroupNotificationService
	GROUP_NEW = 7
	GROUP_DELETED = 8
	GROUP_NAME_UPDATED = 9
	GROUP_DESCRIPTION_UPDATED = 10
	GROUP_PENDING_MEMBER_ADDED = 11
	GROUP_PENDING_MEMBER_REMOVED = 12
	GROUP_MEMBER_JOINED = 13
	GROUP_MEMBER_LEFT = 14
	GROUP_OWN_PERMISSIONS_UPDATED = 15
	GROUP_MEMBER_PERMISSIONS_UPDATED = 16
	GROUP_UPDATE_IN_PROGRESS = 17
	GROUP_UPDATE_FINISHED = 18

	# DiscussionNotificationService
	DISCUSSION_NEW = 19
	DISCUSSION_LOCKED = 20
	DISCUSSION_TITLE_UPDATED = 21
	DISCUSSION_SETTINGS_UPDATED = 22

	# MessageNotificationService
	MESSAGE_RECEIVED = 23
	MESSAGE_SENT = 24
	MESSAGE_DELETED = 25
	MESSAGE_BODY_UPDATED = 26
	MESSAGE_UPLOADED = 27
	MESSAGE_DELIVERED = 28
	MESSAGE_READ = 29
	MESSAGE_LOCATION_RECEIVED = 30
	MESSAGE_LOCATION_SHARING_START = 31
	MESSAGE_LOCATION_SHARING_UPDATE = 32
	MESSAGE_LOCATION_SHARING_END = 33
	MESSAGE_REACTION_ADDED = 34
	MESSAGE_REACTION_UPDATED = 35
	MESSAGE_REACTION_REMOVED = 36

	# AttachmentNotificationService
	ATTACHMENT_RECEIVED = 37
	ATTACHMENT_UPLOADED = 38
		
