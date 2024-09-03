# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: olvid/daemon/datatypes/v1/identity.proto
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
    'olvid/daemon/datatypes/v1/identity.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(olvid/daemon/datatypes/v1/identity.proto\x12\x19olvid.daemon.datatypes.v1\"\xcd\x01\n\x0fIdentityDetails\x12\"\n\nfirst_name\x18\x01 \x01(\tH\x00R\tfirstName\x88\x01\x01\x12 \n\tlast_name\x18\x02 \x01(\tH\x01R\x08lastName\x88\x01\x01\x12\x1d\n\x07\x63ompany\x18\x03 \x01(\tH\x02R\x07\x63ompany\x88\x01\x01\x12\x1f\n\x08position\x18\x04 \x01(\tH\x03R\x08position\x88\x01\x01\x42\r\n\x0b_first_nameB\x0c\n\n_last_nameB\n\n\x08_companyB\x0b\n\t_position\"\x94\x04\n\x08Identity\x12\x0e\n\x02id\x18\x01 \x01(\x04R\x02id\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12\x44\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32*.olvid.daemon.datatypes.v1.IdentityDetailsR\x07\x64\x65tails\x12%\n\x0einvitation_url\x18\x04 \x01(\tR\rinvitationUrl\x12)\n\x10keycloak_managed\x18\x05 \x01(\x08R\x0fkeycloakManaged\x12\x1e\n\x0bhas_a_photo\x18\x06 \x01(\x08R\thasAPhoto\x12\x43\n\x07\x61pi_key\x18\x07 \x01(\x0b\x32*.olvid.daemon.datatypes.v1.Identity.ApiKeyR\x06\x61piKey\x1a\xd7\x01\n\x06\x41piKey\x12U\n\npermission\x18\x01 \x01(\x0b\x32\x35.olvid.daemon.datatypes.v1.Identity.ApiKey.PermissionR\npermission\x12\x31\n\x14\x65xpiration_timestamp\x18\x02 \x01(\x04R\x13\x65xpirationTimestamp\x1a\x43\n\nPermission\x12\x12\n\x04\x63\x61ll\x18\x01 \x01(\x08R\x04\x63\x61ll\x12!\n\x0cmulti_device\x18\x02 \x01(\x08R\x0bmultiDevice\"\xb3\x05\n\x0eIdentityFilter\x12S\n\x08keycloak\x18\x01 \x01(\x0e\x32\x32.olvid.daemon.datatypes.v1.IdentityFilter.KeycloakH\x00R\x08keycloak\x88\x01\x01\x12J\n\x05photo\x18\x02 \x01(\x0e\x32/.olvid.daemon.datatypes.v1.IdentityFilter.PhotoH\x01R\x05photo\x88\x01\x01\x12N\n\x07\x61pi_key\x18\x03 \x01(\x0e\x32\x30.olvid.daemon.datatypes.v1.IdentityFilter.ApiKeyH\x02R\x06\x61piKey\x88\x01\x01\x12\x33\n\x13\x64isplay_name_search\x18\x04 \x01(\tH\x03R\x11\x64isplayNameSearch\x88\x01\x01\x12V\n\x0e\x64\x65tails_search\x18\x05 \x01(\x0b\x32*.olvid.daemon.datatypes.v1.IdentityDetailsH\x04R\rdetailsSearch\x88\x01\x01\"J\n\x08Keycloak\x12\x18\n\x14KEYCLOAK_UNSPECIFIED\x10\x00\x12\x0f\n\x0bKEYCLOAK_IS\x10\x02\x12\x13\n\x0fKEYCLOAK_IS_NOT\x10\x01\"@\n\x05Photo\x12\x15\n\x11PHOTO_UNSPECIFIED\x10\x00\x12\r\n\tPHOTO_HAS\x10\x02\x12\x11\n\rPHOTO_HAS_NOT\x10\x01\"G\n\x06\x41piKey\x12\x17\n\x13\x41PI_KEY_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x41PI_KEY_HAS\x10\x02\x12\x13\n\x0f\x41PI_KEY_HAS_NOT\x10\x01\x42\x0b\n\t_keycloakB\x08\n\x06_photoB\n\n\x08_api_keyB\x16\n\x14_display_name_searchB\x11\n\x0f_details_searchB\xc6\x01\n\x1d\x63om.olvid.daemon.datatypes.v1B\rIdentityProtoP\x01Z\x0folvid.io/daemon\xa2\x02\x03ODD\xaa\x02\x19Olvid.Daemon.Datatypes.V1\xca\x02\x19Olvid\\Daemon\\Datatypes\\V1\xe2\x02%Olvid\\Daemon\\Datatypes\\V1\\GPBMetadata\xea\x02\x1cOlvid::Daemon::Datatypes::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'olvid.daemon.datatypes.v1.identity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.olvid.daemon.datatypes.v1B\rIdentityProtoP\001Z\017olvid.io/daemon\242\002\003ODD\252\002\031Olvid.Daemon.Datatypes.V1\312\002\031Olvid\\Daemon\\Datatypes\\V1\342\002%Olvid\\Daemon\\Datatypes\\V1\\GPBMetadata\352\002\034Olvid::Daemon::Datatypes::V1'
  _globals['_IDENTITYDETAILS']._serialized_start=72
  _globals['_IDENTITYDETAILS']._serialized_end=277
  _globals['_IDENTITY']._serialized_start=280
  _globals['_IDENTITY']._serialized_end=812
  _globals['_IDENTITY_APIKEY']._serialized_start=597
  _globals['_IDENTITY_APIKEY']._serialized_end=812
  _globals['_IDENTITY_APIKEY_PERMISSION']._serialized_start=745
  _globals['_IDENTITY_APIKEY_PERMISSION']._serialized_end=812
  _globals['_IDENTITYFILTER']._serialized_start=815
  _globals['_IDENTITYFILTER']._serialized_end=1506
  _globals['_IDENTITYFILTER_KEYCLOAK']._serialized_start=1215
  _globals['_IDENTITYFILTER_KEYCLOAK']._serialized_end=1289
  _globals['_IDENTITYFILTER_PHOTO']._serialized_start=1291
  _globals['_IDENTITYFILTER_PHOTO']._serialized_end=1355
  _globals['_IDENTITYFILTER_APIKEY']._serialized_start=1357
  _globals['_IDENTITYFILTER_APIKEY']._serialized_end=1428
# @@protoc_insertion_point(module_scope)
