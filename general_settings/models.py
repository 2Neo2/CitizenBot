from django.db import models

from django.utils.translation import gettext_lazy as _


class GeneralSettings(models.Model):
	consultant_id_first = models.CharField(max_length=200, default='', verbose_name=_('Первый консультант'), null=True, blank=True)
	consultant_id_second = models.CharField(max_length=200, default='', verbose_name=_('Второй консультант'), null=True, blank=True)

	class Meta:
		verbose_name = _('Основные')
		verbose_name_plural = _('Основные')

	def __str__(self):
		return str(_('Основные настройки'))
