from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import auth


# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, "index.html")

    # post登录处理
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username, password)

        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名和密码为空"})

        # 数据库验证的账号密码
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 导数据库写session
            response = HttpResponseRedirect("/manage/")
            # response.set_cookie("user", username, 10)  # 设置cookies的失效时间
            request.session['user'] = username
            return response
        else:
            return render(request, "index.html", {"error": "用户名密码错误"})


def logout(request):
    # 退出操作
    auth.logout(request)
    return HttpResponseRedirect("/index/")
