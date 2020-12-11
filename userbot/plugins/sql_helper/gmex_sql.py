from sqlalchemy import Column, String

from userbot.plugins.sql_helper import BASE, SESSION


class GMEX(BASE):
    __tablename__ = "gmex"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)


GMEX.__table__.create(checkfirst=True)


def is_gmex(chat_id, category):
    try:
        return SESSION.query(GMEX).get(str(chat_id))
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_all_gmex():
    try:
        return SESSION.query(GMEX).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def addgmex(chat_id, category):
    try:
        adder = GMEX(str(chat_id))
        SESSION.add(adder)
        SESSION.commit()
    except Exception as e:
        print(str(e))


def removegmex(chat_id, category):
    note = SESSION.query(GMEX).get(str(chat_id))
    if note:
        SESSION.delete(note)
        SESSION.commit()
