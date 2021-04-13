from django.urls import path, include
from rest_framework import routers
from .views import ExercisesViewSet
router = routers.DefaultRouter()
router.register(r'lectures', LecturesViewSet)


urlpatterns = [
    path('', include(router.urls))
]