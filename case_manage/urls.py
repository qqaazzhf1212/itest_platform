from django.urls import path
from case_manage import views

urlpatterns = [
    # 用例管理
    path('', views.case_manage),

    path('case_add/', views.case_add),
    path('case_edit/<int:cid>/', views.case_edit),
    path('case_delete/<int:cid>/', views.case_delete),
]
