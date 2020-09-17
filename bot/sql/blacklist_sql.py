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

""" blacklist Table """

from pyrogram.types import Message
from sqlalchemy import (
    Column,
    String,
    UnicodeText
)
from . import (
    SESSION,
    BASE
)


class BlackList(BASE):
    """ table to store BANned users """
    __tablename__ = "blacklist"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(UnicodeText)

    def __init__(self, chat_id, reason):
        self.chat_id = str(chat_id)  # ensure string
        self.reason = reason

    def __repr__(self):
        return "<BL %s>" % self.chat_id


BlackList.__table__.create(checkfirst=True)


def add_user_to_bl(chat_id: int, reason: str):
    """ add the user to the blacklist """
    __user = BlackList(str(chat_id), reason)
    SESSION.add(__user)
    SESSION.commit()


def check_is_black_list(message: Message):
    """ check if user_id is blacklisted """
    if message and message.from_user and message.from_user.id:
        try:
            s__ = SESSION.query(BlackList).get(str(message.from_user.id))
            return s__
        finally:
            SESSION.close()


def rem_user_from_bl(chat_id: int):
    """ remove the user from the blacklist """
    s__ = SESSION.query(BlackList).get(str(chat_id))
    if s__:
        SESSION.delete(s__)
        SESSION.commit()
        return True
    SESSION.close()
    return False
