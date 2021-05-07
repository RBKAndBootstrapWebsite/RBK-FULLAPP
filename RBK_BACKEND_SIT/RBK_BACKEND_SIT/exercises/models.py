from django.contrib import admin
from django.db import models
from subjects.models import Subject
# Create your models here.


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('question', "subject", "level",
                    "signture", "order", "hint")


class Exercise(models.Model):

    class Meta:
        db_table = "exercises"
    question = models.TextField(default='', blank=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    signture = models.TextField(default='', blank=True)
    order = models.IntegerField(default=0)
    hint = models.TextField(default='', blank=True)

    # class ExerciseAdmin(admin.ModelAdmin):

    def __str__(self):
        return self.question


# admin.site.register(Exercise, ExerciseAdmin)
