import sys
from os import execl

from ..utils import admin_cmd, edit_or_reply
from . import BOTLOG, BOTLOG_CHATID, bot


@borg.on(admin_cmd(pattern="restart$"))
async def _(event):
    if event.fwd_from:
        return
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n" "Bot riavviato")
    await event.edit("Bot in riavvio testalo con .help")
    await bot.disconnect()
    execl(sys.executable, sys.executable, *sys.argv)


@borg.on(admin_cmd(pattern="shutdown$"))
async def _(event):
    if event.fwd_from:
        return
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n" "Spegnimento")
    await event.edit("Spegnimento riaccendilo da heroku")
    await bot.disconnect()
