# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: olvid/daemon/datatypes/v1/attachment.proto
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
    'olvid/daemon/datatypes/v1/attachment.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .....olvid.daemon.datatypes.v1 import message_pb2 as olvid_dot_daemon_dot_datatypes_dot_v1_dot_message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*olvid/daemon/datatypes/v1/attachment.proto\x12\x19olvid.daemon.datatypes.v1\x1a\'olvid/daemon/datatypes/v1/message.proto\"\xa3\x01\n\x0c\x41ttachmentId\x12@\n\x04type\x18\x01 \x01(\x0e\x32,.olvid.daemon.datatypes.v1.AttachmentId.TypeR\x04type\x12\x0e\n\x02id\x18\x02 \x01(\x04R\x02id\"A\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cTYPE_INBOUND\x10\x01\x12\x11\n\rTYPE_OUTBOUND\x10\x02\"\xfd\x01\n\nAttachment\x12\x37\n\x02id\x18\x01 \x01(\x0b\x32\'.olvid.daemon.datatypes.v1.AttachmentIdR\x02id\x12#\n\rdiscussion_id\x18\x02 \x01(\x04R\x0c\x64iscussionId\x12\x43\n\nmessage_id\x18\x03 \x01(\x0b\x32$.olvid.daemon.datatypes.v1.MessageIdR\tmessageId\x12\x1b\n\tfile_name\x18\x04 \x01(\tR\x08\x66ileName\x12\x1b\n\tmime_type\x18\x05 \x01(\tR\x08mimeType\x12\x12\n\x04size\x18\x06 \x01(\x04R\x04size\"\xfb\x05\n\x10\x41ttachmentFilter\x12\x45\n\x04type\x18\x01 \x01(\x0e\x32,.olvid.daemon.datatypes.v1.AttachmentId.TypeH\x00R\x04type\x88\x01\x01\x12V\n\tfile_type\x18\x02 \x01(\x0e\x32\x34.olvid.daemon.datatypes.v1.AttachmentFilter.FileTypeH\x01R\x08\x66ileType\x88\x01\x01\x12(\n\rdiscussion_id\x18\x03 \x01(\x04H\x02R\x0c\x64iscussionId\x88\x01\x01\x12H\n\nmessage_id\x18\x05 \x01(\x0b\x32$.olvid.daemon.datatypes.v1.MessageIdH\x03R\tmessageId\x88\x01\x01\x12,\n\x0f\x66ilename_search\x18\x06 \x01(\tH\x04R\x0e\x66ilenameSearch\x88\x01\x01\x12-\n\x10mime_type_search\x18\x07 \x01(\tH\x05R\x0emimeTypeSearch\x88\x01\x01\x12\x1e\n\x08min_size\x18\x08 \x01(\x04H\x06R\x07minSize\x88\x01\x01\x12\x1e\n\x08max_size\x18\t \x01(\x04H\x07R\x07maxSize\x88\x01\x01\"\xbb\x01\n\x08\x46ileType\x12\x19\n\x15\x46ILE_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x46ILE_TYPE_IMAGE\x10\x03\x12\x13\n\x0f\x46ILE_TYPE_VIDEO\x10\x04\x12\x19\n\x15\x46ILE_TYPE_IMAGE_VIDEO\x10\x05\x12\x13\n\x0f\x46ILE_TYPE_AUDIO\x10\x06\x12\x1a\n\x16\x46ILE_TYPE_LINK_PREVIEW\x10\x07\x12\x1e\n\x1a\x46ILE_TYPE_NOT_LINK_PREVIEW\x10\x08\x42\x07\n\x05_typeB\x0c\n\n_file_typeB\x10\n\x0e_discussion_idB\r\n\x0b_message_idB\x12\n\x10_filename_searchB\x13\n\x11_mime_type_searchB\x0b\n\t_min_sizeB\x0b\n\t_max_sizeB\xc8\x01\n\x1d\x63om.olvid.daemon.datatypes.v1B\x0f\x41ttachmentProtoP\x01Z\x0folvid.io/daemon\xa2\x02\x03ODD\xaa\x02\x19Olvid.Daemon.Datatypes.V1\xca\x02\x19Olvid\\Daemon\\Datatypes\\V1\xe2\x02%Olvid\\Daemon\\Datatypes\\V1\\GPBMetadata\xea\x02\x1cOlvid::Daemon::Datatypes::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'olvid.daemon.datatypes.v1.attachment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.olvid.daemon.datatypes.v1B\017AttachmentProtoP\001Z\017olvid.io/daemon\242\002\003ODD\252\002\031Olvid.Daemon.Datatypes.V1\312\002\031Olvid\\Daemon\\Datatypes\\V1\342\002%Olvid\\Daemon\\Datatypes\\V1\\GPBMetadata\352\002\034Olvid::Daemon::Datatypes::V1'
  _globals['_ATTACHMENTID']._serialized_start=115
  _globals['_ATTACHMENTID']._serialized_end=278
  _globals['_ATTACHMENTID_TYPE']._serialized_start=213
  _globals['_ATTACHMENTID_TYPE']._serialized_end=278
  _globals['_ATTACHMENT']._serialized_start=281
  _globals['_ATTACHMENT']._serialized_end=534
  _globals['_ATTACHMENTFILTER']._serialized_start=537
  _globals['_ATTACHMENTFILTER']._serialized_end=1300
  _globals['_ATTACHMENTFILTER_FILETYPE']._serialized_start=990
  _globals['_ATTACHMENTFILTER_FILETYPE']._serialized_end=1177
# @@protoc_insertion_point(module_scope)
