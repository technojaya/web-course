from django.contrib import admin

from project.apps.core.models import *


class Admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Client, Admin)
admin.site.register(ClientPost)