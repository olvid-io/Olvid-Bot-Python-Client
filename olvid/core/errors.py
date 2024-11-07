from grpc import StatusCode
from grpc.aio import AioRpcError, Metadata
from typing import Optional


class OlvidError(AioRpcError):
	def __init__(self, code: StatusCode = None, details: Optional[str] = None, initial_metadata: Metadata = None, trailing_metadata: Metadata = None, debug_error_string: Optional[str] = None):
		super().__init__(
			code=code,
			initial_metadata=initial_metadata if initial_metadata else Metadata(),
			trailing_metadata=trailing_metadata if trailing_metadata else Metadata(),
			details=details,
			debug_error_string=debug_error_string,
		)
		self._name: str = self.__class__.__name__

	def __str__(self):
		return f"{self._name}: {self._details}"

	@staticmethod
	def _from_aio_rpc_error(original_error: AioRpcError) -> AioRpcError:
		if original_error.code() == StatusCode.CANCELLED:
			return CancelledError(code=original_error.code(), initial_metadata=original_error.initial_metadata(), trailing_metadata=original_error.trailing_metadata(), details=original_error.details(), debug_error_string=original_error.debug_error_string())
		elif original_error.code() == StatusCode.INVALID_ARGUMENT:
			return InvalidArgumentError(code=original_error.code(), initial_metadata=original_error.initial_metadata(), trailing_metadata=original_error.trailing_metadata(), details=original_error.details(), debug_error_string=original_error.debug_error_string())
		elif original_error.code() == StatusCode.NOT_FOUND:
			return NotFoundError(code=original_error.code(), initial_metadata=original_error.initial_metadata(), trailing_metadata=original_error.trailing_metadata(), details=original_error.details(), debug_error_string=original_error.debug_error_string())
		elif original_error.code() == StatusCode.PERMISSION_DENIED:
			return PermissionDeniedError(code=original_error.code(), initial_metadata=original_error.initial_metadata(), trailing_metadata=original_error.trailing_metadata(), details=original_error.details(), debug_error_string=original_error.debug_error_string())
		elif original_error.code() == StatusCode.UNAUTHENTICATED:
			return UnauthenticatedError(code=original_error.code(), initial_metadata=original_error.initial_metadata(), trailing_metadata=original_error.trailing_metadata(), details=original_error.details(), debug_error_string=original_error.debug_error_string())
		elif original_error.code() == StatusCode.UNIMPLEMENTED:
			return UnimplementedError(code=original_error.code(), initial_metadata=original_error.initial_metadata(), trailing_metadata=original_error.trailing_metadata(), details=original_error.details(), debug_error_string=original_error.debug_error_string())
		elif original_error.code() == StatusCode.INTERNAL:
			return InternalError(code=original_error.code(), initial_metadata=original_error.initial_metadata(), trailing_metadata=original_error.trailing_metadata(), details=original_error.details(), debug_error_string=original_error.debug_error_string())
		elif original_error.code() == StatusCode.UNAVAILABLE:
			return UnavailableError(code=original_error.code(), initial_metadata=original_error.initial_metadata(), trailing_metadata=original_error.trailing_metadata(), details=original_error.details(), debug_error_string=original_error.debug_error_string())
		return original_error


"""
Exceptions triggered by Olvid Api
"""
class NotFoundError(OlvidError):
	"""
	The element you requested does not exists.
	"""
	pass

class InvalidArgumentError(OlvidError):
	"""
	The request you sent contains invalid fields, check error details to learn more.
	"""
	pass

class UnauthenticatedError(OlvidError):
	"""
	The client key you provided is not valid (or you haven't provided a client key).
	"""
	pass

class PermissionDeniedError(OlvidError):
	"""
	You tried to access admin methods with a non admin client key.
	"""
	pass

class InternalError(OlvidError):
	"""
	Something wrong happened daemon side. Check daemon logs to get more info.
	"""
	pass


"""
Exceptions triggered by gRPC you might see
"""
class UnavailableError(OlvidError):
	"""
	gRPC server is not available. Your daemon is probably not running or your client cannot connect to it.
	Check your connection url and port.
	"""
	pass

class CancelledError(OlvidError):
	"""
	The operation was cancelled, typically by the caller.
	This might happen if you force quit your program.
	"""
	pass

class UnimplementedError(OlvidError):
	"""
	Your daemon does not implement this method, check that your client and daemon version are the same.
	"""
	pass

# """
# Other gRPC exceptions
# """
# class DeadlineExceededError(AbstractError):
# 	pass
#
# class AlreadyExistsError(AbstractError):
# 	pass
#
# class ResourceExhaustedError(AbstractError):
# 	pass
#
# class FailedPreconditionError(AbstractError):
# 	pass
#
# class AbortedError(AbstractError):
# 	pass
#
# class DataLossError(AbstractError):
# 	pass
#
# class UnknownError(AbstractError):
# 	pass

