from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GeneralSettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'general_settings'
    verbose_name = _('Настройки')
