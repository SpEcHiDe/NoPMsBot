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

""" credentials """

from .get_config import get_config


# The Telegram API things
# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = get_config("APP_ID", should_prompt=True)
# get a token from @BotFather
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)
# array to store the channel ID who are authorized to use the bot
AUTH_USERS = list(set(
    int(x) for x in get_config(
        "AUTH_USERS",
        should_prompt=True
    ).split()
))
# sqlalchemy Database for the bot to operate
DB_URI = get_config(
    "DATABASE_URL",
    should_prompt=True
)
# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
# /start message when other users start your bot
START_OTHER_USERS_TEXT = get_config(
    "START_OTHER_USERS_TEXT",
    (
        "Hi. ☺️\n"
        "You can contact the admins of @Foundation_9and10 through this bot.😬\n\n"
        "ℹ️ Join @Foundation_9and10 if you wish to use this bot❗️❣️"
    )
)
# check online status of your bot
ONLINE_CHECK_START_TEXT = get_config(
    "ONLINE_CHECK_START_TEXT",
    (
        "I am online <b>master</b>\n\n"
        "You can contact the admins here.\n\n\n"
        "ℹ️ Join @Foundation_9and10 now if you are using this bot❗️❣️"
    )
)
# IDEKWBYRW
DERP_USER_S_TEXT = get_config(
    "DERP_USER_S_TEXT",
    "😐"
)
BAN_COMMAND = "/ban"
# message to show when user is banned
IS_BLACK_LIST_ED_MESSAGE_TEXT = get_config(
    "IS_BLACK_LIST_ED_MESSAGE_TEXT",
    (
        "You have been <b>banned</b> forever.\n\n"
        "<u>Reason</u>: <code>{reason}</code>"
    )
)
# IDEKWBYRW
REASON_DE_LIMIT_ER = get_config(
    "REASON_DE_LIMIT_ER",
    "\n\n"
)
UN_BAN_COMMAND = "/unban"
# message to show when user is unbanned
IS_UN_BANED_MESSAGE_TEXT = get_config(
    "IS_UN_BANED_MESSAGE_TEXT",
    (
        "You have been <b>un-banned</b>.\n\n"
        "<u>Reason</u>: <code>{reason}</code>"
    )
)
# message to show if bot was blocked by user
BOT_WS_BLOCKED_BY_USER = get_config(
    "BOT_WS_BLOCKED_BY_USER",
    "Bot was blocked by the user."
)
