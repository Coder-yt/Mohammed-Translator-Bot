# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from keep_alive import keep_alive

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import handlers.start
import handlers.translate

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

app = Client(
    "TranslationBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

if __name__ == "__main__":
    print("=" * 50)
    keep_alive()
    print("🌍 Translation Bot Started Successfully")
    print("=" * 50)

    app.run()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #