import os
from django.conf import settings
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect,reverse
from app06.models import MyUser
from .models import Cartoon
import uuid,hashlib




from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def index(req):
    user= req.user
    uname =  user.username if user.username else '游客'
    return render(req,'lianxi/index.html',{'user_name':uname})


def register(req):
    if req.method == "GET":
        return render(req,'lianxi/register.html')
    else:
        name = req.POST.get("user_info")
        phone = req.POST.get('phone')
        email = req.POST.get('email')
        pwd = req.POST.get('pwd')
        pwd1 = req.POST.get('pwd1')
        if len(name) >0 and pwd==pwd1 and len(pwd)>4:
            MyUser.objects.create_user(
                username=name,
                phone=phone,
                email=email,
                password=pwd
            )
            return HttpResponse("注册成功")
        else:
            return HttpResponse("输入有误")

def my_login(req):
    if req.method == "GET":
        return render(req, 'lianxi/login.html')
    else:
        name = req.POST.get("user_info")

        pwd = req.POST.get('pwd')
        user = authenticate(username=name, password=pwd)
        if user:
            login(req,user)
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("输入有误")

def middle(req):
    if req.method == "GET":
        return render(req, 'lianxi/middle.html')
    else:
        name = req.POST.get("user_info")
        pwd = req.POST.get('pwd')
        return HttpResponse("欢迎{}来到优酷".format(name))

def cortoon(req):
    if req.method == "GET":
        return render(req,'lianxi/cortoon.html')
    else:
        name = req.POST.get('name')
        cover = req.FILES.get('cover')
        car = Cartoon()
        car.name=name
        car.cover=cover
        car.save()
        # cart = Cartoon.objects.create(
        #     name=name,
        #     cover=cover
        # )
        return HttpResponse('ok')

def upload(req):
    uuid_str = str(uuid.uuid4()).encode('utf8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    m = md5.hexdigest()
    if req.method == "GET":
        return render(req,'lianxi/cortoon.html')
    else:
        name = req.POST.get('name')
        cover = req.FILES.get('cover')

        fileName = m + "." + cover.name.split('.')[-1]
        filePath = os.path.join(
            settings.MEDIA_ROOT,fileName
        )
        with open(filePath,'wb') as f:
            for info in cover.chunks():
                f.write(info)
        return HttpResponse('ok')



