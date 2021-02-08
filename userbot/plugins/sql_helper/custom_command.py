from sqlalchemy import Column, String

from userbot.plugins.sql_helper import BASE, SESSION

class CMD(BASE):
    __tablename__ = "custom_command"
    command = Column(String(14), primary_key=True)
    msg = Column(String(127))

    def __init__(self, command, msg):
        self.chat_id = chat_id
        self.reason = reason


CMD.__table__.create(checkfirst=True)


def addCommand(command, msg):
    adder = CMD(str(command), str(msg))
    SESSION.add(adder)
    SESSION.commit()

def delCommand(command):
    rem = SESSION.query(CMD).get(str(command))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()

def getCommand(command):
    try:
        return SESSION.query(CMD).filter(CMD.command == str(command)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()
