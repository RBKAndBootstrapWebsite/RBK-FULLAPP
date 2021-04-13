from django.contrib import admin
from django.db import models
# from days.models import Day


class WeekAdmin(admin.ModelAdmin):
    list_display = ('text', )


class Week(models.Model):
    class Meta:
        db_table = "weeks"
    text = models.TextField(default='', blank=False)
    # status = models.BooleanField(default=False)
    # days= models.OneToMany(Day)

    def __str__(self):
        return self.text
