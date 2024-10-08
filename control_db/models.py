from django.db import models
from asgiref.sync import sync_to_async
from django.utils.translation import gettext_lazy as _


class Client(models.Model):

	STAFF_CHOICES = (
		('admin', _('Administrator')),
	)

	ACTIVE_CHOICES = (
		('active', _('Active')),
		('inactive', _('Inactive')),
	)

	STATUS_CHOICES = STAFF_CHOICES + ACTIVE_CHOICES

	tg_id = models.BigIntegerField(unique=True, verbose_name=_('TG ID'))
	username = models.CharField(
		max_length=200,
		default=_('Anonymous'),
		verbose_name=_('Username')
	)
	register_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Register date'))
	status = models.CharField(
		max_length=100,
		choices=STATUS_CHOICES,
		default='active',
		verbose_name=_('Status')
	)

	state = models.CharField(max_length=50, null=True, blank=True)
	data = models.JSONField(default=dict, null=True, blank=True)

	class Meta:
		verbose_name = _('Client')
		verbose_name_plural = _('Clients')

	def __str__(self):
		return str(self.tg_id)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

	async def set_state(self, state):
		self.state = state
		await self.asave()

	async def clear_state(self):
		self.state = None
		await self.asave()
