from rest_framework import viewsets
from rest_framework.views import APIView
from django.utils.translation import gettext as _
from apps.example_app.models import Translation
from apps.example_app.api.v1.serializers import TranslationSerializer
from common.response import ResponseFormatter


class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer


class ExampleView(APIView):
    def get(self, request):
        data = {
            "message": _("Hello, World!")
        }
        return ResponseFormatter.success(
            message=_("Operation successful"),
            data=data
        )
