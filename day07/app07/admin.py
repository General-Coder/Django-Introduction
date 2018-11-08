from django.contrib import admin
from django.contrib.admin import AdminSite
from lianxi.models import Student,Text


from .models import Engineer,Company,Blog

# Register your models here.

class EngineerInline(admin.TabularInline):
    #在创建公司的时候添加三个工程师
    model = Engineer
    extra = 3


class CompanyAdmin(admin.ModelAdmin):
    inlines = [EngineerInline]



# @admin.register(Engineer)
class EngineerAdmin(admin.ModelAdmin):

    #布尔值显示问题
    def gender(self):
        if self.gender:
            return '男'
        else:
            return '女'
    def isDelete(self):
        if self.isDelete:
            return '已经删除'
        else:
            return "没有删除"
        #给函数名设置显示的属性
    gender.short_description = '性别'
    isDelete.short_description = '逻辑删除'

    #设置显示的字段名，数组里放的是模型属性，定义了方法就放函数名
    list_display = ['name','age',gender,isDelete]
    #设置过滤条件，在右侧
    list_filter = ['name']
    #分页
    list_per_page = 5
    #设置搜索,在上侧
    search_fields = ['name','age']
    #设置排序
    ordering = ['-age']
    #点进具体信息能看到分组信息
    fieldsets = [
        ('基本信息',{'fields':('name','age','gender')}),
        ('额外信息',{'fields':('isDelete',)})
    ]
    #点击进去看见顺序，和fieldsets不能共存
    # fields = ['age','isDelete','gender','name']

    #执行动作的位置
    actions_on_bottom = True
    actions_on_top = False



# admin.site.register(Engineer,EngineerAdmin)

class MySite(admin.AdminSite):
    site_header = '人生苦短，我用python'
    site_url = 'www.baidu.com'
    site_title = '你是个逗比'

site = MySite()




class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.gender:
            return  '男'
        else:
            return '女'
    gender.short_description = '学生性别'
    def isDelete(self):
        if self.isDelete:
            return '删除'
        else:
            return 'no 删除'
    isDelete.short_description = '逻辑删除'
    list_display = ['name','age',gender,isDelete]
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 10
    ordering = ['age']
    fieldsets = (
        ('基本信息',{'fields':('name','age')}),
        ("其他信息",{'fields':('gender','isDelete')})
    )


class TextAdmin(admin.ModelAdmin):
    list_filter = ['blog','title']


site.register(Student,StudentAdmin)
site.register(Engineer,EngineerAdmin)
site.register(Company,CompanyAdmin)
site.register(Blog)
site.register(Text,TextAdmin)
