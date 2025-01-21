# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from .....olvid.daemon.admin.v1 import client_key_admin_pb2 as olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2
from .....olvid.daemon.admin.v1 import identity_admin_pb2 as olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2


class ClientKeyAdminServiceStub(object):
    """ClientKey
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ClientKeyList = channel.unary_stream(
                '/olvid.daemon.services.v1.ClientKeyAdminService/ClientKeyList',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyListRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyListResponse.FromString,
                _registered_method=True)
        self.ClientKeyGet = channel.unary_unary(
                '/olvid.daemon.services.v1.ClientKeyAdminService/ClientKeyGet',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyGetRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyGetResponse.FromString,
                _registered_method=True)
        self.ClientKeyNew = channel.unary_unary(
                '/olvid.daemon.services.v1.ClientKeyAdminService/ClientKeyNew',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyNewRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyNewResponse.FromString,
                _registered_method=True)
        self.ClientKeyDelete = channel.unary_unary(
                '/olvid.daemon.services.v1.ClientKeyAdminService/ClientKeyDelete',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyDeleteRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyDeleteResponse.FromString,
                _registered_method=True)


class ClientKeyAdminServiceServicer(object):
    """ClientKey
    """

    def ClientKeyList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientKeyGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientKeyNew(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientKeyDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientKeyAdminServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ClientKeyList': grpc.unary_stream_rpc_method_handler(
                    servicer.ClientKeyList,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyListRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyListResponse.SerializeToString,
            ),
            'ClientKeyGet': grpc.unary_unary_rpc_method_handler(
                    servicer.ClientKeyGet,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyGetRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyGetResponse.SerializeToString,
            ),
            'ClientKeyNew': grpc.unary_unary_rpc_method_handler(
                    servicer.ClientKeyNew,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyNewRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyNewResponse.SerializeToString,
            ),
            'ClientKeyDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.ClientKeyDelete,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyDeleteRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'olvid.daemon.services.v1.ClientKeyAdminService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('olvid.daemon.services.v1.ClientKeyAdminService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ClientKeyAdminService(object):
    """ClientKey
    """

    @staticmethod
    def ClientKeyList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/olvid.daemon.services.v1.ClientKeyAdminService/ClientKeyList',
            olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyListRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClientKeyGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/olvid.daemon.services.v1.ClientKeyAdminService/ClientKeyGet',
            olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyGetRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyGetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClientKeyNew(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/olvid.daemon.services.v1.ClientKeyAdminService/ClientKeyNew',
            olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyNewRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyNewResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClientKeyDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/olvid.daemon.services.v1.ClientKeyAdminService/ClientKeyDelete',
            olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyDeleteRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_client__key__admin__pb2.ClientKeyDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class IdentityAdminServiceStub(object):
    """Identity
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IdentityList = channel.unary_stream(
                '/olvid.daemon.services.v1.IdentityAdminService/IdentityList',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityListRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityListResponse.FromString,
                _registered_method=True)
        self.IdentityAdminGet = channel.unary_unary(
                '/olvid.daemon.services.v1.IdentityAdminService/IdentityAdminGet',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetResponse.FromString,
                _registered_method=True)
        self.IdentityAdminGetBytesIdentifier = channel.unary_unary(
                '/olvid.daemon.services.v1.IdentityAdminService/IdentityAdminGetBytesIdentifier',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetBytesIdentifierRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetBytesIdentifierResponse.FromString,
                _registered_method=True)
        self.IdentityAdminGetInvitationLink = channel.unary_unary(
                '/olvid.daemon.services.v1.IdentityAdminService/IdentityAdminGetInvitationLink',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetInvitationLinkRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetInvitationLinkResponse.FromString,
                _registered_method=True)
        self.IdentityAdminDownloadPhoto = channel.unary_unary(
                '/olvid.daemon.services.v1.IdentityAdminService/IdentityAdminDownloadPhoto',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminDownloadPhotoRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminDownloadPhotoResponse.FromString,
                _registered_method=True)
        self.IdentityDelete = channel.unary_unary(
                '/olvid.daemon.services.v1.IdentityAdminService/IdentityDelete',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityDeleteRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityDeleteResponse.FromString,
                _registered_method=True)
        self.IdentityNew = channel.unary_unary(
                '/olvid.daemon.services.v1.IdentityAdminService/IdentityNew',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityNewRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityNewResponse.FromString,
                _registered_method=True)
        self.IdentityKeycloakNew = channel.unary_unary(
                '/olvid.daemon.services.v1.IdentityAdminService/IdentityKeycloakNew',
                request_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityKeycloakNewRequest.SerializeToString,
                response_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityKeycloakNewResponse.FromString,
                _registered_method=True)


class IdentityAdminServiceServicer(object):
    """Identity
    """

    def IdentityList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IdentityAdminGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IdentityAdminGetBytesIdentifier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IdentityAdminGetInvitationLink(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IdentityAdminDownloadPhoto(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IdentityDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IdentityNew(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IdentityKeycloakNew(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IdentityAdminServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IdentityList': grpc.unary_stream_rpc_method_handler(
                    servicer.IdentityList,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityListRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityListResponse.SerializeToString,
            ),
            'IdentityAdminGet': grpc.unary_unary_rpc_method_handler(
                    servicer.IdentityAdminGet,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetResponse.SerializeToString,
            ),
            'IdentityAdminGetBytesIdentifier': grpc.unary_unary_rpc_method_handler(
                    servicer.IdentityAdminGetBytesIdentifier,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetBytesIdentifierRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetBytesIdentifierResponse.SerializeToString,
            ),
            'IdentityAdminGetInvitationLink': grpc.unary_unary_rpc_method_handler(
                    servicer.IdentityAdminGetInvitationLink,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetInvitationLinkRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetInvitationLinkResponse.SerializeToString,
            ),
            'IdentityAdminDownloadPhoto': grpc.unary_unary_rpc_method_handler(
                    servicer.IdentityAdminDownloadPhoto,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminDownloadPhotoRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminDownloadPhotoResponse.SerializeToString,
            ),
            'IdentityDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.IdentityDelete,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityDeleteRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityDeleteResponse.SerializeToString,
            ),
            'IdentityNew': grpc.unary_unary_rpc_method_handler(
                    servicer.IdentityNew,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityNewRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityNewResponse.SerializeToString,
            ),
            'IdentityKeycloakNew': grpc.unary_unary_rpc_method_handler(
                    servicer.IdentityKeycloakNew,
                    request_deserializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityKeycloakNewRequest.FromString,
                    response_serializer=olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityKeycloakNewResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'olvid.daemon.services.v1.IdentityAdminService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('olvid.daemon.services.v1.IdentityAdminService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class IdentityAdminService(object):
    """Identity
    """

    @staticmethod
    def IdentityList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/olvid.daemon.services.v1.IdentityAdminService/IdentityList',
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityListRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def IdentityAdminGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/olvid.daemon.services.v1.IdentityAdminService/IdentityAdminGet',
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def IdentityAdminGetBytesIdentifier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/olvid.daemon.services.v1.IdentityAdminService/IdentityAdminGetBytesIdentifier',
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetBytesIdentifierRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetBytesIdentifierResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def IdentityAdminGetInvitationLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/olvid.daemon.services.v1.IdentityAdminService/IdentityAdminGetInvitationLink',
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetInvitationLinkRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminGetInvitationLinkResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def IdentityAdminDownloadPhoto(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/olvid.daemon.services.v1.IdentityAdminService/IdentityAdminDownloadPhoto',
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminDownloadPhotoRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityAdminDownloadPhotoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def IdentityDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/olvid.daemon.services.v1.IdentityAdminService/IdentityDelete',
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityDeleteRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def IdentityNew(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/olvid.daemon.services.v1.IdentityAdminService/IdentityNew',
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityNewRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityNewResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def IdentityKeycloakNew(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/olvid.daemon.services.v1.IdentityAdminService/IdentityKeycloakNew',
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityKeycloakNewRequest.SerializeToString,
            olvid_dot_daemon_dot_admin_dot_v1_dot_identity__admin__pb2.IdentityKeycloakNewResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
