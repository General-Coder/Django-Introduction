from celery import task
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.template import loader
from  .my_utils import *
import oss2
from io import BytesIO

@task
def send_verify_mail(url,user_id,reveiver):
    #发送邮件
    title = '欢迎注册'
    content = ''
    templates = loader.get_template('user/email.html')
    html = templates.render({'url':url})
    email_from = settings.EMAIL_HOST_USER
    send_mail(title,content,email_from,[reveiver],html_message=html)
    #设置缓存
    cache.set(url.split('/')[-1],user_id,settings.CACHE_AGE)

@task
def upload_to_oss(f,img_file):
    endpoint = 'http://oss-cn-shanghai.aliyuncs.com'
    access_key_id = 'LTAIYRooVAgBYAyx'
    access_key_secret = 'xieuygrcdHaJFm34Qe9iz5ok3cTP3Y'
    bucket_name = 'zdbuck'
    bucket_name_host = "zdbuck.oss-cn-shanghai.aliyuncs.com"
    # 生成一个认证对象
    auth = oss2.Auth(access_key_id, access_key_secret)
    # 实例化写写入到内存
    buf = BytesIO()
    bucket = oss2.Bucket(auth, endpoint, bucket_name)
    for i in img_file.chunks():
        buf.write(i)
    # 调整文件指针到开头
    buf.seek(0)    # 上传
    bucket.put_object(f, buf.getvalue())


