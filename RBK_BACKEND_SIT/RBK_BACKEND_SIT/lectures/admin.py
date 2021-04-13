from django.contrib import admin

from .models import Lecture, LectureAdmin

admin.site.register(Lecture, LectureAdmin)
