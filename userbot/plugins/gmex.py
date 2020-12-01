from .sql_helper.gmex_sql import get_all_gmex, addgmex, removegmex, is_gmex
from ..utils import admin_cmd
import asyncio

@borg.on(admin_cmd(pattern="addgmex (.*)"))
async def _(event):
    if event.fwd_from:
        return
    chat_id = event.chat_id
    msg = event.pattern_match.group(1).strip().split(" ")[0]
    if is_gmex(chat_id, msg):
        await event.edit("Gruppo "+str(chat_id)+" già aggiunto nella lista "+msg)
        await asyncio.sleep(2)
        await event.delete()
    else:
        addgmex(chat_id, msg)
        await event.edit("Gruppo "+str(chat_id)+" aggiunto con successo alla lista "+msg)
        await asyncio.sleep(2)
        await event.delete() 

@borg.on(admin_cmd(pattern="gmex (.*)"))
async def _(event):
    if event.fwd_from:
        return
    groups = get_all_gmex()
    msg = event.pattern_match.group(1)
    category = event.pattern_match.group(1).strip().split(" ")[0]
    msg = msg.replace(category, "").strip()
    await event.delete() 
    for x in groups:
        cate = x.category.strip()
        ids = int(x.chat_id.strip())
        if str(cate) == str(category).strip():
            await event.client.send_message(ids, msg)

@borg.on(admin_cmd(pattern="rmgmex (.*)"))
async def _(event):
    if event.fwd_from:
        return
    chat_id = event.chat_id
    msg = event.pattern_match.group(1).strip().split(" ")[0]
    if is_gmex(chat_id) == None:
        await event.edit("Gruppo "+str(chat_id)+" mai aggiunto nella lista "+msg)
        await asyncio.sleep(2)
        await event.delete()
    else:
        removegmex(chat_id, msg)
        await event.edit("Gruppo "+str(chat_id)+" rimosso con successo dalla lista "+msg)
        await asyncio.sleep(2)
        await event.delete()
    
@borg.on(admin_cmd(pattern="listgmex"))
async def _(event):
    if event.fwd_from:
        return
    msg = "Gruppi con gmex attivo:\n"
    for x in groups:
        cate = x.category
        ids = x.chat_id
        msg = msg + str(ids)+": "+str(cate)+"\n"
    if msg == "Gruppi con gmex attivo:\n":
        msg = "Nessun gruppo con gmex attivo"
    await event.edit(msg)
