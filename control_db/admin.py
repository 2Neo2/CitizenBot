from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import *
from django.db.models import Q


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'username', 'register_date', '_status']
    search_fields = ['tg_id', 'username']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        staff = Client.objects.filter(status__in=[status[0] for status in Client.STAFF_CHOICES])
        extra_context = {
            'staff': staff,
        }

        return super().changelist_view(request, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = [field.name for field in obj.__class__._meta.fields]
            self.readonly_fields.remove('status')

            self.readonly_fields.append('_status')

        return self.readonly_fields

    def _status(self, obj):
        style = ''

        match obj.status:
            case 'active':
                style = 'color: green;'

        return format_html(f'<span style="{style}">{obj.get_status_display()}</span>')
    _status.short_description = _('Статус')

    fieldsets = (
        (_('Общая информация'), {'fields': ('tg_id', 'username')}),
        (_('Статус'), {'fields': ('register_date', 'status')}),
    )
    
@admin.register(ClientAppeal)
class ClientAppealAdmin(admin.ModelAdmin):
    readonly_fields = ['appeal_id', 'client', 'status', 'register_date', 'appeal', 'consultant', 'answer']
    list_display = ['appeal_id', 'register_date', 'status', 'client']
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    fieldsets = (
        (_('Инфо обращения'), {'fields': ('appeal_id', )}),
        (_('Статус'), {'fields': ('register_date', 'status')}),
        (_('Взаимодействие'), {'fields': ('client', 'consultant', 'appeal', 'answer')})
    )
