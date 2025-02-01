from rest_framework import status
from rest_framework.response import Response
from django.utils.translation import gettext as _


class ResponseFormatter:
    @staticmethod
    def success(message, data=None, status_code=status.HTTP_200_OK):
        """Format success response with translation."""
        return Response({
            "success": True,
            "statusCode": int(status_code),
            "message": _(message),  # Use Django's translation
            "data": data
        }, status=status_code)

    @staticmethod
    def error(message, errors=None, status_code=status.HTTP_400_BAD_REQUEST):
        """Format error response with translation."""
        return Response({
            "success": False,
            "statusCode": int(status_code),
            "message": _(message),  # Use Django's translation
            "errors": errors if isinstance(
                errors, list
            ) else [str(errors)] if errors else []
        }, status=status_code)
