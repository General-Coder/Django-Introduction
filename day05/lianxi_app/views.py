from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse,HttpResponse,HttpResponseNotAllowed
# Create your views here.

def No_ne(req):
    return render(req,'lianxi_app/8000.html')

def my_json(req):
    data = {
        "name":"张定",
        'age':23,
        'gender':'男',
        'content':'我是个逗比'
    }
    return  JsonResponse(data)

def test_res(req):
    response = HttpResponse()
    response.content = "完美"
    response.status_code=404
    response.write('我是wrute写的追加')
    response.flush()
    response.content='我来也'
    return  response

def index(req):
    # u_name = req.COOKIES.get('user','游客')
    res = req.session.get('pwd')
    u_name = req.session.get('user','游客')
    return  render(req,'lianxi_app/index.html',{'username':u_name})

def login(req):
    if req.method == "GET":
        return render(req,'lianxi_app/register.html')
    elif req.method == "POST":
        parms = req.POST
        name = parms.get("username")
        pwd = parms.get("pwd")
        response = redirect(reverse('lianxi_app:index'))
        # response.set_cookie('user',name)
        req.session['user'] = name
        req.session['pwd'] = pwd
        return  response

def logout(req):
    response = redirect(reverse('lianxi_app:index'))
    # response.delete_cookie('user')
    del req.session['pwd']
    del req.session['user']
    return  response