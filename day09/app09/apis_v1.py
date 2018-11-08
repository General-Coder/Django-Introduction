from .models import  Stu
from django.http import JsonResponse, QueryDict
from django.views.generic import  View
from django.forms  import  model_to_dict


class StuAPI(View):

    def get(self,req):
        #返回所有的学生信息
        #1，拿到所有学生信息
        data = Stu.objects.all()
        stus = [model_to_dict(i) for i in data]

        result = {
            'code':1,
            'msg':'ok',
            'data':stus
        }
        return JsonResponse(result)

    def post(self,req):
        #解析参数
        parms = req.POST
        name = parms.get('name')
        age = parms.get('age')
        try:
            age = int(age)
        except TypeError as e:
            result = {
                'code':2,
                'msg':'年纪是数字类型',
                'data':None
            }
            return  JsonResponse(result)
        #创建对象
        stu = Stu.objects.create(
            name=name,
            age = age
        )
        #返回结果
        result = {
            'code':1,
            'msg':'ok',
            'data':model_to_dict(stu)
        }
        return  JsonResponse(result)

    def delete(self,req):
        #解析参数
        params = QueryDict(req.body)
        try:
            id = int(params.get('s_id'))
            #查询数据
            stu = Stu.objects.get(pk = id)
            stu.delete()
            return  JsonResponse({
                'code':1,
                'msg':'deleted',
                'data':id
            })
        except TypeError as e:
            result = {
                'code':2,
                'msg':'s_id是数字类型',
                'data':None
            }
            return  JsonResponse(result)



class TestAPI(View):
    def post(self,req):
        parms = req.POST
        name = parms.get('name')
        age = int(parms.get('age'))
        stu = Stu()
        stu.name = name
        stu.age = age
        stu.save()
        return JsonResponse({'msg':'ok'})

