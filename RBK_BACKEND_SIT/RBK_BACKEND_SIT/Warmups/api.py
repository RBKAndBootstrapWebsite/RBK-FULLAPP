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


@csrf_exempt
@api_view(['POST', ])
def getAllWarmUps_view(request):
    print(request.data["is_staff"])
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
               
                g.first_name as staff_name,
              
                d.first_name as student_name 
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
            print(desc)
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
            return Response(data)
        else :
            raise ValidationError

    except NewUser.DoesNotExist:
        return Response(status=HTTPStatus.BAD_REQUEST)

    return Response(status=HTTPStatus.FORBIDDEN)
    


            
    
          
  