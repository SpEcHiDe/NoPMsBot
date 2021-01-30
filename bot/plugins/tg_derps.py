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


from pyrogram.types import (
    CallbackQuery,
    Message
)
from typing import List
from bot import (
    AUTH_CHANNEL,
    DELETED_MESSAGES_NOTIFICATION_TEXT,
    DERP_USER_S_TEXT
)
from bot.bot import Bot
from bot.sql.users_sql import get_chek_dmid


@Bot.on_deleted_messages()
async def on_del_mesgs(client: Bot, messages: List[Message]):
    for message in messages:
        ym = get_chek_dmid(message.message_id)
        if ym:
            await client.send_message(
                chat_id=AUTH_CHANNEL,
                text=DELETED_MESSAGES_NOTIFICATION_TEXT,
                reply_to_message_id=ym.message_id
            )


@Bot.on_callback_query()
async def on_cb_qry(_, callback_query: CallbackQuery):
    await callback_query.answer(
        text=DERP_USER_S_TEXT,
        show_alert=False,
        cache_time=0
    )
