import asyncio

import requests
from telethon import functions

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import ALIVE_NAME, CMD_HELP, CMD_LIST, SUDO_LIST

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "galaxy"

HELPTYPE = Config.HELP_INLINETYPE or True


@bot.on(admin_cmd(outgoing=True, pattern="help ?(.*)"))
async def cmd_list(event):
    global HELPTYPE
    reply_to_id = None
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    input_str = event.pattern_match.group(1)
    if input_str == "text":
        string = "{count} comandi trovati in {plugincount} plugin di GalaxyUserbot\n\n"
        catcount = 0
        plugincount = 0
        for i in sorted(CMD_LIST):
            plugincount += 1
            string += f"{plugincount}) comandi trovati " + i + "\n"
            for iter_list in CMD_LIST[i]:
                string += "    " + str(iter_list)
                string += "\n"
                catcount += 1
            string += "\n"
        if len(string) > 4095:
            data = string.format(count=catcount, plugincount=plugincount)
            key = (
                requests.post(
                    "https://nekobin.com/api/documents", json={"content": data}
                )
                .json()
                .get("result")
                .get("key")
            )
            url = f"https://nekobin.com/{key}"
            reply_text = f"**Tutti i comandi possono essere trovati qui [here]({url})**"
            await event.edit(reply_text)
            return
        await event.edit(string.format(count=catcount, plugincount=plugincount))
        return
    if input_str:
        if input_str in CMD_LIST:
            string = "<b>{count} comandi trovati in {input_str}:</b>\n\n"
            catcount = 0
            for i in CMD_LIST[input_str]:
                string += f"  ◆  <code>{i}</code>"
                string += "\n"
                catcount += 1
            await event.edit(
                string.format(count=catcount, input_str=input_str), parse_mode="HTML"
            )
        else:
            await event.edit(input_str + " plugin non trovato")
            await asyncio.sleep(3)
            await event.delete()
    else:
        if HELPTYPE is True:
            help_string = f"Userbot creato da ThePlayer372\
                          \n__Fai__ `.help` __nome del plugin per ottenere i comandi.__"
            tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername, help_string
            )
            await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
            await event.delete()
        else:
            string = "<b>Perfavore specifica il nome del plugin\
                \nPlugin attivi: </b><code>{count}</code>\
                \n<b>Usa:</b> <code>.help</code> nome plugin\n\n"
            catcount = 0
            for i in sorted(CMD_LIST):
                string += "◆" + f"<code>{str(i)}</code>"
                string += "   "
                catcount += 1
            await event.edit(string.format(count=catcount), parse_mode="HTML")

@bot.on(admin_cmd(outgoing=True, pattern="setinline (true|false)"))
async def _(event):
    global HELPTYPE
    input_str = event.pattern_match.group(1)
    if input_str == "true":
        type = True
    else:
        type = False
    if HELPTYPE is True:
        if type is True:
            await event.edit("`Inline mode già attiva`")
        else:
            HELPTYPE = type
            await event.edit("`Inline mode disattivata`")
    else:
        if type is True:
            HELPTYPE = type
            await event.edit("`Inline mode attiva`")
        else:
            await event.edit("`Inline mode già disattiva`")
