# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import sqlite3
from config import DATABASE_NAME

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(
            DATABASE_NAME,
            check_same_thread=False
        )
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            username TEXT,
            language TEXT DEFAULT 'en'
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            source_text TEXT,
            translated_text TEXT,
            source_lang TEXT,
            target_lang TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

    # -------------------------
    # Users
    # -------------------------

    def add_user(self, user_id, first_name, username):
        self.cursor.execute("""
        INSERT OR IGNORE INTO users
        (user_id, first_name, username)
        VALUES (?, ?, ?)
        """, (
            user_id,
            first_name,
            username
        ))
        self.conn.commit()

    def set_language(self, user_id, language):
        self.cursor.execute("""
        UPDATE users
        SET language=?
        WHERE user_id=?
        """, (
            language,
            user_id
        ))
        self.conn.commit()

    def get_language(self, user_id):
        self.cursor.execute("""
        SELECT language
        FROM users
        WHERE user_id=?
        """, (user_id,))
        row = self.cursor.fetchone()

        if row:
            return row[0]

        return "en"

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

    # -------------------------
    # History
    # -------------------------

    def save_translation(
        self,
        user_id,
        source_text,
        translated_text,
        source_lang,
        target_lang
    ):
        self.cursor.execute("""
        INSERT INTO history(
            user_id,
            source_text,
            translated_text,
            source_lang,
            target_lang
        )
        VALUES (?, ?, ?, ?, ?)
        """, (
            user_id,
            source_text,
            translated_text,
            source_lang,
            target_lang
        ))
        self.conn.commit()

    def get_history(self, user_id, limit=10):
        self.cursor.execute("""
        SELECT
        source_text,
        translated_text,
        source_lang,
        target_lang,
        created_at
        FROM history
        WHERE user_id=?
        ORDER BY id DESC
        LIMIT ?
        """, (
            user_id,
            limit
        ))

        return self.cursor.fetchall()

    def clear_history(self, user_id):
        self.cursor.execute("""
        DELETE FROM history
        WHERE user_id=?
        """, (user_id,))
        self.conn.commit()


db = Database()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #