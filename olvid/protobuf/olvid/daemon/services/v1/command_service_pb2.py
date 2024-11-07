# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: olvid/daemon/services/v1/command_service.proto
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
    'olvid/daemon/services/v1/command_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .....olvid.daemon.command.v1 import attachment_commands_pb2 as olvid_dot_daemon_dot_command_dot_v1_dot_attachment__commands__pb2
from .....olvid.daemon.command.v1 import contact_commands_pb2 as olvid_dot_daemon_dot_command_dot_v1_dot_contact__commands__pb2
from .....olvid.daemon.command.v1 import discussion_commands_pb2 as olvid_dot_daemon_dot_command_dot_v1_dot_discussion__commands__pb2
from .....olvid.daemon.command.v1 import group_commands_pb2 as olvid_dot_daemon_dot_command_dot_v1_dot_group__commands__pb2
from .....olvid.daemon.command.v1 import identity_commands_pb2 as olvid_dot_daemon_dot_command_dot_v1_dot_identity__commands__pb2
from .....olvid.daemon.command.v1 import invitation_commands_pb2 as olvid_dot_daemon_dot_command_dot_v1_dot_invitation__commands__pb2
from .....olvid.daemon.command.v1 import message_commands_pb2 as olvid_dot_daemon_dot_command_dot_v1_dot_message__commands__pb2
from .....olvid.daemon.command.v1 import storage_commands_pb2 as olvid_dot_daemon_dot_command_dot_v1_dot_storage__commands__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.olvid/daemon/services/v1/command_service.proto\x12\x18olvid.daemon.services.v1\x1a\x31olvid/daemon/command/v1/attachment_commands.proto\x1a.olvid/daemon/command/v1/contact_commands.proto\x1a\x31olvid/daemon/command/v1/discussion_commands.proto\x1a,olvid/daemon/command/v1/group_commands.proto\x1a/olvid/daemon/command/v1/identity_commands.proto\x1a\x31olvid/daemon/command/v1/invitation_commands.proto\x1a.olvid/daemon/command/v1/message_commands.proto\x1a.olvid/daemon/command/v1/storage_commands.proto2\xc5\x08\n\x16IdentityCommandService\x12j\n\x0bIdentityGet\x12+.olvid.daemon.command.v1.IdentityGetRequest\x1a,.olvid.daemon.command.v1.IdentityGetResponse\"\x00\x12\x88\x01\n\x15IdentityUpdateDetails\x12\x35.olvid.daemon.command.v1.IdentityUpdateDetailsRequest\x1a\x36.olvid.daemon.command.v1.IdentityUpdateDetailsResponse\"\x00\x12\x82\x01\n\x13IdentityRemovePhoto\x12\x33.olvid.daemon.command.v1.IdentityRemovePhotoRequest\x1a\x34.olvid.daemon.command.v1.IdentityRemovePhotoResponse\"\x00\x12{\n\x10IdentitySetPhoto\x12\x30.olvid.daemon.command.v1.IdentitySetPhotoRequest\x1a\x31.olvid.daemon.command.v1.IdentitySetPhotoResponse\"\x00(\x01\x12\x85\x01\n\x14IdentityKeycloakBind\x12\x34.olvid.daemon.command.v1.IdentityKeycloakBindRequest\x1a\x35.olvid.daemon.command.v1.IdentityKeycloakBindResponse\"\x00\x12\x8b\x01\n\x16IdentityKeycloakUnbind\x12\x36.olvid.daemon.command.v1.IdentityKeycloakUnbindRequest\x1a\x37.olvid.daemon.command.v1.IdentityKeycloakUnbindResponse\"\x00\x12|\n\x11IdentitySetApiKey\x12\x31.olvid.daemon.command.v1.IdentitySetApiKeyRequest\x1a\x32.olvid.daemon.command.v1.IdentitySetApiKeyResponse\"\x00\x12\x9d\x01\n\x1cIdentitySetConfigurationLink\x12<.olvid.daemon.command.v1.IdentitySetConfigurationLinkRequest\x1a=.olvid.daemon.command.v1.IdentitySetConfigurationLinkResponse\"\x00\x32\xdb\x06\n\x18InvitationCommandService\x12u\n\x0eInvitationList\x12..olvid.daemon.command.v1.InvitationListRequest\x1a/.olvid.daemon.command.v1.InvitationListResponse\"\x00\x30\x01\x12p\n\rInvitationGet\x12-.olvid.daemon.command.v1.InvitationGetRequest\x1a..olvid.daemon.command.v1.InvitationGetResponse\"\x00\x12p\n\rInvitationNew\x12-.olvid.daemon.command.v1.InvitationNewRequest\x1a..olvid.daemon.command.v1.InvitationNewResponse\"\x00\x12y\n\x10InvitationAccept\x12\x30.olvid.daemon.command.v1.InvitationAcceptRequest\x1a\x31.olvid.daemon.command.v1.InvitationAcceptResponse\"\x00\x12|\n\x11InvitationDecline\x12\x31.olvid.daemon.command.v1.InvitationDeclineRequest\x1a\x32.olvid.daemon.command.v1.InvitationDeclineResponse\"\x00\x12p\n\rInvitationSas\x12-.olvid.daemon.command.v1.InvitationSasRequest\x1a..olvid.daemon.command.v1.InvitationSasResponse\"\x00\x12y\n\x10InvitationDelete\x12\x30.olvid.daemon.command.v1.InvitationDeleteRequest\x1a\x31.olvid.daemon.command.v1.InvitationDeleteResponse\"\x00\x32\xc6\x06\n\x15\x43ontactCommandService\x12l\n\x0b\x43ontactList\x12+.olvid.daemon.command.v1.ContactListRequest\x1a,.olvid.daemon.command.v1.ContactListResponse\"\x00\x30\x01\x12g\n\nContactGet\x12*.olvid.daemon.command.v1.ContactGetRequest\x1a+.olvid.daemon.command.v1.ContactGetResponse\"\x00\x12p\n\rContactDelete\x12-.olvid.daemon.command.v1.ContactDeleteRequest\x1a..olvid.daemon.command.v1.ContactDeleteResponse\"\x00\x12\x82\x01\n\x13\x43ontactIntroduction\x12\x33.olvid.daemon.command.v1.ContactIntroductionRequest\x1a\x34.olvid.daemon.command.v1.ContactIntroductionResponse\"\x00\x12\xac\x01\n!ContactInviteToOneToOneDiscussion\x12\x41.olvid.daemon.command.v1.ContactInviteToOneToOneDiscussionRequest\x1a\x42.olvid.daemon.command.v1.ContactInviteToOneToOneDiscussionResponse\"\x00\x12\xaf\x01\n\"ContactDowngradeOneToOneDiscussion\x12\x42.olvid.daemon.command.v1.ContactDowngradeOneToOneDiscussionRequest\x1a\x43.olvid.daemon.command.v1.ContactDowngradeOneToOneDiscussionResponse\"\x00\x32\xc2\n\n\x13GroupCommandService\x12\x66\n\tGroupList\x12).olvid.daemon.command.v1.GroupListRequest\x1a*.olvid.daemon.command.v1.GroupListResponse\"\x00\x30\x01\x12\x61\n\x08GroupGet\x12(.olvid.daemon.command.v1.GroupGetRequest\x1a).olvid.daemon.command.v1.GroupGetResponse\"\x00\x12\x88\x01\n\x15GroupNewStandardGroup\x12\x35.olvid.daemon.command.v1.GroupNewStandardGroupRequest\x1a\x36.olvid.daemon.command.v1.GroupNewStandardGroupResponse\"\x00\x12\x8e\x01\n\x17GroupNewControlledGroup\x12\x37.olvid.daemon.command.v1.GroupNewControlledGroupRequest\x1a\x38.olvid.daemon.command.v1.GroupNewControlledGroupResponse\"\x00\x12\x88\x01\n\x15GroupNewReadOnlyGroup\x12\x35.olvid.daemon.command.v1.GroupNewReadOnlyGroupRequest\x1a\x36.olvid.daemon.command.v1.GroupNewReadOnlyGroupResponse\"\x00\x12\x88\x01\n\x15GroupNewAdvancedGroup\x12\x35.olvid.daemon.command.v1.GroupNewAdvancedGroupRequest\x1a\x36.olvid.daemon.command.v1.GroupNewAdvancedGroupResponse\"\x00\x12m\n\x0cGroupDisband\x12,.olvid.daemon.command.v1.GroupDisbandRequest\x1a-.olvid.daemon.command.v1.GroupDisbandResponse\"\x00\x12g\n\nGroupLeave\x12*.olvid.daemon.command.v1.GroupLeaveRequest\x1a+.olvid.daemon.command.v1.GroupLeaveResponse\"\x00\x12j\n\x0bGroupUpdate\x12+.olvid.daemon.command.v1.GroupUpdateRequest\x1a,.olvid.daemon.command.v1.GroupUpdateResponse\"\x00\x12v\n\x0fGroupUnsetPhoto\x12/.olvid.daemon.command.v1.GroupUnsetPhotoRequest\x1a\x30.olvid.daemon.command.v1.GroupUnsetPhotoResponse\"\x00\x12r\n\rGroupSetPhoto\x12-.olvid.daemon.command.v1.GroupSetPhotoRequest\x1a..olvid.daemon.command.v1.GroupSetPhotoResponse\"\x00(\x01\x32\xbf\t\n\x18\x44iscussionCommandService\x12u\n\x0e\x44iscussionList\x12..olvid.daemon.command.v1.DiscussionListRequest\x1a/.olvid.daemon.command.v1.DiscussionListResponse\"\x00\x30\x01\x12p\n\rDiscussionGet\x12-.olvid.daemon.command.v1.DiscussionGetRequest\x1a..olvid.daemon.command.v1.DiscussionGetResponse\"\x00\x12\x8b\x01\n\x16\x44iscussionGetByContact\x12\x36.olvid.daemon.command.v1.DiscussionGetByContactRequest\x1a\x37.olvid.daemon.command.v1.DiscussionGetByContactResponse\"\x00\x12\x85\x01\n\x14\x44iscussionGetByGroup\x12\x34.olvid.daemon.command.v1.DiscussionGetByGroupRequest\x1a\x35.olvid.daemon.command.v1.DiscussionGetByGroupResponse\"\x00\x12v\n\x0f\x44iscussionEmpty\x12/.olvid.daemon.command.v1.DiscussionEmptyRequest\x1a\x30.olvid.daemon.command.v1.DiscussionEmptyResponse\"\x00\x12\x88\x01\n\x15\x44iscussionSettingsGet\x12\x35.olvid.daemon.command.v1.DiscussionSettingsGetRequest\x1a\x36.olvid.daemon.command.v1.DiscussionSettingsGetResponse\"\x00\x12\x88\x01\n\x15\x44iscussionSettingsSet\x12\x35.olvid.daemon.command.v1.DiscussionSettingsSetRequest\x1a\x36.olvid.daemon.command.v1.DiscussionSettingsSetResponse\"\x00\x12\x87\x01\n\x14\x44iscussionLockedList\x12\x34.olvid.daemon.command.v1.DiscussionLockedListRequest\x1a\x35.olvid.daemon.command.v1.DiscussionLockedListResponse\"\x00\x30\x01\x12\x8b\x01\n\x16\x44iscussionLockedDelete\x12\x36.olvid.daemon.command.v1.DiscussionLockedDeleteRequest\x1a\x37.olvid.daemon.command.v1.DiscussionLockedDeleteResponse\"\x00\x32\xc7\t\n\x15MessageCommandService\x12l\n\x0bMessageList\x12+.olvid.daemon.command.v1.MessageListRequest\x1a,.olvid.daemon.command.v1.MessageListResponse\"\x00\x30\x01\x12g\n\nMessageGet\x12*.olvid.daemon.command.v1.MessageGetRequest\x1a+.olvid.daemon.command.v1.MessageGetResponse\"\x00\x12s\n\x0eMessageRefresh\x12..olvid.daemon.command.v1.MessageRefreshRequest\x1a/.olvid.daemon.command.v1.MessageRefreshResponse\"\x00\x12p\n\rMessageDelete\x12-.olvid.daemon.command.v1.MessageDeleteRequest\x1a..olvid.daemon.command.v1.MessageDeleteResponse\"\x00\x12j\n\x0bMessageSend\x12+.olvid.daemon.command.v1.MessageSendRequest\x1a,.olvid.daemon.command.v1.MessageSendResponse\"\x00\x12\x99\x01\n\x1aMessageSendWithAttachments\x12:.olvid.daemon.command.v1.MessageSendWithAttachmentsRequest\x1a;.olvid.daemon.command.v1.MessageSendWithAttachmentsResponse\"\x00(\x01\x12\x82\x01\n\x13MessageSendLocation\x12\x33.olvid.daemon.command.v1.MessageSendLocationRequest\x1a\x34.olvid.daemon.command.v1.MessageSendLocationResponse\"\x00\x12m\n\x0cMessageReact\x12,.olvid.daemon.command.v1.MessageReactRequest\x1a-.olvid.daemon.command.v1.MessageReactResponse\"\x00\x12|\n\x11MessageUpdateBody\x12\x31.olvid.daemon.command.v1.MessageUpdateBodyRequest\x1a\x32.olvid.daemon.command.v1.MessageUpdateBodyResponse\"\x00\x12v\n\x0fMessageSendVoip\x12/.olvid.daemon.command.v1.MessageSendVoipRequest\x1a\x30.olvid.daemon.command.v1.MessageSendVoipResponse\"\x00\x32\x82\x04\n\x18\x41ttachmentCommandService\x12u\n\x0e\x41ttachmentList\x12..olvid.daemon.command.v1.AttachmentListRequest\x1a/.olvid.daemon.command.v1.AttachmentListResponse\"\x00\x30\x01\x12p\n\rAttachmentGet\x12-.olvid.daemon.command.v1.AttachmentGetRequest\x1a..olvid.daemon.command.v1.AttachmentGetResponse\"\x00\x12y\n\x10\x41ttachmentDelete\x12\x30.olvid.daemon.command.v1.AttachmentDeleteRequest\x1a\x31.olvid.daemon.command.v1.AttachmentDeleteResponse\"\x00\x12\x81\x01\n\x12\x41ttachmentDownload\x12\x32.olvid.daemon.command.v1.AttachmentDownloadRequest\x1a\x33.olvid.daemon.command.v1.AttachmentDownloadResponse\"\x00\x30\x01\x32\xc6\x03\n\x15StorageCommandService\x12l\n\x0bStorageList\x12+.olvid.daemon.command.v1.StorageListRequest\x1a,.olvid.daemon.command.v1.StorageListResponse\"\x00\x30\x01\x12g\n\nStorageGet\x12*.olvid.daemon.command.v1.StorageGetRequest\x1a+.olvid.daemon.command.v1.StorageGetResponse\"\x00\x12g\n\nStorageSet\x12*.olvid.daemon.command.v1.StorageSetRequest\x1a+.olvid.daemon.command.v1.StorageSetResponse\"\x00\x12m\n\x0cStorageUnset\x12,.olvid.daemon.command.v1.StorageUnsetRequest\x1a-.olvid.daemon.command.v1.StorageUnsetResponse\"\x00\x32\xcc\x04\n\x1f\x44iscussionStorageCommandService\x12\x8a\x01\n\x15\x44iscussionStorageList\x12\x35.olvid.daemon.command.v1.DiscussionStorageListRequest\x1a\x36.olvid.daemon.command.v1.DiscussionStorageListResponse\"\x00\x30\x01\x12\x85\x01\n\x14\x44iscussionStorageGet\x12\x34.olvid.daemon.command.v1.DiscussionStorageGetRequest\x1a\x35.olvid.daemon.command.v1.DiscussionStorageGetResponse\"\x00\x12\x85\x01\n\x14\x44iscussionStorageSet\x12\x34.olvid.daemon.command.v1.DiscussionStorageSetRequest\x1a\x35.olvid.daemon.command.v1.DiscussionStorageSetResponse\"\x00\x12\x8b\x01\n\x16\x44iscussionStorageUnset\x12\x36.olvid.daemon.command.v1.DiscussionStorageUnsetRequest\x1a\x37.olvid.daemon.command.v1.DiscussionStorageUnsetResponse\"\x00\x42\xc7\x01\n\x1c\x63om.olvid.daemon.services.v1B\x13\x43ommandServiceProtoP\x01Z\x0folvid.io/daemon\xa2\x02\x03ODS\xaa\x02\x18Olvid.Daemon.Services.V1\xca\x02\x18Olvid\\Daemon\\Services\\V1\xe2\x02$Olvid\\Daemon\\Services\\V1\\GPBMetadata\xea\x02\x1bOlvid::Daemon::Services::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'olvid.daemon.services.v1.command_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.olvid.daemon.services.v1B\023CommandServiceProtoP\001Z\017olvid.io/daemon\242\002\003ODS\252\002\030Olvid.Daemon.Services.V1\312\002\030Olvid\\Daemon\\Services\\V1\342\002$Olvid\\Daemon\\Services\\V1\\GPBMetadata\352\002\033Olvid::Daemon::Services::V1'
  _globals['_IDENTITYCOMMANDSERVICE']._serialized_start=469
  _globals['_IDENTITYCOMMANDSERVICE']._serialized_end=1562
  _globals['_INVITATIONCOMMANDSERVICE']._serialized_start=1565
  _globals['_INVITATIONCOMMANDSERVICE']._serialized_end=2424
  _globals['_CONTACTCOMMANDSERVICE']._serialized_start=2427
  _globals['_CONTACTCOMMANDSERVICE']._serialized_end=3265
  _globals['_GROUPCOMMANDSERVICE']._serialized_start=3268
  _globals['_GROUPCOMMANDSERVICE']._serialized_end=4614
  _globals['_DISCUSSIONCOMMANDSERVICE']._serialized_start=4617
  _globals['_DISCUSSIONCOMMANDSERVICE']._serialized_end=5832
  _globals['_MESSAGECOMMANDSERVICE']._serialized_start=5835
  _globals['_MESSAGECOMMANDSERVICE']._serialized_end=7058
  _globals['_ATTACHMENTCOMMANDSERVICE']._serialized_start=7061
  _globals['_ATTACHMENTCOMMANDSERVICE']._serialized_end=7575
  _globals['_STORAGECOMMANDSERVICE']._serialized_start=7578
  _globals['_STORAGECOMMANDSERVICE']._serialized_end=8032
  _globals['_DISCUSSIONSTORAGECOMMANDSERVICE']._serialized_start=8035
  _globals['_DISCUSSIONSTORAGECOMMANDSERVICE']._serialized_end=8623
# @@protoc_insertion_point(module_scope)
