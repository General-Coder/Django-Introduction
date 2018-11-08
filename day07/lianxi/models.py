from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class Student(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='学生姓名'
    )
    age  = models.IntegerField(
        verbose_name='学生年纪'
    )
    gender = models.BooleanField(
        default=True,
        verbose_name='学生性别'
    )
    isDelete = models.BooleanField(
        default=False,
        verbose_name = '逻辑删除'
    )

    class Meta:
        verbose_name = '学生'
        db_table = 'students'


class Text(models.Model):
    blog = HTMLField()
    title= models.CharField(
        verbose_name='主题',
        max_length=20
    )