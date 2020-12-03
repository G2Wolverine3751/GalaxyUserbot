from ..utils import admin_cmd
import asyncio
from telethon import events, functions
from .sql_helper.pmsecurity_sqld import add, is_in, rm_all, remove
from .sql_helper.pmpermit_sql import approve, disapprove, is_approved

@borg.on(admin_cmd(pattern="a"))
async def _(event):
    if event.fwd_from:
        return
    approve(event.chat_id, "Approvato da te")
    remove(event.chat_id)
    await event.edit("Approvato")
    
@borg.on(admin_cmd(pattern="dall"))
async def _(event):
    if event.fwd_from:
        return
    rm_all()
    await event.edit("Disapprovati tutti")

@bot.on(events.NewMessage(incoming=True))
async def onMessage(event):
    if event.sender_id == event.client.uid:
        if is_approved(event.chat_id) == None:
            approve(event.chat_id, "")
        return
    if not event.is_private:
        return
    if is_approved(event.chat_id):
        return
    if is_in(event.sender_id):
        await event.delete()
        return
    chat_id = event.sender_id
    add(chat_id)
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER
    results = await bot.inline_query(tgbotusername, "**Security")
    await results[0].click(event.chat_id, hide_via=True)
    
    
