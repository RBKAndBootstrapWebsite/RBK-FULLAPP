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
from rest_framework.permissions import AllowAny
from django.core.serializers.json import DjangoJSONEncoder
import itertools
from http import HTTPStatus
from rest_framework.exceptions import ValidationError, ParseError


# --------------------- Delete WarmUps ----------------------------#

@csrf_exempt
@api_view(['POST', ])
def SaveSurvays_view(request):

    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.HTTP_406_NOT_ACCEPTABLE)
    else:
        try:
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO rbkbackend.survey
                            (id
                            title,
                            description,
                            url)
                            VALUES
                            (max())
                            ''',
                    [
                        
                    request.data["title"],
                    request.data["description"],
                    request.data["url"],
                    ])

            cursor.execute('''SELECT LAST_INSERT_ID()''')
            print( desc = cursor.description)    

            desc = cursor.description
            print(cursor.description)
            return Response({
               
                "mark":    request.data["title"],
                "notes":  request.data["description"],
                "cohort_id":  request.data["url"],
            
            })
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)



# --------------------- Delete WarmUps ----------------------------#

@csrf_exempt
@api_view(['POST', ])
def DeleteSurvy_view(request):

    print(request.data["id"])

    print(request.data["cohort_id"])
    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.HTTP_406_NOT_ACCEPTABLE)
    else:
        try:
    
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM 
            rbkbackend.survey_cohort
            WHERE rbkbackend.survey_cohort.cohort_id=%s
            and rbkbackend.survey_cohort.survey_id =%s
            ''',
            [
            request.data["cohort_id"],
            request.data["id"]
            ])

          
            return Response(request.data["id"])
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)


# --------------------- Update WarmUps ----------------------------#

@csrf_exempt
@api_view(['POST', ])
def UpdateSurvys_view(request):
    permission_classes = (permissions.IsAuthenticated,)

    if request.data['is_staff'] ==0:
        return Response(status=HTTPStatus.BAD_REQUEST)
    else :
        try:
    
            cursor = connection.cursor()
            cursor.execute('''UPDATE rbkbackend.survey
            SET
            title = %s,
            description = %s,
            url = %s
            WHERE id =%s; ''',[
            request.data["title"],
            request.data["description"],
            request.data["url"],
            request.data["id"]])

            desc = cursor.description
            return Response({"id":request.data["id"],
                        "title":request.data["title"],
                        "description":request.data["description"],
                        "url":request.data["url"]})
        except :
            return Response(status=HTTPStatus.BAD_REQUEST)

    


@csrf_exempt
@api_view(['POST', ])
def getAllServeysOfaCohort_view(request):
   
    permission_classes = (permissions.IsAuthenticated,)
    try:
        if request.data["cohort_id"] :
            cursor = connection.cursor()
            cursor.execute('''SELECT survey.id,
                survey.title,
                survey.description,
                survey.url
                FROM rbkbackend.survey
                left join rbkbackend.survey_cohort on rbkbackend.survey_cohort.survey_id = rbkbackend.survey.id
                where rbkbackend.survey_cohort.cohort_id=%s
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
    


            
    
          
  