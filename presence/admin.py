from django.contrib import admin
from presence.models import Presence,Permit

# Register your models here.
class PresenceAdmin (admin.ModelAdmin):
    list_display = ['worker', 'presence_type', 'time']
    list_filter = ('presence_type',)
    search_fields = []
    list_per_page = 20

admin.site.register(Presence, PresenceAdmin)

class PermitAdmin(admin.ModelAdmin):
    list_display = ['worker', 'presence_type', 'begin_time', 'end_time', 'approvement']
    list_filter = ('presence_type', 'approvement')
    search_fields = ['reason']
    list_per_page = 25

admin.site.register(Permit, PermitAdmin)