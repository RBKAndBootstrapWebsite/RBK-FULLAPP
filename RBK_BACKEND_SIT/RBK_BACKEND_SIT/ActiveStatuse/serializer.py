from rest_framework import serializers, viewsets
from .models import ActiveState


class ActiveStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActiveState
        fields = ['subject', 'day','week','cohort','subjectActive',"weekisActive","dayisActive"]