from django.db import models
from django.contrib import admin
from django.conf import settings
from week.models import Week
from days.models import Day
from cohort.models import Cohort

class WarmupsAdmin(admin.ModelAdmin):
    list_display = ('student_name', "staff_name", "week","day", "mark",  "notes")
    list_filter = ("student_name", "week","day")

# Create your models here.


class Warmups(models.Model):
    class Meta:
        db_table = "Warmups"
    student_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="studentname+")
    staff_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name=" staffname+")
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    # title=models.TextField(default='NotSolved', blank=False)
    mark = models.TextField(default='NotSolved', blank=False)
    notes = models.TextField(default='', blank=False)

    def __str__(self):
        return self.mark
