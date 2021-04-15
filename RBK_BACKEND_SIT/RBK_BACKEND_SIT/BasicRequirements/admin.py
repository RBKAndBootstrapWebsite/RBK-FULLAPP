from django.contrib import admin

# Register your models here.
from .models import BasicRequirement, BasicRequirementAdmin

admin.site.register(BasicRequirement, BasicRequirementAdmin)
