from sqlalchemy import Column, String

from userbot.plugins.sql_helper import BASE, SESSION


class PMPermits(BASE):
    __tablename__ = "pmpermits"
    user_id = Column(String(127), primary_key=True)

    def __init__(self, user_id):
        self.user_id = str(user_id)


PMPermits.__table__.create(checkfirst=True)


def is_in(user_id):
    try:
        return SESSION.query(PMPermits).get(str(user_id))
    except BaseException:
        return None
    finally:
        SESSION.close()


def add(user_id):
    adder = PMPermits(str(user_id))
    SESSION.add(adder)
    SESSION.commit()


def remove(user_id):
    rem = SESSION.query(PMPermits).get(str(user_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_add():
    rem = SESSION.query(PMPermits).all()
    SESSION.close()
    return rem
