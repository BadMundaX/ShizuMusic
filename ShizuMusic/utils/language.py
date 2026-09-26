# --------------------------------------------------------------------------------
#  ShizuMusic © 2026
#  Developed by Bad Munda ❤️
#
#  Unauthorized copying, editing, re-uploading or removing credits
#  from this source code is strictly prohibited.
# --------------------------------------------------------------------------------

from ShizuMusic.strings import DEFAULT_LANG, get_string
from ShizuMusic.utils.db import get_chat_lang


def chat_strings(chat_id: int) -> dict:
    """This chat's chosen language strings (falls back to English)."""
    try:
        lang = get_chat_lang(chat_id)
    except Exception:
        lang = DEFAULT_LANG
    return get_string(lang)
