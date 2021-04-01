#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""porcello.py: Execute porcello from command-line.

   :synopsis: Execute porcello from command-line.
   :platform: Unix, Windows

.. moduleauthor:: Francesco Rolando <ogekuri@gmail>

"""

import sys

import discord
from discord.ext import commands

_author_ = "Francesco Rolando"
_email_ = "ogekuri@gmail.com"
_copyright_ = "Copyright 2020, Francesco Rolando"
_version_ = "1.0.0"


def main():
    """Example: Execute porcello.

    Execute porcello.

    Returns:
         int: 0 for success, >0 otherwise.

    """
    _ret = 0
    _interactive = False

    bot = commands.Bot(command_prefix='!')

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('****')

    return _ret


if __name__ == "__main__":
    # execute main
    ret = main()
    sys.exit(ret)
