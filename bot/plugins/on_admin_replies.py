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
    Filters,
    Message
)
from bot import (
    AUTH_USERS
)
from bot.sql.users_sql import (
    get_user_id
)


@Client.on_message(
    Filters.chat(AUTH_USERS) &
    Filters.create(
        lambda _, message: message.reply_to_message and message.reply_to_message.from_user.is_self
    )
)
async def on_pm_s(client: Client, message: Message):
    user_id, reply_message_id = get_user_id(
        message.reply_to_message.message_id
    )
    # 🥺 check two conditions 🤔🤔
    if message.media:
        _, file_id = get_file_id(message)
        caption = message.caption.html
        await client.send_cached_media(
            chat_id=user_id,
            file_id=file_id,
            caption=caption,
            reply_markup=message.reply_markup,
            disable_notification=True,
            reply_to_message_id=reply_message_id
        )
    else:
        await client.send_message(
            chat_id=user_id,
            text=message.text.html,
            disable_web_page_preview=True,
            disable_notification=True,
            reply_to_message_id=reply_message_id
        )
