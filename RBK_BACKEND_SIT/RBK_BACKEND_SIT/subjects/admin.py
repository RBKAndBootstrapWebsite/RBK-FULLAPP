from django.contrib import admin

from .models import Subject, SubjectAdmin

admin.site.register(Subject, SubjectAdmin)
