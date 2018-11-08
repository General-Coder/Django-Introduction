import os
from django.core.cache import cache



from .other_func import get_unique_str
from django.conf import settings
from django.core.mail import send_mail,send_mass_mail,EmailMessage
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def test_email(req):
    title = "我是晚上练习的"
    msg = '我说晚上练习的主要内容'
    receive = [
        '17625904460@163.com',
        '1574070307@qq.com',
        '1936812210@qq.com'
    ]
    email_from = settings.EMAIL_HOST_USER
    send_mail(title,msg,email_from,receive)
    return HttpResponse('ok')

def mail_html(req):
    title = "我是晚上练习的"
    msg = '我说晚上练习的主要内容'
    receive = [
        '17625904460@163.com',
        '1574070307@qq.com',
        '1936812210@qq.com'
    ]
    email_from = settings.EMAIL_HOST_USER
    templates = loader.get_template('lianxi/templates.html')
    html = templates.render({'title':'欢迎注册','url':'http://www.baidu.com'})
    send_mail(title,msg,email_from,receive,html_message=html)
    return HttpResponse('ok')

def image_mail(req):
    title = "我是晚上练习的"
    msg = '我说晚上练习的主要内容'
    receive = [
        '17625904460@163.com',
        '1574070307@qq.com',
        '1936812210@qq.com'
    ]
    email_from = settings.EMAIL_HOST_USER
    message = EmailMessage(title,msg,email_from,receive)
    filePath = os.path.join(settings.STATICFILES_DIRS[0],'ti对方是否mg.jpg')
    message.attach_file(filePath,'image/jpg')
    message.send()
    return HttpResponse('ok')

def send_many_mail(req):
    title = "我是晚上练习的"
    msg = '我说晚上练习的主要内容'
    receive = [
        '17625904460@163.com',
        '1574070307@qq.com',
        '1936812210@qq.com'
    ]
    email_from = settings.EMAIL_HOST_USER
    message1 = (title,msg,email_from,receive)
    message2 = ('title',msg,email_from,receive)
    send_mass_mail((message1,message2))
    return HttpResponse('ok')


def register(req):
    uuid_str = get_unique_str()
    url = 'http://' + req.get_host() + '/lianxi/previry/' +uuid_str
    title = "我是晚上练习的"
    msg = '我说晚上练习的主要内容'
    receive = ['17625904460@163.com']
    email_from = settings.EMAIL_HOST_USER
    templates = loader.get_template('lianxi/templates.html')
    html = templates.render({'title': '欢迎注册', 'url': url})
    send_mail(title,msg,email_from,receive,html_message=html)
    cache.set(uuid_str,receive[0],60)
    return HttpResponse('ok')

def previry(req,code):
    res = cache.get(code)
    if res:
        return HttpResponse('注册成功')
    else:
        return HttpResponse('验证失败')