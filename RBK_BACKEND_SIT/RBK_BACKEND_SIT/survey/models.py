from django.contrib import admin
from django.db import models
from cohort.models import Cohort


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', "description", "url")
    list_filter = ["title"]


class Survey(models.Model):
    class Meta:
        db_table = "survey"
    title = models.TextField(default='', blank=False)
    description = models.TextField(default='', blank=False)
    url = models.TextField(default='', blank=False)
    cohort =models.ManyToManyField(Cohort)

    def __str__(self):
        return self.title
