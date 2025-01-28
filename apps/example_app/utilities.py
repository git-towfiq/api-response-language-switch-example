import os
import openai
from django.conf import settings

# Load OpenAI API Key from settings or .env
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OpenAI API Key is missing")

# Initialize OpenAI client properly
client = openai.OpenAI(api_key=openai_api_key)


def translate_using_llm(text, target_language):
    try:
        response = client.chat.completions.create(
            model=settings.LLM_PROVIDERS["openai"]["model"],
            messages=[
                {"role": "system", "content": "You are a helpful AI translator."},
                {"role": "user", "content": f"Translate the following text to {target_language}: {text}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except openai.OpenAIError as e:
        return f"OpenAI API Error: {str(e)}"





