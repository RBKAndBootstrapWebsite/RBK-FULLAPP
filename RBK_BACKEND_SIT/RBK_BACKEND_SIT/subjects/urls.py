from django.urls import path, include
from rest_framework import routers
from .views import SubjectViewSet
from .api import  getStudentCohortSubhectsdaysOfTheWeek_view,ChangeSubjectVisibility_view
router = routers.DefaultRouter()
router.register(r'subjects', SubjectViewSet)

app_name='subjects'
urlpatterns = [
    path('', include(router.urls)),
    path('getStudentCohortSubhectsdaysOfTheWeek_view', getStudentCohortSubhectsdaysOfTheWeek_view, name="getStudentCohortdaysOfTheWeekview" ),
    path('ChangeSubjectVisibility_view', ChangeSubjectVisibility_view, name="ChangeSubjectVisibility_view")
]