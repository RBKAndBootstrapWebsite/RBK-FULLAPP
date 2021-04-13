from django.urls import path, include
from rest_framework import routers
from .views import SubjectViewSet
router = routers.DefaultRouter()
router.register(r'subjects', SubjectViewSet)


urlpatterns = [
    path('', include(router.urls))
]