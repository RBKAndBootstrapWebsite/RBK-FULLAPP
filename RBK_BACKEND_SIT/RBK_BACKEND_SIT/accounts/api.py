from rest_framework import viewsets, permissions
from rest_framework.response import Response
from http import HTTPStatus
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

@csrf_exempt
@api_view(['POST', ])
def getUserData_view(request):
    permission_classes = (permissions.IsAuthenticated,)
 

    try:
        if request.data["email"]:
            cursor = connection.cursor()
            cursor.execute('''SELECT 
            rbkbackend.accounts_newuser.Last_name, 
            rbkbackend.cohort_user.cohort_id,
            rbkbackend.accounts_newuser.email,
            rbkbackend.accounts_newuser.first_name,
            rbkbackend.accounts_newuser.id,
            rbkbackend.accounts_newuser.is_active,
            rbkbackend.accounts_newuser.is_staff,
            rbkbackend.accounts_newuser.is_superuser,
            rbkbackend.accounts_newuser.id,
            rbkbackend.accounts_newuser.user_name
            FROM rbkbackend.accounts_newuser
            join rbkbackend.cohort_user 
            on newuser_id = accounts_newuser.id 
            where accounts_newuser.email=%s ;
            ''',[request.data['email']])

            desc = cursor.description
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)
        else:
            return Response(status=HTTPStatus.BAD_REQUEST)

    except NewUser.DoesNotExist:
        return Response(status=HTTPStatus.BAD_REQUEST)

    return Response(status=HTTPStatus.FORBIDDEN)

@csrf_exempt
@api_view(['POST', ])
def getStudentsData_view(request):
    permission_classes = (permissions.IsAuthenticated,)
 

    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT 
        CONCAT(first_name , " ",Last_name) as fullName,
        rbkbackend.accounts_newuser.id 
        FROM rbkbackend.accounts_newuser 
        inner join
        rbkbackend.cohort_user 
        on rbkbackend.accounts_newuser.id = rbkbackend.cohort_user.newuser_id 
        where rbkbackend.cohort_user.cohort_id =%s 
        and rbkbackend.accounts_newuser.is_staff=0;
            ''',[request.data['cohort_id']])

        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
        return Response(data)
    except :
        return Response({'data':[]})