# import core clients
# noinspection PyUnusedImports
from .core import OlvidClient
# noinspection PyUnusedImports
from .core import OlvidAdminClient
# noinspection PyUnusedImports
from .core import errors

# import core elements
# noinspection PyUnusedImports
from . import listeners

# import overlay modules
# noinspection PyUnusedImports
from . import datatypes
# noinspection PyUnusedImports
from . import internal

# import bots
# noinspection PyUnusedImports
from . import tools

# delete imported modules
if "core" in locals() or "core" in globals():
	del core

if "protobuf" in locals() or "protobuf" in globals():
	# noinspection PyUnresolvedReferences
	del protobuf

# noinspection PyUnusedImports
from .version import __version__
# noinspection PyUnusedImports
from .version import __docker_version__
del version
