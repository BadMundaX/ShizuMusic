# --------------------------------------------------------------------------------
#  ShizuMusic © 2026
#  Developed by Bad Munda ❤️
#
#  Unauthorized copying, editing, re-uploading or removing credits
#  from this source code is strictly prohibited.
# --------------------------------------------------------------------------------
#
#  ALL inline keyboards used across the bot live here — one place to add,
#  rename or restyle a button instead of hunting through every module.
# --------------------------------------------------------------------------------

from typing import Optional

from pyrogram import enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from ShizuMusic.utils.formatters import progress_bar


# ═════════════════════════════════════════════════════════════════════════════
# PLAYER CONTROLS  (now-playing message + /seek result)
# ═════════════════════════════════════════════════════════════════════════════
def player_controls_kb(elapsed: float, total: float) -> InlineKeyboardMarkup:
    """▷ / II / skip / stop, with the progress bar as its own (no-op) row."""
    bar = progress_bar(elapsed, total)
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(bar, callback_data="noop")],
        [
            InlineKeyboardButton("▷", callback_data="resume"),
            InlineKeyboardButton("II", callback_data="pause"),
            InlineKeyboardButton("‣‣I", callback_data="skip"),
            InlineKeyboardButton("▢", callback_data="stop"),
        ],
    ])


# ═════════════════════════════════════════════════════════════════════════════
# QUEUE
# ═════════════════════════════════════════════════════════════════════════════
def skip_clear_kb() -> InlineKeyboardMarkup:
    """Shown under 'Added to queue' when a song lands behind another one."""
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("⌯ sᴋɪᴘ ⌯", callback_data="skip"),
        InlineKeyboardButton("⌯ ᴄʟᴇᴀʀ ⌯", callback_data="clear"),
    ]])


# ═════════════════════════════════════════════════════════════════════════════
# SUPPORT / REPO
# ═════════════════════════════════════════════════════════════════════════════
def support_kb() -> InlineKeyboardMarkup:
    """Single 'Support' button (used by /ping)."""
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("🍬 sᴜᴘᴘᴏʀᴛ 🍬", url=config.SUPPORT_GROUP),
    ]])


def repo_kb(source_url: str) -> InlineKeyboardMarkup:
    """Source / Fork / Support / Updates grid (used by /repo)."""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🍡 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🍡", url=source_url, style=enums.ButtonStyle.PRIMARY),
            InlineKeyboardButton("🔱 ғᴏʀᴋ 🔱", url=source_url, style=enums.ButtonStyle.PRIMARY),
        ],
        [
            InlineKeyboardButton("🍬 sᴜᴘᴘᴏʀᴛ 🍬", url=config.SUPPORT_GROUP, style=enums.ButtonStyle.SUCCESS),
            InlineKeyboardButton("🍹 ᴜᴘᴅᴀᴛᴇs 🍹", url=config.UPDATES_CHANNEL, style=enums.ButtonStyle.SUCCESS),
        ],
    ])


# ═════════════════════════════════════════════════════════════════════════════
# ADMIN INVITE  (new group / manual admin-request retry)
# ═════════════════════════════════════════════════════════════════════════════
def make_admin_kb(bot_id: int, styled: bool = False) -> InlineKeyboardMarkup:
    """'⚡ Make me admin ⚡' — deep-links straight to the bot's profile."""
    btn = InlineKeyboardButton(
        "⚡ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ⚡",
        url=f"tg://user?id={bot_id}",
        **({"style": enums.ButtonStyle.DANGER} if styled else {}),
    )
    return InlineKeyboardMarkup([[btn]])


def added_by_kb(user_id: int, user_name: str) -> InlineKeyboardMarkup:
    """Small '👤 <name>' button used on the new-group log card."""
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(f"👤 {user_name}", user_id=user_id),
    ]])


# ═════════════════════════════════════════════════════════════════════════════
# /start
# ═════════════════════════════════════════════════════════════════════════════
def start_private_kb() -> InlineKeyboardMarkup:
    """Full 4-row panel shown on /start in a private chat."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "⛩️ ᴧᴅᴅ мᴇ ʙᴧʙʏ ⛩️",
            url=f"{config.BOT_LINK}?startgroup=true",
            style=enums.ButtonStyle.PRIMARY,
        )],
        [
            InlineKeyboardButton("🍬 sᴜᴘᴘᴏʀᴛ 🍬", url=config.SUPPORT_GROUP, style=enums.ButtonStyle.SUCCESS),
            InlineKeyboardButton("🍹 ᴜᴘᴅᴀᴛᴇs 🍹", url=config.UPDATES_CHANNEL, style=enums.ButtonStyle.SUCCESS),
        ],
        [InlineKeyboardButton(
            "🏩 ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs 🏩",
            callback_data="show_help",
            style=enums.ButtonStyle.PRIMARY,
        )],
        [
            InlineKeyboardButton("🫧 ᴏᴡɴᴇʀ 🫧", url=f"tg://user?id={config.OWNER_ID}", style=enums.ButtonStyle.DEFAULT),
            InlineKeyboardButton("🍡 sᴏᴜʀᴄᴇ 🍡", url="https://github.com/Badmunda05/ShizuMusic/fork", style=enums.ButtonStyle.DEFAULT),
        ],
    ])


def start_group_kb() -> InlineKeyboardMarkup:
    """Short 2-row panel shown on /start inside a group."""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⛩️ ᴧᴅᴅ мᴇ ʙᴧʙʏ ⛩️", url=f"{config.BOT_LINK}?startgroup=true", style=enums.ButtonStyle.PRIMARY),
            InlineKeyboardButton("🍬 sᴜᴘᴘᴏʀᴛ 🍬", url=config.SUPPORT_GROUP, style=enums.ButtonStyle.SUCCESS),
        ],
        [InlineKeyboardButton(
            "🏩 ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs 🏩",
            callback_data="show_help",
            style=enums.ButtonStyle.PRIMARY,
        )],
    ])


# ═════════════════════════════════════════════════════════════════════════════
# HELP MENU
# ═════════════════════════════════════════════════════════════════════════════
def _help_grid_rows() -> list:
    """The 3x3 category grid shared by every /help keyboard."""
    return [
        [
            InlineKeyboardButton("ᴧᴅᴍɪɴ", callback_data="help_admin", style=enums.ButtonStyle.PRIMARY),
            InlineKeyboardButton("ᴧ-ᴘʟᴀʏ", callback_data="help_autoplay", style=enums.ButtonStyle.PRIMARY),
            InlineKeyboardButton("ɢ-ᴄᴧsᴛ", callback_data="help_gcast", style=enums.ButtonStyle.PRIMARY),
        ],
        [
            InlineKeyboardButton("ʙʟ-ᴄʜᴧᴛ", callback_data="help_blchat", style=enums.ButtonStyle.PRIMARY),
            InlineKeyboardButton("ʙʟ-ᴜsᴇʀs", callback_data="help_blusers", style=enums.ButtonStyle.PRIMARY),
            InlineKeyboardButton("ᴘɪɴɢ", callback_data="help_ping", style=enums.ButtonStyle.PRIMARY),
        ],
        [
            InlineKeyboardButton("ᴘʟᴀʏ", callback_data="help_play", style=enums.ButtonStyle.PRIMARY),
            InlineKeyboardButton("sᴘᴇᴇᴅ", callback_data="help_speed", style=enums.ButtonStyle.PRIMARY),
            InlineKeyboardButton("ɪɴғᴏ", callback_data="help_info", style=enums.ButtonStyle.PRIMARY),
        ],
    ]


def help_menu_kb() -> InlineKeyboardMarkup:
    """/help — grid + a Close button (nothing to go 'back' to yet)."""
    return InlineKeyboardMarkup(_help_grid_rows() + [
        [InlineKeyboardButton("⌯ ᴄʟᴏsᴇ ⌯", callback_data="close_help", style=enums.ButtonStyle.DANGER)],
    ])


def help_menu_home_kb() -> InlineKeyboardMarkup:
    """'show_help' callback (returning to the grid from a category) — grid + Home."""
    return InlineKeyboardMarkup(_help_grid_rows() + [
        [InlineKeyboardButton("⌯ ʜᴏᴍᴇ ⌯", callback_data="go_back", style=enums.ButtonStyle.SUCCESS)],
    ])


def help_back_kb() -> InlineKeyboardMarkup:
    """Under every category screen: Back to grid / Close."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⌯ ʙᴀᴄᴋ ⌯", callback_data="show_help", style=enums.ButtonStyle.PRIMARY)],
        [InlineKeyboardButton("⌯ ᴄʟᴏsᴇ ⌯", callback_data="close_help", style=enums.ButtonStyle.DANGER)],
    ])


# ═════════════════════════════════════════════════════════════════════════════
# /language
# ═════════════════════════════════════════════════════════════════════════════
def language_kb(languages_present: dict, current: str, row_width: int = 2) -> InlineKeyboardMarkup:
    """
    One button per language in strings/langs/ (label comes from that file's
    'name:' key), plus a Close row. The current language gets a ✓ marker.
    """
    buttons = [
        InlineKeyboardButton(
            f"✓ {name}" if code == current else name,
            callback_data=f"setlang:{code}",
        )
        for code, name in languages_present.items()
    ]
    rows = [buttons[i:i + row_width] for i in range(0, len(buttons), row_width)]
    rows.append([InlineKeyboardButton("⌯ ᴄʟᴏsᴇ ⌯", callback_data="close_help", style=enums.ButtonStyle.DANGER)])
    return InlineKeyboardMarkup(rows)
