from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'get_message', 'need_why', 'location')
    list_filter = ('need_why', 'location')
    ordering = ('message_id',)
