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


    response = f"""
🌍 Translation Complete

📝 Original
{text}

🔤 Detected Language
{source_lang.upper()}

🎯 Target Language
{target_lang.upper()}

✅ Translation
{translated_text}
"""

    await message.reply_text(
        response,
        quote=True
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(filters.command("history"))
async def history_command(client: Client, message: Message):

    history = db.get_history(message.from_user.id)

    if not history:
        await message.reply_text(
            "📭 No translation history found."
        )
        return

    text = "🕘 Your Recent Translations\n\n"

    for i, item in enumerate(history, start=1):

        source_text = item[0]
        translated_text = item[1]
        source_lang = item[2]
        target_lang = item[3]

        if len(source_text) > 30:
            source_text = source_text[:30] + "..."

        if len(translated_text) > 30:
            translated_text = translated_text[:30] + "..."

        text += (
            f"{i}. "
            f"{source_lang.upper()} ➜ {target_lang.upper()}\n"
            f"📝 {source_text}\n"
            f"✅ {translated_text}\n\n"
        )

    await message.reply_text(text)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(filters.command("clearhistory"))
async def clear_history(client: Client, message: Message):

    db.clear_history(message.from_user.id)

    await message.reply_text(
        "🗑️ Your translation history has been cleared."
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #