from django.urls import path
from project_manage.views import views_manage

urlpatterns = [
    # 项目管理
    path('', views_manage.manage),
    path('project_add/', views_manage.project_add),
    path('project_edit/<int:pid>/', views_manage.project_edit),
    path('project_delete/<int:pid>/', views_manage.project_delete),
]
