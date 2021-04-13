from django.shortcuts import render
from .models import Exercise
from .serializers import ExerciseSerializer
from rest_framework import viewsets


class ExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer