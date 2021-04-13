from rest_framework import serializers, viewsets
from .models import Day


class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = ['text',  'id']