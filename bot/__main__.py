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


import os
from pyrogram import (
    Client
)
from bot import (
    API_HASH,
    APP_ID,
    DOWNLOAD_LOCATION,
    TG_BOT_TOKEN
)


if __name__ == "__main__":
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    app = Client(
        ":memory:",
        api_hash=API_HASH,
        api_id=APP_ID,
        bot_token=TG_BOT_TOKEN,
        plugins=dict(
            root="bot/plugins"
        ),
        workers=343,
        workdir=DOWNLOAD_LOCATION
    )
    app.set_parse_mode("html")
    app.run()
