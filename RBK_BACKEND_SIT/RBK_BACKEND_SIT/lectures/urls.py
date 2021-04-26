from django.urls import path, include
from rest_framework import routers
from .views import LecturesViewSet
router = routers.DefaultRouter()
router.register(r'lectures', LecturesViewSet)
from .api import getAllSubjectsLectures

app_name='lectures'
urlpatterns = [
    path('', include(router.urls)),
    path('getAllSubjectsLectures', getAllSubjectsLectures, name="getAllSubjectsLectures")
]