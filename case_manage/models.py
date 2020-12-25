from django.db import models

# Create your models here.
from project_manage.models import Module


class TestCase(models.Model):
    '''
    测试用例
    '''
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=50, null=False)
    url = models.TextField('URL', null=False)
    method = models.IntegerField('请求方式', null=False)  # 1:GET 2:POST 3:PUT 4:DELETE
    request_type = models.IntegerField('参数类型', null=False)  # 1:form-data 2:json
    request_body = models.TextField('参数内容', null=False)
    response = models.TextField('结果', null=False)
    # response_type = models.IntegerField('断言类型', null=False)
    response_assert = models.TextField('断言', null=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name
