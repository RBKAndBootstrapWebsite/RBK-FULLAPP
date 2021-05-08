from django.shortcuts import render
from .models import Week
# from subjects.models import Subject
# from resources.models import Resources
from .serializer import ActiveStateSerializer
# from subjects.serlializer import SubjectSerializer
# from resources.serializers import ResourceSerializer
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer
from lectures.serializers import LectureSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from lectures.models import Lecture
from days.models import Day
from .models import ActiveState


class WeeksViewSet(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = ActiveStateSerializer

    def create(self, request, *args , **kwargs):
        data = request.data;
        # newActive= ActiveState.
