# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: olvid/daemon/datatypes/v1/message.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'olvid/daemon/datatypes/v1/message.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'olvid/daemon/datatypes/v1/message.proto\x12\x19olvid.daemon.datatypes.v1\"\x9d\x01\n\tMessageId\x12=\n\x04type\x18\x01 \x01(\x0e\x32).olvid.daemon.datatypes.v1.MessageId.TypeR\x04type\x12\x0e\n\x02id\x18\x02 \x01(\x04R\x02id\"A\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cTYPE_INBOUND\x10\x01\x12\x11\n\rTYPE_OUTBOUND\x10\x02\"\xaa\x04\n\x07Message\x12\x34\n\x02id\x18\x01 \x01(\x0b\x32$.olvid.daemon.datatypes.v1.MessageIdR\x02id\x12#\n\rdiscussion_id\x18\x02 \x01(\x04R\x0c\x64iscussionId\x12\x1b\n\tsender_id\x18\x03 \x01(\x04R\x08senderId\x12\x12\n\x04\x62ody\x18\x04 \x01(\tR\x04\x62ody\x12\x1d\n\nsort_index\x18\x05 \x01(\x01R\tsortIndex\x12\x1c\n\ttimestamp\x18\x06 \x01(\x04R\ttimestamp\x12+\n\x11\x61ttachments_count\x18\x07 \x01(\x04R\x10\x61ttachmentsCount\x12W\n\x12replied_message_id\x18\x08 \x01(\x0b\x32$.olvid.daemon.datatypes.v1.MessageIdH\x00R\x10repliedMessageId\x88\x01\x01\x12Z\n\x10message_location\x18\n \x01(\x0b\x32*.olvid.daemon.datatypes.v1.MessageLocationH\x01R\x0fmessageLocation\x88\x01\x01\x12H\n\treactions\x18\x0b \x03(\x0b\x32*.olvid.daemon.datatypes.v1.MessageReactionR\treactionsB\x15\n\x13_replied_message_idB\x13\n\x11_message_location\"\x92\x01\n\x13MessageEphemerality\x12\x1b\n\tread_once\x18\x01 \x01(\x08R\x08readOnce\x12-\n\x12\x65xistence_duration\x18\x02 \x01(\x04R\x11\x65xistenceDuration\x12/\n\x13visibility_duration\x18\x03 \x01(\x04R\x12visibilityDuration\"j\n\x0fMessageReaction\x12\x1d\n\ncontact_id\x18\x01 \x01(\x04R\tcontactId\x12\x1a\n\x08reaction\x18\x02 \x01(\tR\x08reaction\x12\x1c\n\ttimestamp\x18\x03 \x01(\x04R\ttimestamp\"\xc7\x03\n\x0fMessageLocation\x12K\n\x04type\x18\x01 \x01(\x0e\x32\x37.olvid.daemon.datatypes.v1.MessageLocation.LocationTypeR\x04type\x12\x1c\n\ttimestamp\x18\x02 \x01(\x04R\ttimestamp\x12\x1a\n\x08latitude\x18\x03 \x01(\x01R\x08latitude\x12\x1c\n\tlongitude\x18\x04 \x01(\x01R\tlongitude\x12\x1f\n\x08\x61ltitude\x18\x05 \x01(\x01H\x00R\x08\x61ltitude\x88\x01\x01\x12!\n\tprecision\x18\x06 \x01(\x01H\x01R\tprecision\x88\x01\x01\x12\x1d\n\x07\x61\x64\x64ress\x18\x07 \x01(\tH\x02R\x07\x61\x64\x64ress\x88\x01\x01\"\x84\x01\n\x0cLocationType\x12\x1d\n\x19LOCATION_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12LOCATION_TYPE_SEND\x10\x01\x12\x19\n\x15LOCATION_TYPE_SHARING\x10\x02\x12\"\n\x1eLOCATION_TYPE_SHARING_FINISHED\x10\x03\x42\x0b\n\t_altitudeB\x0c\n\n_precisionB\n\n\x08_address\"\x9f\n\n\rMessageFilter\x12\x42\n\x04type\x18\x01 \x01(\x0e\x32).olvid.daemon.datatypes.v1.MessageId.TypeH\x01R\x04type\x88\x01\x01\x12(\n\rdiscussion_id\x18\x02 \x01(\x04H\x02R\x0c\x64iscussionId\x88\x01\x01\x12/\n\x11sender_contact_id\x18\x03 \x01(\x04H\x03R\x0fsenderContactId\x88\x01\x01\x12$\n\x0b\x62ody_search\x18\x05 \x01(\tH\x04R\nbodySearch\x88\x01\x01\x12X\n\nattachment\x18\x06 \x01(\x0e\x32\x33.olvid.daemon.datatypes.v1.MessageFilter.AttachmentH\x05R\nattachment\x88\x01\x01\x12R\n\x08location\x18\x07 \x01(\x0e\x32\x31.olvid.daemon.datatypes.v1.MessageFilter.LocationH\x06R\x08location\x88\x01\x01\x12(\n\rmin_timestamp\x18\x08 \x01(\x04H\x07R\x0cminTimestamp\x88\x01\x01\x12(\n\rmax_timestamp\x18\t \x01(\x04H\x08R\x0cmaxTimestamp\x88\x01\x01\x12R\n\x08reaction\x18\n \x01(\x0e\x32\x31.olvid.daemon.datatypes.v1.MessageFilter.ReactionH\tR\x08reaction\x88\x01\x01\x12T\n\x10reactions_filter\x18\x0b \x03(\x0b\x32).olvid.daemon.datatypes.v1.ReactionFilterR\x0freactionsFilter\x12-\n\x12reply_to_a_message\x18\r \x01(\x08H\x00R\x0freplyToAMessage\x12\x39\n\x19\x64o_not_reply_to_a_message\x18\x0e \x01(\x08H\x00R\x14\x64oNotReplyToAMessage\x12T\n\x12replied_message_id\x18\x0f \x01(\x0b\x32$.olvid.daemon.datatypes.v1.MessageIdH\x00R\x10repliedMessageId\"V\n\nAttachment\x12\x1a\n\x16\x41TTACHMENT_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x41TTACHMENT_HAVE\x10\x01\x12\x17\n\x13\x41TTACHMENT_HAVE_NOT\x10\x02\"\x9f\x01\n\x08Location\x12\x18\n\x14LOCATION_UNSPECIFIED\x10\x00\x12\x11\n\rLOCATION_HAVE\x10\x01\x12\x15\n\x11LOCATION_HAVE_NOT\x10\x02\x12\x14\n\x10LOCATION_IS_SEND\x10\x03\x12\x17\n\x13LOCATION_IS_SHARING\x10\x05\x12 \n\x1cLOCATION_IS_SHARING_FINISHED\x10\x06\"L\n\x08Reaction\x12\x18\n\x14REACTION_UNSPECIFIED\x10\x00\x12\x10\n\x0cREACTION_HAS\x10\x01\x12\x14\n\x10REACTION_HAS_NOT\x10\x02\x42\x07\n\x05replyB\x07\n\x05_typeB\x10\n\x0e_discussion_idB\x14\n\x12_sender_contact_idB\x0e\n\x0c_body_searchB\r\n\x0b_attachmentB\x0b\n\t_locationB\x10\n\x0e_min_timestampB\x10\n\x0e_max_timestampB\x0b\n\t_reaction\"\xa7\x01\n\x0eReactionFilter\x12$\n\rreacted_by_me\x18\n \x01(\x08H\x00R\x0breactedByMe\x12\x33\n\x15reacted_by_contact_id\x18\x0b \x01(\x04H\x00R\x12reactedByContactId\x12\x1f\n\x08reaction\x18\x0c \x01(\tH\x01R\x08reaction\x88\x01\x01\x42\x0c\n\nreacted_byB\x0b\n\t_reactionB\xc5\x01\n\x1d\x63om.olvid.daemon.datatypes.v1B\x0cMessageProtoP\x01Z\x0folvid.io/daemon\xa2\x02\x03ODD\xaa\x02\x19Olvid.Daemon.Datatypes.V1\xca\x02\x19Olvid\\Daemon\\Datatypes\\V1\xe2\x02%Olvid\\Daemon\\Datatypes\\V1\\GPBMetadata\xea\x02\x1cOlvid::Daemon::Datatypes::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'olvid.daemon.datatypes.v1.message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.olvid.daemon.datatypes.v1B\014MessageProtoP\001Z\017olvid.io/daemon\242\002\003ODD\252\002\031Olvid.Daemon.Datatypes.V1\312\002\031Olvid\\Daemon\\Datatypes\\V1\342\002%Olvid\\Daemon\\Datatypes\\V1\\GPBMetadata\352\002\034Olvid::Daemon::Datatypes::V1'
  _globals['_MESSAGEID']._serialized_start=71
  _globals['_MESSAGEID']._serialized_end=228
  _globals['_MESSAGEID_TYPE']._serialized_start=163
  _globals['_MESSAGEID_TYPE']._serialized_end=228
  _globals['_MESSAGE']._serialized_start=231
  _globals['_MESSAGE']._serialized_end=785
  _globals['_MESSAGEEPHEMERALITY']._serialized_start=788
  _globals['_MESSAGEEPHEMERALITY']._serialized_end=934
  _globals['_MESSAGEREACTION']._serialized_start=936
  _globals['_MESSAGEREACTION']._serialized_end=1042
  _globals['_MESSAGELOCATION']._serialized_start=1045
  _globals['_MESSAGELOCATION']._serialized_end=1500
  _globals['_MESSAGELOCATION_LOCATIONTYPE']._serialized_start=1329
  _globals['_MESSAGELOCATION_LOCATIONTYPE']._serialized_end=1461
  _globals['_MESSAGEFILTER']._serialized_start=1503
  _globals['_MESSAGEFILTER']._serialized_end=2814
  _globals['_MESSAGEFILTER_ATTACHMENT']._serialized_start=2337
  _globals['_MESSAGEFILTER_ATTACHMENT']._serialized_end=2423
  _globals['_MESSAGEFILTER_LOCATION']._serialized_start=2426
  _globals['_MESSAGEFILTER_LOCATION']._serialized_end=2585
  _globals['_MESSAGEFILTER_REACTION']._serialized_start=2587
  _globals['_MESSAGEFILTER_REACTION']._serialized_end=2663
  _globals['_REACTIONFILTER']._serialized_start=2817
  _globals['_REACTIONFILTER']._serialized_end=2984
# @@protoc_insertion_point(module_scope)
