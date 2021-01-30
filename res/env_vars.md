# Telegram Relay Bot

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [COPYING](./../COPYING) for more details.


## ENVironment VARiables

#### Mandatory Environment Variables

* `TG_BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.

* `APP_ID`
* `API_HASH`: Get these two values from [my.telegram.org/apps](https://my.telegram.org/apps).
  * N.B.: if Telegram is blocked by your ISP, try our [Telegram bot](https://telegram.dog/UseTGXBot) to get the IDs.

* `AUTH_CHANNEL`:
Create a Super Group in Telegram, add `@GoogleIMGBot` to the group, and send /id in the chat, to get this value.

* `DATABASE_URL`: ~~if you are using Heroku, this value is automatically filled by the Postgres Plugin.~~ if you are not using Heroku, Read the guide on [how to Install Database?](https://github.com/SpEcHiDe/NoPMsBot/wiki/How-to-Install-Database-%3F).

#### Optional Environment Variables

* `TG_BOT_WORKERS`: Number of workers to use. 4 is the recommended (and default) amount, but your experience may vary.
 __Note__ that going crazy with more workers won't necessarily speed up your bot, given the amount of sql data accesses, and the way python asynchronous calls work.

* `COMMM_AND_PRE_FIX`: The command prefix. Telegram, by default, recommeds the use of `/`, which is the default prefix.

* `BAN_COMMAND`: The command that can be used by administrators of the bot to ban users. The default is `ban`.

* `UN_BAN_COMMAND`: The command that can be used by administrators of the bot to unban users. The default is `unban`.

* `START_COMMAND`: The command to check if the bot is alive, or for users to start the robot.

* `START_OTHER_USERS_TEXT`: Send a Message in your `AUTH_CHANNEL`, and paste message_id in this value.

* `ONLINE_CHECK_START_TEXT`: The message that the bot administrators can use to check if bot is online.

* `DELETED_MESSAGES_NOTIFICATION_TEXT`: The message that the bot administrators can see if any message was deleted by the user.

* `DERP_USER_S_TEXT`: Keep this to the default value, unless you know what you are doing.

* `IS_BLACK_LIST_ED_MESSAGE_TEXT`: The message to be displayed to the user, when an administrator bans them from the bot.

* `REASON_DE_LIMIT_ER`: Keep this to the default value, unless you know what you are doing.

* `IS_UN_BANED_MESSAGE_TEXT`: The message to be displayed to the user, when an administrator unbans them from the bot.

* `BOT_WS_BLOCKED_BY_USER`: The message to be displayed to the administrator, if bot was blocked by the user.

* `LOG_FILE_ZZGEVC`: The path to store log files.


## Credits, and Thanks to

* [ThankTelegram](https://telegram.dog/ThankTelegram)
* [Dan Tès](https://telegram.dog/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)
