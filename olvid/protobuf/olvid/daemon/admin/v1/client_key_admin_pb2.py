# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: olvid/daemon/admin/v1/client_key_admin.proto
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
    'olvid/daemon/admin/v1/client_key_admin.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .....olvid.daemon.datatypes.v1 import client_key_pb2 as olvid_dot_daemon_dot_datatypes_dot_v1_dot_client__key__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,olvid/daemon/admin/v1/client_key_admin.proto\x12\x15olvid.daemon.admin.v1\x1a*olvid/daemon/datatypes/v1/client_key.proto\"j\n\x14\x43lientKeyListRequest\x12G\n\x06\x66ilter\x18\x01 \x01(\x0b\x32*.olvid.daemon.datatypes.v1.ClientKeyFilterH\x00R\x06\x66ilter\x88\x01\x01\x42\t\n\x07_filter\"^\n\x15\x43lientKeyListResponse\x12\x45\n\x0b\x63lient_keys\x18\x01 \x03(\x0b\x32$.olvid.daemon.datatypes.v1.ClientKeyR\nclientKeys\"4\n\x13\x43lientKeyGetRequest\x12\x1d\n\nclient_key\x18\x01 \x01(\tR\tclientKey\"[\n\x14\x43lientKeyGetResponse\x12\x43\n\nclient_key\x18\x01 \x01(\x0b\x32$.olvid.daemon.datatypes.v1.ClientKeyR\tclientKey\"J\n\x13\x43lientKeyNewRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bidentity_id\x18\x02 \x01(\x04R\nidentityId\"[\n\x14\x43lientKeyNewResponse\x12\x43\n\nclient_key\x18\x01 \x01(\x0b\x32$.olvid.daemon.datatypes.v1.ClientKeyR\tclientKey\"7\n\x16\x43lientKeyDeleteRequest\x12\x1d\n\nclient_key\x18\x01 \x01(\tR\tclientKey\"\x19\n\x17\x43lientKeyDeleteResponseB\xb8\x01\n\x19\x63om.olvid.daemon.admin.v1B\x13\x43lientKeyAdminProtoP\x01Z\x0folvid.io/daemon\xa2\x02\x03ODA\xaa\x02\x15Olvid.Daemon.Admin.V1\xca\x02\x15Olvid\\Daemon\\Admin\\V1\xe2\x02!Olvid\\Daemon\\Admin\\V1\\GPBMetadata\xea\x02\x18Olvid::Daemon::Admin::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'olvid.daemon.admin.v1.client_key_admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.olvid.daemon.admin.v1B\023ClientKeyAdminProtoP\001Z\017olvid.io/daemon\242\002\003ODA\252\002\025Olvid.Daemon.Admin.V1\312\002\025Olvid\\Daemon\\Admin\\V1\342\002!Olvid\\Daemon\\Admin\\V1\\GPBMetadata\352\002\030Olvid::Daemon::Admin::V1'
  _globals['_CLIENTKEYLISTREQUEST']._serialized_start=115
  _globals['_CLIENTKEYLISTREQUEST']._serialized_end=221
  _globals['_CLIENTKEYLISTRESPONSE']._serialized_start=223
  _globals['_CLIENTKEYLISTRESPONSE']._serialized_end=317
  _globals['_CLIENTKEYGETREQUEST']._serialized_start=319
  _globals['_CLIENTKEYGETREQUEST']._serialized_end=371
  _globals['_CLIENTKEYGETRESPONSE']._serialized_start=373
  _globals['_CLIENTKEYGETRESPONSE']._serialized_end=464
  _globals['_CLIENTKEYNEWREQUEST']._serialized_start=466
  _globals['_CLIENTKEYNEWREQUEST']._serialized_end=540
  _globals['_CLIENTKEYNEWRESPONSE']._serialized_start=542
  _globals['_CLIENTKEYNEWRESPONSE']._serialized_end=633
  _globals['_CLIENTKEYDELETEREQUEST']._serialized_start=635
  _globals['_CLIENTKEYDELETEREQUEST']._serialized_end=690
  _globals['_CLIENTKEYDELETERESPONSE']._serialized_start=692
  _globals['_CLIENTKEYDELETERESPONSE']._serialized_end=717
# @@protoc_insertion_point(module_scope)
