import os
import grpc
from typing import Optional

class GrpcTlsConfiguration:
	"""
	If daemon uses TLS you will need to set it up. You can create and pass a GrpcTlsConfiguration as a parameter,
	use environment or add symlinks to appropriate files to have a more persistent configuration.
	There are two valid TLS configuration: a "simple" configuration (use daemon certificate to encrypt communications)
	and a mutual authentication configuration where you need a signed certificate to authenticate on daemon.

	To set up a simple configuration, choose between one of this:
	- use OlvidClient tls_configuration __init__ parameter and pass an OlvidClient.GrpcSimpleTlsConfiguration instance,
	 	with daemon certificate file path as parameter
	- set OLVID_SERVER_CERTIFICATE_PATH in environment to the daemon certificate file path.
	- create a file / a symlink named .server.pem to the daemon certificate file.

	To set up a mutual authentication configuration, choose between one of this:
	- use OlvidClient tls_configuration __init__ parameter and pass an OlvidClient.GrpcMutualAuthTlsConfiguration instance.
		Set root_certificate_path to the CA certificate file path, certificate_chain_path to your certificate file path,
		and private_key_path to your private key file path.
	- use environment variables:
		- OLVID_ROOT_CERTIFICATE_PATH: CA certificate file path
		- OLVID_CERTIFICATE_CHAIN_PATH: your client certificate file path
		- OLVID_PRIVATE_KEY_PATH: your client key file path
	- create a file / a symlink to get a persistent configuration:
		- .ca.pem: CA certificate file path
		- .client.pem: your client certificate file path
		- .client.key: your client key file path
	"""
	# create grpc channel credentials from current instance
	def get_channel_credentials(self) -> grpc.ChannelCredentials:
		raise NotImplementedError()

	# try to load a tls configuration using env and default file names
	@staticmethod
	def load_implicit_configuration() -> Optional:
		raise NotImplementedError()


# Use to connect to a daemon using https
class GrpcSslConfiguration(GrpcTlsConfiguration):
	# create grpc channel credentials from current instance
	def get_channel_credentials(self) -> grpc.ChannelCredentials:
		return grpc.ssl_channel_credentials()

	# try to load a tls configuration using env and default file names
	@staticmethod
	def load_implicit_configuration() -> Optional:
		return


class GrpcSimpleTlsConfiguration(GrpcTlsConfiguration):
	_SERVER_CERTIFICATE_PATH_VARIABLE_NAME: str = "OLVID_SERVER_CERTIFICATE_PATH"
	_SERVER_CERTIFICATE_DEFAULT_PATH: str = ".server.pem"

	def __init__(self, server_certificate_path: str):
		self.server_certificate_path = server_certificate_path

	def get_channel_credentials(self) -> grpc.ChannelCredentials:
		with open(self.server_certificate_path, "rb") as fd:
			server_certificate: bytes = fd.read()
		return grpc.ssl_channel_credentials(root_certificates=server_certificate)

	@staticmethod
	def load_implicit_configuration() -> Optional[GrpcTlsConfiguration]:
		if os.getenv(GrpcSimpleTlsConfiguration._SERVER_CERTIFICATE_PATH_VARIABLE_NAME):
			return GrpcSimpleTlsConfiguration(os.getenv(GrpcSimpleTlsConfiguration._SERVER_CERTIFICATE_PATH_VARIABLE_NAME))
		elif os.path.isfile(GrpcSimpleTlsConfiguration._SERVER_CERTIFICATE_DEFAULT_PATH):
			return GrpcSimpleTlsConfiguration(GrpcSimpleTlsConfiguration._SERVER_CERTIFICATE_DEFAULT_PATH)
		else:
			return None


class GrpcMutualAuthTlsConfiguration(GrpcTlsConfiguration):
	_ROOT_CERTIFICATE_PATH_VARIABLE_NAME: str = "OLVID_ROOT_CERTIFICATE_PATH"
	_ROOT_CERTIFICATE_DEFAULT_PATH: str = ".ca.pem"

	_CERTIFICATE_CHAIN_PATH_VARIABLE_NAME: str = "OLVID_CERTIFICATE_CHAIN_PATH"
	_CERTIFICATE_CHAIN_DEFAULT_PATH: str = ".client.pem"

	_PRIVATE_KEY_PATH_VARIABLE_NAME: str = "OLVID_PRIVATE_KEY_PATH"
	_PRIVATE_KEY_DEFAULT_PATH: str = ".client.key"

	def __init__(self, root_certificate_path: str, certificate_chain_path: str, private_key_path: str):
		self.root_certificate_path = root_certificate_path
		self.certificate_chain_path = certificate_chain_path
		self.private_key_path = private_key_path

	def get_channel_credentials(self) -> grpc.ChannelCredentials:
		with open(self.root_certificate_path, "rb") as fd:
			root_certificate: bytes = fd.read()
		with open(self.certificate_chain_path, "rb") as fd:
			certificate_chain: bytes = fd.read()
		with open(self.private_key_path, "rb") as fd:
			private_key: bytes = fd.read()

		return grpc.ssl_channel_credentials(
			root_certificates=root_certificate,
			certificate_chain=certificate_chain,
			private_key=private_key
		)

	@staticmethod
	def load_implicit_configuration() -> Optional[GrpcTlsConfiguration]:
		if os.getenv(GrpcMutualAuthTlsConfiguration._ROOT_CERTIFICATE_PATH_VARIABLE_NAME):
			root_certificate_path = os.getenv(GrpcMutualAuthTlsConfiguration._ROOT_CERTIFICATE_PATH_VARIABLE_NAME)
		elif os.path.isfile(GrpcMutualAuthTlsConfiguration._ROOT_CERTIFICATE_DEFAULT_PATH):
			root_certificate_path = GrpcMutualAuthTlsConfiguration._ROOT_CERTIFICATE_DEFAULT_PATH
		else:
			return None

		if os.getenv(GrpcMutualAuthTlsConfiguration._CERTIFICATE_CHAIN_PATH_VARIABLE_NAME):
			certificate_chain_path = os.getenv(GrpcMutualAuthTlsConfiguration._CERTIFICATE_CHAIN_PATH_VARIABLE_NAME)
		elif os.path.isfile(GrpcMutualAuthTlsConfiguration._CERTIFICATE_CHAIN_DEFAULT_PATH):
			certificate_chain_path = GrpcMutualAuthTlsConfiguration._CERTIFICATE_CHAIN_DEFAULT_PATH
		else:
			return None

		if os.getenv(GrpcMutualAuthTlsConfiguration._PRIVATE_KEY_PATH_VARIABLE_NAME):
			private_key_path = os.getenv(GrpcMutualAuthTlsConfiguration._PRIVATE_KEY_PATH_VARIABLE_NAME)
		elif os.path.isfile(GrpcMutualAuthTlsConfiguration._PRIVATE_KEY_DEFAULT_PATH):
			private_key_path = GrpcMutualAuthTlsConfiguration._PRIVATE_KEY_DEFAULT_PATH
		else:
			return None

		return GrpcMutualAuthTlsConfiguration(
			root_certificate_path=root_certificate_path,
			certificate_chain_path=certificate_chain_path,
			private_key_path=private_key_path
		)
