from django.shortcuts import render
from django.http import JsonResponse
from project_manage.models import Project, Module
import requests
import json
from case_manage.models import TestCase
from django.forms.models import model_to_dict
from task_manage.models import TaskCase, Task


# Create your views here.

def debug(request):
    '''
    json数据的传输
    '''
    if request.method == "POST":

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
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": "接口返回结果"})


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


def add_case(request):
    '''
    保存测试用例
    '''
    if request.method == "POST":
        req_url = request.POST.get('req_url', '')
        req_method = request.POST.get('req_method', '')
        req_par = request.POST.get('req_par', '')
        req_type = request.POST.get('req_type', '')
        assert_result = request.POST.get('assert_result', '')
        assert_text = request.POST.get('assert_text', '')
        case_cmodule = request.POST.get('case_cmodule', '')
        case_name = request.POST.get('case_name', '')

        if (req_url == "" or req_method == "" or req_par == "" or
                req_type == "" or assert_result == '' or case_cmodule == '' or
                case_name == '' or assert_text == ''):
            return JsonResponse({"code": 10101, "msg": "账号密码不能为空", "data": ""})

        # req_par_data = json.loads(req_par)

        if req_method == "GET":
            req_method = 1
        elif req_method == "POST":
            req_method = 2
        else:
            return JsonResponse({"code": 10103, "msg": "method请求方法不支持", "data": ""})

        if req_type == "data":
            req_type = 1
        elif req_type == "json":
            req_type = 2
        else:
            return JsonResponse({"code": 10104, "msg": "请求方法不支持", "data": ""})

        # module_obj = Module.objects.get(id=case_cmodule)

        TestCase.objects.create(
            name=case_name,
            url=req_url,
            method=req_method,
            request_type=req_type,
            request_body=req_par,
            response=assert_result,
            response_assert=assert_text,
            module_id=case_cmodule,
        )
        return JsonResponse({"code": 200, "msg": "success", "data": []})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": "[]"})


def get_case_info(request, cid):
    '''获取用例的信息'''
    print("cid-->", cid)
    if request.method == "GET":
        try:
            case = TestCase.objects.get(id=cid)

        except TestCase.DoesNotExist:
            return JsonResponse({"code": 401, "msg": "用例信息不存在 ", "data": "[]"})
        try:
            print("模块id", case.module_id)
            module = Module.objects.get(id=case.module_id)
            print("项目id", module.project_id)

        except Module.DoesNotExist:
            return JsonResponse({"code": 200, "msg": "模块信息不存在", "data": "[]"})

        case_dict = model_to_dict(case)
        case_dict["project"] = module.project_id
        print(case_dict)
        return JsonResponse({"code": 200, "msg": "add success", "data": case_dict})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": "[]"})


def get_case_tree(request, tid):
    '''
    返回项目模块的树
    '''
    if request.method == "GET":
        if tid != 0:
            cases_list = []
            cases = TaskCase.objects.filter(task_id=tid)
            for c in cases:
                cases_list.append(c.case)

        data_list = []
        projects = Project.objects.all()
        for p in projects:
            project_dict = {
                "id": p.id,
                "name": p.name,
                "children": []
            }
            modules = Module.objects.filter(project=p)
            for m in modules:
                module_dict = {
                    "id": m.id,
                    "name": m.name,
                    "children": []
                }
                if tid == 0:
                    cases = TestCase.objects.filter(module=m)
                    for c in cases:
                        case_dict = {
                            "id": c.id,
                            "name": c.name,
                            "checked": False
                        }
                        module_dict["children"].append(case_dict)
                else:
                    cases = TestCase.objects.filter(module=m)
                    for c in cases:
                        if c.id in cases_list:
                            case_dict = {
                                "id": c.id,
                                "name": c.name,
                                "checked": True
                            }
                            print("---", c.id)
                        else:
                            case_dict = {
                                "id": c.id,
                                "name": c.name,
                                "checked": False
                            }
                        module_dict["children"].append(case_dict)

                project_dict["children"].append(module_dict)
            data_list.append(project_dict)
        return JsonResponse({"code": 200, "msg": "success", "data": data_list})
    else:
        return JsonResponse({"code": 400, "msg": "请求方法错误", "data": ""})


def task_add(request):
    if request.method == "POST":
        task_name = request.POST.get("task_name", "")
        task_desc = request.POST.get("task_desc", "")
        task_cases = request.POST.get("task_cases", "")
        print(task_cases)
        print(task_name)
        if task_name == "":
            return JsonResponse({"code": 404, "msg": "success", "data": "任务名不能为空"})

        cases_list = json.loads(task_cases)
        if cases_list is []:
            return JsonResponse({"code": 404, "msg": "success", "data": "请选择用例"})
        task = Task.objects.create(name=task_name, describe=task_desc)
        print('===', task.id)
        for case in cases_list:
            TaskCase.objects.create(task_id=task.id, case=case)
        return JsonResponse({"code": 200, "msg": "success", "data": "提交成功"})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": "[]"})


def get_task(request, tid):
    if request.method == "GET":
        if tid == "":
            return JsonResponse({"code": '200', "msg": 'taskid is null', 'data': '[]'})
        try:
            task = Task.objects.get(id=tid)
        except Task.DoesNotExist:
            return JsonResponse({"code": '100200', "msg": 'taskid is error', 'data': '[]'})
        task_dict = model_to_dict(task)
        return JsonResponse({"code": '200', "msg": 'success', 'data': task_dict})
    else:
        return JsonResponse({"code": '400', "msg": '请求方法错误', 'data': ''})


def edit_task(request, tid):
    '''
    编辑保存
    '''
    if request.method == "POST":
        task_name = request.POST.get("task_name", "")
        task_desc = request.POST.get("task_desc", "")
        task_cases = request.POST.get("task_cases", "")
        print(task_cases)
        print(task_name)

        if task_name == "":
            return JsonResponse({"code": 404, "msg": "task name is null", "data": "任务名不能为空"})

        cases_list = json.loads(task_cases)
        if cases_list is []:
            return JsonResponse({"code": 404, "msg": "case is null", "data": "请选择用例"})

        # task = Task.objects.create(name=task_name, describe=task_desc)
        task = Task.objects.get(id=tid)
        task.name = task_name
        task.describe = task_desc
        task.save()

        taskcase = TaskCase.objects.filter(task_id=task.id)
        taskcase.delete()

        for case in cases_list:
            TaskCase.objects.create(task_id=task.id, case=case)
        return JsonResponse({"code": 200, "msg": "success", "data": "提交成功"})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": "[]"})
