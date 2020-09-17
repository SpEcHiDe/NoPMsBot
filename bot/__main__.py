#  MIT License
#
#  Copyright (c) 2019-2020 Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person
#  obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software
#  without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be
#  included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
#  THE USE OR OTHER DEALINGS IN THE SOFTWARE.

""" copied from PyroGram Assistant """

try:
    from .bot import Bot
    Bot().run()
except ImportError:
    mandatory_vars = [
        "API_HASH",
        "APP_ID",
        "TG_BOT_TOKEN",
        "AUTH_USERS",
        "DATABASE_URL"
    ]
    optional_vars = [
        "TG_BOT_WORKERS",
        "COMMM_AND_PRE_FIX",
        "BAN_COMMAND",
        "UN_BAN_COMMAND",
        "START_COMMAND",
        "LOG_FILE_ZZGEVC",
        "START_OTHER_USERS_TEXT",
        "ONLINE_CHECK_START_TEXT",
        "DERP_USER_S_TEXT",
        "IS_BLACK_LIST_ED_MESSAGE_TEXT",
        "REASON_DE_LIMIT_ER",
        "IS_UN_BANED_MESSAGE_TEXT",
        "BOT_WS_BLOCKED_BY_USER"
    ]
    print("a 'run.sh' will be created / replaced")
    with open("run.sh", "w+") as f_d:
        for name in mandatory_vars:
            val = input(f"enter {name}'s value: ")
            f_d.write(f"{name}=\"{val}\" \\\n")
        for name in optional_vars:
            val = input(f"enter {name}'s value: ")
            f_d.write(f"{name}=\"{val}\" \\\n")
        f_d.write("python -m bot")
    print("open 'run.sh' in a Text Editor, and verify the variables\n")
    print("finally, run 'bash run.sh' in your Terminal to start the RoBot")
