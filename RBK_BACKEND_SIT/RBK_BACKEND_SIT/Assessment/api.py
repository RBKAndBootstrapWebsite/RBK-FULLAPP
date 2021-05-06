from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Assessment
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
def SaveAssessment_view(request):

    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.HTTP_406_NOT_ACCEPTABLE)
    else:
        try:
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO rbkbackend.assessments
                    (refactored,mark,comments,cohort_id,staff_name_id,student_name_id,week_id)
                    VALUES 
                    ( %s, %s, %s, %s, %s, %s,%s);''',
                    [
                    request.data["refactored"],
                    request.data["mark"],
                    request.data["comments"],
                    request.data["cohort_id"],
                    request.data["staff_name_id"],
                    request.data["student_name_id"],
                    request.data["week_id"],
                    ])

            desc = cursor.description
            print(cursor.description)
            return Response({
               "refactored": request.data["refactored"],
                "mark":    request.data["mark"],
                "comments":  request.data["comments"],
                "cohort_id":  request.data["cohort_id"],
                "staff_name_id": request.data["staff_name_id"],
                "student_name_id": request.data["student_name_id"],
                "week_id": request.data["week_id"]
            })
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)



# --------------------- Delete WarmUps ----------------------------#

@csrf_exempt
@api_view(['POST', ])
def DeleteAssessment_view(request):

    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.BAD_REQUEST)
    else:
        try:
    
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM rbkbackend.assessments
                WHERE rbkbackend.assessments.id in (%s)
                    ''',[request.data["ArrayOfWarmUpsIds"]])

            desc = cursor.description
            return Response(request.data["ArrayOfWarmUpsIds"])
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)


# --------------------- Update WarmUps ----------------------------#

@csrf_exempt
@api_view(['POST', ])
def UpdateAssessment_view(request):
    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.BAD_REQUEST)
    else :
        try:
    
            cursor = connection.cursor()
            cursor.execute('''UPDATE rbkbackend.assessments
                SET
            mark = %s,
            comments = %s,
            refactored=%s
            WHERE id = %s; 
            ''',[request.data["mark"],request.data["comments"],request.data["refactored"],request.data["id"]])

            desc = cursor.description
            return Response({"mark":request.data["mark"],
                        "comments":request.data["comments"],
                        "refactored":request.data["refactored"],
                        "id":request.data["id"]})
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)

    


@csrf_exempt
@api_view(['POST', ])
def getAllAssessment_view(request):
   
    permission_classes = (permissions.IsAuthenticated,)
    try:
        if request.data["cohort_id"] :
            cursor = connection.cursor()
            cursor.execute('''SELECT 
            rbkbackend.assessments.id,
            rbkbackend.cohort.name as cohort_name,
            rbkbackend.assessments.comments,
            rbkbackend.assessments.refactored,
            rbkbackend.assessments.mark,
            rbkbackend.weeks.text as weektitle,
            g.first_name as staff_name,
            d.first_name as student_name 
            FROM rbkbackend.assessments
            right join rbkbackend.cohort on rbkbackend.assessments.cohort_id = rbkbackend.cohort.id
            right join rbkbackend.weeks on rbkbackend.weeks.id = rbkbackend.assessments.week_id
            right join rbkbackend.accounts_newuser  as g on g.id = rbkbackend.assessments.staff_name_id
            right join rbkbackend.accounts_newuser as d on d.id = rbkbackend.assessments.student_name_id
            where rbkbackend.assessments.cohort_id=%s
            order by 
            rbkbackend.assessments.cohort_id ASC,rbkbackend.assessments.week_id ASC,rbkbackend.assessments.student_name_id ASC ;  
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
    


            
    
          
  