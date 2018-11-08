from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Company(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='公司名字'
    )
    class Meta:
        verbose_name = '公司'


class Engineer(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='名字'
    )
    age = models.IntegerField(
        verbose_name='年纪'
    )
    gender = models.BooleanField(
        default=True,
        verbose_name='性别'
    )
    isDelete= models.BooleanField(
        default=False,
        verbose_name='逻辑删除'
    )
    company = models.ForeignKey(
        Company,
        max_length=20,
        verbose_name='公司id',
        null=True
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name= '工程师'


class Blog(models.Model):
    title = models.CharField(
        verbose_name='主题',
        max_length=30
    )
    content = HTMLField(
        verbose_name='内容'
    )
    class Meta:
        verbose_name = '博客'