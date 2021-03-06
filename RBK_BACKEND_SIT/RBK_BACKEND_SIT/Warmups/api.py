from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Warmups
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
from rest_framework.exceptions import ValidationError, ParseError


# --------------------- Delete WarmUps ----------------------------#

@csrf_exempt
@api_view(['POST', ])
def SaveWarmUps_view(request):

    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.HTTP_406_NOT_ACCEPTABLE)
    else:
        try:
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO rbkbackend.warmups
                    (mark,notes,day_id,staff_name_id,student_name_id,week_id,cohort_id)
                    VALUES 
                    ( %s, %s, %s, %s, %s, %s, %s);''',
                    [
                    request.data["mark"],
                    request.data["notes"],
                    request.data["day_id"],
                    request.data["staff_id"],
                    request.data["student_id"],
                    request.data["week_id"],
                    request.data["cohort_id"],
                    ])

            desc = cursor.description
            return Response({
               "mark": request.data["mark"],
                "notes":   request.data["notes"],
                "day_id":  request.data["day_id"],
                "staff_id":  request.data["staff_id"],
                "student_id":  request.data["student_id"],
                "week_id": request.data["week_id"],
                "cohort_id": request.data["cohort_id"]
            })
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)



# --------------------- Delete WarmUps ----------------------------#

@csrf_exempt
@api_view(['POST', ])
def DeleteWarmUps_view(request):

    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.BAD_REQUEST)
    else:
        try:
    
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM rbkbackend.warmups
                WHERE rbkbackend.warmups.id in (%s)
                    ''',[request.data["ArrayOfWarmUpsIds"]])

            desc = cursor.description
            return Response(request.data["ArrayOfWarmUpsIds"])
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)


# --------------------- Update WarmUps ----------------------------#

@csrf_exempt
@api_view(['POST', ])
def UpdateWarmUps_view(request):
    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.BAD_REQUEST)
    else :
        try:
    
            cursor = connection.cursor()
            cursor.execute('''UPDATE rbkbackend.warmups
                SET
            mark = %s,
            notes = %s
            WHERE id = %s; 
            ''',[request.data["mark"],request.data["notes"],request.data["id"]])

            desc = cursor.description
            return Response({"mark":request.data["mark"],"notes":request.data["mark"],"id":request.data["id"]})
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)

    


@csrf_exempt
@api_view(['POST', ])
def getAllWarmUps_view(request):
   
    permission_classes = (permissions.IsAuthenticated,)
    try:
        if request.data["cohort_id"] :
            cursor = connection.cursor()
            cursor.execute('''SELECT 
                rbkbackend.warmups.id,
                rbkbackend.cohort.name as cohort_name,
                rbkbackend.warmups.notes,
                rbkbackend.warmups.mark,
               
                rbkbackend.days.text as daytitle
             
                , rbkbackend.weeks.text as weektitle,
               
                concat( g.first_name ," " ,g.Last_name) as staff_name,
               concat( d.first_name," " ,d.Last_name) as student_name 
              
                FROM rbkbackend.warmups
                right join rbkbackend.cohort on rbkbackend.warmups.cohort_id = rbkbackend.cohort.id
                right join rbkbackend.days on rbkbackend.days.id = rbkbackend.warmups.day_id
                right join rbkbackend.weeks on rbkbackend.weeks.id = rbkbackend.warmups.week_id
                right join rbkbackend.accounts_newuser  as g on g.id = rbkbackend.warmups.staff_name_id
                right join rbkbackend.accounts_newuser as d on d.id = rbkbackend.warmups.student_name_id
                where rbkbackend.warmups.cohort_id=%s order by 
                rbkbackend.warmups.cohort_id ASC,rbkbackend.warmups.week_id ASC,rbkbackend.warmups.day_id ASC, rbkbackend.warmups.student_name_id ASC ;;
            ''',[int(request.data['cohort_id']),])

            desc = cursor.description
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)
        else :
            raise ValidationError

    except NewUser.DoesNotExist:
        return Response(status=HTTPStatus.BAD_REQUEST)

    return Response(status=HTTPStatus.FORBIDDEN)
    


            
    
          
  