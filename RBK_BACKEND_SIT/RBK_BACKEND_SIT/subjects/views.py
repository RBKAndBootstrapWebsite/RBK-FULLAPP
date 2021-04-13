from django.shortcuts import render
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework import viewsets


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer