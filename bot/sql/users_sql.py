from sqlalchemy import (
    Column, String, Boolean, UnicodeText, Integer, func, distinct
)

from bot.sql import (
    SESSION,
    BASE
)


class Users(BASE):
    __tablename__ = "users"
    message_id = Column(Integer, primary_key=True)
    chat_id = Column(String(14))
    um_id = Column(Integer)

    def __init__(self, message_id, chat_id, um_id):
        self.message_id = message_id
        self.chat_id = str(chat_id)  # ensure string
        self.um_id = um_id


    def __repr__(self):
        return "<User %s>" % self.chat_id


Users.__table__.create(checkfirst=True)


def add_user_to_db(message_id, chat_id, um_id):
    __user = Users(message_id, str(chat_id), um_id)
    SESSION.add(__user)
    SESSION.commit()


def get_user_id(message_id):
    try:
        s__ = SESSION.query(Users).get(str(message_id))
        return int(s__.chat_id), s__.um_id
    finally:
        SESSION.close()
