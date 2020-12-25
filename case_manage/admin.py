from django.contrib import admin
from case_manage.models import TestCase


# Register your models here.
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ["module", "name", "url", "method", "request_type", "request_body", "response", "response_assert",
                    "create_time", "update_time"]


admin.site.register(TestCase, TestCaseAdmin)
