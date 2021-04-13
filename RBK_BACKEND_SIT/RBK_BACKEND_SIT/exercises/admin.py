from django.contrib import admin

from .models import Exercise, ExerciseAdmin

admin.site.register(Exercise, ExerciseAdmin)
