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
    IS_BLACK_LIST_ED_MESSAGE_TEXT,
    START_COMMAND
)
from bot.bot import Bot
from bot.hf.flifi import uszkhvis_chats_ahndler
from bot.sql.users_sql import (
    add_user_to_db,
    get_chek_dmid
)
from bot.sql.blacklist_sql import (
    check_is_black_list
)


@Bot.on_message(
    ~filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    ~uszkhvis_chats_ahndler([AUTH_CHANNEL]) &
    filters.incoming &
    filters.private
)
async def on_pm_s(client: Bot, message: Message):
    check_ban = check_is_black_list(message)
    if check_ban:
        await message.reply_text(
            text=IS_BLACK_LIST_ED_MESSAGE_TEXT.format(
                reason=check_ban.reason
            )
        )
        return

    fwded_mesg = None
    if message.edit_date:
        ym = get_chek_dmid(message.message_id)
        reply_to_message_id = None
        if ym:
            reply_to_message_id = ym.message_id
        fwded_mesg = await message.copy(
            chat_id=AUTH_CHANNEL,
            disable_notification=True,
            reply_to_message_id=reply_to_message_id,
            reply_markup=message.reply_markup
        )
    else:
        fwded_mesg = await message.copy(
            chat_id=AUTH_CHANNEL,
            disable_notification=True,
            reply_markup=message.reply_markup
        )

    # just store, we don't need to SPAM users
    # mimick LiveGramBot, not @LimitatiBot ..!
    add_user_to_db(
        fwded_mesg.message_id,
        message.from_user.id,
        message.message_id
    )


