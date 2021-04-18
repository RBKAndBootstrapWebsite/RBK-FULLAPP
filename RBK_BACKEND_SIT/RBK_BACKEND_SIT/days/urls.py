from django.urls import path, include


from .api import getStudentCohortdaysOfTheWeek_view




app_name='days'
urlpatterns = [
    # path('', include(router.urls)),
    path('getStudentCohortdaysOfTheWeek_view',getStudentCohortdaysOfTheWeek_view, name='getStudentCohortdaysOfTheWeekview'),
]