from rest_framework import status
from rest_framework.response import Response
from apps.example_app.handlers import get_translated_message


class ResponseFormatter:
    @staticmethod
    def success(message, data=None, status_code=status.HTTP_200_OK, request=None, translate_fields=None):
        """Format success response with optional translation for specific fields."""
        translated_message = ResponseFormatter.translate_message(message, request)

        if data and isinstance(data, dict) and translate_fields:
            data = ResponseFormatter.translate_fields(data, request, translate_fields)

        return Response({  # ✅ Ensure Response object is returned
            "success": True,
            "statusCode": int(status_code),
            "message": str(translated_message),
            "data": data
        }, status=status_code)

    @staticmethod
    def error(message, errors=None, status_code=status.HTTP_400_BAD_REQUEST, request=None, translate_fields=None):
        """Format error response with optional translation for specific fields."""
        translated_message = ResponseFormatter.translate_message(message, request)

        if errors and isinstance(errors, list) and translate_fields:
            errors = [ResponseFormatter.translate_message(err, request) for err in errors]

        return Response({  # ✅ Ensure Response object is returned
            "success": False,
            "statusCode": int(status_code),
            "message": str(translated_message),
            "errors": errors if isinstance(errors, list) else [str(errors)] if errors else []
        }, status=status_code)

    @staticmethod
    def translate_message(message, request):
        """
        Translates the message field based on `lang` and `llm_provider` parameters.
        """
        if not request:
            return message

        lang = request.GET.get("lang")
        llm_provider = request.GET.get("llm_provider", "openai")

        if lang:
            return get_translated_message(message, lang, message, llm_provider)

        return message

    @staticmethod
    def translate_fields(data, request, translate_fields):
        """
        Translates specific fields in the response data.
        """
        lang = request.GET.get("lang")
        llm_provider = request.GET.get("llm_provider", "openai")

        if not lang or not isinstance(data, dict):
            return data  # No translation needed

        translated_data = data.copy()
        for field in translate_fields:
            if field in translated_data and isinstance(translated_data[field], str):
                translated_data[field] = get_translated_message(translated_data[field], lang, translated_data[field], llm_provider)

        return translated_data

