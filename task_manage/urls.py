from django.urls import path
from task_manage import views

urlpatterns = [
    # 用例管理
    path('', views.task_lists),
    path('add/', views.task_add),
    path('edit/<int:tid>/', views.task_edit),
    path('delete/<int:tid>/', views.task_delete),
    path('running/<int:tid>/', views.running),
]
