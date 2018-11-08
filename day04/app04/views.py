from django.shortcuts import render,redirect
from django.urls import reverse

from .models import *
from django.http import  HttpResponse,HttpResponseRedirect
from django.template import loader
# Create your views here.


#主页接口
def index(req):
    return render(req,'app04/index.html')

#主页跳转所有语言接口,代底层实现机制
def langs(req):

    # 查询语言数据
    data = Language.objects.all()
    # return render(req, 'langs.html', {"langs": data})

    #底层实现
    #先加载模板
    html = loader.get_template('app04/langs.html')
    html_str = html.render({"langs":data})
    # print(html_str)
    return HttpResponse(html_str)


#重定向
def new_index(req):
    print("被执行")
    # return HttpResponseRedirect('/app04/langs')
    # return redirect('/app04/langs')
    #反向解析
    return redirect(reverse('app04:langs'))


#正则的分组，分页
def myindex_with_param(req,p1):
    #得到传入的数字,类型为str（\d）
    # print(p1)
    # print(type(p1))
    try:
        lua = Language.objects.get(pk=int(p1))
        res = '{}的描述是{}'.format(lua.name, lua.desc)
    except (Language.DoesNotExist,Language.MultipleObjectsReturned):
        res = "没有数据了"
    return  HttpResponse(res)


#正则的分组，分页，升级版
def myindex_with_param_v1(req,p2):
    #得到传入的数字,类型为str（\d）
    # print(p1)
    # print(type(p1))
    try:
        lua = Language.objects.get(pk=int(p2))
        res = '{}的描述是{}'.format(lua.name, lua.desc)
    except (Language.DoesNotExist,Language.MultipleObjectsReturned):
        res = "没有数据了"
    return  HttpResponse(res)


#新的重定向
def new_reverse(req):
    # return  redirect(reverse('app04:myindex_with_param',args=(2,)))
    return  redirect(reverse('app04:myindex_with_param_v1',
                             kwargs={"p2":3}))

def home(req):
    return render(req,'app04/hehe.html')