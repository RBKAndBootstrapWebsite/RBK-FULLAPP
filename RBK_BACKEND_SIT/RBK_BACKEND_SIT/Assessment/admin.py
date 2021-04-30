from django.contrib import admin

# Register your models here.
from .models import Assessment, AssessmentAdmin

admin.site.register(Assessment, AssessmentAdmin)
