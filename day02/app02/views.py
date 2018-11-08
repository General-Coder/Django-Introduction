from django.shortcuts import render
from   django.http import HttpResponse
from .models import  Category,Item,Classes,Students
# Create your views here.

#获取商品页面
def get_html(req):
    return render(req,'item.html')

#添加商品
def create_item(req):
    #解析参数
    parms = req.POST
    name = parms.get("i_name")
    barcode = parms.get('i_barcode')
    cate_id = int(parms.get('cate_id'))
    item = Item.objects.create(
        name = name,
        barcode = barcode,
        category_id = cate_id)
    return HttpResponse("添加成功{}".format(item.name))

#查询练习
def selete_data(req):
    #使用fifter查名字
    # data = Item.objects.filter(name="美女")
    # print(data)

    # 查看以可乐结尾的数据，并包含中国
    '''data = Item.objects.filter(name__endswith="可乐").filter(name__contains='中国')
    print(dir(data))'''

    #与filter相反
    # data = Item.objects.exclude(name='美女')

    #大于等于
    # data = Item.objects.filter(id__gt = 3)

    # data = Item.objects.filter(id__in=[1,3,4])

    # data = Item.objects.all().order_by('-id')

    # data = Item.objects.filter(id__lt = 4).values('name','id','barcode')
    # data = data.order_by('-id')
    # print(data.first())
    # print(data.last())
    # data = data[1:]
    # print(len(data))
    # print(data.count())
    # print(data.exists())

    # tmp = Item.objects.filter(category_id=1)
    # print(tmp)

    # data =Item.objects.filter(name__contains='可')



    return render(req,'items.html',{'items':data})

# 练习
def get_category(req):
    cates = Category.objects.all()
    return  render(req,'cates.html',{'cates':cates})

# 根据商品分类拿数据
def get_item_by_c_id(req):
    #解析get请求的c_id参数
    c_id = int(req.GET.get('c_id'))
    #获取商品数据
    items = Item.objects.filter(category_id= c_id)
    return  render(req,'items.html',{'items':items})

#学生查询页面
def students(req):
    return  render(req,'students.html')

#添加学生
def add_student(req):
    name = req.POST.get("s_name")
    age = int(req.POST.get("s_age"))
    python = float(req.POST.get("p_score"))
    english = float(req.POST.get("e_score"))
    cls_id = int(req.POST.get("cls_id"))
    stu = Students.objects.create(
        name =name,
        age = age,
        python_score = python,
        english_score = english,
        cls_id_id = cls_id
    )
    return  HttpResponse("添加成功{}".format(stu.name))

#查询学生
def select_student(req):
    data1 = Students.objects.filter(python_score__gt = 80)
    data2 = Students.objects.filter(age__gte=18).filter(age__lte=20)
    data3 = Students.objects.filter(english_score__in=[100,59,99])
    return  render(req,'select_student.html',{"data1":data1,"data2":data2,"data3":data3})