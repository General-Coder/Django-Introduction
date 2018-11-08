import os
from django.conf import settings
from io import BytesIO
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from  django.http import HttpResponse
import random
from .myutil import get_unique_str,get_random_color
import oss2
from .models import *
from PIL import Image,ImageDraw,ImageFont

# Create your views here.

#自定义登录和认证
def my_login(req):
    if req.method=="GET":
        return render(req,'app06/login.html')
    else:
        #解析参数
        parms = req.POST
        user_info = parms.get("user_info")
        pwd = parms.get("pwd")
        code = parms.get('code')
        server_code = req.session.get('verify_code')
        #认证
        user = authenticate(username=user_info,password= pwd)

        #判断是否校验成功

        if user and code and  len(code) > 0 and code.lower() == server_code.lower():
            login(req,user)

            return HttpResponse("登陆成功")
        else:
            return HttpResponse("有错误")

#抽奖api，中间件
def get_prize(req):
    #生成一个随机数
    num = random.randint(1,100)
    if num > 90:
        return HttpResponse('奖金一万块')
    else:
        return HttpResponse("酱油一瓶")

#上传文件
def create_book_v1(req):
    if req.method=="GET":
        return render(req,'app06/mybook.html')
    name = req.POST.get('name')
    myfile = req.FILES.get('icon')

    #实例化一个数据
    book = Book.objects.create(
        name = name,
        icon = myfile
    )
    return HttpResponse('ok')

#上传文件版本2
def create_book_v2(req):
    if req.method=="GET":
        return render(req,'app06/mybook.html')
    else:
        #拿到参数
        name = req.POST.get("name")
        myfile = req.FILES.get('icon')

        #文件路径
        fileName = get_unique_str() + "." + myfile.name.split(".")[-1]
        filePath = os.path.join(settings.MEDIA_ROOT,fileName)
        with open(filePath,'wb') as fp:
            for info in myfile.readlines():
                fp.write(info)
            return HttpResponse("ok")

#阿里云oss上传文件
def upload_to_oss(req):
    if req.method == "GET":
        return render(req,'app06/mybook.html')
    elif req.method == 'POST':
        endpoint = 'http://oss-cn-shanghai.aliyuncs.com'
        access_key_id = 'LTAIYRooVAgBYAyx'
        access_key_secret = 'xieuygrcdHaJFm34Qe9iz5ok3cTP3Y'
        bucket_name = 'zdbuck'
        bucket_name_host = "zdbuck.oss-cn-shanghai.aliyuncs.com"
        #生成一个认证对象
        auth = oss2.Auth(access_key_id,access_key_secret)
        f = req.FILES.get('icon')
        #实例化写写入到内存
        buf = BytesIO()
        bucket = oss2.Bucket(auth,endpoint,bucket_name)
        for i in f.chunks():
            buf.write(i)
        #调整文件指针到开头
        buf.seek(0)
        #上传
        fileNmae = fileName = get_unique_str() + "." + f.name.split(".")[-1]
        bucket.put_object(fileName,buf.getvalue())
        file_url = 'https://' + bucket_name_host + '/'+fileName
        return HttpResponse(file_url)

#验证码
def get_confirm_code(req):
    #画布大小
    img_size = (150,50)
    #画布背景色
    img_color = get_random_color()
    # img_color = (255,0,0)
    # 实例化一个画布
    img = Image.new("RGB",img_size,img_color)

    #实例化一个画笔
    draw = ImageDraw.Draw(img)
    #坐标
    code_xy = (20,20)
    #填充色
    # code_color = (0,255,0)

    #实例化一个字体
    #字体路径
    font_path = os.path.join(settings.STATICFILES_DIRS[0],'fonts/ADOBEARABIC-BOLD.OTF')
    #字体大小
    font_size  =30
    font = ImageFont.truetype(font_path,font_size)

    #画一个字母
    # draw.text(code_xy,'L',font=font,fill=code_color)
    # draw.text(code_xy,'O',font=font,fill=code_color)
    source= 'zxcvbnmlkjhgfdsaqwertyuiop0987654321QWERTYUIOPLKJHGFDSAZXCVBNM'
    res = ''
    for i in range(4):
        #随记出一个字母
        code_color = get_random_color()
        index = random.randint(0,len(source)-1)
        my_str = source[index]
        #生成字符串
        res += my_str
        draw.text((20+30*i,10), my_str, font=font, fill=code_color)
    #画点
    for i in range(500):
        x = random.randint(0,150)
        y = random.randint(0,50)

        draw.point((x,y),fill=get_random_color())
    buf = BytesIO()
    #保存
    img.save(buf,'png')

    #删除画笔
    del draw
    #保存到session
    req.session['verify_code'] = res
    return HttpResponse(buf.getvalue(),content_type='image/png')
