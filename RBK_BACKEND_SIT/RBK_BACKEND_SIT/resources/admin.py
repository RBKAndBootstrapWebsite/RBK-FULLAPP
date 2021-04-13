from django.contrib import admin

from .models import Resources, ResourcesAdmin

admin.site.register(Resources, ResourcesAdmin)
