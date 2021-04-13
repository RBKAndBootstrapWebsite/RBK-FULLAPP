from django.db import models
from django.contrib import admin
from days.models import Day
from week.models import Week
from cohort.models import Cohort
from subjects.models import Subject

# Create your models here.
# @admin.register(Cohort)
# class ActiveStatusAdmin(admin.ModelAdmin):
#     list_display = ( 'weekisActive', 'dayisActive' )


class ActiveState(models.Model):
    class Meta:
        db_table = "activestatus"
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    dayisActive = models.BooleanField(default=False)
    weekisActive = models.BooleanField(default=False)
    subjectActive = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


   


@admin.register(ActiveState)
class ActiveStatusAdmin(admin.ModelAdmin):
    list_display = ( 'weekisActive', 'dayisActive' )
