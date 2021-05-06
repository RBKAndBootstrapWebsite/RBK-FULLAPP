from django.urls import path, include
from rest_framework import routers

from .api import  getAllAssessment_view,UpdateAssessment_view,DeleteAssessment_view,SaveAssessment_view



app_name='Assessment'
urlpatterns = [
   
    path('getAllAssessment_view', getAllAssessment_view, name="getAllAssessment_view" ),
    path('UpdateAssessment_view',UpdateAssessment_view,name="UpdateAssessment_view"),
    path('DeleteAssessment_view',DeleteAssessment_view,name="DeleteAssessment_view"),
    path('SaveAssessment_view', SaveAssessment_view, name="SaveAssessment_view")
   
]