from django.db import models

# Create your models here.
class ap1(models.Model):
    username = models.CharField(max_length=30)
    class Meta:
        app_label = 'app02'  #如果指定将在app02对应的数据库下创建数据表

class ap2(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()