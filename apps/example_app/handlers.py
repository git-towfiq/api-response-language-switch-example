from django.core.cache import cache
from .models import Translation
from .services import LLMTranslationService
import hashlib


def generate_cache_key(key, language, llm_provider):
    raw_key = f"translation:{key}:{language}:{llm_provider}"
    return hashlib.md5(raw_key.encode()).hexdigest()  # Generates a safe hash


def get_translated_message(
        key, language, default_message=None, llm_provider='openai'
):
    """
    Fetches translation from the database, falls back to an LLM if not found.
    Uses caching for optimization.
    """
    cache_key = generate_cache_key(key, language, llm_provider)
    cached_translation = cache.get(cache_key)

    if cached_translation:
        return cached_translation  # Return cached response if available

    translation = Translation.objects.filter(key=key, language=language).first()
    if translation:
        cache.set(cache_key, translation.message, timeout=86400)  # Cache for 1 day
        return translation.message

    if default_message:
        llm_service = LLMTranslationService(provider=llm_provider)
        translated_text = llm_service.translate(default_message, language)
        cache.set(cache_key, translated_text, timeout=86400)  # Cache LLM result
        return translated_text

    return None
