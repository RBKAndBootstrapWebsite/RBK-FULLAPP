from django.urls import path
from .views import CustomUserCreate
from .api import getUserData_view

app_name='accounts'
urlpatterns = [
    path('register/',CustomUserCreate.as_view(), name='create_user'),
    path('getInfo/',getUserData_view, name='getUerData'),
]