from rest_framework import serializers, viewsets
from .models import Resources
from week.serializer import WeekSerializer


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
 

    class Meta:
        model = Resources
        fields = ['title', 'url']