from django.contrib import admin

# Register your models here.
from .models import Survey, SurveyAdmin

admin.site.register(Survey, SurveyAdmin)
