"""itest_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from project_manage.views import views_login
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views_login.index),
    path('index/', views_login.index),
    path('manage/', include('project_manage.urls')),
    path('logout/', views_login.logout),

    # 用例管理
    path('case/', include('case_manage.urls')),

    # 接口的管理

    path('api/', include('api_manage.urls'))
]
