from rest_framework import serializers, viewsets
from .models import Subject
from week.serializer import WeekSerializer


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    week = WeekSerializer()

    class Meta:
        model = Subject
        fields = ['title', 'week', 'part',  'part']