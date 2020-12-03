from ..utils import admin_cmd
import asyncio
from telethon import events, functions
from .sql_helper.pmsecurity_sqld import add, is_in, rm_all
from .sql_helper import pmpermit_sql

@borg.on(admin_cmd(pattern="dall"))
async def _(event):
    if event.fwd_from:
        return
    rm_all()

@bot.on(events.NewMessage(incoming=True))
async def onMessage(event):
    if event.sender_id == event.client.uid:
        if pmpermit_sql.is_approved(event.chat_id) == None:
            pmpermit_sql.approve(event.chat_id, "")
        return
    if not event.is_private:
        return
    if pmpermit_sql.is_approved(event.chat_id):
        return
    if is_in(event.sender_id):
        await event.delete()
        return
    chat_id = event.sender_id
    add(chat_id)
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER
    results = await bot.inline_query(tgbotusername, "**Security")
    await results[0].click(event.chat_id, hide_via=True)
    
    
