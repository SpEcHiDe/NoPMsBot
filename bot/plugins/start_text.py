#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from bot import (
    AUTH_CHANNEL,
    COMMM_AND_PRE_FIX,
    ONLINE_CHECK_START_TEXT,
    START_COMMAND
)
from bot.bot import Bot
from bot.hf.flifi import uszkhvis_chats_ahndler


@Bot.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    ~uszkhvis_chats_ahndler([AUTH_CHANNEL])
)
async def num_start_message(client: Bot, message: Message):
    await message.reply_text(
        client.commandi[START_COMMAND],
        quote=True
    )


@Bot.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    uszkhvis_chats_ahndler([AUTH_CHANNEL])
)
async def nimda_start_message(_, message: Message):
    await message.reply_text(
        ONLINE_CHECK_START_TEXT,
        quote=True
    )
