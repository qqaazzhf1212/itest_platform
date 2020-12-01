from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_manage.models import Project, Module
from project_manage.form import ProjectForm


# 不允许直接进入页面
@login_required
def project(request):
    '''
    项目管理页面
    '''
    username = request.session.get('user', '')
    projects = Project.objects.all()
    return render(request, "manage.html", {"user": username, "projects": projects})


# 不允许直接进入页面
@login_required
def project_add(request):
    '''
    项目添加
    '''
    print(request.method)

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name, describe=describe, status=status)
            return HttpResponseRedirect('/manage/')
    else:
        form = ProjectForm()
        username = request.session.get('user', '')
        return render(request, "project/add.html", {"user": username, "form": form})


@login_required
def project_edit(request, pid):
    username = request.session.get('user', '')
    print("pid", pid)
    if request.method == "POST":
        # 更新已经提交的数据
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.get(id=pid)
            project.name = form.cleaned_data['name']
            project.describe = form.cleaned_data['describe']
            project.status = form.cleaned_data['status']
            project.save()
        return HttpResponseRedirect('/manage/')
    else:
        # 打开表单页面，把旧的需要编辑的数据写入表单里面
        if pid:
            try:
                p = Project.objects.get(id=pid)
                form = ProjectForm(instance=p)
                return render(request, "project/edit.html", {"username": username, "form": form, "pid": pid})
            except Project.DoesNotExist:
                return HttpResponseRedirect('/manage/')


@login_required
def project_delete(request, pid):
    """
    删除项目
    """
    if request.method == "GET":
        try:
            P = Project.objects.get(id=pid)
            P.delete()
            return HttpResponseRedirect('/manage/')
        except Project.DoesNotExist:
            return HttpResponseRedirect('/manage/')
        else:
            return HttpResponseRedirect('/manage/')
