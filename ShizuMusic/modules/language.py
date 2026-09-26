# --------------------------------------------------------------------------------
#  ShizuMusic © 2026
#  Developed by Bad Munda ❤️
#
#  Unauthorized copying, editing, re-uploading or removing credits
#  from this source code is strictly prohibited.
# --------------------------------------------------------------------------------
#
#  /language — pick the bot's reply language for this chat.
#  Add a new language by dropping a file in strings/langs/ — see that
#  folder's __init__.py for how. No code change needed for it to show up.
# --------------------------------------------------------------------------------

from pyrogram import filters
from pyrogram.types import CallbackQuery, Message

from ShizuMusic import bot
from ShizuMusic.modules.block import group_allowed, user_allowed
from ShizuMusic.strings import languages_present
from ShizuMusic.utils.buttons import language_kb
from ShizuMusic.utils.db import get_chat_lang, set_chat_lang
from ShizuMusic.utils.language import chat_strings
from ShizuMusic.utils.permissions import is_user_authorized
from ShizuMusic.utils.rich_ui import rich_heading, rich_note, rich_send, rich_edit


@bot.on_message(
    filters.group
    & filters.command(["language", "setlang", "lang"])
    & group_allowed
    & user_allowed
)
async def language_cmd(_, message: Message) -> None:
    chat_id = message.chat.id
    lang = chat_strings(chat_id)

    current = get_chat_lang(chat_id)
    await rich_send(
        bot, chat_id,
        rich_heading("🌐 ʟᴀɴɢᴜᴀɢᴇ", level=3)
        + rich_note(lang["lang_1"]),
        reply_markup=language_kb(languages_present, current),
    )


@bot.on_callback_query(filters.regex(r"^setlang:(.+)$"))
async def language_cb(_, cbq: CallbackQuery) -> None:
    chat_id = cbq.message.chat.id
    lang = chat_strings(chat_id)

    if not await is_user_authorized(cbq):
        await cbq.answer(lang["lang_5"], show_alert=True)
        return

    code = cbq.data.split(":", 1)[1]

    if code not in languages_present:
        await cbq.answer(lang["lang_3"], show_alert=True)
        return

    if code == get_chat_lang(chat_id):
        await cbq.answer(lang["lang_4"], show_alert=True)
        return

    set_chat_lang(chat_id, code)
    new_lang = chat_strings(chat_id)   # re-read: text below is now in the NEW language

    await cbq.answer(new_lang["lang_2"], show_alert=True)

    try:
        await rich_edit(
            cbq.message,
            rich_heading("🌐 ʟᴀɴɢᴜᴀɢᴇ", level=3)
            + rich_note(new_lang["lang_1"]),
            reply_markup=language_kb(languages_present, code),
        )
    except Exception:
        pass
