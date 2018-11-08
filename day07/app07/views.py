from django.core.cache import cache
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from .models import Company,Engineer
from django.views.decorators.cache import cache_page
from .models import Engineer
from django.core.paginator import Paginator
import time
PEE_PAGE = 5




@cache_page(30)
def get_data(req):
    #假装在拼命搜索数据 超级耗时
    time.sleep(5)
    # 1.解析参数
    page_num = req.GET.get('page')
    # 2.查出所有数据
    data = Engineer.objects.all()
    # 3.实例化一个分页器
    paginator = Paginator(data,PEE_PAGE)
    page = None

    # 4.通过传过来的页码，获取page对象
    try:
        page = paginator.page(page_num)
        # 5.把page里的数据 我们读取出来 然后返回给前端（前端也需要有个页面）
        result = page.object_list
    except:
        result = []
    res = {'data':result,
           'page_range':paginator.page_range,
           'page':page,
           'page_count':paginator.num_pages}
    return render(req,'app07/data.html',res)



def my_cache_test(req):
    #看缓存是否有数据
    res = cache.get('data')
    if res:
        print("有缓存")
        return JsonResponse(res)
    else:
        print('被执行')
        #查询modle
        data = Company.objects.all()
        #把对象转成字典 modletodirc
        # model_to_dict()
        c_data = [model_to_dict(i) for i in data]  #列表生成式
        result = {'my_data':c_data}
        cache.set('data',result,30)
        #返回数据给前端
        return  JsonResponse(result)