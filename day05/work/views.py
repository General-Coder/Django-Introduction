from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from login_app.models import MyUser


User = get_user_model()

# Create your views here.
class MyUserBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

backend = MyUserBackend()


def index(req):
    user = req.user
    uname = user.username if user.username else "游客"
    return render(req,'work/index.html',{'username':uname})

def login(req):
    if req.method == "GET":
        return render(req,'work/register.html')
    elif req.method == "POST":
        name = req.POST.get("user")
        pwd = req.POST.get("pwd")
        if len(name) == 0 or len(pwd) == 0:
            return HttpResponse("用户名或密码不能为空")
        user = backend.authenticate(username=name,password=pwd)
        if user is None:
            return  HttpResponse("用户名不存在")
        else:
            login(user)
            return redirect(reverse('work:index'))
    else:
        return HttpResponse("请求方式不正确")

def register(req):
    if req.method == "GET":
        return render(req,'work/register.html')
    elif req.method == "POST":
        user = req.POST.get("user")
        email = req.POST.get("email")
        pwd = req.POST.get("pwd")
        pwd1 = req.POST.get("pwd1")
        if pwd == pwd1 and len(pwd) >=4 and len(user)>3:
            if not User.objects.filter(username = user).exists():
                user1 = User.objects.create_user(
                    username=user,
                    email=email,
                    password=pwd
                )
                return redirect(reverse('work:login'))
            else:
                return  HttpResponse("用户已存在")
        else:
            return  HttpResponse("输入格式不对")
    else:
        return HttpResponse("请求方式错误")
