from .sql_helper.mute_sql import is_muted, mute, unmute
from ..utils import admin_cmd
import asyncio

@bot.on(admin_cmd(outgoing=True, pattern="gmute"))
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    if reply is not None:
        userid = reply.sender_id
    elif event.is_private:
        userid = event.chat_id
    else:
        await event.edit("Rispondi al messaggio di un utente per gmutarlo")
        return
    if str(userid) == "713459844":
        await event.edit("Non puoi gmutare il mio dev")
        return
    if is_muted(userid, "gmute"):
        await event.edit("Utente già gmutato")
        return
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("C'è stato un errore.\n" + str(e))
    else:
        await event.edit("Utente gmutato")

@bot.on(admin_cmd(outgoing=True, pattern="ungmute"))
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    if reply is not None:
        userid = reply.sender_id
    elif event.is_private:
        userid = event.chat_id
    else:
        await event.edit("Rispondi al messaggio di un utente per gmutarlo")
        return
    if not is_muted(userid, "gmute"):
        return await event.edit("Questo utente non è gmutato")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("C'è stato un errore.\n" + str(e))
    else:
        await event.edit("Utente ungmutato")

@command(incoming=True)
async def _(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
