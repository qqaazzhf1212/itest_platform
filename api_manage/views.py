from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def debug(request):
    return JsonResponse({"code": 200, "msg": "success", "data": ["接口返回结果"]})
 