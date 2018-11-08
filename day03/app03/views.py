from django.db.models import Avg, Sum, Q, F
from django.http import HttpResponse
from django.shortcuts import render
from .models import  Humen
# Create your views here.

# 求钱大于10050的人的平均年纪,聚合函数
def get_data(req):

    # humens = Humen.objects.filter(money__gt=10050)
    # avg_age = humens.aggregate(Avg('age'))
    # return  HttpResponse(avg_age.get('age__avg'))

    humens = Humen.objects.filter(money__gt=10050)
    avg_age = humens.aggregate(Sum('age'))
    return  HttpResponse(avg_age.get('age__sum'))


#获取金钱大于10050或者年纪小于10岁的人，Q对象
def get_data_by_q(req):
    # data  = Humen.objects.filter(Q(age__lt=10) | Q(money__gte=10050))

    #id小于10，年纪大于10
    # data  = Humen.objects.filter(id__lt = 10,age__gt=10)
    data  = Humen.objects.filter(Q(id__lt = 10) & Q(age__gt=10))
    return  render(req,'humens.html',{'humens':data})


#自己的年纪大于自己的编号，F对象
def get_data_by_f(req):
    # data = Humen.objects.filter(age__gt=F('id'))
    data = Humen.objects.filter(age__gt=F('money'))
    res = Humen.new_objects.create_girl("赵丽颖")
    print(res)
    return render(req, 'humens.html', {'humens': data})


#自己年纪小于编号的平均年纪
def exercise(req):
    data = Humen.objects.filter(age__lt=F("id")).aggregate(Avg("age"))
    return HttpResponse(data.get("age__avg"))


#数据表的删除,先查询，再用delete函数删除
def delete_humen(req):
    #解析参数
    param = req.GET
    h_id = param.get("h_id")
    h_id = int(h_id)
    #数据查询及删除
    # obj = Humen.objects.get(pk=h_id).delete()

    objs = Humen.objects.filter(id__lt = h_id).delete()
    return  HttpResponse("删除成功")


#数据表的更新(1)先查询得到数据，在修改数据，用sava保存
        # (2)用update方法,可以修改多个
def updata_humen(req):
    #解析参数
    new_name = req.GET.get('name')
    #拿到数据集合的第一个
    # obj = Humen.objects.all().first()
    # obj.name = new_name
    # obj.save()

    data = {
        'name':new_name,
        'age':1000
    }
    res = Humen.objects.filter(id = 6).update(**data)
    return  HttpResponse("更新成功")