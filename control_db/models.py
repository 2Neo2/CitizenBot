from django.db import models
from asgiref.sync import sync_to_async
from django.utils.translation import gettext_lazy as _

class Client(models.Model):

    STAFF_CHOICES = (
        ('consultant', _('Консультант')),
    )

    ACTIVE_CHOICES = (
        ('active', _('Активный')),
        ('inactive', _('Неактивный')),
    )

    STATUS_CHOICES = STAFF_CHOICES + ACTIVE_CHOICES

    tg_id = models.BigIntegerField(unique=True, verbose_name=_('TG ID'))
    username = models.CharField(
        max_length=200,
        default=_('Anonymous'),
        verbose_name=_('Имя пользователя')
    )
    register_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата регистрации'))
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name=_('Статус')
    )

    class Meta:
        verbose_name = _('Пользователя')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return str(self.tg_id)

    # def save(self, *args, **kwargs):
    # 	super().save(*args, **kwargs)

    # async def set_state(self, state):
    #     self.state = state
    #     await self.asave()

    # async def set_data(self, data):
    #     self.data = data
    #     await self.asave()

    # async def clear_state(self):
    #     self.state = None
    #     await self.asave()


class ClientAppeal(models.Model):
    STATUS_CHOICES = (
        ('processing', _('В процессе')),
        ('work', _('В работе')),
        ('completed', _('Выполнено')),
    )
        
    appeal_id = models.CharField(max_length=200, unique=True, verbose_name=_('Id Обращения'))
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        related_name='client_appeals'
    )
    register_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='processing',
        verbose_name=_('Статус')
    )
    appeal = models.TextField(verbose_name=_('Текст вопроса'))
    consultant = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name=_('Консультант'),
        null=True,
        related_name='consultant_appeals'
    )
    answer = models.TextField(verbose_name='Ответ', blank=True, null=True)

    class Meta:
        verbose_name = _('Обращение')
        verbose_name_plural = _('Обращения')

    def __str__(self):
        return str(self.appeal_id)
