from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.generic import View
from .models import *
from .tasks import *


# Create your views here.
class Change_User_API(View):
    def get(self, req):
        user = req.user
        data = {
            'title': '修改用户',
            'uname': user.username
        }
        return render(req, 'user/change_user.html',data)

    def post(self, req):
        user = req.user
        u_tel = req.POST.get('u_tel')
        u_addr = req.POST.get('u_addr')
        print(u_tel, u_addr, user.username)
        user_obj = MyUser.objects.get(username=user.username)
        user_obj.adress = u_addr
        user_obj.phone = u_tel
        user_obj.save()
        result = {
            'code': 1,
            'msg': 'ok',
            'data': '/axf/cart'
        }
        return JsonResponse(result)


def home(req):
    wheels = Wheel.objects.all()
    menus = Nav.objects.all()
    mustbuy = MustBuy.objects.all()
    shops = Shop.objects.all()
    mainshows = MainShow.objects.all()
    result = {
        'title': '首页',
        'wheels': wheels,
        'menus': menus,
        'mustbuy': mustbuy,
        'shop0': shops[0],
        'shop1_3': shops[1:3],
        'shop3_7': shops[3:7],
        'shop_last': shops[7:],
        'mainshows': mainshows,
    }
    return render(req, 'home/home.html', result)


def market(req):
    return redirect(reverse('axf:market_params', args=('104749', '0', 0)))


def market_with_params(req, type_id, sub_type_id, order_type):
    # 获取所有的一级分类

    types = FoodTypes.objects.all()

    # 获取二级分类
    current_cate = types.filter(typeid=type_id)[0]
    childtypenames = current_cate.childtypenames.split('#')
    # sub_types = []
    # for i in childtypenames:
    #     tmp = i.split(':')
    #     sub_types.append(tmp)

    sub_types = [i.split(':') for i in childtypenames]

    # 根据type_id搜索商品信息
    goods = Goods.objects.filter(
        categoryid=int(type_id)
    )

    # 根据二级分类的id，查询数据
    if sub_type_id == '0':
        pass
    else:
        goods = goods.filter(childcid=int(sub_type_id))
    # 添加num属性
    # 知道用户的购物车里的商品对应数量

    NO_SORT = 0
    PRICE_SORT = 1
    SALES_SORT = 2

    if int(order_type) == NO_SORT:
        pass
    elif int(order_type) == PRICE_SORT:
        goods = goods.order_by('price')
    else:
        goods = goods.order_by('productnum')
    user = req.user
    if isinstance(user, MyUser):
        # tem_dict = {}
        # 去购物车查询数据
        # cart_nums = Cart.objects.filter(user=user)
        # for i in cart_nums:
        #     tem_dict[i.goods.id] = i.num
        tem_dict = {i.goods_id: i.num for i in Cart.objects.filter(user=user)}
        for i in goods:
            i.num = tem_dict.get(i.id) if tem_dict.get(i.id) else 0
    result = {
        'title': '闪购',
        'types': types,
        'goods': goods,
        'current_type_id': type_id,
        'sub_types': sub_types,
        'current_sub_type_id': sub_type_id,
        'order_type': int(order_type)
    }
    return render(req, 'market/market.html', result)


@login_required(login_url='/axf/login')
def cart(req):
    # 确定用户
    user = req.user
    # 根据用户，去购物车数据搜索该用户的数据
    data = Cart.objects.filter(user_id=user.id)
    # data = Cart.objects.filter(user = user)
    # 算钱
    # 判断全选按钮的状态,有购物车商品并且没有未被选中的商品存在
    if data.exists() and data.filter(is_selected=True).exists():
        data.filter(is_selected=True).update(is_selected=False)
        is_all_select = False
    else:
        is_all_select = False
    sum_money = get_cart_money(data)
    result = {
        'title': '购物车',
        'uname': user.username,
        'phone': user.phone if user.phone else '暂无',
        'address': user.adress if user.adress else '暂无',
        'cart_items': data,
        'sum_money': sum_money,
        'is_all_select': is_all_select,
    }
    return render(req, 'cart/cart.html', result)


# @login_required(login_url='/axf/login')
def mine(req):
    btns = MineBtns.objects.filter(is_used=True)
    # 拿当前用户
    user = req.user
    is_login = True
    if isinstance(user, AnonymousUser):
        is_login = False
    u_name = user.username if is_login else ''
    try:
        icon = user.icon_url
    except:
        icon = None
    result = {
        'title': '我的',
        'btns': btns,
        'is_login': is_login,
        'u_name': u_name,
        'icon': icon
    }
    return render(req, 'mine/mine.html', result)


class Register_API(View):

    def get(self, req):
        return render(req, 'user/register.html')

    def post(self, req):
        params = req.POST
        icon = req.FILES.get('u_icon')
        name = params.get('u_name')
        pwd = params.get('u_pwd')
        confirm_pwd = params.get('u_confirm_pwd')
        email = params.get('email')
        try:
            fileName = get_unique_str() + "." + icon.name.split(".")[-1]
            file_url = 'https://' + "zdbuck.oss-cn-shanghai.aliyuncs.com" + '/' + fileName
        except:
            # 校验密码
            file_url = None
            fileName = None
        if pwd and confirm_pwd and confirm_pwd == pwd:
            # 判断用户名是否可用
            if MyUser.objects.filter(username=name).exists():
                return render(req, 'user/register.html', {'help_msg': '该用户已存在'})
            else:
                user = MyUser.objects.create_user(
                    username=name,
                    password=pwd,
                    email=email,
                    is_active=False,
                    icon_url=file_url
                )
                # 生成验证连接
                url = 'http://' + req.get_host() + '/axf/confirm/' + get_unique_str()
                # 发送邮件,异步调用
                send_verify_mail.delay(url, user.id, email)
                # 异步上传文件
                upload_to_oss.delay(fileName, icon)
                # 返回登录页面
                return redirect(reverse('axf:login'))


class Login_API(View):

    def get(self, req):
        return render(req, 'user/login.html')

    def post(self, req):
        name = req.POST.get('name')
        pwd = req.POST.get('pwd')
        if not name or not pwd:
            data = {
                'code': 2,
                'msg': '账号或密码不能为空',
                'data': ''
            }
            return JsonResponse(data)
        user = authenticate(username=name, password=pwd)
        if user:
            login(req, user)
            data = {
                'code': 1,
                'msg': 'ok',
                'data': '/axf/mine'
            }
            return JsonResponse(data)
        else:
            data = {
                'code': 3,
                'msg': '账户或密码错误',
                'data': ''
            }
            return JsonResponse(data)


class Logout_API(View):

    def get(self, req):
        logout(req)
        return redirect(reverse('axf:mine'))


def verify_email(req, uuid_str):
    user_id = cache.get(uuid_str)
    if user_id:
        user = MyUser.objects.get(pk=int(user_id))
        user.is_active = True
        user.save()
        return redirect(reverse('axf:login'))
    else:
        return HttpResponse('<h2>链接已失效</h2>')


def check_uname(req):
    # 解析参数
    uname = req.GET.get('uname')
    data = {
        'code': 1,
        'data': ''
    }
    # 判断数据不能是空白，然后去搜索用户
    if uname and len(uname) >= 3:
        if MyUser.objects.filter(username=uname).exists():
            data['msg'] = '账号已存在'
        else:
            data['msg'] = '账号可用'
    else:
        data['msg'] = '用户名过短'
    return JsonResponse(data)


class Cart_API(View):

    def post(self, req):
        # 先看用户是否登录
        user = req.user
        if not isinstance(user, MyUser):
            data = {
                'code': 2,
                'msg': 'not login',
                'data': '/axf/login'
            }
            return JsonResponse(data)
        # 拿参数
        op_type = req.POST.get('type')
        g_id = int(req.POST.get('g_id'))
        # 先获取商品数据
        goods = Goods.objects.get(pk=g_id)
        # 判断是加减操作
        if op_type == 'add':
            # 添加购物车操作
            goods_num = 1
            if goods.storenums > 1:
                cart_goods = Cart.objects.filter(
                    user=user,
                    goods=goods
                )
                if cart_goods.exists():
                    cart_item = cart_goods.first()
                    cart_item.num = cart_item.num + 1
                    cart_item.save()
                    goods_num = cart_item.num
                else:
                    # 是第一次添加
                    Cart.objects.create(user=user, goods=goods)
                data = {
                    'code': 1,
                    'msg': 'ok',
                    'data': goods_num
                }
                return JsonResponse(data)

            else:
                data = {
                    'code': 3,
                    'msg': '库存不足',
                    'data': ''
                }
                return JsonResponse(data)

        elif op_type == 'sub':
            goods_num = 0
            # 先去查购物车的数据
            cart_item = Cart.objects.get(
                user=user,
                goods=goods
            )
            cart_item.num -= 1
            cart_item.save()
            if cart_item.num == 0:
                # 如果减到0 就删除购物车商品
                cart_item.delete()
            else:
                goods_num = cart_item.num
            data = {
                'code': 1,
                'msg': 'ok',
                'data': goods_num
            }
            return JsonResponse(data)


class Cart_Status_API(View):
    def patch(self, req):
        params = QueryDict(req.body)
        c_id = int(params.get('c_id'))
        user = req.user
        # 先拿到和这个人有关系的购物车书库
        cart_items = Cart.objects.filter(user_id=user.id)
        # 拿到c_id对应的数据
        cart_data = cart_items.get(id=c_id)
        # 修改状态,取反
        cart_data.is_selected = not cart_data.is_selected
        cart_data.save()
        # 算钱
        sum_money = get_cart_money(cart_items)
        # 判断是否是全选
        if cart_items.filter(is_selected=False).exists():
            is_all_select = False
        else:
            is_all_select = True
        result = {
            'code': 1,
            'msg': 'ok',
            'data': {
                'is_select_all': is_all_select,
                'sum_money': sum_money,
                'status': cart_data.is_selected
            }
        }
        return JsonResponse(result)


class Cart_All_Status_API(View):
    def put(self, req):
        user = req.user
        # 判断操作
        cart_items = Cart.objects.filter(user_id=user.id)
        # 默认没有商品，没有选中
        is_select_all = False
        # 由于当前处于为全选状态，那么我们需要把所有商品全选
        if cart_items.exists() and cart_items.filter(is_selected=False).exists():

            # for i in cart_items.filter(is_selected=False):
            #     i.is_selected = True
            #     i.save()
            cart_items.filter(is_selected=False).update(is_selected=True)
            is_select_all = True
            # 算钱
            sum_money = get_cart_money(cart_items)
        else:
            # 将所有的商品状态取反
            cart_items.update(is_selected=False)
            sum_money = 0
        # 返回数据
        result = {
            'code': 1,
            'msg': 'ok',
            'data': {
                'sum_money': sum_money,
                'all_select': is_select_all
            }
        }
        return JsonResponse(result)

#购物车按钮加减操作
class Cart_Item_API(View):
    #加操作，post请求
    def post(self,req):
        user = req.user
        c_id = int(req.POST.get('c_id'))
        #确定购物车数据
        cart_item = Cart.objects.get(pk=c_id)
        #确定库存
        if cart_item.goods.storenums < 1:
            data = {
                'code':2,
                'msg':'库存不足',
                'data':''
            }
            return  JsonResponse(data)
        #库存足够数量+1
        cart_item.num += 1
        cart_item.save()

        cart_items = Cart.objects.filter(
            user_id=user.id,
            is_selected=True
        )
        sum_money = get_cart_money(cart_items)

        #返回数据
        data = {
            'code':1,
            'msg':'ok',
            'data':{
                'sum_money':sum_money,
                'num':cart_item.num
            }
        }
        return  JsonResponse(data)

    #减操作，delete请求
    def delete(self,req):
        params = QueryDict(req.body)
        #拿到用户
        user = req.user
        c_id = int(params.get('c_id'))
        #获取id为c_id的商品,c_id即为点击的商品
        cart_item = Cart.objects.get(pk=c_id)
        #点击的商量-1
        cart_item.num -= 1
        # 保存修改的数据
        cart_item.save()
        #如果商品数量为0，删除购物车数据,返回前端数量
        if cart_item.num == 0:
            goods_num = 0
            cart_item.delete()
        else:
            goods_num = cart_item.num
        #获取该用户的所有商品
        cart_items = Cart.objects.filter(user_id=user.id)
        #根据商品算钱
        sum_money = get_cart_money(cart_items)
        #返回给前端数据
        data = {
            'code':1,
            'msg':'ok',
            'data':{
                'num':goods_num,
                'sum_money':sum_money
            }
        }
        return  JsonResponse(data)


class Order_API(View):
    def get(self,req):
        user = req.user
        cart_items = Cart.objects.filter(
            user_id=user.id,
            is_selected=True
        )
        if not cart_items.exists():
            return render(req, 'order/order_detail.html')
        #创建order
        order = Order.objects.create(
            user=user
        )
        #循环创建订单数据
        for i in cart_items:
            OrderItem.objects.create(
                order=order,
                goods=i.goods,
                num=i.num,
                buy_money=i.goods.price
            )
        #算钱
        sum_money = get_cart_money(cart_items)
        #清空购物车内商品
        cart_items.delete()
        data = {
            'sum_money':sum_money,
            'order':order
        }
        return render(req,'order/order_detail.html',data)



