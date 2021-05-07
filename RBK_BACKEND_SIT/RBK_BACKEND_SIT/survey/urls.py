from django.urls import path, include
from rest_framework import routers
from .api import getAllServeysOfaCohort_view


app_name='survey'
urlpatterns = [

    path('getAllServeysOfaCohort_view',getAllServeysOfaCohort_view,name="getAllServeysOfaCohort_view")
]