from django.urls import path, include
from rest_framework import routers
from .views import ExercisesViewSet
router = routers.DefaultRouter()
from .api import getAllSubjectsExrsize
router.register(r'exercises', ExercisesViewSet)

app_name='exercises'
urlpatterns = [
    path('', include(router.urls)),
    path('getAllSubjectsExrsize',getAllSubjectsExrsize,name="getAllSubjectsExrsize")
]