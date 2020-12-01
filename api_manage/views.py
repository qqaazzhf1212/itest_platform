from django.shortcuts import render
from django.http import JsonResponse
from project_manage.models import Project, Module
import requests
import json


# Create your views here.

def debug(request):
    '''
    json数据的传输
    '''
    if request.method == "GET":
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": "接口返回结果"})

    req_url = request.POST.get("req_url", "")
    req_method = request.POST.get("req_method", "")
    req_par = request.POST.get("req_par", "")
    req_type = request.POST.get("req_type", "")

    # json类型数据转换为字符串
    date_par = json.loads(req_par)
    if request.method == 'GET':
        req_gettxt = requests.get(req_url, params=date_par)
        result = req_gettxt.text

    if request.method == 'POST':
        if req_type == "data":
            req_posttxt = requests.post(req_url, data=date_par)
            result = req_posttxt.text
        if req_type == "json":
            req_posttxt = requests.post(req_url, json=date_par)
            result = req_posttxt.text

    return JsonResponse({"code": 200, "msg": "success", "data": result})


def assert_result(request):
    '''
    断言的验证
    '''
    if request.method == "GET":
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": "接口返回结果"})

    result = request.POST.get("assert_result", "")
    text = request.POST.get("assert_text", "")

    if text in result:
        return JsonResponse({"code": 200, "msg": "success", "data": ""})
    else:
        return JsonResponse({"code": 10102, "msg": "assert fail", "data": ""})


def select_data(request):
    '''
    二级菜单的渲染
    '''
    if request.method == "POST":
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": "接口返回结果"})

    data_list = []
    project = Project.objects.all()
    for p in project:
        project_dict = {
            "id": p.id,
            "name": p.name,
            "moduleList": [],
        }
        # module = Module.objects.filter(project=p)     //查询模块的对象
        module = Module.objects.filter(project_id=p.id)  # 查询模块的id
        print(module)
        for m in module:
            module_dict = {
                "id": m.id,
                "name": m.name,
            }
            project_dict["moduleList"].append(module_dict)
        data_list.append(project_dict)
    return JsonResponse({"code": 200, "msg": "success", "data": data_list})
