from django.shortcuts import render
from .models import Subject
from .serlializer import SubjectSerializer
from rest_framework import viewsets


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer