from ..utils import admin_cmd

@bot.on(admin_cmd(pattern="spam ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    num = event.pattern_match.group(1).strip().split(" ")[0]
    msg = event.pattern_match.group(1).replace(str(num), "")
    chat_id = event.chat_id
    for x in range(0, int(num)):
        try:
            await event.client.send_message(chat_id, msg)
        except:
            break
