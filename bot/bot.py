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

""" MtProto Bot """

from pyrogram import (
    Client,
    __version__
)
from bot import (
    API_HASH,
    APP_ID,
    AUTH_CHANNEL,
    DEFAULT_START_TEXT,
    LOGGER,
    START_COMMAND,
    START_OTHER_USERS_TEXT,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS
)


class Bot(Client):
    """ modded client for NoPMsBot """
    commandi = {}

    def __init__(self):
        super().__init__(
            "NoPMsBot",
            api_hash=API_HASH,
            api_id=APP_ID,
            bot_token=TG_BOT_TOKEN,
            plugins={
                "root": "bot/plugins"
            },
            workers=TG_BOT_WORKERS
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        try:
            check_m = await self.get_messages(
                chat_id=AUTH_CHANNEL,
                message_ids=START_OTHER_USERS_TEXT,
                replies=0
            )
        except ValueError:
            self.commandi[START_COMMAND] = DEFAULT_START_TEXT
        else:
            if check_m:
                self.commandi[START_COMMAND] = check_m.text.html
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
            "Try /start."
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("NoPMsBot stopped. Bye.")
