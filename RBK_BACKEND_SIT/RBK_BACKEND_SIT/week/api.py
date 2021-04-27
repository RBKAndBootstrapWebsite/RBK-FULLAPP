from rest_framework import viewsets, permissions
from rest_framework.response import Response

from django.db import connection
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from accounts.models import NewUser
from django.db import connection
import json
from .models import Week
from rest_framework.permissions import AllowAny
from django.core.serializers.json import DjangoJSONEncoder
import itertools

@csrf_exempt
@api_view(['POST', ])
def getStudentCohortWeeks_view(request):
    permission_classes = (permissions.IsAuthenticated,)
    try:
        if request.data["cohort"] and not request.data["is_staff"]:
            cursor = connection.cursor()
            cursor.execute('''SELECT DISTINCT 
             rbkbackend.weeks.id,
            rbkbackend.weeks.text,
            rbkbackend.activestatus.week_id,
            rbkbackend.activestatus.weekisActive,
            rbkbackend.activestatus.cohort_id
            FROM rbkbackend.weeks
            left join rbkbackend.activestatus 
            on rbkbackend.activestatus.week_id=rbkbackend.weeks.id 
            where rbkbackend.activestatus.cohort_id =%s
            and rbkbackend.activestatus.weekisActive= true;
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
            rbkbackend.weeks.id,
            rbkbackend.weeks.text,
            rbkbackend.activestatus.week_id,
            rbkbackend.activestatus.weekisActive,
            rbkbackend.activestatus.cohort_id
            FROM rbkbackend.weeks
            left join rbkbackend.activestatus 
            on rbkbackend.activestatus.week_id=rbkbackend.weeks.id 
            ''')

            desc = cursor.description
           
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)
    except Week.DoesNotExist:
        return Response({"ServerError":"DataNot Found"})

    
@csrf_exempt
@api_view(['POST', ])
def ChangeWeekVisibility_view(request):
    permission_classes = (permissions.IsAuthenticated,)
    try:
   
        print(request.data["week"], request.data["weekisActive"])
        cursor = connection.cursor()
        cursor.execute('''SELECT  
            rbkbackend.subjects.day_id,
            rbkbackend.subjects.id as subject , 
            rbkbackend.subjects.week_id
            from rbkbackend.subjects 
            where rbkbackend.subjects.day_id
            in (select rbkbackend.days.id 
            from rbkbackend.days 
            where rbkbackend.days.week_id =%s)
            and rbkbackend.subjects.week_id=%s;
            
            ''',[int(request.data["week"]),int(request.data["week"])])


        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row))
            for row in cursor.fetchall()]

        print(data)

        for sub in data :
            print(sub)
            try:
                cursor = connection.cursor()
                cursor.execute('''INSERT INTO activestatus
                (cohort_id, day_id, subject_id, week_id,weekisActive)
                VALUES
                (%s, %s, %s, %s ,%s)
                ON DUPLICATE KEY UPDATE
                weekisActive =%s
                '''
                ,[request.data["cohort"]
                ,sub['day_id'],
                sub['subject'],
                sub['week_id'], 
                request.data["weekisActive"],
                request.data["weekisActive"]
                ])
            
            except Week.DoesNotExist:
                return Response({"ServerError":"DataNot Found"})
        return Response({"week":request.data["week"],
                 "weekisActive":request.data["weekisActive"]})
            
    
          
    except Week.DoesNotExist: 
        return Response({"ServerError":"DataNot Found"})

