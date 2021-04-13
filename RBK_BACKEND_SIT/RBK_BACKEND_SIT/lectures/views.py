from django.shortcuts import render
from .models import Lecture
from .serializers import LectureSerializer
from rest_framework import viewsets


class LecturesViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer