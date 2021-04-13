from django.contrib import admin

from .models import Day, DayAdmin

admin.site.register(Day, DayAdmin)
