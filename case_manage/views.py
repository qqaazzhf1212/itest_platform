from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_manage.models import Project, Module
from project_manage.form import ProjectForm, ModuleForm


# Create your views here.

@login_required
def case_manage(request):
    """
    用例管理
    """
    return render(request, 'postman.html')
