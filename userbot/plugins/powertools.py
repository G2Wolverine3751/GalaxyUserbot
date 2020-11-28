import sys
from os import execl
from time import sleep

from ..utils import admin_cmd, edit_or_reply
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot


@borg.on(admin_cmd(pattern="restart$"))
async def _(event):
    if event.fwd_from:
        return
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n" "Bot riavviato")
    await edit_or_reply(
        event,
        "Bot in riavvio testalo con .help",
    )
    await bot.disconnect()
    execl(sys.executable, sys.executable, *sys.argv)


@borg.on(admin_cmd(pattern="shutdown$"))
async def _(event):
    if event.fwd_from:
        return
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n" "Spegnimento")
    await edit_or_reply(event, "Spegnimento riaccendilo da heroku")
    await bot.disconnect()
