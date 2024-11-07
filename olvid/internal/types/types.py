####
# WARNING: DO NOT EDIT: this code is automatically generated, see overlay_generator/generate_protobuf_overlay
####

from ..notifications import *
from ..commands import *
from ..admin import *

from typing import Union


NotificationMessageType = Union[SubscribeToAttachmentReceivedNotification, AttachmentReceivedNotification, SubscribeToAttachmentUploadedNotification, AttachmentUploadedNotification, SubscribeToContactNewNotification, ContactNewNotification, SubscribeToContactDeletedNotification, ContactDeletedNotification, SubscribeToContactDetailsUpdatedNotification, ContactDetailsUpdatedNotification, SubscribeToDiscussionNewNotification, DiscussionNewNotification, SubscribeToDiscussionLockedNotification, DiscussionLockedNotification, SubscribeToDiscussionTitleUpdatedNotification, DiscussionTitleUpdatedNotification, SubscribeToDiscussionSettingsUpdatedNotification, DiscussionSettingsUpdatedNotification, SubscribeToGroupNewNotification, GroupNewNotification, SubscribeToGroupDeletedNotification, GroupDeletedNotification, SubscribeToGroupNameUpdatedNotification, GroupNameUpdatedNotification, SubscribeToGroupDescriptionUpdatedNotification, GroupDescriptionUpdatedNotification, SubscribeToGroupPendingMemberAddedNotification, GroupPendingMemberAddedNotification, SubscribeToGroupPendingMemberRemovedNotification, GroupPendingMemberRemovedNotification, SubscribeToGroupMemberJoinedNotification, GroupMemberJoinedNotification, SubscribeToGroupMemberLeftNotification, GroupMemberLeftNotification, SubscribeToGroupOwnPermissionsUpdatedNotification, GroupOwnPermissionsUpdatedNotification, SubscribeToGroupMemberPermissionsUpdatedNotification, GroupMemberPermissionsUpdatedNotification, SubscribeToGroupUpdateInProgressNotification, GroupUpdateInProgressNotification, SubscribeToGroupUpdateFinishedNotification, GroupUpdateFinishedNotification, SubscribeToIdentityCreatedNotification, IdentityCreatedNotification, SubscribeToIdentityDeletedNotification, IdentityDeletedNotification, SubscribeToIdentityUpdatedNotification, IdentityDetailsUpdatedNotification, SubscribeToInvitationReceivedNotification, InvitationReceivedNotification, SubscribeToInvitationSentNotification, InvitationSentNotification, SubscribeToInvitationDeletedNotification, InvitationDeletedNotification, SubscribeToInvitationUpdatedNotification, InvitationUpdatedNotification, SubscribeToMessageReceivedNotification, MessageReceivedNotification, SubscribeToMessageSentNotification, MessageSentNotification, SubscribeToMessageDeletedNotification, MessageDeletedNotification, SubscribeToMessageBodyUpdatedNotification, MessageBodyUpdatedNotification, SubscribeToMessageUploadedNotification, MessageUploadedNotification, SubscribeToMessageDeliveredNotification, MessageDeliveredNotification, SubscribeToMessageReadNotification, MessageReadNotification, SubscribeToMessageLocationReceivedNotification, MessageLocationReceivedNotification, SubscribeToMessageLocationSharingStartNotification, MessageLocationSharingStartNotification, SubscribeToMessageLocationSharingUpdateNotification, MessageLocationSharingUpdateNotification, SubscribeToMessageLocationSharingEndNotification, MessageLocationSharingEndNotification, SubscribeToMessageReactionAddedNotification, MessageReactionAddedNotification, SubscribeToMessageReactionUpdatedNotification, MessageReactionUpdatedNotification, SubscribeToMessageReactionRemovedNotification, MessageReactionRemovedNotification]
CommandRequestMessageType = Union[ClientKeyListRequest, ClientKeyGetRequest, ClientKeyNewRequest, ClientKeyDeleteRequest, IdentityListRequest, IdentityAdminGetRequest, IdentityNewRequest, IdentityDeleteRequest, IdentityKeycloakNewRequest, AttachmentListRequest, AttachmentGetRequest, AttachmentDeleteRequest, AttachmentDownloadRequest, ContactListRequest, ContactGetRequest, ContactDeleteRequest, ContactIntroductionRequest, ContactInviteToOneToOneDiscussionRequest, ContactDowngradeOneToOneDiscussionRequest, DiscussionListRequest, DiscussionGetRequest, DiscussionGetByContactRequest, DiscussionGetByGroupRequest, DiscussionEmptyRequest, DiscussionSettingsGetRequest, DiscussionSettingsSetRequest, DiscussionLockedListRequest, DiscussionLockedDeleteRequest, GroupListRequest, GroupGetRequest, GroupNewStandardGroupRequest, GroupNewControlledGroupRequest, GroupNewReadOnlyGroupRequest, GroupNewAdvancedGroupRequest, GroupDisbandRequest, GroupLeaveRequest, GroupUpdateRequest, GroupUnsetPhotoRequest, GroupSetPhotoRequest, IdentityGetRequest, IdentityUpdateDetailsRequest, IdentityRemovePhotoRequest, IdentitySetPhotoRequest, IdentityKeycloakBindRequest, IdentityKeycloakUnbindRequest, IdentitySetApiKeyRequest, IdentitySetConfigurationLinkRequest, InvitationListRequest, InvitationGetRequest, InvitationNewRequest, InvitationAcceptRequest, InvitationDeclineRequest, InvitationSasRequest, InvitationDeleteRequest, MessageListRequest, MessageGetRequest, MessageRefreshRequest, MessageDeleteRequest, MessageSendRequest, MessageSendWithAttachmentsRequest, MessageSendLocationRequest, MessageReactRequest, MessageUpdateBodyRequest, MessageSendVoipRequest, StorageListRequest, StorageGetRequest, StorageSetRequest, StorageUnsetRequest, DiscussionStorageListRequest, DiscussionStorageGetRequest, DiscussionStorageSetRequest, DiscussionStorageUnsetRequest]
CommandResponseMessageType = Union[ClientKeyListResponse, ClientKeyGetResponse, ClientKeyNewResponse, ClientKeyDeleteResponse, IdentityListResponse, IdentityAdminGetResponse, IdentityNewResponse, IdentityDeleteResponse, IdentityKeycloakNewResponse, AttachmentListResponse, AttachmentGetResponse, AttachmentDeleteResponse, AttachmentDownloadResponse, ContactListResponse, ContactGetResponse, ContactDeleteResponse, ContactIntroductionResponse, ContactInviteToOneToOneDiscussionResponse, ContactDowngradeOneToOneDiscussionResponse, DiscussionListResponse, DiscussionGetResponse, DiscussionGetByContactResponse, DiscussionGetByGroupResponse, DiscussionEmptyResponse, DiscussionSettingsGetResponse, DiscussionSettingsSetResponse, DiscussionLockedListResponse, DiscussionLockedDeleteResponse, GroupListResponse, GroupGetResponse, GroupNewStandardGroupResponse, GroupNewControlledGroupResponse, GroupNewReadOnlyGroupResponse, GroupNewAdvancedGroupResponse, GroupDisbandResponse, GroupLeaveResponse, GroupUpdateResponse, GroupUnsetPhotoResponse, GroupSetPhotoResponse, IdentityGetResponse, IdentityUpdateDetailsResponse, IdentityRemovePhotoResponse, IdentitySetPhotoResponse, IdentityKeycloakBindResponse, IdentityKeycloakUnbindResponse, IdentitySetApiKeyResponse, IdentitySetConfigurationLinkResponse, InvitationListResponse, InvitationGetResponse, InvitationNewResponse, InvitationAcceptResponse, InvitationDeclineResponse, InvitationSasResponse, InvitationDeleteResponse, MessageListResponse, MessageGetResponse, MessageRefreshResponse, MessageDeleteResponse, MessageSendResponse, MessageSendWithAttachmentsResponse, MessageSendLocationResponse, MessageReactResponse, MessageUpdateBodyResponse, MessageSendVoipResponse, StorageListResponse, StorageGetResponse, StorageSetResponse, StorageUnsetResponse, DiscussionStorageListResponse, DiscussionStorageGetResponse, DiscussionStorageSetResponse, DiscussionStorageUnsetResponse]
