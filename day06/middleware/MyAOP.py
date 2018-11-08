import random
from django.http import HttpResponse,HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin



class YJMiddleWare(MiddlewareMixin):
    def process_request(self, req):
        # name = req.GET.get('name')
        # if name == "tom":
        #     return HttpResponse("恭喜获得特斯拉一辆")
        # elif name == 'zd':
        #    return HttpResponse("特斯拉模型一辆")
        # elif name == "班长":
        #     return  HttpResponse("咖妃")

        black_ip = []
        #获取ip
        ip = req.META.get('REMOTE_ADDR')
        if ip in black_ip:
            return HttpResponseForbidden("黑名单成员 无法访问")
        else:
            return HttpResponse("欢迎进入真人赌场，体验美女荷官")




