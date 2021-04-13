from rest_framework import serializers, viewsets
from .models import Week


class WeekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Week
        fields = ['text', 'id']