from django.urls import path, include


from .api import getStudentCohortdaysOfTheWeek_view,ChangeDaysVisibility_view




app_name='days'
urlpatterns = [
    # path('', include(router.urls)),
    path('getStudentCohortdaysOfTheWeek_view',getStudentCohortdaysOfTheWeek_view, name='getStudentCohortdaysOfTheWeekview'),
    path('ChangeDaysVisibility_view',ChangeDaysVisibility_view, name='ChangeDaysVisibility_view'),

]
