from django.urls import path, include
from rest_framework import routers
from .api import  getAllWarmUps_view



app_name='Warmups'
urlpatterns = [
   
    path('getAllWarmUps_view', getAllWarmUps_view, name="getAllWarmUps_view" ),
   
]