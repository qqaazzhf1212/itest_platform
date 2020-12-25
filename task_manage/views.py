from django.shortcuts import render
from task_manage.models import Task


# Create your views here.
def task_lists(request):
    '''
    返回任务列表
    :param request:
    :return:
    '''
    task = Task.objects.all()
    context = {
        'tasks': task,
    }
    return render(request, 'task.html', context=context)


def task_add(request):
    return render(request, "task/add.html")


def task_edit(request, tid):
    print(tid)
    return render(request, "task/edit.html")


def task_delete(request, tid):
    pass


def running(request, tid):
    pass
