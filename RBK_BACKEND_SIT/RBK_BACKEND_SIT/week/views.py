from django.shortcuts import render
from .models import Week
from subjects.models import Subject
from resources.models import Resources
from .serializers import WeekSerializer
from subjects.serializers import SubjectSerializer
from resources.serializers import ResourceSerializer
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer
from lectures.serializers import LectureSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from lectures.models import Lecture
from days.models import Day
from days.serializers import DaySerializer


class WeeksViewSet(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer
    @action(detail=False, methods=['GET'])
    def get_weeks(self, request):
        final = {}
        final['weeks'] = []
        days = []
        weeks = Week.objects.all()

        for w in range(len(weeks)):
            week_serlized = WeekSerializer(weeks[w])
            days_filterd = Day.objects.filter(week_id=w)
            final['weeks'].append({
                # 'status': week_serlized.data['status'],
                'id': week_serlized.data['id'],
                'text': week_serlized.data['text'],
                'days': []
            })

        for d in range(len(final['weeks'])):
            days_filterd = Day.objects.filter(week_id=final['weeks'][d]['id'])
            for s in range(len(days_filterd)):
                final['weeks'][d]['days'].append({
                    # 'status': days_filterd[s].status,
                    'text': days_filterd[s].text,
                    'id': days_filterd[s].id,
                    'subjects': []
                })

        for f in range(len(final['weeks'])):
            for h in range(len(final['weeks'][f]['days'])):
                subjects = Subject.objects.filter(week_id=final['weeks'][f]['id'], day_id=final['weeks'][f]['days'][h]['id'])
                for k in range(len(subjects)):
                    print(subjects[k])
                    final['weeks'][f]['days'][h]['subjects'].append({
                            'id': subjects[k].id,
                            'title': subjects[k].title,
                            'lecures': [],
                            'excersies': []
                    })
        return Response(final)