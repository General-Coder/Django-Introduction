from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.db import  connection,transaction

# Create your views here.

#一对一关系
# 通过人名拿身份证号
def get_idcard_by_humen(req):
    # 有个人
    humen = Person.objects.get(pk=1)
    # 访问身份证的数据
    num = humen.idcard.num
    return HttpResponse(num)


# 通过身份证号拿人名,一对一关系的反向查询
def get_humen_by_idcard(req):
    idcard = IdCard.objects.get(pk=1).num
    obj = IdCard.objects.get(num=idcard)
    # 反向查询，类名小写
    humen_name = obj.person.name
    return HttpResponse(humen_name)


# 跨关系查找，查身份证的签发单位是呵呵的人名
def get_humen_v1(req):
    obj = Person.objects.filter(idcard__addr__contains="呵")
    print(obj)
    return HttpResponse("ok")


# 删除
def delete_humen(req):
    #删除人
    # humen = Person.objects.get(pk=1)
    # humen.delete()


    #删除身份证,人也消失
    IdCard.objects.get(pk=2).delete()
    return  HttpResponse("删除成功")




#一对多关系
#通过学生查班级
def get_grade_by_stu(req):
    stu = Students.objects.get(pk=1)
    return HttpResponse(stu.grade.name)

#通过班级查询学生
def get_stu_by_grade(req):
    grade = Grade.objects.get(pk=1)
    #学生类名小写_set_all()
    obj = grade.students_set.all()
    print(obj)
    return  HttpResponse(obj)




#多对多关系
#通过书查询作者，正向查询
def get_author_by_book(req):
    book = Book.objects.get(pk =3)
    # res = book.author.all()
    res = book.author.filter(name="鲁迅")
    return  HttpResponse(res)


#通过作者查书，反向查找
def get_book_by_author(req):
    author = Author.objects.get(pk = 1)
    res = author.book_set.all()
    return  HttpResponse(res)

def get_raw_grade(req):
    obj = Grade.objects.raw('select * from app03_1_grade;')
    for i in obj:
        print(i)
    return HttpResponse('ok')

def get_raw_grade1(req):
    obj = Grade.objects.raw('select * from app03_1_grade where id >2 ;')[0]
    print(obj)
    return HttpResponse('ok')

def get_raw_grade2(req):
    obj = Grade.objects.raw('select * from app03_1_grade limit 1 ;')[0]
    print(obj)
    return HttpResponse('ok')

