# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from database import db
from utils.translator import translate_text
from utils.keyboards import language_keyboard

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_callback_query(filters.regex("^languages$"))
async def languages_menu(client: Client, query: CallbackQuery):

    await query.message.edit_text(
        "🌍 Select your preferred language:",
        reply_markup=language_keyboard()
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_callback_query(filters.regex("^lang_"))
async def set_language(client: Client, query: CallbackQuery):

    language = query.data.replace("lang_", "")

    db.set_language(
        query.from_user.id,
        language
    )

    await query.answer(
        "✅ Language updated!",
        show_alert=True
    )

    await query.message.edit_text(
        f"✅ Preferred language set to: {language.upper()}"
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(
    filters.text &
    ~filters.command(
        [
            "start",
            "help",
            "about"
        ]
    )
)
async def translate_handler(
    client: Client,
    message: Message
):

    if not message.from_user:
        return

    text = message.text.strip()

    if not text:
        return

    target_language = db.get_language(
        message.from_user.id
    )

    translated_text, source_lang, target_lang = translate_text(
        text=text,
        target_language=target_language
    )

    db.save_translation(
        message.from_user.id,
        text,
        translated_text,
        source_lang,
        target_lang
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #