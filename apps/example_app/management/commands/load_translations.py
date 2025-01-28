import json
from django.core.management.base import BaseCommand
from apps.example_app.models import Translation


class Command(BaseCommand):
    help = "Load translations from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path', type=str, help='Path to the JSON file'
        )

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                Translation.objects.update_or_create(
                    key=item['key'],
                    language=item['language'],
                    defaults={'message': item['message']}
                )
        self.stdout.write(
            self.style.SUCCESS('Successfully loaded translations')
        )
