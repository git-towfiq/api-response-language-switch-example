from rest_framework import serializers
from apps.example_app.models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ['id', 'key', 'language', 'message']
