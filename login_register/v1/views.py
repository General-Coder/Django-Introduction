import os
from django.db.models import Q
from .tasks import  send_email_v1
from .models import MyUser
from io import BytesIO
import random
from django.conf import settings
from django.core.cache import cache,caches
from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse, JsonResponse
from PIL import Image,ImageDraw,ImageFont
from .models import MyUser
from .my_until import  get_unique_str,get_random_color
from django.contrib.auth import authenticate, login, logout

# cache_num = caches['num']
# Create your views here.

def index(req):
    user = req.user
    print(user)
    uname = user.username if user.username else "游客"
    return render(req,'v1/index.html',{'user_name':uname})

def register(req):
    if req.method == "GET":
        return  render(req,'v1/register.html')
    else:
        host_name = req.get_host()
        parms = req.POST
        name = parms.get("name")
        email = parms.get('email')
        pwd = parms.get('pwd')
        phone = parms.get('phone')
        confirm_pwd = parms.get('confirm_pwd')
        str00 = '1234567890'
        str01 = ''
        for i in range(6):
            temp = random.randint(0, 9)
            str01 += str00[temp]
        if pwd and len(pwd) >=4 and pwd == confirm_pwd:
            #继续校验用户是否存在
            if not MyUser.objects.filter(username=name).exists():
                #创建用户
                user = MyUser.objects.create_user(username=name,
                                                email=email,
                                                  password=pwd,
                                                  phone=phone)
                req.session['num'] = str01
                req.session.set_expiry(600)
                send_email_v1.delay(host_name,email,str01)
                return HttpResponse('注册成功，请注意查收邮件,点击邮箱正式激活账号')

            else:
                return HttpResponse('用户已存在')
        else:
            return  HttpResponse("账号或密码有问题")



def verify(req,code):
    #去缓存拿数据
    email = cache.get(code)
    if email:
        #找到用户对象,然后更新用户状态字段 is_active=True save()
        user = MyUser.objects.get(email=email)
        user.is_active = True
        user.save()
        return redirect(reverse('v1:verify_num'))
    else:
        return HttpResponse('验证无效')

def verify_num(req):
    if  req.method == "GET":
        return render(req,'v1/verify_num.html')
    else:
        num = req.POST.get('num')
        num1 = req.session.get('num')
        if num == num1:
            data = {
                'code':'1',
                'msg':'ok',
                'data':'/v1/login'
            }
            return JsonResponse(data)
        else:
            data = {
                'code': '2',
                'msg': '验证码错误',
                'data': ''
            }
            return JsonResponse(data)

def my_login(req):
    if req.method=="GET":
        return render(req,'v1/login.html')
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

            return redirect(reverse('v1:index'))
        else:
            return HttpResponse("有错误")

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


def my_logout(req):
    logout(req)
    return redirect(reverse('v1:index'))

def reset_pwd(req):
    if req.method == "GET":
        return render(req,'v1/reset_pwd.html')
    else:
        username = req.POST.get('name')
        pwd = req.POST.get('pwd')
        pwd1 = req.POST.get('pwd1')
        try:
            user = MyUser.objects.get(Q(username=username) |
                                  Q(phone=username) |
                                  Q(email=username))
            if pwd == pwd1:
                user.set_password(pwd)
                user.save()

                return HttpResponse('密码修改成功')

        except:
            return  HttpResponse("用户名不存在")

