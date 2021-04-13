from django.contrib import admin
from django.db import models
from subjects.models import Subject


class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('title', "url", "subject")

# Create your models here.


class Resources(models.Model):
    class Meta:
        db_table = "resources"
    title = models.CharField(max_length=255, default='', blank=False)
    url = models.CharField(max_length=255, default='', blank=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
