from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import BasicRequirement
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
def SaveBasicRequirement_view(request):

    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.HTTP_406_NOT_ACCEPTABLE)
    else:
        try:
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO rbkbackend.basicrequirements
                    (mark,
                    notes,
                    cohort_id,
                    staff_name_id,
                    student_name_id
                    ,subject_id,
                     note2)
                    VALUES 
                    ( %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s)''',
                    [
                    request.data["mark"],
                    request.data["notes"],
                    request.data["cohort_id"],
                    request.data["staff_name_id"],
                    request.data["student_name_id"],
                    request.data["subject_id"],
                    request.data["note2"],
                    ])

            desc = cursor.description
            print(cursor.description)
            return Response({
               
                "mark":    request.data["mark"],
                "notes":  request.data["notes"],
                "cohort_id":  request.data["cohort_id"],
                "staff_name_id": request.data["staff_name_id"],
                "student_name_id": request.data["student_name_id"],
                "subject_id": request.data["subject_id"],
                "note2":request.data["note2"]
            })
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)



# --------------------- Delete WarmUps ----------------------------#

@csrf_exempt
@api_view(['POST', ])
def DeleteBasicRequirement_view(request):

    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.BAD_REQUEST)
    else:
        try:
    
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM rbkbackend.basicrequirements
                WHERE rbkbackend.basicrequirements.id in (%s)
                    ''',[request.data["ArrayOfWarmUpsIds"]])

            desc = cursor.description
            return Response(request.data["ArrayOfWarmUpsIds"])
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)


# --------------------- Update WarmUps ----------------------------#

@csrf_exempt
@api_view(['POST', ])
def UpdateBasicRequirement_view(request):
    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.BAD_REQUEST)
    else :
        try:
    
            cursor = connection.cursor()
            cursor.execute('''UPDATE rbkbackend.basicrequirements
            SET
            mark = %s,
            notes = %s,
            note2=%s
            WHERE id = %s; 
            ''',[
            request.data["mark"],
            request.data["notes"],
            request.data["note2"],
            request.data["id"]])

            desc = cursor.description
            return Response({"mark":request.data["mark"],
                        "comments":request.data["notes"],
                        "refactored":request.data["note2"],
                        "id":request.data["id"]})
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)

    


@csrf_exempt
@api_view(['POST', ])
def getAllBasicRequirments_view(request):
   
    permission_classes = (permissions.IsAuthenticated,)
    try:
        if request.data["cohort_id"] :
            cursor = connection.cursor()
            cursor.execute('''SELECT 
            rbkbackend.basicrequirements.id,
            rbkbackend.cohort.name as cohort_name,
            rbkbackend.basicrequirements.notes,
            rbkbackend.basicrequirements.note2,
            rbkbackend.basicrequirements.mark,
            concat(g.first_name , " ", g.Last_name) as staff_name,
            concat(d.first_name , " ", d.Last_name) as student_name ,
			v.title as subject
            FROM rbkbackend.basicrequirements
            right join rbkbackend.cohort on rbkbackend.basicrequirements.cohort_id = rbkbackend.cohort.id
            right join rbkbackend.accounts_newuser  as g on g.id = rbkbackend.basicrequirements.staff_name_id
            right join rbkbackend.accounts_newuser as d on d.id = rbkbackend.basicrequirements.student_name_id
            right join rbkbackend.subjects as v on v.id = rbkbackend.basicrequirements.subject_id
            where rbkbackend.basicrequirements.cohort_id=%s
            order by 
            rbkbackend.basicrequirements.student_name_id ASC, rbkbackend.basicrequirements.subject_id ;    
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
    


            
    
          
  