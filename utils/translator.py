# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from deep_translator import GoogleTranslator
from langdetect import detect

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def detect_language(text: str) -> str:
    """
    Detect the language of the given text.
    Returns language code (e.g. 'en', 'hi', 'fr').
    """
    try:
        return detect(text)
    except Exception:
        return "auto"

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def translate_text(
    text: str,
    target_language: str = "en"
):
    """
    Detect source language and translate text.
    Returns:
    (translated_text, source_lang, target_lang)
    """

    try:
        source_lang = detect_language(text)

        translated = GoogleTranslator(
            source="auto",
            target=target_language
        ).translate(text)

        return (
            translated,
            source_lang,
            target_language
        )

    except Exception:
        return (
            "❌ Translation failed.",
            "unknown",
            target_language
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def get_supported_languages():
    """
    Returns supported languages dictionary.
    """

    return GoogleTranslator().get_supported_languages(as_dict=True)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #