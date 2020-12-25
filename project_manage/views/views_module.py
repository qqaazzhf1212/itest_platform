from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_manage.models import Project, Module
from project_manage.form import ProjectForm, ModuleForm


# 不允许直接进入页面
@login_required
def module(request):
    '''
    模块管理页面
    '''
    username = request.session.get('user', '')
    module = Module.objects.all()
    return render(request, "module.html", {"user": username, "module": module})


@login_required
def module_add(request):
    '''
    模块添加
    '''
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project = form.cleaned_data['project']
            Module.objects.create(name=name, describe=describe, project=project)
            return HttpResponseRedirect('/manage/module/')
    else:
        form = ModuleForm()
        username = request.session.get('user', '')
        return render(request, "module/module_add.html", {"user": username, "form": form})


@login_required
def module_edit(request, mid):
    username = request.session.get('user', '')
    if request.method == "POST":
        # 更新已经提交的数据
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = Module.objects.get(id=mid)
            module.name = form.cleaned_data['name']
            module.describe = form.cleaned_data['describe']
            module.project = form.cleaned_data['project']
            module.save()
            return HttpResponseRedirect('/manage/module/')
    else:
        # 打开表单页面，把旧的需要编辑的数据写入表单里面
        if mid:
            try:
                m = Module.objects.get(id=mid)
                form = ModuleForm(instance=m)
                return render(request, "module/module_edit.html", {"user": username, "form": form, "mid": mid})
            except Module.DoesNotExist:
                return HttpResponseRedirect('/manage/module/')


@login_required
def module_delete(request, mid):
    """
    删除项目
    """
    if request.method == "GET":
        try:
            m = Module.objects.get(id=mid)
            m.delete()
            return HttpResponseRedirect('/manage/module/')
        except Module.DoesNotExist:
            return HttpResponseRedirect('/manage/module/')
    else:
        return HttpResponseRedirect('/manage/module/')
