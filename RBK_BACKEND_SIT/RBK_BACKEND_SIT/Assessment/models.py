from django.db import models
from django.contrib import admin
from django.conf import settings
from week.models import Week
from days.models import Day
from cohort.models import Cohort

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('student_name', "staff_name", "week","refactored", "mark",  "comments")
    list_filter = ("student_name", "week","mark")

# Create your models here.


class Assessment(models.Model):
   
    student_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="studentname+")
    staff_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name=" staffname+")
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    refactored = models.BooleanField(default=False)
    mark = models.IntegerField(default=0)
    comments = models.TextField(default='', blank=False)
    class Meta:
        db_table = "assessments"
        unique_together = ('student_name', 'cohort','week')

    def __str__(self):
        return self.comments

