# Telegram Relay Bot

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [COPYING](./COPYING) for more details.

## Demo RoBot

- [@shriMADhaBot](https://telegram.dog/shriMADhaBot)


## installing

#### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## ENVironment VARiables

#### Mandatory Environment Variables

* `TG_BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.

* `APP_ID`
* `API_HASH`: Get these two values from [my.telegram.org/apps](https://my.telegram.org/apps).
  * N.B.: if Telegram is blocked by your ISP, try our [Telegram bot](https://telegram.dog/UseTGXBot) to get the IDs.

* `AUTH_USERS`:
Create a Super Group in Telegram, add `@GoogleIMGBot` to the group, and send /id in the chat, to get this value.
You can add multiple IDs seperated by space.

* `DATABASE_URL`: ~~if you are using Heroku, this value is automatically filled by the Postgres Plugin.~~ if you are not using Heroku, Read the guide on how to Install Database?, below.

#### Optional Environment Variables

* `TG_BOT_WORKERS`: Number of workers to use. 4 is the recommended (and default) amount, but your experience may vary.
 __Note__ that going crazy with more workers won't necessarily speed up your bot, given the amount of sql data accesses, and the way python asynchronous calls work.

* `START_OTHER_USERS_TEXT`: The message that your bot users would see on sending /start message.

* `ONLINE_CHECK_START_TEXT`: The message that the bot administrators can use to check if bot is online.

* `DERP_USER_S_TEXT`: Keep this to the default value, unless you know what you are doing.

* `BAN_COMMAND`: The command that can be used by administrators of the bot to ban users. The default is `/ban`.

* `IS_BLACK_LIST_ED_MESSAGE_TEXT`: The message to be displayed to the user, when an administrator bans them from the bot.

* `REASON_DE_LIMIT_ER`: Keep this to the default value, unless you know what you are doing.

* `UN_BAN_COMMAND`: The command that can be used by administrators of the bot to unban users. The default is `/unban`.

* `IS_UN_BANED_MESSAGE_TEXT`: The message to be displayed to the user, when an administrator unbans them from the bot.

* `BOT_WS_BLOCKED_BY_USER`: The message to be displayed to the administrator, if bot was blocked by the user.


## How to Install Database ?

I use postgres, so I recommend using it for optimal compatibility.

In the case of postgres, this is how you would set up a the database on a Arch Linux system. Other distributions may vary.

- install postgresql:

`sudo pacman -Syy && sudo pacman -S postgresql`

- change to the postgres user:

`sudo -iu postgres`

- initialize the database cluster

`initdb --locale=en_US.UTF-8 -E UTF8 -D /var/lib/postgres/data`

- create a new database user (change YOUR_USER appropriately):

`createuser -P -s -e YOUR_USER`

This will be followed by you needing to input your password.

- create a new database table:

`createdb -O YOUR_USER YOUR_DB_NAME`

Change YOUR_USER and YOUR_DB_NAME appropriately.

- testing your database connection:

`psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER`

This will allow you to connect to your database via your terminal.
By default, YOUR_HOST should be 0.0.0.0:5432.

You should now be able to build your database URI. This will be:

`sqldbtype://username:pw@hostname:port/db_name`

To secure your DataBase installation, please read https://wiki.archlinux.org/index.php/PostgreSQL

Replace sqldbtype with whichever db youre using (eg postgres, mysql, sqllite, etc)
repeat for your username, password, hostname (localhost?), port (5432?), and db name.

## Credits, and Thanks to

* [me](https://github.com/sudoshell/NoPMsBot)
* [Dan Tès](https://telegram.dog/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)
