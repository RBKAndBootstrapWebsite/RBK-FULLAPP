from django.contrib import admin
from django.db import models
from subjects.models import Subject
# Create your models here.


class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', "url",'subject')


class Lecture(models.Model):
    class Meta:
        db_table = "lectures"
    title = models.TextField(default='', blank=False)
    url = models.TextField(default='', blank=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
