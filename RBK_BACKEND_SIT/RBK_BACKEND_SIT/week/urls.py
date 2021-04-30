from django.urls import path, include
from rest_framework import routers
# from .views import WeeksViewSet
from .api import getStudentCohortWeeks_view , ChangeWeekVisibility_view

# router = routers.DefaultRouter()
# router.register(r'weeks', WeeksViewSet)


app_name='week'
urlpatterns = [
    # path('', include(router.urls)),
    path('getStudentCohortWeeks_view',getStudentCohortWeeks_view, name='getstudentactiveWeek'),
    path('ChangeWeekVisibility_view',ChangeWeekVisibility_view,name="ChangeWeekVisibility_view")
]