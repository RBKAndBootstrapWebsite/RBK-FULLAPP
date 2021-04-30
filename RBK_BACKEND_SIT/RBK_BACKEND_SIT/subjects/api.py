from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Subject
from django.db import connection
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from accounts.models import NewUser
from django.db import connection
import json
from rest_framework.permissions import AllowAny
from django.core.serializers.json import DjangoJSONEncoder
import itertools
from http import HTTPStatus

@csrf_exempt
@api_view(['POST', ])
def getStudentCohortSubhectsdaysOfTheWeek_view(request):
    permission_classes = (permissions.IsAuthenticated,)
    try:
        if request.data["cohort"] and not request.data["is_staff"]:
            cursor = connection.cursor()
            cursor.execute('''SELECT DISTINCT 
			 rbkbackend.subjects.id,
             rbkbackend.subjects.title,
             rbkbackend.subjects.los,
             rbkbackend.subjects.learningObjective,
             rbkbackend.subjects.part,
             rbkbackend.activestatus.week_id,
             rbkbackend.activestatus.day_id,
             rbkbackend.activestatus.subjectActive,
             rbkbackend.activestatus.cohort_id
            FROM rbkbackend.subjects
            left join rbkbackend.activestatus 
            on  rbkbackend.activestatus.subject_id = rbkbackend.subjects.id
            and rbkbackend.activestatus.day_id =rbkbackend.subjects.day_id
            and rbkbackend.activestatus.week_id =rbkbackend.subjects.week_id
            where rbkbackend.activestatus.cohort_id =%s
            and rbkbackend.activestatus.dayisActive= true  
            and rbkbackend.activestatus.weekisActive=true 
            and rbkbackend.activestatus.subjectActive=true
            ''',[int(request.data['cohort'])])

            desc = cursor.description
            print(desc)
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)
        else:
            cursor = connection.cursor()
            cursor.execute('''SELECT DISTINCT 
			 rbkbackend.subjects.id,
             rbkbackend.subjects.title,
             rbkbackend.subjects.los,
             rbkbackend.subjects.learningObjective,
             rbkbackend.subjects.part,
             rbkbackend.activestatus.week_id,
             rbkbackend.activestatus.day_id,
             rbkbackend.activestatus.subjectActive,
             rbkbackend.activestatus.cohort_id
            FROM rbkbackend.subjects
            left join rbkbackend.activestatus 
            on  rbkbackend.activestatus.subject_id = rbkbackend.subjects.id
            where rbkbackend.activestatus.cohort_id =%s
            
            ''',[int(request.data['cohort'])])

            desc = cursor.description
            print(desc)
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)

    except NewUser.DoesNotExist:
        return Response(status=HTTPStatus.BAD_REQUEST)

    return Response(status=HTTPStatus.FORBIDDEN)
    



@csrf_exempt
@api_view(['POST', ])
def ChangeSubjectVisibility_view(request):
    permission_classes = (permissions.IsAuthenticated,)
    try:
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO activestatus
        (cohort_id, day_id, subject_id, week_id,subjectActive)
         VALUES
         (%s, %s, %s, %s ,%s)
         ON DUPLICATE KEY UPDATE
        subjectActive =%s
                '''
        ,[request.data["cohort"],
        request.data['day_id'],
        request.data['id'],
        request.data['week_id'], 
        request.data["subjectActive"],
        request.data["subjectActive"],
        ])
            
    except Subject.DoesNotExist:
            return Response({"ServerError":"DataNot Found"})
    return Response({"sub":request.data['id'],
                 "subjectActive":request.data["subjectActive"]})
            
    
          
  