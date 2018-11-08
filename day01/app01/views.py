from django.shortcuts import render,HttpResponse
from  .models import Humen
# Create your views here

def hello(req):
    return  HttpResponse("hello world")

def index(req):
    return render(req,'app01/index.html')

def get_humen(req):
    data = Humen.objects.all()
    return  render(req,'app01/humen.html',{'humen':data})

def hehe(req):
    parms = req.GET
    print(parms.get("data"))
    print(parms.get("msg"))
    return  HttpResponse("呵呵")

def search_women(req):
    parms = req.GET
    name = parms.get('name')
    yz = int(parms.get('yz'))
    age = int(parms.get('age'))
    money = int(parms.get('money'))

    if money >= 1000 and yz >= 80 and age >= 18 and age <= 22:
        return  HttpResponse("我好中意你")
    elif yz > 80 and age > 18 and age < 22 and money < 1000:
        return  HttpResponse("喜得好人卡")
    else:
        return  HttpResponse("呵呵")