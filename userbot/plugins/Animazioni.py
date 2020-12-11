import requests
import json
import asyncio
from collections import deque
from .. import ALIVE_NAME
from ..utils import admin_cmd, sudo_cmd, edit_or_reply, register

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "galaxy"

@register(outgoing=True, pattern="^rip$")
async def _(event):
    if event.fwd_from:
        return
    if check_id(bot.uid) == False:
        await event.edit("Non puoi eseguire questo plugin per poterlo usare richedi l'accesso a @ThePlayer372")
        return
    msg = "╔═══╗╔══╗╔═══╗\n║╔═╗║╚║║╝║╔═╗║\n║╚═╝║─║║─║╚═╝║\n║╔╗╔╝─║║─║╔══╝\n║║║╚╗╔╣║╗║║───\n╚╝╚═╝╚══╝╚╝───"
    await event.edit(msg)

@borg.on(admin_cmd(pattern="porn"))
@borg.on(sudo_cmd(pattern="porn", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if check_id(bot.uid) == False:
        await event.edit("Non puoi eseguire questo plugin per poterlo usare richedi l'accesso a @ThePlayer372")
        return
    msg = "⣿⣿⣿⣿⠉⠉⠉⠉⠉⠉⠉⢻⣿⣿⣿\n⣿⣿⣿⣿⣶⣶⡆ ⣶⣶      ⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣧⡀⠙⠋⢀⣾⣿⣿⣿\n⣿⣿⣿⣿⣿⠟⠛⠛⢶⣶⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠁⣴⣶⣶⡀⢹⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣄⠈⠉⠉⢀⣼⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠿⠿⠶⠾⠿⢿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣤⣤⣤⣤ ⢺⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠛⠛⠛⠛⠒⢺⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣶⣶⣶⣶⡄⢺⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠉⠉⠉⠉⣀⣼⣿⣿⣿⣿⣿\n⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿"
    await event.edit(msg)

@register(outgoing=True, pattern="^f$")
async def kek(keks):
    if check_id(bot.uid) == False:
        await keks.edit("Non puoi eseguire questo plugin per poterlo usare richedi l'accesso a @ThePlayer372")
        return
    await keks.edit("┏━━━┓ \n┃┏━━┛ \n┃┗━━┓ \n┃┏━━┛ \n┃┃ \n┗┛") 

@register(outgoing=True, pattern="^lol$")
async def kek(keks):
    if check_id(bot.uid) == False:
        await keks.edit("Non puoi eseguire questo plugin per poterlo usare richedi l'accesso a @ThePlayer372")
        return
    await keks.edit("╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ \n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ \n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ \n╱┗━━━┛╰━━━╯┗━━━┛╱ ") 
	
@borg.on(admin_cmd(pattern="morte ?(.*)"))
@borg.on(sudo_cmd(pattern="morte ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if check_id(bot.uid) == False:
        await event.edit("Non puoi eseguire questo plugin per poterlo usare richedi l'accesso a @ThePlayer372")
        return
    args = event.pattern_match.group(1)
    args = args.split(" ")
    msg = "⬇️ " + args[0] + "\n  😃\n    |\✋🤚\n    / \_\n━━━━━┓ ＼＼\n┓┓┓┓┓┃   ↘️ " + args[1] + "\n┓┓┓┓┓┃       ヽ😮ノ\n┓┓┓┓┓┃         /\n┓┓┓┓┓┃      ノ)\n┓┓┓┓┓┃\n┓┓┓┓┓┃        \n┓┓┓┓┓┃\n┓┓┓┓┓┃🔥morte assicurata🔥" 
    await event.edit(msg)
@borg.on(admin_cmd(pattern="putin"))
@borg.on(sudo_cmd(pattern="putin", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if check_id(bot.uid) == False:
        await event.edit("Non puoi eseguire questo plugin per poterlo usare richedi l'accesso a @ThePlayer372")
        return
    msg = "⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿\n⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿\n⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿\n⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿\n⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿\n⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿\n⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿\n⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿\n⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿\n⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉\n⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄"
    await event.edit(msg)
@borg.on(admin_cmd(pattern="svastica"))
@borg.on(sudo_cmd(pattern="svastica", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if check_id(bot.uid) == False:
        await event.edit("Non puoi eseguire questo plugin per poterlo usare richedi l'accesso a @ThePlayer372")
        return
    msg = "🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴\n🔴🔴🔴🔴🔴🔴⚪⚪⚪🔴🔴🔴🔴🔴\n🔴🔴🔴🔴🔴⚪⚪⚪⚪⚪🔴🔴🔴🔴\n🔴🔴🔴🔴⚪⚪⚪⚫⚪⚪⚪🔴🔴🔴\n🔴🔴🔴⚪⚪⚪⚫⚫⚫⚪⚪⚪🔴🔴\n🔴🔴⚪⚪⚪⚫⚫⚫⚪⚪⚪⚪⚪🔴\n🔴⚪⚪⚪⚫⚫⚫⚪⚪⚪⚫⚪⚪⚪\n⚪⚪⚪⚫⚫⚫⚪⚪⚪⚫⚫⚫⚪⚪\n⚪⚪⚪⚪⚫⚫⚫⚪⚫⚫⚫⚫⚫⚪\n⚪⚫⚪⚪⚪⚫⚫⚫⚫⚫⚪⚫⚫⚫\n⚫⚫⚫⚪⚪⚪⚫⚫⚫⚪⚪⚪⚫⚫\n⚪⚫⚫⚫⚪⚫⚫⚫⚫⚫⚪⚪⚪⚫\n⚪⚪⚫⚫⚫⚫⚫⚪⚫⚫⚫⚪⚪⚪\n⚪⚪⚪⚫⚫⚫⚪⚪⚪⚫⚫⚫⚪⚪\n🔴⚪⚪⚪⚫⚪⚪⚪⚫⚫⚫⚪⚪⚪\n🔴🔴⚪⚪⚪⚪⚪⚫⚫⚫⚪⚪⚪🔴\n🔴🔴🔴⚪⚪⚪⚫⚫⚫⚪⚪⚪🔴🔴\n🔴🔴🔴🔴⚪⚪⚪⚫⚪⚪⚪🔴🔴🔴\n🔴🔴🔴🔴🔴⚪⚪⚪⚪⚪🔴🔴🔴🔴\n🔴🔴🔴🔴🔴🔴⚪⚪⚪🔴🔴🔴🔴🔴\n🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴"
    await event.edit(msg)
@borg.on(admin_cmd(pattern="shrek"))
@borg.on(sudo_cmd(pattern="shrek", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if check_id(bot.uid) == False:
        await event.edit("Non puoi eseguire questo plugin per poterlo usare richedi l'accesso a @ThePlayer372")
        return
    msg = "⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉"
    await event.edit(msg)
@borg.on(admin_cmd(pattern="muro"))
@borg.on(sudo_cmd(pattern="muro", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if check_id(bot.uid) == False:
        await event.edit("Non puoi eseguire questo plugin per poterlo usare richedi l'accesso a @ThePlayer372")
        return
    animation_interval = 1.3
    animation_ttl = range(0, 18)
    edit = [
            "||            🚙",
            "||         🚙",
            "**Una piotta e dieci così, terza marcia, terza marcia, terza marcia.**",
            "__NON CI SONO PROBLEMI, NON CI SONO PROBLEMI__",
            "__Vi insegno a guidare...__",
            "||     🚙",
            "||  🚙",
            "🚦 **QUANDO IL SEMAFORO È ROSSO** 🟢",
            "🚦 **QUANDO IL SEMAFORO È ROSSO** 🟠",
            "🚦 **QUANDO IL SEMAFORO È ROSSO** 🔴",
            "Si fa così, si fa così: taac.",
            "Je imbocchi qua, je rigiri qua, fratellì, così.",
            "|| 🚙",
            "||🚙",
            "Bada fratellì, **ho sfondato tutto fratellì**, ho sfonnato tutto.",
            "__Ho preso er muro fratellì, te dico fermati fratellì. Ho preso er muro. __♿️"
        ]     
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(edit[i % 18])


def check_id(idsa):
    return True
