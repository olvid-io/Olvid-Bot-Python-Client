# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: olvid/daemon/services/v1/notification_service.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'olvid/daemon/services/v1/notification_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .....olvid.daemon.notification.v1 import attachment_notifications_pb2 as olvid_dot_daemon_dot_notification_dot_v1_dot_attachment__notifications__pb2
from .....olvid.daemon.notification.v1 import contact_notifications_pb2 as olvid_dot_daemon_dot_notification_dot_v1_dot_contact__notifications__pb2
from .....olvid.daemon.notification.v1 import discussion_notifications_pb2 as olvid_dot_daemon_dot_notification_dot_v1_dot_discussion__notifications__pb2
from .....olvid.daemon.notification.v1 import group_notifications_pb2 as olvid_dot_daemon_dot_notification_dot_v1_dot_group__notifications__pb2
from .....olvid.daemon.notification.v1 import invitation_notifications_pb2 as olvid_dot_daemon_dot_notification_dot_v1_dot_invitation__notifications__pb2
from .....olvid.daemon.notification.v1 import message_notifications_pb2 as olvid_dot_daemon_dot_notification_dot_v1_dot_message__notifications__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3olvid/daemon/services/v1/notification_service.proto\x12\x18olvid.daemon.services.v1\x1a;olvid/daemon/notification/v1/attachment_notifications.proto\x1a\x38olvid/daemon/notification/v1/contact_notifications.proto\x1a;olvid/daemon/notification/v1/discussion_notifications.proto\x1a\x36olvid/daemon/notification/v1/group_notifications.proto\x1a;olvid/daemon/notification/v1/invitation_notifications.proto\x1a\x38olvid/daemon/notification/v1/message_notifications.proto2\x8d\x05\n\x1dInvitationNotificationService\x12\x9d\x01\n\x12InvitationReceived\x12G.olvid.daemon.notification.v1.SubscribeToInvitationReceivedNotification\x1a<.olvid.daemon.notification.v1.InvitationReceivedNotification0\x01\x12\x91\x01\n\x0eInvitationSent\x12\x43.olvid.daemon.notification.v1.SubscribeToInvitationSentNotification\x1a\x38.olvid.daemon.notification.v1.InvitationSentNotification0\x01\x12\x9a\x01\n\x11InvitationDeleted\x12\x46.olvid.daemon.notification.v1.SubscribeToInvitationDeletedNotification\x1a;.olvid.daemon.notification.v1.InvitationDeletedNotification0\x01\x12\x9a\x01\n\x11InvitationUpdated\x12\x46.olvid.daemon.notification.v1.SubscribeToInvitationUpdatedNotification\x1a;.olvid.daemon.notification.v1.InvitationUpdatedNotification0\x01\x32\x8c\x05\n\x1a\x43ontactNotificationService\x12\x87\x01\n\nContactNew\x12?.olvid.daemon.notification.v1.SubscribeToContactNewNotification\x1a\x34.olvid.daemon.notification.v1.ContactNewNotification\"\x00\x30\x01\x12\x93\x01\n\x0e\x43ontactDeleted\x12\x43.olvid.daemon.notification.v1.SubscribeToContactDeletedNotification\x1a\x38.olvid.daemon.notification.v1.ContactDeletedNotification\"\x00\x30\x01\x12\xa8\x01\n\x15\x43ontactDetailsUpdated\x12J.olvid.daemon.notification.v1.SubscribeToContactDetailsUpdatedNotification\x1a?.olvid.daemon.notification.v1.ContactDetailsUpdatedNotification\"\x00\x30\x01\x12\xa2\x01\n\x13\x43ontactPhotoUpdated\x12H.olvid.daemon.notification.v1.SubscribeToContactPhotoUpdatedNotification\x1a=.olvid.daemon.notification.v1.ContactPhotoUpdatedNotification\"\x00\x30\x01\x32\x87\x11\n\x18GroupNotificationService\x12\x81\x01\n\x08GroupNew\x12=.olvid.daemon.notification.v1.SubscribeToGroupNewNotification\x1a\x32.olvid.daemon.notification.v1.GroupNewNotification\"\x00\x30\x01\x12\x8d\x01\n\x0cGroupDeleted\x12\x41.olvid.daemon.notification.v1.SubscribeToGroupDeletedNotification\x1a\x36.olvid.daemon.notification.v1.GroupDeletedNotification\"\x00\x30\x01\x12\x99\x01\n\x10GroupNameUpdated\x12\x45.olvid.daemon.notification.v1.SubscribeToGroupNameUpdatedNotification\x1a:.olvid.daemon.notification.v1.GroupNameUpdatedNotification\"\x00\x30\x01\x12\x9c\x01\n\x11GroupPhotoUpdated\x12\x46.olvid.daemon.notification.v1.SubscribeToGroupPhotoUpdatedNotification\x1a;.olvid.daemon.notification.v1.GroupPhotoUpdatedNotification\"\x00\x30\x01\x12\xae\x01\n\x17GroupDescriptionUpdated\x12L.olvid.daemon.notification.v1.SubscribeToGroupDescriptionUpdatedNotification\x1a\x41.olvid.daemon.notification.v1.GroupDescriptionUpdatedNotification\"\x00\x30\x01\x12\xae\x01\n\x17GroupPendingMemberAdded\x12L.olvid.daemon.notification.v1.SubscribeToGroupPendingMemberAddedNotification\x1a\x41.olvid.daemon.notification.v1.GroupPendingMemberAddedNotification\"\x00\x30\x01\x12\xb4\x01\n\x19GroupPendingMemberRemoved\x12N.olvid.daemon.notification.v1.SubscribeToGroupPendingMemberRemovedNotification\x1a\x43.olvid.daemon.notification.v1.GroupPendingMemberRemovedNotification\"\x00\x30\x01\x12\x9c\x01\n\x11GroupMemberJoined\x12\x46.olvid.daemon.notification.v1.SubscribeToGroupMemberJoinedNotification\x1a;.olvid.daemon.notification.v1.GroupMemberJoinedNotification\"\x00\x30\x01\x12\x96\x01\n\x0fGroupMemberLeft\x12\x44.olvid.daemon.notification.v1.SubscribeToGroupMemberLeftNotification\x1a\x39.olvid.daemon.notification.v1.GroupMemberLeftNotification\"\x00\x30\x01\x12\xb7\x01\n\x1aGroupOwnPermissionsUpdated\x12O.olvid.daemon.notification.v1.SubscribeToGroupOwnPermissionsUpdatedNotification\x1a\x44.olvid.daemon.notification.v1.GroupOwnPermissionsUpdatedNotification\"\x00\x30\x01\x12\xc0\x01\n\x1dGroupMemberPermissionsUpdated\x12R.olvid.daemon.notification.v1.SubscribeToGroupMemberPermissionsUpdatedNotification\x1aG.olvid.daemon.notification.v1.GroupMemberPermissionsUpdatedNotification\"\x00\x30\x01\x12\xa8\x01\n\x15GroupUpdateInProgress\x12J.olvid.daemon.notification.v1.SubscribeToGroupUpdateInProgressNotification\x1a?.olvid.daemon.notification.v1.GroupUpdateInProgressNotification\"\x00\x30\x01\x12\xa2\x01\n\x13GroupUpdateFinished\x12H.olvid.daemon.notification.v1.SubscribeToGroupUpdateFinishedNotification\x1a=.olvid.daemon.notification.v1.GroupUpdateFinishedNotification\"\x00\x30\x01\x32\xb3\x05\n\x1d\x44iscussionNotificationService\x12\x90\x01\n\rDiscussionNew\x12\x42.olvid.daemon.notification.v1.SubscribeToDiscussionNewNotification\x1a\x37.olvid.daemon.notification.v1.DiscussionNewNotification\"\x00\x30\x01\x12\x99\x01\n\x10\x44iscussionLocked\x12\x45.olvid.daemon.notification.v1.SubscribeToDiscussionLockedNotification\x1a:.olvid.daemon.notification.v1.DiscussionLockedNotification\"\x00\x30\x01\x12\xab\x01\n\x16\x44iscussionTitleUpdated\x12K.olvid.daemon.notification.v1.SubscribeToDiscussionTitleUpdatedNotification\x1a@.olvid.daemon.notification.v1.DiscussionTitleUpdatedNotification\"\x00\x30\x01\x12\xb4\x01\n\x19\x44iscussionSettingsUpdated\x12N.olvid.daemon.notification.v1.SubscribeToDiscussionSettingsUpdatedNotification\x1a\x43.olvid.daemon.notification.v1.DiscussionSettingsUpdatedNotification\"\x00\x30\x01\x32\xa5\x12\n\x1aMessageNotificationService\x12\x96\x01\n\x0fMessageReceived\x12\x44.olvid.daemon.notification.v1.SubscribeToMessageReceivedNotification\x1a\x39.olvid.daemon.notification.v1.MessageReceivedNotification\"\x00\x30\x01\x12\x8a\x01\n\x0bMessageSent\x12@.olvid.daemon.notification.v1.SubscribeToMessageSentNotification\x1a\x35.olvid.daemon.notification.v1.MessageSentNotification\"\x00\x30\x01\x12\x93\x01\n\x0eMessageDeleted\x12\x43.olvid.daemon.notification.v1.SubscribeToMessageDeletedNotification\x1a\x38.olvid.daemon.notification.v1.MessageDeletedNotification\"\x00\x30\x01\x12\x9f\x01\n\x12MessageBodyUpdated\x12G.olvid.daemon.notification.v1.SubscribeToMessageBodyUpdatedNotification\x1a<.olvid.daemon.notification.v1.MessageBodyUpdatedNotification\"\x00\x30\x01\x12\x96\x01\n\x0fMessageUploaded\x12\x44.olvid.daemon.notification.v1.SubscribeToMessageUploadedNotification\x1a\x39.olvid.daemon.notification.v1.MessageUploadedNotification\"\x00\x30\x01\x12\x99\x01\n\x10MessageDelivered\x12\x45.olvid.daemon.notification.v1.SubscribeToMessageDeliveredNotification\x1a:.olvid.daemon.notification.v1.MessageDeliveredNotification\"\x00\x30\x01\x12\x8a\x01\n\x0bMessageRead\x12@.olvid.daemon.notification.v1.SubscribeToMessageReadNotification\x1a\x35.olvid.daemon.notification.v1.MessageReadNotification\"\x00\x30\x01\x12\xae\x01\n\x17MessageLocationReceived\x12L.olvid.daemon.notification.v1.SubscribeToMessageLocationReceivedNotification\x1a\x41.olvid.daemon.notification.v1.MessageLocationReceivedNotification\"\x00\x30\x01\x12\xba\x01\n\x1bMessageLocationSharingStart\x12P.olvid.daemon.notification.v1.SubscribeToMessageLocationSharingStartNotification\x1a\x45.olvid.daemon.notification.v1.MessageLocationSharingStartNotification\"\x00\x30\x01\x12\xbd\x01\n\x1cMessageLocationSharingUpdate\x12Q.olvid.daemon.notification.v1.SubscribeToMessageLocationSharingUpdateNotification\x1a\x46.olvid.daemon.notification.v1.MessageLocationSharingUpdateNotification\"\x00\x30\x01\x12\xb4\x01\n\x19MessageLocationSharingEnd\x12N.olvid.daemon.notification.v1.SubscribeToMessageLocationSharingEndNotification\x1a\x43.olvid.daemon.notification.v1.MessageLocationSharingEndNotification\"\x00\x30\x01\x12\xa5\x01\n\x14MessageReactionAdded\x12I.olvid.daemon.notification.v1.SubscribeToMessageReactionAddedNotification\x1a>.olvid.daemon.notification.v1.MessageReactionAddedNotification\"\x00\x30\x01\x12\xab\x01\n\x16MessageReactionUpdated\x12K.olvid.daemon.notification.v1.SubscribeToMessageReactionUpdatedNotification\x1a@.olvid.daemon.notification.v1.MessageReactionUpdatedNotification\"\x00\x30\x01\x12\xab\x01\n\x16MessageReactionRemoved\x12K.olvid.daemon.notification.v1.SubscribeToMessageReactionRemovedNotification\x1a@.olvid.daemon.notification.v1.MessageReactionRemovedNotification\"\x00\x30\x01\x32\xe3\x02\n\x1d\x41ttachmentNotificationService\x12\x9f\x01\n\x12\x41ttachmentReceived\x12G.olvid.daemon.notification.v1.SubscribeToAttachmentReceivedNotification\x1a<.olvid.daemon.notification.v1.AttachmentReceivedNotification\"\x00\x30\x01\x12\x9f\x01\n\x12\x41ttachmentUploaded\x12G.olvid.daemon.notification.v1.SubscribeToAttachmentUploadedNotification\x1a<.olvid.daemon.notification.v1.AttachmentUploadedNotification\"\x00\x30\x01\x42\xcc\x01\n\x1c\x63om.olvid.daemon.services.v1B\x18NotificationServiceProtoP\x01Z\x0folvid.io/daemon\xa2\x02\x03ODS\xaa\x02\x18Olvid.Daemon.Services.V1\xca\x02\x18Olvid\\Daemon\\Services\\V1\xe2\x02$Olvid\\Daemon\\Services\\V1\\GPBMetadata\xea\x02\x1bOlvid::Daemon::Services::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'olvid.daemon.services.v1.notification_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.olvid.daemon.services.v1B\030NotificationServiceProtoP\001Z\017olvid.io/daemon\242\002\003ODS\252\002\030Olvid.Daemon.Services.V1\312\002\030Olvid\\Daemon\\Services\\V1\342\002$Olvid\\Daemon\\Services\\V1\\GPBMetadata\352\002\033Olvid::Daemon::Services::V1'
  _globals['_INVITATIONNOTIFICATIONSERVICE']._serialized_start=437
  _globals['_INVITATIONNOTIFICATIONSERVICE']._serialized_end=1090
  _globals['_CONTACTNOTIFICATIONSERVICE']._serialized_start=1093
  _globals['_CONTACTNOTIFICATIONSERVICE']._serialized_end=1745
  _globals['_GROUPNOTIFICATIONSERVICE']._serialized_start=1748
  _globals['_GROUPNOTIFICATIONSERVICE']._serialized_end=3931
  _globals['_DISCUSSIONNOTIFICATIONSERVICE']._serialized_start=3934
  _globals['_DISCUSSIONNOTIFICATIONSERVICE']._serialized_end=4625
  _globals['_MESSAGENOTIFICATIONSERVICE']._serialized_start=4628
  _globals['_MESSAGENOTIFICATIONSERVICE']._serialized_end=6969
  _globals['_ATTACHMENTNOTIFICATIONSERVICE']._serialized_start=6972
  _globals['_ATTACHMENTNOTIFICATIONSERVICE']._serialized_end=7327
# @@protoc_insertion_point(module_scope)
