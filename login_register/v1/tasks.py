import random
from celery import  task
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.template import loader
from .my_until import  get_unique_str


@task
def  send_email_v1(host_name,email,str01):
    uuid_str = get_unique_str()
    url = 'http://' + host_name+ '/v1/verify/' + uuid_str
    # 加载模板，然后渲染
    template = loader.get_template('v1/email_template.html')
    html = template.render({'title': '你是个逗比', 'url': url,'str00':str01})
    title = '欢迎注册，谢谢'
    user_emal = email
    receives = [
        user_emal
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(title, '', email_from, receives, html_message=html)
    # 设置缓存
    cache.set(uuid_str, user_emal, settings.VERIFY_CODE_MAX_AGE)

