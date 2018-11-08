from django.http import JsonResponse,HttpResponse,HttpResponseNotAllowed
from django.shortcuts import render,reverse,redirect
import json

# Create your views here.

def play(req):
    return render(req, '2048.html')

def json_test(req):
    data = {
        'code':1,
        'msg':'呵呵呵ok',
        'data':[1,2,3,4,23,2]
    }
    print('请求方法：',req.method)
    print('host：',req.get_host())
    print('GET：',req.GET)
    print('POST：',req.POST)
    print('files：',req.FILES)
    # print('meta：',req.META)
    return JsonResponse(data)
    # return HttpResponse(json.dumps(data))

def test_res(req):
    #实例化
    response = HttpResponse()
    # 设置返回内容
    response.content = "完美"
    #设置状态码
    response.status_code = 404
    response.write('我是write写的')
    response.flush()
    response.content='来也匆匆 去也冲冲'
    return response

def mylogin(req):
    if req.method == 'GET':
        return  render(req,'register.html')
    elif req.method == 'POST':
        #做登录操作
        #解析参数
        parms = req.POST
        name = parms.get('uname')
        pwd = parms.get('pwd')
        #假设有校验并且通过了
        #登录 重定向到首页
        response = redirect(reverse('app05:index'))
        response.set_cookie('user',name,max_age=30)

        #也设置session
        req.session['pwd'] = pwd
        req.session.set_expiry(30)
        return  response
    else:
        return HttpResponseNotAllowed("请求方式不被允许")

def index(req):
    u_name = req.COOKIES.get('user')
    u_name = u_name if u_name else '游客'
    #获取session
    res = req.session.get('pwd')
    print('session的结果',res)
    return render(req,'index.html',{'username':u_name})

def mylogout(req):
    response = redirect(reverse('app05:index'))
    #删除cookie
    response.delete_cookie('user')
    del req.session['pwd']
    return response