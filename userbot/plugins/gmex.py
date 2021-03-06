from .sql_helper.gmex_sql import get_all_gmex, addgmex, removegmex, is_gmex
from ..utils import admin_cmd
import asyncio

@borg.on(admin_cmd(pattern="addgmex"))
async def _(event):
    if event.fwd_from:
        return
    chat_id = event.chat_id
    if is_gmex(chat_id):
        await event.edit("Gruppo "+str(chat_id)+" già aggiunto")
        await asyncio.sleep(2)
        await event.delete()
    else:
        addgmex(chat_id)
        await event.edit("Gruppo "+str(chat_id)+" aggiunto con successo")
        await asyncio.sleep(2)
        await event.delete() 

@borg.on(admin_cmd(pattern="gmex (.*)"))
async def _(event):
    if event.fwd_from:
        return
    groups = get_all_gmex()
    msg = event.pattern_match.group(1)
    await event.delete() 
    for x in groups:
        try:
            ids = int(x.chat_id)
            await event.client.send_message(ids, msg)
        except Exception as e:
            pass

@borg.on(admin_cmd(pattern="rmgmex"))
async def _(event):
    if event.fwd_from:
        return
    chat_id = event.chat_id
    if is_gmex(chat_id) == None:
        await event.edit("Gruppo "+str(chat_id)+" mai aggiunto")
        await asyncio.sleep(2)
        await event.delete()
    else:
        removegmex(chat_id)
        await event.edit("Gruppo "+str(chat_id)+" rimosso con successo")
        await asyncio.sleep(2)
        await event.delete()
    
@borg.on(admin_cmd(pattern="listgmex"))
async def _(event):
    if event.fwd_from:
        return
    msg = "Gruppi con gmex attivo:\n"
    groups = get_all_gmex()
    if groups:
        for x in groups:
            ids = x.chat_id
            msg = msg + str(ids)+"\n"
    else:
        msg = "Nessun gruppo inserito"
    await event.edit(msg)
