from django.urls import path, include
from rest_framework import routers
from .views import WeeksViewSet


router = routers.DefaultRouter()
router.register(r'weeks', WeeksViewSet)


urlpatterns = [
    path('', include(router.urls))
]