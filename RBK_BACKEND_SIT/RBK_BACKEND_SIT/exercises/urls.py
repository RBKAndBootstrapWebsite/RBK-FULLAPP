from django.urls import path, include
from rest_framework import routers
from .views import ExercisesViewSet
router = routers.DefaultRouter()
router.register(r'exercises', ExercisesViewSet)


urlpatterns = [
    path('', include(router.urls))
]