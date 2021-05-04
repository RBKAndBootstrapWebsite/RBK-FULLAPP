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

@csrf_exempt
@api_view(['POST', ])
def getAllSubjectsLectures(request):
    permission_classes = (permissions.IsAuthenticated,)
    try:
        if request.data["subjectList"]!=[]  and request.data["is_staff"]:
            cursor = connection.cursor()
            cursor.execute('''SELECT *
            FROM rbkbackend.lectures 
            where lectures.subject_id in %s;

            ''',[request.data['subjectList']])

            desc = cursor.description
        
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)
        else:
            cursor = connection.cursor()
            cursor.execute('''SELECT *
            FROM rbkbackend.lectures 
            ''')

            desc = cursor.description
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)

    except NewUser.DoesNotExist:
        return Response(status=HTTPStatus.BAD_REQUEST)

    return Response(status=HTTPStatus.FORBIDDEN)
    
    