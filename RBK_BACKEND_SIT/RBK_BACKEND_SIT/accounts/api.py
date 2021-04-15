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

@csrf_exempt
@api_view(['POST', ])
def getUserData_view(request):
    permission_classes = AllowAny

    try:
        if request.data["email"]:
            cursor = connection.cursor()
            cursor.execute('''SELECT * 
            FROM rbkbackend.accounts_newuser
            join rbkbackend.cohort_user 
            on newuser_id = accounts_newuser.id 
            where accounts_newuser.email=%s ;
            ''',[request.data['email']])

            desc = cursor.description
            print(desc)
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    except NewUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    