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

from pyrogram import Client, filters
from pyrogram.types import Message

from bot import AUTH_CHANNEL, COMMM_AND_PRE_FIX, BROADCAST_COMMAND
from bot.bot import Bot
from bot.hf.flifi import uszkhvis_chats_ahndler
from bot.sql.users_sql import get_chats


@Bot.on_message(
    filters.command(BROADCAST_COMMAND, COMMM_AND_PRE_FIX)
    & uszkhvis_chats_ahndler([AUTH_CHANNEL])
)
async def num_start_message(client: Bot, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to Message..", quote=True)
    reply = message.reply_to_message
    All = get_chats()
    TTL = len(All)
    SUCCESS = 0
    for chat in All:
        try:
            await reply.copy(chat)
            SUCCESS += 1
        except BaseException as e:
            print(e, chat)
    MSG = "**BroadCast Completed !**\n"
    MSG += f"Succeed : {SUCCESS} Chats!"
    if TTL != SUCCESS:
        MSG += f"\nFailed : {All-SUCCESS} Chats."
    await message.reply_text(MSG, quote=True)
