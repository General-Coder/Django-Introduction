from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q


# Create your views here.

from django.contrib.auth.hashers import make_password
User = get_user_model()

class MyUserBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(phone=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

backend = MyUserBackend()




def index(req):
    user = req.user
    uname = user.username if user.username else "游客"
    return render(req,'login_app/index.html',{'user_name':uname})



def register(req):
    if req.method == "GET":
        return  render(req,'login_app/register.html')
    else:
        parms = req.POST
        name = parms.get("name")
        pwd = parms.get('pwd')
        phone = parms.get('phone')
        confirm_pwd = parms.get('confirm_pwd')
        if pwd and len(pwd) >=4 and pwd == confirm_pwd:
            #继续校验用户是否存在
            if not User.objects.filter(username=name).exists():
                #创建用户
                user = User.objects.create_user(username=name,
                                                  password=pwd,
                                                  phone=phone)
                return  redirect(reverse('login_app:login'))
        else:
            return  HttpResponse("账号或密码有问题")

def mylogin(req):
    if req.method == "GET":
        return  render(req,'login_app/register.html')
    else:
        parms = req.POST
        name = parms.get("name")
        pwd = parms.get("pwd")
        if len(name) == 0 or len(pwd) == 0:
            return HttpResponse("不能为空")

        user = backend.authenticate(username = name,password = pwd) or backend.authenticate(phone=name,password=pwd)

        if user is None:
            return HttpResponse("账号或密码错误")
        else:
            login(req,user)
            return redirect(reverse('login_app:index'))


def mylogout(req):
    logout(req)
    return redirect(reverse('login_app:index'))

def forget_pwd(req):
    return render(req,'login_app/forget.html')

def forget(req):
    name = req.POST.get("fname")
    #不存在调到注册页面
    if  not User.objects.filter(username=name).exists():
        return  render(req,'login_app/register.html')
    #存在跳转到重置密码页面
    else:
        return render(req,'login_app/forget_pwd.html',{'fname':name})

def reset(req):
    fname = req.POST.get('fname')
    pwd1 = req.POST.get('pwd1')
    pwd2 = req.POST.get('pwd2')
    if pwd1 == pwd2 and len(pwd1) >= 4:
        user = User.objects.get(username=fname)
        user.delete()
        user1 = User.objects.create_user(username=fname, password=pwd1)

        return  render(req,'login_app/skip.html')
    else:
        return HttpResponse("密码输入不规范")