# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: olvid/daemon/notification/v1/message_notifications.proto
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
    'olvid/daemon/notification/v1/message_notifications.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .....olvid.daemon.datatypes.v1 import message_pb2 as olvid_dot_daemon_dot_datatypes_dot_v1_dot_message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8olvid/daemon/notification/v1/message_notifications.proto\x12\x1colvid.daemon.notification.v1\x1a\'olvid/daemon/datatypes/v1/message.proto\"(\n&SubscribeToMessageReceivedNotification\"[\n\x1bMessageReceivedNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\"$\n\"SubscribeToMessageSentNotification\"W\n\x17MessageSentNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\"\'\n%SubscribeToMessageDeletedNotification\"Z\n\x1aMessageDeletedNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\"+\n)SubscribeToMessageBodyUpdatedNotification\"\x83\x01\n\x1eMessageBodyUpdatedNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\x12#\n\rprevious_body\x18\x02 \x01(\tR\x0cpreviousBody\"(\n&SubscribeToMessageUploadedNotification\"[\n\x1bMessageUploadedNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\")\n\'SubscribeToMessageDeliveredNotification\"\\\n\x1cMessageDeliveredNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\"$\n\"SubscribeToMessageReadNotification\"W\n\x17MessageReadNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\"0\n.SubscribeToMessageLocationReceivedNotification\"c\n#MessageLocationReceivedNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\",\n*SubscribeToMessageLocationSentNotification\"_\n\x1fMessageLocationSentNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\"4\n2SubscribeToMessageLocationSharingStartNotification\"g\n\'MessageLocationSharingStartNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\"5\n3SubscribeToMessageLocationSharingUpdateNotification\"\xc1\x01\n(MessageLocationSharingUpdateNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\x12W\n\x11previous_location\x18\x02 \x01(\x0b\x32*.olvid.daemon.datatypes.v1.MessageLocationR\x10previousLocation\"2\n0SubscribeToMessageLocationSharingEndNotification\"e\n%MessageLocationSharingEndNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\"-\n+SubscribeToMessageReactionAddedNotification\"\xa8\x01\n MessageReactionAddedNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\x12\x46\n\x08reaction\x18\x02 \x01(\x0b\x32*.olvid.daemon.datatypes.v1.MessageReactionR\x08reaction\"/\n-SubscribeToMessageReactionUpdatedNotification\"\x83\x02\n\"MessageReactionUpdatedNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\x12\x46\n\x08reaction\x18\x02 \x01(\x0b\x32*.olvid.daemon.datatypes.v1.MessageReactionR\x08reaction\x12W\n\x11previous_reaction\x18\x03 \x01(\x0b\x32*.olvid.daemon.datatypes.v1.MessageReactionR\x10previousReaction\"/\n-SubscribeToMessageReactionRemovedNotification\"\xaa\x01\n\"MessageReactionRemovedNotification\x12<\n\x07message\x18\x01 \x01(\x0b\x32\".olvid.daemon.datatypes.v1.MessageR\x07message\x12\x46\n\x08reaction\x18\x02 \x01(\x0b\x32*.olvid.daemon.datatypes.v1.MessageReactionR\x08reactionB\xe1\x01\n com.olvid.daemon.notification.v1B\x19MessageNotificationsProtoP\x01Z\x0folvid.io/daemon\xa2\x02\x03ODN\xaa\x02\x1cOlvid.Daemon.Notification.V1\xca\x02\x1cOlvid\\Daemon\\Notification\\V1\xe2\x02(Olvid\\Daemon\\Notification\\V1\\GPBMetadata\xea\x02\x1fOlvid::Daemon::Notification::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'olvid.daemon.notification.v1.message_notifications_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.olvid.daemon.notification.v1B\031MessageNotificationsProtoP\001Z\017olvid.io/daemon\242\002\003ODN\252\002\034Olvid.Daemon.Notification.V1\312\002\034Olvid\\Daemon\\Notification\\V1\342\002(Olvid\\Daemon\\Notification\\V1\\GPBMetadata\352\002\037Olvid::Daemon::Notification::V1'
  _globals['_SUBSCRIBETOMESSAGERECEIVEDNOTIFICATION']._serialized_start=131
  _globals['_SUBSCRIBETOMESSAGERECEIVEDNOTIFICATION']._serialized_end=171
  _globals['_MESSAGERECEIVEDNOTIFICATION']._serialized_start=173
  _globals['_MESSAGERECEIVEDNOTIFICATION']._serialized_end=264
  _globals['_SUBSCRIBETOMESSAGESENTNOTIFICATION']._serialized_start=266
  _globals['_SUBSCRIBETOMESSAGESENTNOTIFICATION']._serialized_end=302
  _globals['_MESSAGESENTNOTIFICATION']._serialized_start=304
  _globals['_MESSAGESENTNOTIFICATION']._serialized_end=391
  _globals['_SUBSCRIBETOMESSAGEDELETEDNOTIFICATION']._serialized_start=393
  _globals['_SUBSCRIBETOMESSAGEDELETEDNOTIFICATION']._serialized_end=432
  _globals['_MESSAGEDELETEDNOTIFICATION']._serialized_start=434
  _globals['_MESSAGEDELETEDNOTIFICATION']._serialized_end=524
  _globals['_SUBSCRIBETOMESSAGEBODYUPDATEDNOTIFICATION']._serialized_start=526
  _globals['_SUBSCRIBETOMESSAGEBODYUPDATEDNOTIFICATION']._serialized_end=569
  _globals['_MESSAGEBODYUPDATEDNOTIFICATION']._serialized_start=572
  _globals['_MESSAGEBODYUPDATEDNOTIFICATION']._serialized_end=703
  _globals['_SUBSCRIBETOMESSAGEUPLOADEDNOTIFICATION']._serialized_start=705
  _globals['_SUBSCRIBETOMESSAGEUPLOADEDNOTIFICATION']._serialized_end=745
  _globals['_MESSAGEUPLOADEDNOTIFICATION']._serialized_start=747
  _globals['_MESSAGEUPLOADEDNOTIFICATION']._serialized_end=838
  _globals['_SUBSCRIBETOMESSAGEDELIVEREDNOTIFICATION']._serialized_start=840
  _globals['_SUBSCRIBETOMESSAGEDELIVEREDNOTIFICATION']._serialized_end=881
  _globals['_MESSAGEDELIVEREDNOTIFICATION']._serialized_start=883
  _globals['_MESSAGEDELIVEREDNOTIFICATION']._serialized_end=975
  _globals['_SUBSCRIBETOMESSAGEREADNOTIFICATION']._serialized_start=977
  _globals['_SUBSCRIBETOMESSAGEREADNOTIFICATION']._serialized_end=1013
  _globals['_MESSAGEREADNOTIFICATION']._serialized_start=1015
  _globals['_MESSAGEREADNOTIFICATION']._serialized_end=1102
  _globals['_SUBSCRIBETOMESSAGELOCATIONRECEIVEDNOTIFICATION']._serialized_start=1104
  _globals['_SUBSCRIBETOMESSAGELOCATIONRECEIVEDNOTIFICATION']._serialized_end=1152
  _globals['_MESSAGELOCATIONRECEIVEDNOTIFICATION']._serialized_start=1154
  _globals['_MESSAGELOCATIONRECEIVEDNOTIFICATION']._serialized_end=1253
  _globals['_SUBSCRIBETOMESSAGELOCATIONSENTNOTIFICATION']._serialized_start=1255
  _globals['_SUBSCRIBETOMESSAGELOCATIONSENTNOTIFICATION']._serialized_end=1299
  _globals['_MESSAGELOCATIONSENTNOTIFICATION']._serialized_start=1301
  _globals['_MESSAGELOCATIONSENTNOTIFICATION']._serialized_end=1396
  _globals['_SUBSCRIBETOMESSAGELOCATIONSHARINGSTARTNOTIFICATION']._serialized_start=1398
  _globals['_SUBSCRIBETOMESSAGELOCATIONSHARINGSTARTNOTIFICATION']._serialized_end=1450
  _globals['_MESSAGELOCATIONSHARINGSTARTNOTIFICATION']._serialized_start=1452
  _globals['_MESSAGELOCATIONSHARINGSTARTNOTIFICATION']._serialized_end=1555
  _globals['_SUBSCRIBETOMESSAGELOCATIONSHARINGUPDATENOTIFICATION']._serialized_start=1557
  _globals['_SUBSCRIBETOMESSAGELOCATIONSHARINGUPDATENOTIFICATION']._serialized_end=1610
  _globals['_MESSAGELOCATIONSHARINGUPDATENOTIFICATION']._serialized_start=1613
  _globals['_MESSAGELOCATIONSHARINGUPDATENOTIFICATION']._serialized_end=1806
  _globals['_SUBSCRIBETOMESSAGELOCATIONSHARINGENDNOTIFICATION']._serialized_start=1808
  _globals['_SUBSCRIBETOMESSAGELOCATIONSHARINGENDNOTIFICATION']._serialized_end=1858
  _globals['_MESSAGELOCATIONSHARINGENDNOTIFICATION']._serialized_start=1860
  _globals['_MESSAGELOCATIONSHARINGENDNOTIFICATION']._serialized_end=1961
  _globals['_SUBSCRIBETOMESSAGEREACTIONADDEDNOTIFICATION']._serialized_start=1963
  _globals['_SUBSCRIBETOMESSAGEREACTIONADDEDNOTIFICATION']._serialized_end=2008
  _globals['_MESSAGEREACTIONADDEDNOTIFICATION']._serialized_start=2011
  _globals['_MESSAGEREACTIONADDEDNOTIFICATION']._serialized_end=2179
  _globals['_SUBSCRIBETOMESSAGEREACTIONUPDATEDNOTIFICATION']._serialized_start=2181
  _globals['_SUBSCRIBETOMESSAGEREACTIONUPDATEDNOTIFICATION']._serialized_end=2228
  _globals['_MESSAGEREACTIONUPDATEDNOTIFICATION']._serialized_start=2231
  _globals['_MESSAGEREACTIONUPDATEDNOTIFICATION']._serialized_end=2490
  _globals['_SUBSCRIBETOMESSAGEREACTIONREMOVEDNOTIFICATION']._serialized_start=2492
  _globals['_SUBSCRIBETOMESSAGEREACTIONREMOVEDNOTIFICATION']._serialized_end=2539
  _globals['_MESSAGEREACTIONREMOVEDNOTIFICATION']._serialized_start=2542
  _globals['_MESSAGEREACTIONREMOVEDNOTIFICATION']._serialized_end=2712
# @@protoc_insertion_point(module_scope)
