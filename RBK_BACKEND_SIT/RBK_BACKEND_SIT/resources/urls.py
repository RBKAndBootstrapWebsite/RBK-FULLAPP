from django.urls import path, include
from rest_framework import routers
from .views import ResourcesViewSet
from .api import  getAllSubjectResources
router = routers.DefaultRouter()
router.register(r'resources', ResourcesViewSet)

app_name='resources'
urlpatterns = [
    path('', include(router.urls)),
    path('getAllSubjectResources', getAllSubjectResources, name="getAllSubjectResources" )
]