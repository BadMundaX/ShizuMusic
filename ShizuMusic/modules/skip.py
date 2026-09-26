# --------------------------------------------------------------------------------
#  ShizuMusic © 2026
#  Developed by Bad Munda ❤️
#
#  Unauthorized copying, editing, re-uploading or removing credits
#  from this source code is strictly prohibited.
# --------------------------------------------------------------------------------

from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from ShizuMusic import bot
from ShizuMusic.core.player import play_song
from ShizuMusic.core.queue import peek_current, pop_current, queue_size
from ShizuMusic.modules.block import group_allowed, user_allowed
from ShizuMusic.utils.formatters import short
from ShizuMusic.utils.helpers import delete_file
from ShizuMusic.utils.permissions import is_user_authorized
from ShizuMusic.utils.rich_ui import (
    rich_edit,
    rich_esc,
    rich_heading,
    rich_kv_table,
    rich_note,
    rich_send,
)


@bot.on_message(
    filters.group
    & filters.command("skip")
    & group_allowed
    & user_allowed
)
async def skip_cmd(_, message: Message) -> None:

    chat_id = message.chat.id

    if not await is_user_authorized(message):
        await rich_send(
            bot, chat_id,
            rich_heading("⛔ ᴀᴅᴍɪɴ ᴏɴʟʏ", level=3)
            + rich_note("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ғᴏʀ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs."),
        )
        return

    if not queue_size(chat_id):
        await rich_send(
            bot, chat_id,
            rich_heading("❍ ǫᴜᴇᴜᴇ ɪs ᴇᴍᴘᴛʏ", level=3)
            + rich_note("ɴᴏ sᴏɴɢs ᴛᴏ sᴋɪᴘ."),
        )
        return

    sm = await rich_send(bot, chat_id, rich_heading("⏭ sᴋɪᴘᴘɪɴɢ ᴄᴜʀʀᴇɴᴛ ᴛʀᴀᴄᴋ...", level=3))

    skipped = pop_current(chat_id)

    try:
        delete_file(skipped.get("file_path", ""))
    except Exception:
        pass

    nxt = peek_current(chat_id)

    if not nxt:
        # queue is empty: let AutoPlay (if ON) add one related song
        try:
            from ShizuMusic.core.autoplay import autoplay_next
            if await autoplay_next(chat_id, skipped):
                nxt = peek_current(chat_id)
        except Exception:
            pass

    if nxt:
        try:
            from ShizuMusic.core.autoplay import schedule_prefetch
            schedule_prefetch(chat_id, nxt)
        except Exception:
            pass

        await rich_edit(
            sm,
            rich_heading("⏭ ᴛʀᴀᴄᴋ sᴋɪᴘᴘᴇᴅ", level=3)
            + rich_kv_table([
                ("sᴋɪᴘᴘᴇᴅ", f"<code>{rich_esc(short(skipped['title']))}</code>"),
                ("ɴᴏᴡ ᴘʟᴀʏɪɴɢ", f"<code>{rich_esc(nxt['title'])}</code>"),
            ]),
        )
        dm = await rich_send(
            bot, chat_id,
            rich_heading("❍ ɴᴇxᴛ ᴛʀᴀᴄᴋ", level=3)
            + rich_kv_table([("ᴛɪᴛʟᴇ", f"<code>{rich_esc(nxt['title'])}</code>")]),
        )
        await play_song(chat_id, dm, nxt)
    else:
        await rich_edit(
            sm,
            rich_heading("⏭ ᴛʀᴀᴄᴋ sᴋɪᴘᴘᴇᴅ", level=3)
            + rich_kv_table([("sᴋɪᴘᴘᴇᴅ", f"<code>{rich_esc(short(skipped['title']))}</code>")])
            + rich_note("ǫᴜᴇᴜᴇ ɪs ɴᴏᴡ ᴇᴍᴘᴛʏ"),
        )

