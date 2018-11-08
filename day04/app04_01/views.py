from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse

from .models import  Person
# Create your views here.

def index(req):

    return  render(req,'app04_01/index.html')

def show_info(req):
    data = Person.objects.all()
    html = loader.get_template('app04_01/all.html')
    html_str = html.render({"data":data})
    return HttpResponse(html_str)

def new_index(req):
    return  redirect(reverse("app04_01:show_info"))

def new_show_info(req,num):
    num = int(num)
    try:
        obj = Person.objects.get(pk=num)
        data = {
            "name":obj.name,
            "content":obj.content
        }
        return HttpResponse("我是{name}，我的描述{content}".format(**data))
    except BaseException:
        return HttpResponse("没有数据了")

def show_info1(req,num):
    num = int(num)
    try:
        obj = Person.objects.get(pk=num)
        data = {
            "name":obj.name,
            "content":obj.content
        }
        return HttpResponse("我是{name}，我的描述{content}".format(**data))
    except BaseException:
        return HttpResponse("没有数据了")

def demos1(req,num):
    num = int(num)
    obj = Person.objects.all()
    return  render(req,'app04_01/all.html',{"data":obj[10*(num-1):10*num]})