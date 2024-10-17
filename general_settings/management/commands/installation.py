from django.core.management.base import BaseCommand
from general_settings.models import GeneralSettings

class Command(BaseCommand):
    help = 'Инициализация настроек'

    def handle(self, *args, **kwargs):
        default_settings = {
            'consultant_id_first': '',  # Укажите дефолтные значения
            'consultant_id_second': '',  # Укажите дефолтные значения
        }

        GeneralSettings.objects.get_or_create(id=1, defaults=default_settings)