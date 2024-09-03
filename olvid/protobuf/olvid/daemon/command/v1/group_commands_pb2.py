# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: olvid/daemon/command/v1/group_commands.proto
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
    'olvid/daemon/command/v1/group_commands.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .....olvid.daemon.datatypes.v1 import group_pb2 as olvid_dot_daemon_dot_datatypes_dot_v1_dot_group__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,olvid/daemon/command/v1/group_commands.proto\x12\x17olvid.daemon.command.v1\x1a%olvid/daemon/datatypes/v1/group.proto\"b\n\x10GroupListRequest\x12\x43\n\x06\x66ilter\x18\x01 \x01(\x0b\x32&.olvid.daemon.datatypes.v1.GroupFilterH\x00R\x06\x66ilter\x88\x01\x01\x42\t\n\x07_filter\"M\n\x11GroupListResponse\x12\x38\n\x06groups\x18\x01 \x03(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x06groups\",\n\x0fGroupGetRequest\x12\x19\n\x08group_id\x18\x01 \x01(\x04R\x07groupId\"J\n\x10GroupGetResponse\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05group\"\xa3\x01\n\x1cGroupNewStandardGroupRequest\x12\x17\n\x04name\x18\x01 \x01(\tH\x00R\x04name\x88\x01\x01\x12%\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x01R\x0b\x64\x65scription\x88\x01\x01\x12*\n\x11\x61\x64min_contact_ids\x18\x03 \x03(\x04R\x0f\x61\x64minContactIdsB\x07\n\x05_nameB\x0e\n\x0c_description\"W\n\x1dGroupNewStandardGroupResponse\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05group\"\xc6\x01\n\x1eGroupNewControlledGroupRequest\x12\x17\n\x04name\x18\x01 \x01(\tH\x00R\x04name\x88\x01\x01\x12%\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x01R\x0b\x64\x65scription\x88\x01\x01\x12*\n\x11\x61\x64min_contact_ids\x18\x03 \x03(\x04R\x0f\x61\x64minContactIds\x12\x1f\n\x0b\x63ontact_ids\x18\x04 \x03(\x04R\ncontactIdsB\x07\n\x05_nameB\x0e\n\x0c_description\"Y\n\x1fGroupNewControlledGroupResponse\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05group\"\xc4\x01\n\x1cGroupNewReadOnlyGroupRequest\x12\x17\n\x04name\x18\x01 \x01(\tH\x00R\x04name\x88\x01\x01\x12%\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x01R\x0b\x64\x65scription\x88\x01\x01\x12*\n\x11\x61\x64min_contact_ids\x18\x03 \x03(\x04R\x0f\x61\x64minContactIds\x12\x1f\n\x0b\x63ontact_ids\x18\x04 \x03(\x04R\ncontactIdsB\x07\n\x05_nameB\x0e\n\x0c_description\"W\n\x1dGroupNewReadOnlyGroupResponse\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05group\"\xc8\x02\n\x1cGroupNewAdvancedGroupRequest\x12\x17\n\x04name\x18\x01 \x01(\tH\x00R\x04name\x88\x01\x01\x12%\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x01R\x0b\x64\x65scription\x88\x01\x01\x12r\n\x16\x61\x64vanced_configuration\x18\x03 \x01(\x0b\x32\x36.olvid.daemon.datatypes.v1.Group.AdvancedConfigurationH\x02R\x15\x61\x64vancedConfiguration\x88\x01\x01\x12@\n\x07members\x18\x04 \x03(\x0b\x32&.olvid.daemon.datatypes.v1.GroupMemberR\x07membersB\x07\n\x05_nameB\x0e\n\x0c_descriptionB\x19\n\x17_advanced_configuration\"W\n\x1dGroupNewAdvancedGroupResponse\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05group\"0\n\x13GroupDisbandRequest\x12\x19\n\x08group_id\x18\x01 \x01(\x04R\x07groupId\"N\n\x14GroupDisbandResponse\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05group\".\n\x11GroupLeaveRequest\x12\x19\n\x08group_id\x18\x01 \x01(\x04R\x07groupId\"L\n\x12GroupLeaveResponse\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05group\"L\n\x12GroupUpdateRequest\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05group\"M\n\x13GroupUpdateResponse\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05group\"3\n\x16GroupUnsetPhotoRequest\x12\x19\n\x08group_id\x18\x01 \x01(\x04R\x07groupId\"Q\n\x17GroupUnsetPhotoResponse\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05group\"r\n\x1cGroupSetPhotoRequestMetadata\x12\x19\n\x08group_id\x18\x01 \x01(\x04R\x07groupId\x12\x1a\n\x08\x66ilename\x18\x02 \x01(\tR\x08\x66ilename\x12\x1b\n\tfile_size\x18\x03 \x01(\x04R\x08\x66ileSize\"\x92\x01\n\x14GroupSetPhotoRequest\x12S\n\x08metadata\x18\x01 \x01(\x0b\x32\x35.olvid.daemon.command.v1.GroupSetPhotoRequestMetadataH\x00R\x08metadata\x12\x1a\n\x07payload\x18\x02 \x01(\x0cH\x00R\x07payloadB\t\n\x07request\"O\n\x15GroupSetPhotoResponse\x12\x36\n\x05group\x18\x01 \x01(\x0b\x32 .olvid.daemon.datatypes.v1.GroupR\x05groupB\xc1\x01\n\x1b\x63om.olvid.daemon.command.v1B\x12GroupCommandsProtoP\x01Z\x0folvid.io/daemon\xa2\x02\x03ODC\xaa\x02\x17Olvid.Daemon.Command.V1\xca\x02\x17Olvid\\Daemon\\Command\\V1\xe2\x02#Olvid\\Daemon\\Command\\V1\\GPBMetadata\xea\x02\x1aOlvid::Daemon::Command::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'olvid.daemon.command.v1.group_commands_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.olvid.daemon.command.v1B\022GroupCommandsProtoP\001Z\017olvid.io/daemon\242\002\003ODC\252\002\027Olvid.Daemon.Command.V1\312\002\027Olvid\\Daemon\\Command\\V1\342\002#Olvid\\Daemon\\Command\\V1\\GPBMetadata\352\002\032Olvid::Daemon::Command::V1'
  _globals['_GROUPLISTREQUEST']._serialized_start=112
  _globals['_GROUPLISTREQUEST']._serialized_end=210
  _globals['_GROUPLISTRESPONSE']._serialized_start=212
  _globals['_GROUPLISTRESPONSE']._serialized_end=289
  _globals['_GROUPGETREQUEST']._serialized_start=291
  _globals['_GROUPGETREQUEST']._serialized_end=335
  _globals['_GROUPGETRESPONSE']._serialized_start=337
  _globals['_GROUPGETRESPONSE']._serialized_end=411
  _globals['_GROUPNEWSTANDARDGROUPREQUEST']._serialized_start=414
  _globals['_GROUPNEWSTANDARDGROUPREQUEST']._serialized_end=577
  _globals['_GROUPNEWSTANDARDGROUPRESPONSE']._serialized_start=579
  _globals['_GROUPNEWSTANDARDGROUPRESPONSE']._serialized_end=666
  _globals['_GROUPNEWCONTROLLEDGROUPREQUEST']._serialized_start=669
  _globals['_GROUPNEWCONTROLLEDGROUPREQUEST']._serialized_end=867
  _globals['_GROUPNEWCONTROLLEDGROUPRESPONSE']._serialized_start=869
  _globals['_GROUPNEWCONTROLLEDGROUPRESPONSE']._serialized_end=958
  _globals['_GROUPNEWREADONLYGROUPREQUEST']._serialized_start=961
  _globals['_GROUPNEWREADONLYGROUPREQUEST']._serialized_end=1157
  _globals['_GROUPNEWREADONLYGROUPRESPONSE']._serialized_start=1159
  _globals['_GROUPNEWREADONLYGROUPRESPONSE']._serialized_end=1246
  _globals['_GROUPNEWADVANCEDGROUPREQUEST']._serialized_start=1249
  _globals['_GROUPNEWADVANCEDGROUPREQUEST']._serialized_end=1577
  _globals['_GROUPNEWADVANCEDGROUPRESPONSE']._serialized_start=1579
  _globals['_GROUPNEWADVANCEDGROUPRESPONSE']._serialized_end=1666
  _globals['_GROUPDISBANDREQUEST']._serialized_start=1668
  _globals['_GROUPDISBANDREQUEST']._serialized_end=1716
  _globals['_GROUPDISBANDRESPONSE']._serialized_start=1718
  _globals['_GROUPDISBANDRESPONSE']._serialized_end=1796
  _globals['_GROUPLEAVEREQUEST']._serialized_start=1798
  _globals['_GROUPLEAVEREQUEST']._serialized_end=1844
  _globals['_GROUPLEAVERESPONSE']._serialized_start=1846
  _globals['_GROUPLEAVERESPONSE']._serialized_end=1922
  _globals['_GROUPUPDATEREQUEST']._serialized_start=1924
  _globals['_GROUPUPDATEREQUEST']._serialized_end=2000
  _globals['_GROUPUPDATERESPONSE']._serialized_start=2002
  _globals['_GROUPUPDATERESPONSE']._serialized_end=2079
  _globals['_GROUPUNSETPHOTOREQUEST']._serialized_start=2081
  _globals['_GROUPUNSETPHOTOREQUEST']._serialized_end=2132
  _globals['_GROUPUNSETPHOTORESPONSE']._serialized_start=2134
  _globals['_GROUPUNSETPHOTORESPONSE']._serialized_end=2215
  _globals['_GROUPSETPHOTOREQUESTMETADATA']._serialized_start=2217
  _globals['_GROUPSETPHOTOREQUESTMETADATA']._serialized_end=2331
  _globals['_GROUPSETPHOTOREQUEST']._serialized_start=2334
  _globals['_GROUPSETPHOTOREQUEST']._serialized_end=2480
  _globals['_GROUPSETPHOTORESPONSE']._serialized_start=2482
  _globals['_GROUPSETPHOTORESPONSE']._serialized_end=2561
# @@protoc_insertion_point(module_scope)
