from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="分类名",
        # 改数据表字段名字
        db_column="cate_name"
    )
    cate_num = models.CharField(
        max_length=20,
        null=True,
        verbose_name="分类的编号"
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name="修改时间"
    )
    class Meta:
        # 改数据库表名
        db_table = "category"

class Item(models.Model):
     name = models.CharField(
         max_length=40,
         verbose_name="商品名字"
     )
     barcode = models.CharField(
         max_length=13,
         verbose_name="条码",
         null=True
     )
     category = models.ForeignKey(
        Category,
        db_index=True
     )
     class Meta:
         db_table = "item"

     def __str__(self):
         return self.name + "的id是" + str(self.id)

class Classes(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="班级名称"
    )
    class Meta:
        db_table = "Classes"

class Students(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
        validators='学会姓名'
    )
    age = models.IntegerField(
        null=True,
        verbose_name='学生年纪'
    )
    python_score = models.FloatField(
        max_length=20,
        verbose_name='python成绩'
    )
    english_score = models.FloatField(
        max_length=20,
        verbose_name='英语成绩'
    )
    cls_id = models.ForeignKey(
        Classes,
        db_index=True
    )
    class Meta:
        db_table = "students"


