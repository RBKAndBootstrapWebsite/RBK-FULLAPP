from rest_framework import serializers, viewsets
from .models import Lecture



class LectureSerializer(serializers.HyperlinkedModelSerializer):
   

    class Meta:
        model = Lecture
        fields = ['title','url','id']