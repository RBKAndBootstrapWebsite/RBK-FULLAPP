from django.urls import path, include
from rest_framework import routers
from .api import getAllServeysOfaCohort_view,SaveSurvays_view,UpdateSurvys_view,DeleteSurvy_view


app_name='survey'
urlpatterns = [

    path('getAllServeysOfaCohort_view',getAllServeysOfaCohort_view,name="getAllServeysOfaCohort_view"),
    path('UpdateSurvys_view',UpdateSurvys_view,name="UpdateSurvys_view"),
     path('DeleteSurvy_view',DeleteSurvy_view,name="DeleteSurvy_view")
]