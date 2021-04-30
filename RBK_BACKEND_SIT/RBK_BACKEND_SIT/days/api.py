from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Day
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
def getStudentCohortdaysOfTheWeek_view(request):
    permission_classes = (permissions.IsAuthenticated,)
    try:
        if request.data["cohort"] and  request.data["is_staff"] != 1:
            print(request.data["cohort"])
            print("33333333333333333333333333333333333")
            cursor = connection.cursor()
            cursor.execute('''SELECT DISTINCT 
			rbkbackend.days.id,
            rbkbackend.days.text,
            rbkbackend.activestatus.week_id,
             rbkbackend.activestatus.day_id,
             rbkbackend.activestatus.dayisActive,
            rbkbackend.activestatus.cohort_id
            FROM rbkbackend.days
            left join rbkbackend.activestatus 
            on rbkbackend.activestatus.week_id=rbkbackend.days.week_id and  rbkbackend.activestatus.day_id =rbkbackend.days.id
            where rbkbackend.activestatus.cohort_id =%s and rbkbackend.activestatus.dayisActive= true  and rbkbackend.activestatus.weekisActive=true
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
			rbkbackend.days.id,
            rbkbackend.days.text,
            rbkbackend.activestatus.week_id,
             rbkbackend.activestatus.day_id,
             rbkbackend.activestatus.dayisActive,
            rbkbackend.activestatus.cohort_id
            FROM rbkbackend.days
            left join rbkbackend.activestatus 
            on rbkbackend.activestatus.week_id=rbkbackend.days.week_id 
            where rbkbackend.activestatus.cohort_id =%s ''',
            [int(request.data['cohort'])])

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
def ChangeDaysVisibility_view(request):
    permission_classes = (permissions.IsAuthenticated,)
    try:
   
        print(request.data["day"], request.data["dayisActive"])
        cursor = connection.cursor()
        cursor.execute('''SELECT  
            rbkbackend.subjects.day_id,
            rbkbackend.subjects.id as subject , 
            rbkbackend.subjects.week_id
            from rbkbackend.subjects 
            where rbkbackend.subjects.day_id =%s
            ''',[int(request.data["day"])])


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
                (cohort_id, day_id, subject_id, week_id,dayisActive)
                VALUES
                (%s, %s, %s, %s ,%s)
                ON DUPLICATE KEY UPDATE
                dayisActive =%s
                '''
                ,[request.data["cohort"]
                ,sub['day_id'],
                sub['subject'],
                sub['week_id'], 
                request.data["dayisActive"],
                request.data["dayisActive"]
                ])
            
            except Day.DoesNotExist:
                return Response({"ServerError":"DataNot Found"})
        return Response({"day":request.data["day"],
                 "dayisActive":request.data["dayisActive"]})
            
    
          
    except Day.DoesNotExist: 
        return Response({"ServerError":"DataNot Found"})