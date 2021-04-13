from django.contrib import admin
from django.db import models
from week.models import Week
from days.models import Day


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', "week", "day", "part",  "los")
    list_filter = ("week", "day")

# Create your models here.


class Subject(models.Model):
    class Meta:
        db_table = "subjects"
    title = models.TextField(default='', blank=False)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    part = models.IntegerField(default=0)
    # status = models.BooleanField(default=False)
    los = models.TextField(default='', blank=False)

    def __str__(self):
        return self.title
