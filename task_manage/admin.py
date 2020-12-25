from django.contrib import admin
from task_manage.models import Task, TaskCase


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "status", "create_time"]


class TaskCaseAdmin(admin.ModelAdmin):
    list_display = ["task", "case",  "update_time", "create_time"]


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskCase, TaskCaseAdmin)
