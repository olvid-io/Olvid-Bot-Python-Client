# import core clients
# noinspection PyUnresolvedReferences
from .core import OlvidClient
# noinspection PyUnresolvedReferences
from .core import OlvidBot
# noinspection PyUnresolvedReferences
from .core import OlvidAdminClient

# import core elements
# noinspection PyUnresolvedReferences
from . import listeners

# import overlay modules
# noinspection PyUnresolvedReferences
from . import datatypes
# noinspection PyUnresolvedReferences
from . import internal

# import bots
# noinspection PyUnresolvedReferences
from . import tools

# delete imported modules
if "core" in locals() or "core" in globals():
	del core

if "protobuf" in locals() or "protobuf" in globals():
	# noinspection PyUnresolvedReferences
	del protobuf

# noinspection PyUnresolvedReferences
from .version import __version__
del version
