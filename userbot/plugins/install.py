import asyncio
import os
from datetime import datetime
from pathlib import Path

from .. import ALIVE_NAME
from ..utils import admin_cmd, edit_or_reply, load_module, remove_plugin, sudo_cmd

DELETE_TIMEOUT = 5
thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@borg.on(admin_cmd(pattern="install$"))
@borg.on(sudo_cmd(pattern="install$", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit(
                    "Plugin `{}` installato".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await event.edit("Errore questo plugin è già installato")
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@borg.on(admin_cmd(pattern=r"send (?P<shortname>\w+)$", outgoing=True))
@borg.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)$", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    reply_to_id = None
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        caat = await event.client.send_file(  # pylint:disable=E0602
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            thumb=thumb,
        )
        end = datetime.now()
        (end - start).seconds
        await event.delete()
        await caat.edit(
            f"__**➥ Plugin:- {input_str} .**__\n__➥ Inviato da :-**__ {DEFAULTUSER}"
        )
    else:
        await edit_or_reply(event, "Plugin non trovato")


@borg.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$", outgoing=True))
@borg.on(sudo_cmd(pattern=r"unload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"Plugin {shortname} disabilitato ")
    except Exception as e:
        await edit_or_reply(
            event, "Plugin {shortname} disabilitato".format(shortname, str(e))
        )


@borg.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$", outgoing=True))
@borg.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await edit_or_reply(event, f"Plugin {shortname} abilitare con successo")
    except Exception as e:
        await edit_or_reply(
            event,
            f"Impossibile abilitare il plugin {shortname}:\n{str(e)}",
        )
