from django.db import models


# Create your models here.
class Task(models.Model):
    '''
    测试任务表
    '''
    name = models.CharField("名称", max_length=100, blank=False, default='')
    describe = models.TextField('描述', default='')
    status = models.IntegerField('状态', default=0)  # 0 未执行 、1 执行中、 2、执行完成
    # cases = models.TextField('关联用例', default="")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name


class TaskCase(models.Model):
    ''''
    模块表
    '''
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    case = models.IntegerField('状态', default='')
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
