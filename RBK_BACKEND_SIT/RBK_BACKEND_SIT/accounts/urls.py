from django.urls import path
from .views import CustomUserCreate
from .api import getUserData_view,getStudentsData_view

app_name='accounts'
urlpatterns = [
    path('getStudentsData_view', getStudentsData_view,name="StudensList"),
    path('register/',CustomUserCreate.as_view(), name='createuser'),
    path('getInfo/',getUserData_view, name='getUerData'),
]