"""AFK Plugin for @UniBorg
Syntax: .afk REASON"""
import asyncio
import datetime
from datetime import datetime
from telethon import events
from telethon.tl import functions, types
from userbot import CMD_HELP
from userbot.utils import admin_cmd

global USER_AFK  
global afk_time  
global last_afk_message  
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}

@borg.on(events.NewMessage(outgoing=True))  
async def set_not_afk(event):
    global USER_AFK  
    global afk_time  
    global last_afk_message  
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:
        USER_AFK = {}  
        afk_time = None  


@borg.on(events.NewMessage(
    incoming=True,
    func=lambda e: bool(e.mentioned or e.is_private)
))
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        return False
    if USER_AFK and not (await event.get_sender()).bot:  
        msg = None
        message_to_reply = f"Il mio capo in questo momento non è disponibile ti contatterà appena lo sarà" \
            if reason \
            else f"Il mio capo in questo momento non è disponibile ti contatterà appena lo sarà "
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_afk_message:  
            await last_afk_message[event.chat_id].delete()  
        last_afk_message[event.chat_id] = msg  


@borg.on(admin_cmd(pattern=r"afk ?(.*)", outgoing=True))  
async def _(event):
    if event.fwd_from:
        return
    global USER_AFK  
    global afk_time  
    global last_afk_message  
    global afk_start
    global afk_end
    global reason
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    if not USER_AFK:  
        last_seen_status = await borg(  
            functions.account.GetPrivacyRequest(
                types.InputPrivacyKeyStatusTimestamp()
            )
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  
        USER_AFK = f"yes: {reason}"  
        if reason:
            await event.edit(event.chat_id, f"Sto andando afk")
        else:
            await event.edit(event.chat_id, f"Sto andando afk")
