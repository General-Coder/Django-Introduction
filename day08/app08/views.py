import os
from django.core.cache import cache
import logging
from .my_util import get_unique_str
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage,send_mass_mail
from django.template import loader
# Create your views here.

#实例化一个日志对象
log = logging.getLogger('django')

def test(req):
    log.info('冒烟 先关电')

    return HttpResponse('收工')


def test_mail(req):
    title = '来自django的问候'
    msg = '今天是个好日子'
    receives = [
        '1574070307@qq.com',
        '17625904460@163.com',
        '412651598@qq.com'
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(title,msg,email_from,receives)
    return HttpResponse('ok')


def send_html(req):
    title = '沙漠骆驼'
    #有html才行  先加载  后渲染
    #在发送邮件
    template = loader.get_template('app08/email_template.html')
    html = template.render({'title':'变聪明了',
                            'url':'http://www.mobiletrain.org/?pinzhuanbdtg=biaoti'})
    receives = [
        '1574070307@qq.com',
        '17625904460@163.com',
        '412651598@qq.com',
        '1084633674qq.com'
    ]
    email_from = settings.DEFAULT_FROM_EMAIL

    send_mail(title, '', email_from, receives,html_message=html)

    return HttpResponse('ok')

def file_email(req):
    title = '送你一个大妹子'
    msg = '清纯可爱'
    receives = [
        '1574070307@qq.com',
        '17625904460@163.com',
        '412651598@qq.com',
        '1084633674qq.com'
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    message = EmailMessage(title,msg,email_from,receives)
    file_path = os.path.join(settings.STATICFILES_DIRS[0],'ti对方是否mg.jpg')

    message.attach_file(file_path,'image/jpg')
    message.send()
    return HttpResponse('ok')


def send_many_msg(req):
    receives = [
        '1574070307@qq.com',
        '17625904460@163.com',
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    msg1 = ('标题','张定哈哈哈',email_from,receives)
    msg2 = ('标题2','张定呵呵呵',email_from,receives)
    send_mass_mail((msg1,msg2))
    return HttpResponse('ok')


def send_verify_mail(req):
    uuid_str = get_unique_str()
    url = 'http://' + req.get_host() + '/app08/verify/' + uuid_str
    #加载模板，然后渲染
    template = loader.get_template('app08/email_template.html')
    html = template.render({'title':'你是个逗比','url':url})
    title = '呵呵'
    user_emal = '17625904460@163.com'
    receives = [
        user_emal
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(title,'',email_from,receives,html_message=html)
    #设置缓存
    cache.set(uuid_str,user_emal,settings.VERIFY_CODE_MAX_AGE)

    return HttpResponse('注册成功，请注意查收邮件')

def verify(req,code):
    #去缓存拿数据
    email = cache.get(code)
    if email:
        #找到用户对象,然后更新用户状态字段 is_active=True save()
        return HttpResponse('email'+'验证成功')
    else:
        return HttpResponse('验证无效')


def cz_api(req):
    if req.method == "GET":
        return  render(req,'app08/cz.html')
    else:
        parms = req.POST
        name = parms.get('name')
        num = parms.get('num')

        return HttpResponse('给{}充值{}'.format(name,num))


