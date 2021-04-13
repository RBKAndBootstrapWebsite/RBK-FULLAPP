from django.contrib import admin
from django.db import models
from week.models import Week


class DayAdmin(admin.ModelAdmin):
    list_display = ('text',  )


class Day(models.Model):
    class Meta:
        db_table = "days"
    text = models.TextField(default='', blank=False)
    # status = models.BooleanField(default=False)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    # week = models.OneToMany(Week, on_delete=models.CASCADE)


    def __str__(self):
        return self.text
