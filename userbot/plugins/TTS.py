from ..utils import admin_cmd

from .. import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "galaxy"

@borg.on(admin_cmd(pattern="tts"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            reply = await event.get_reply_message()
            results = await bot.inline_query("TTSBot", reply.message)
            reply_to_id = event.reply_to_msg_id
            await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
            await event.delete()
        except Exception as e:
            await event.edit(str(e))
