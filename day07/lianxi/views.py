from django.core.cache import cache
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
import time
from .models import Student

# Create your views here.


EVERY_PAGE_NUM = 5  #分页API每一页显示的数据
@cache_page(30)
def page_num(req):
    # time.sleep(5)
    page = None
    page_num = req.GET.get('page')
    obj = Student.objects.all()
    paginator = Paginator(obj,EVERY_PAGE_NUM)
    try:
        page = paginator.page(page_num)
        result = page.object_list

    except:
       result = []

    data = {
        'data':result,
        'page_range':paginator.page_range,
        'page':page,
        'page_count':paginator.num_pages

    }
    return  render(req,'lianxi/page.html',data)


def my_cache(req):
    #判断是否有缓存
    res = cache.get('data')
    if res:
        print('有缓存')
        return  JsonResponse(res)
    else:
        #查询modle
        data = Student.objects.all()
        #把查询到的对象转换成字典
        c_data = [model_to_dict(i) for i in data]
        #把数据存入缓存
        result = {'my_data':c_data}
        cache.set('data',result,30)
        print('被执行')
        #把界面返回给前端
        return JsonResponse(result)







