from django.urls import path
from project_manage.views import views_project, views_module

urlpatterns = [
    # 项目管理
    path('', views_project.project),
    path('project_add/', views_project.project_add),
    path('project_edit/<int:pid>/', views_project.project_edit),
    path('project_delete/<int:pid>/', views_project.project_delete),

    # 模块管理
    path('module/', views_module.module),
    path('module_add/', views_module.module_add),
    path('module_edit/<int:mid>/', views_module.module_edit),
    path('module_delete/<int:mid>/', views_module.module_delete),
]
