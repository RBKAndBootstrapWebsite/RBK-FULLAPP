from rest_framework import serializers, viewsets
from .models import Exercise



class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
 

    class Meta:
        model = Exercise
        fields = ['question', 'level', 'signture',  'order','hint']