from typing import Union, List

from pyrogram import filters

from config import PrinceX

other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded
other_filters2 = filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded


def command(commands: Union[str, List[str]]):
    return filters.command(commands, PrinceX.COMMAND_PREFIXES)
