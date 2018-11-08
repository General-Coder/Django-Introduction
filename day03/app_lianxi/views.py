from django.shortcuts import render
from .models import  *
from django.http import  HttpResponse
# Create your views here.

def add_home(req):
    # ho = Home.create_home("汤臣一品")
    # ho.save()

    ho = Home.homeObj.create_home("恭王府")
    ho.save()
    return HttpResponse("成功")

def get_home_by_humen(req):
    humen =Humen.objects.get(pk = 2)
    obj = humen.jia.name
    return  HttpResponse(obj)

def get_human_by_home(req):
    # home_name = "恭王府"
    # obj = Home.objects.get(name = home_name)
    # humen = obj.humen.name
    humen = Home.objects.filter(humen__name="张定")

    return HttpResponse(humen)

def get_stu_by_grade(req):
    grade = Grade.objects.get(pk =1)
    obj = grade.students_set.all()
    return  HttpResponse(obj)

def get_grade_by_student(req):
    student = Students.objects.filter(pk__lte =3)
    list = []
    for student1 in student:
        data = student1.grade.name
        list.append(data)
    return   HttpResponse(list)

def get_phone_by_xinpian(req):
    xinpian = Xinpian.objects.get(pk =3)
    phone = xinpian.phone_set.all()
    return HttpResponse(phone)

def get_u_by_phone(req):
    phone = Phone.objects.get(pk =1)
    res = phone.u.all()
    return  HttpResponse(res)