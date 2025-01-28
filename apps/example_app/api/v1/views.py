from rest_framework import viewsets
from rest_framework.views import APIView
from apps.example_app.models import Translation
from apps.example_app.api.v1.serializers import TranslationSerializer
from common.response import ResponseFormatter


class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer


class ExampleView(APIView):
    def get(self, request):
        message = "Operation successful"
        data = {
            "title": "Welcome to our platform",
            "description": "This is a demo description",
            "note": "You need to verify your email"
        }

        # Specify which fields in `data` need translation
        translate_fields = ["title", "description"]

        return ResponseFormatter.success(
            message=message,
            data=data,
            request=request,
            translate_fields=translate_fields
        )
