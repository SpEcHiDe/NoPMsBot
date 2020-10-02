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

from typing import List, Union
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)


def uszkhvis_chats_ahndler(chats: List[Union[str, int]]):
    async def func(flt, client: Client, message: Message):
        chats = flt.chats
        return bool(
            message.chat and (
                message.chat.id in chats
            )
        )
    # "chats" kwarg is accessed with "flt.chats" above
    return filters.create(func, chats=chats)
