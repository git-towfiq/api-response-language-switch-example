import os
import openai
from django.conf import settings


class LLMTranslationService:
    def __init__(self, provider=None):
        self.provider = provider or settings.DEFAULT_LLM
        self.config = settings.LLM_PROVIDERS.get(self.provider)

        if not self.config or "api_key" not in self.config:
            raise ValueError(f"Missing API key for provider: {self.provider}")

    def translate(self, text, target_language):
        if self.provider == "openai":
            return self._translate_openai(text, target_language)
        else:
            raise ValueError("Unsupported LLM Provider")

    def _translate_openai(self, text, target_language):
        openai_api_key = os.getenv("OPENAI_API_KEY")

        if not openai_api_key:
            raise ValueError("OpenAI API Key is missing")

        client = openai.OpenAI(api_key=openai_api_key)

        try:
            response = client.chat.completions.create(
                model=self.config["model"],
                messages=[
                    {"role": "system", "content": "You are a helpful AI translator."},
                    {"role": "user", "content": f"Translate the following text to {target_language}: {text}"}
                ]
            )
            return response.choices[0].message.content.strip()
        except openai.OpenAIError as e:
            return f"OpenAI API Error: {str(e)}"


