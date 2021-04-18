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
def getStudentCohortdaysOfTheWeek_view(request):
    permission_classes = (permissions.IsAuthenticated,)
    try:
        if request.data["cohort"]:
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
            where rbkbackend.activestatus.cohort_id = and rbkbackend.activestatus.dayisActive= true  and rbkbackend.activestatus.weekisActive=true
            ''',[int(request.data['cohort'])])

            desc = cursor.description
            print(desc)
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)
        else:
             return Response(status=HTTPStatus.BAD_REQUEST)

    except NewUser.DoesNotExist:
        return Response(status=HTTPStatus.BAD_REQUEST)

    return Response(status=HTTPStatus.FORBIDDEN)
    
    