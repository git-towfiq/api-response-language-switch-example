from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from apps.example_app.handlers import get_translated_message


class TranslationMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if 'lang' in request.GET:
            language = request.GET['lang']
            llm_provider = request.GET.get('llm_provider', 'openai')  # Default to OpenAI if not specified

            if isinstance(response, JsonResponse):
                data = response.json()
                if 'message' in data:
                    data['message'] = get_translated_message(
                        data['message'], language, data['message'], llm_provider
                    )
                    return JsonResponse(data)

        return response
