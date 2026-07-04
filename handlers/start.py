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
from utils.keyboards import main_menu

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):

    user = message.from_user

    db.add_user(
        user.id,
        user.first_name or "",
        user.username or ""
    )

    text = f"""
👋 Hello {user.mention}!

🌍 Welcome to Translation Bot.

✨ Features

• Translate 100+ languages
• Auto language detection
• Save translation history
• Works in Groups & PM
• Fast & Accurate

Choose an option below.
"""

    await message.reply_text(
        text,
        reply_markup=main_menu()
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):

    await message.reply_text(
"""
📖 Help

Commands

/start - Start Bot
/help - Help Menu
/about - About Bot

Simply send any text to translate it.

Use the Languages button to change your preferred language.
"""
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(filters.command("about"))
async def about_command(client: Client, message: Message):

    await message.reply_text(
"""
🌍 Translation Bot

👨‍💻 Developer: @Mr_Mohammed_29 
⚡ Fast Translation
🌐 100+ Languages
🤖 Auto Detect Language
💾 Translation History
👥 Group & Private Support

Made with ❤️ 
"""
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_callback_query(filters.regex("^about$"))
async def about_callback(client: Client, query: CallbackQuery):

    await query.message.edit_text(
"""
🌍 Translation Bot

Translate text instantly into 100+ languages.

Thank you for using the bot ❤️
""",
        reply_markup=main_menu()
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_callback_query(filters.regex("^close$"))
async def close_callback(client: Client, query: CallbackQuery):

    await query.message.delete()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #