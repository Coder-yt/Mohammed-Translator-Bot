# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# Popular languages
POPULAR_LANGUAGES = [
    ("🇺🇸 English", "en"),
    ("🇮🇳 Hindi", "hi"),
    ("🇮🇳 Telugu", "te"),
    ("🇮🇳 Tamil", "ta"),
    ("🇮🇳 Kannada", "kn"),
    ("🇮🇳 Malayalam", "ml"),
    ("🇪🇸 Spanish", "es"),
    ("🇫🇷 French", "fr"),
    ("🇩🇪 German", "de"),
    ("🇮🇹 Italian", "it"),
    ("🇯🇵 Japanese", "ja"),
    ("🇰🇷 Korean", "ko"),
    ("🇨🇳 Chinese", "zh-CN"),
    ("🇷🇺 Russian", "ru"),
    ("🇸🇦 Arabic", "ar"),
    ("🇵🇹 Portuguese", "pt"),
]

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def main_menu():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🌍 Translate",
                    callback_data="translate"
                )
            ],
            [
                InlineKeyboardButton(
                    "🌐 Languages",
                    callback_data="languages"
                ),
                InlineKeyboardButton(
                    "🕘 History",
                    callback_data="history"
                )
            ],
            [
                InlineKeyboardButton(
                    "⚙ Settings",
                    callback_data="settings"
                ),
                InlineKeyboardButton(
                    "ℹ About",
                    callback_data="about"
                )
            ]
        ]
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def language_keyboard():
    buttons = []

    for i in range(0, len(POPULAR_LANGUAGES), 2):
        row = []

        lang1 = POPULAR_LANGUAGES[i]
        row.append(
            InlineKeyboardButton(
                lang1[0],
                callback_data=f"lang_{lang1[1]}"
            )
        )

        if i + 1 < len(POPULAR_LANGUAGES):
            lang2 = POPULAR_LANGUAGES[i + 1]
            row.append(
                InlineKeyboardButton(
                    lang2[0],
                    callback_data=f"lang_{lang2[1]}"
                )
            )

        buttons.append(row)

    buttons.append(
        [
            InlineKeyboardButton(
                "❌ Close",
                callback_data="close"
            )
        ]
    )

    return InlineKeyboardMarkup(buttons)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #