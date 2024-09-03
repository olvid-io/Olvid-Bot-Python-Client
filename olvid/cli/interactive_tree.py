import asyncclick as click

from .tools.click_wrappers import WrapperGroup


@click.group(cls=WrapperGroup)
async def interactive_tree():
	pass


# noinspection PyUnresolvedReferences
from .handler.identity_tree import *
# noinspection PyUnresolvedReferences
from .handler.key_tree import *
# noinspection PyUnresolvedReferences
from .handler.discussion_tree import *
# noinspection PyUnresolvedReferences
from .handler.message_tree import *
# noinspection PyUnresolvedReferences
from .handler.attachment_tree import *
# noinspection PyUnresolvedReferences
from .handler.invitation_tree import *
# noinspection PyUnresolvedReferences
from .handler.contact_tree import *
# noinspection PyUnresolvedReferences
from .handler.group_tree import *
# noinspection PyUnresolvedReferences
from .handler.storage_tree import *
# noinspection PyUnresolvedReferences
from .handler.tools_tree import *
