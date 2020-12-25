from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_manage.models import Project, Module
from project_manage.form import ProjectForm, ModuleForm
from case_manage.models import TestCase


# Create your views here.

@login_required
def case_manage(request):
    """
    用例管理
    """
    case = TestCase.objects.all()
    return render(request, 'case.html', {"cases": case})


@login_required
def case_add(request):
    """
    用例添加
    """
    return render(request, 'case/add.html')


@login_required
def case_edit(request, cid):
    """
    用例添加
    """
    return render(request, 'case/edit.html')


@login_required
def case_delete(request, cid):
    """
    用例添加
    """
    return render(request, 'case/edit.html')
