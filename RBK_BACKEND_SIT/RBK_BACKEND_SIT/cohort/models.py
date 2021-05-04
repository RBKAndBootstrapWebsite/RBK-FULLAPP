from django.contrib import admin
from django.db import models

from django.conf import settings

# Create your models here.


# class LectureAdmin(admin.ModelAdmin):
#     list_display = ('content', "subject")

# admin.site.register(UserTage)

# class UserTage(models.Model):
#     name= models.CharField(max_length=200, null=True)

class Cohort(models.Model):
    class Meta:
        db_table = "cohort"
    name = models.TextField(default='', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    

    def __str__(self):
        return self.name 



@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):  
    list_display = ('name', "created_at")
