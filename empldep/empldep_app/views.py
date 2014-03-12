import json
from django.core import serializers
from django.http import HttpResponse
from .models import Department, Employee


def users_json(request):
    users = Employee.objects.all()
    res = []
    for user in users:
        res.append({'user': user.last_name, 'department': user.department})
    data = json.dumps(res)
    return HttpResponse(data, 'application/json')


def user_json(request, user_id):
    users = Employee.objects.all()
    data = serializers.serialize("json", users)
    return HttpResponse(data, content_type='application/json')