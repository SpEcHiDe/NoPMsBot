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


@Client.on_message(
    Filters.chat(AUTH_USERS) &
    Filters.create(
        lambda _, message: message.reply_to_message and message.reply_to_message.from_user.is_self
    )
)
async def on_pm_s(client: Client, message: Message):
    print(message)
