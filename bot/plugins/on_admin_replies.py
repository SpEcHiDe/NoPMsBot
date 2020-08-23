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
    AUTH_USERS,
    BAN_COMMAND,
    DERP_USER_S_TEXT,
    IS_BLACK_LIST_ED_MESSAGE_TEXT,
    IS_UN_BANED_MESSAGE_TEXT,
    REASON_DE_LIMIT_ER,
    UN_BAN_COMMAND
)
from bot.hf.gfi import (
    get_file_id
)
from bot.sql.users_sql import (
    get_user_id
)
from bot.sql.blacklist_sql import (
    add_user_to_bl,
    rem_user_from_bl
)


@Client.on_message(
    Filters.chat(AUTH_USERS) &
    Filters.create(
        lambda _, message: message.reply_to_message and
        message.reply_to_message.from_user.is_self
    )
)
async def on_pm_s(client: Client, message: Message):
    user_id, reply_message_id = get_user_id(
        message.reply_to_message.message_id
    )
    recvd_text = message.text.html + " "

    cmnd_message, ban_un_reason = recvd_text.split(" ", 1)
    cmnd_message = cmnd_message.strip()
    ban_un_reason = ban_un_reason.strip()

    if cmnd_message == BAN_COMMAND:
        add_user_to_bl(user_id, ban_un_reason)

        black_list_message = IS_BLACK_LIST_ED_MESSAGE_TEXT.format(
            reason=ban_un_reason
        )
        if not ban_un_reason:
            black_list_message = black_list_message.split(
                REASON_DE_LIMIT_ER
            )[0]

        await client.send_message(
            chat_id=user_id,
            text=black_list_message,
            disable_web_page_preview=True,
            reply_markup=message.reply_markup,
            disable_notification=True,
            reply_to_message_id=reply_message_id
        )

        await message.reply_text(
            f"<a href='tg://user?id={user_id}'>"
            "user"
            "</a> <b>banned</b> <i>forever</i>."
        )

    elif cmnd_message == UN_BAN_COMMAND:
        rem_user_from_bl(user_id)

        black_list_message = IS_UN_BANED_MESSAGE_TEXT.format(
            reason=ban_un_reason
        )
        if not ban_un_reason:
            black_list_message = black_list_message.split(
                REASON_DE_LIMIT_ER
            )[0]

        await client.send_message(
            chat_id=user_id,
            text=black_list_message,
            disable_web_page_preview=True,
            reply_markup=message.reply_markup,
            disable_notification=True,
            reply_to_message_id=reply_message_id
        )

        await message.reply_text(
            f"<a href='tg://user?id={user_id}'>"
            "user"
            "</a> <b>unbanned</b>."
        )

    else:
        await send_message_to_user(
            client,
            message,
            user_id,
            reply_message_id
        )


async def send_message_to_user(
    client: Client,
    message: Message,
    user_id: int,
    reply_message_id: int
):
    # 🥺 check two conditions 🤔🤔
    if message.media:
        _, file_id = get_file_id(message)
        caption = (
            message.caption and message.caption.html
        ) or ""
        await client.send_cached_media(
            chat_id=user_id,
            file_id=file_id,
            caption=caption,
            reply_markup=message.reply_markup,
            disable_notification=True,
            reply_to_message_id=reply_message_id
        )
    else:
        caption = (
            message.text and message.text.html
        ) or DERP_USER_S_TEXT
        await client.send_message(
            chat_id=user_id,
            text=caption,
            disable_web_page_preview=True,
            reply_markup=message.reply_markup,
            disable_notification=True,
            reply_to_message_id=reply_message_id
        )
