# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: olvid/daemon/datatypes/v1/discussion.proto
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
    'olvid/daemon/datatypes/v1/discussion.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*olvid/daemon/datatypes/v1/discussion.proto\x12\x19olvid.daemon.datatypes.v1\"~\n\nDiscussion\x12\x0e\n\x02id\x18\x01 \x01(\x04R\x02id\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12\x1f\n\ncontact_id\x18\x03 \x01(\x04H\x00R\tcontactId\x12\x1b\n\x08group_id\x18\x04 \x01(\x04H\x00R\x07groupIdB\x0c\n\nidentifier\"\xb6\x01\n\x12\x44iscussionSettings\x12#\n\rdiscussion_id\x18\x01 \x01(\x04R\x0c\x64iscussionId\x12\x1b\n\tread_once\x18\x02 \x01(\x08R\x08readOnce\x12-\n\x12\x65xistence_duration\x18\x03 \x01(\x04R\x11\x65xistenceDuration\x12/\n\x13visibility_duration\x18\x04 \x01(\x04R\x12visibilityDuration\"\xa7\x02\n\x10\x44iscussionFilter\x12I\n\x04type\x18\x01 \x01(\x0e\x32\x30.olvid.daemon.datatypes.v1.DiscussionFilter.TypeH\x01R\x04type\x88\x01\x01\x12\x1f\n\ncontact_id\x18\x02 \x01(\x04H\x00R\tcontactId\x12\x1b\n\x08group_id\x18\x03 \x01(\x04H\x00R\x07groupId\x12&\n\x0ctitle_search\x18\x04 \x01(\tH\x02R\x0btitleSearch\x88\x01\x01\":\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08TYPE_OTO\x10\x01\x12\x0e\n\nTYPE_GROUP\x10\x02\x42\x0c\n\nidentifierB\x07\n\x05_typeB\x0f\n\r_title_searchB\xc8\x01\n\x1d\x63om.olvid.daemon.datatypes.v1B\x0f\x44iscussionProtoP\x01Z\x0folvid.io/daemon\xa2\x02\x03ODD\xaa\x02\x19Olvid.Daemon.Datatypes.V1\xca\x02\x19Olvid\\Daemon\\Datatypes\\V1\xe2\x02%Olvid\\Daemon\\Datatypes\\V1\\GPBMetadata\xea\x02\x1cOlvid::Daemon::Datatypes::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'olvid.daemon.datatypes.v1.discussion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.olvid.daemon.datatypes.v1B\017DiscussionProtoP\001Z\017olvid.io/daemon\242\002\003ODD\252\002\031Olvid.Daemon.Datatypes.V1\312\002\031Olvid\\Daemon\\Datatypes\\V1\342\002%Olvid\\Daemon\\Datatypes\\V1\\GPBMetadata\352\002\034Olvid::Daemon::Datatypes::V1'
  _globals['_DISCUSSION']._serialized_start=73
  _globals['_DISCUSSION']._serialized_end=199
  _globals['_DISCUSSIONSETTINGS']._serialized_start=202
  _globals['_DISCUSSIONSETTINGS']._serialized_end=384
  _globals['_DISCUSSIONFILTER']._serialized_start=387
  _globals['_DISCUSSIONFILTER']._serialized_end=682
  _globals['_DISCUSSIONFILTER_TYPE']._serialized_start=584
  _globals['_DISCUSSIONFILTER_TYPE']._serialized_end=642
# @@protoc_insertion_point(module_scope)