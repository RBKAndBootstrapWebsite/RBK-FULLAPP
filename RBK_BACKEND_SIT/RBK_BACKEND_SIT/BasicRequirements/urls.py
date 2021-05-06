from django.urls import path, include
from rest_framework import routers

from .api import  getAllBasicRequirments_view,UpdateBasicRequirement_view,DeleteBasicRequirement_view,SaveBasicRequirement_view



app_name='BasicRequirements'
urlpatterns = [
   
    path('getAllBasicRequirments_view', getAllBasicRequirments_view, name="getAllBasicRequirments_view" ),
    path('UpdateBasicRequirement_view',UpdateBasicRequirement_view,name="UpdateBasicRequirement_view"),
    path('DeleteBasicRequirement_view',DeleteBasicRequirement_view,name="DeleteBasicRequirement_view"),
    path('SaveBasicRequirement_view', SaveBasicRequirement_view, name="SaveBasicRequirement_view")
   
]