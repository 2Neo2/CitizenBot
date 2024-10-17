from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect

from .models import *


# Register your models here.
admin.site.site_header = 'Гражданский админ'

@admin.register(GeneralSettings)
class GeneralSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request):
         return HttpResponseRedirect('/admin/general_settings/generalsettings/1/change/')
    
    fieldsets = (
        ('Consultation info', {'fields': ('consultant_id_first', 'consultant_id_second')}),
    )