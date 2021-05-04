from django.urls import path, include
from rest_framework import routers

from .api import  getAllWarmUps_view,DeleteWarmUps_view,UpdateWarmUps_view,SaveWarmUps_view



app_name='Warmups'
urlpatterns = [
   
    path('getAllWarmUps_view', getAllWarmUps_view, name="getAllWarmUps_view" ),
    path('DeleteWarmUps_view',DeleteWarmUps_view,name="DeleteWarmUps_view"),
    path('UpdateWarmUps_view',UpdateWarmUps_view,name="UpdateWarmUps_view"),
    path('SaveWarmUps_view', SaveWarmUps_view, name="SaveWarmUps_view")
   
]