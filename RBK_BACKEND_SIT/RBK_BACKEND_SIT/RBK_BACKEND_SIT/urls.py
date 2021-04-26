"""RBK_BACKEND_SIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path
from django.conf.urls import url, include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path("", views.catchall),
    # path("/", views.catchall),
    path('login', views.catchall),
    path('logout',views.catchall ),
    path('admin/', admin.site.urls),
   
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/lectures/', include('lectures.urls', namespace="lectures")),
    path('api/users/', include('accounts.urls', namespace="accounts")),
    path("api/exercises/",include('exercises.urls', namespace="exercises")),
    path('api/subjects/',include('subjects.urls' ,namespace="subjects")),
    path('api/days/', include('days.urls', namespace="days")),
    path('api/weeks/', include('week.urls', namespace="weeks")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]


# urlpatterns = [
    
#     re_path(r'^.*', TemplateView.as_view(template_name='index.html')),

# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)