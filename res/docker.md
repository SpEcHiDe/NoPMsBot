# Telegram Relay Bot

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [COPYING](./../COPYING) for more details.


#### The Easy Way [ 🐳 ]

Writing this again, since I have seen many users recommending **SUDO** to install Docker.
It is not recommended to use "sudo", while using Docker.
GNU/Linux Permissions are highly customisable, and it is generally not required to have "ROOT" permission, ~~unless you know what you are doing~~.
You can still install all the dependencies in your system [with ROOT permissions],
but please be aware of the potential issues when doing so. The installed packages
may conflict with the system package manager's installed packages, which can
cause trouble down the road and errors when upgrading conflicting packages.
**You have been warned.**

- **Install docker**: Follow the official docker [installation guide](https://docs.docker.com/engine/install/).

- **Install Docker-compose**: Follow the official composer [installation guide](https://docs.docker.com/compose/install/).

- **create CONFIG file**: 
  - ```wget https://raw.githubusercontent.com/SpEcHiDe/NoPMsBot/master/sample_config.env -O config.env```
  - edit the file by removing the `#` in the required fields, and adding values.

- **downloading the NoPMsBot** `docker-compose` YAML file:
  - ```wget https://raw.githubusercontent.com/SpEcHiDe/NoPMsBot/master/docker-compose.yml```

- **start the bot**: ```docker-compose up -d```

- The bot should be running now. Check logs with ```docker-compose logs -f```


## Credits, and Thanks to

* [ThankTelegram](https://telegram.dog/ThankTelegram)
* [Dan Tès](https://telegram.dog/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)
