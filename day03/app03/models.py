from django.db import models

# Create your models here.

class HumenManage(models.Manager):
    def create_girl(self,name):
        res = Humen.objects.create(
            name = name,
            age = 18,
            money = 1
        )
        return  res


class Humen(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )
    age = models.IntegerField(
        default=1
    )
    money = models.IntegerField(
        default=0
    )
    #定义objects属性
    # my_objects = models.Manager()
    objects = models.Manager()

    #实例化HumenManage对象

    new_objects = HumenManage()