from django.http import HttpResponse
from django.shortcuts import render
from  .models import *
from  app02.models import *

# Create your views here.

def add_ap1(req):
    ap2 = ap1.objects.create(
        username='zd'
    )
    ap2.save()
    return HttpResponse('OK')

def add_ap2(req):
    ap1 = ap2.objects.create(
        first_name = 'zd',
        last_name = 'xk',
        birth_date = '2018-11-3'
    )
    ap1.save()
    return HttpResponse('ok')

def add_ap3(req):
    ap1 = ap3.objects.create(
        first_name = 'zd',
        last_name = 'xk',
        birth_date = '2018-11-3'
    )
    ap1.save()
    return HttpResponse('ok')
