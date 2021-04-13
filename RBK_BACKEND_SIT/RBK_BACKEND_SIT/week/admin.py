from django.contrib import admin

from .models import Week, WeekAdmin

admin.site.register(Week, WeekAdmin)


# class WeeksAdmin