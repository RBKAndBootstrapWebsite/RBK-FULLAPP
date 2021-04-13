from django.shortcuts import render
from .models import Resources
from .serializers import ResourceSerializer
from rest_framework import viewsets


class ResourcesViewSet(viewsets.ModelViewSet):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer
