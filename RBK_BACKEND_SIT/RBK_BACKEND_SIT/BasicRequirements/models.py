from django.db import models
from django.contrib import admin
from django.conf import settings
from subjects.models import Subject
from cohort.models import Cohort

class BasicRequirementAdmin(admin.ModelAdmin):
    list_display = ('student_name', "staff_name", "subject", "mark",  "notes")
    list_filter = ("student_name", "subject")

# Create your models here.


class BasicRequirement(models.Model):
   
    student_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="studentname+")
    staff_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name=" staffname+")
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.IntegerField(default=0)
    notes = models.TextField(default='', blank=False)
    note2 = models.TextField(default='', blank=False)

    class Meta:
        db_table = "basicrquirements"
        unique_together = ('student_name', 'staff_name','cohort','subject')

    def __str__(self):
        return self.notes
