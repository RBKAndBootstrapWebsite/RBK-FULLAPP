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
def getStudentCohortWeeks_view(request):
    permission_classes = (permissions.IsAuthenticated,)
    try:
        if request.data["cohort"]:
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
            where rbkbackend.activestatus.cohort_id =%s;
            ''',[int(request.data['cohort'])])

            desc = cursor.description
            print(desc)
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)
        else:
            return Response({"ServerError":"DataNot Found"})
    except NewUser.DoesNotExist:
        return Response({"ServerError":"DataNot Found"})

    