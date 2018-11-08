from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    phone = models.CharField(
        max_length=20,
        verbose_name='手机号'
    )
    age = models.IntegerField(
        verbose_name='年纪',
        null=True
    )

class Book(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name='书名'
    )
    icon = models.ImageField(
        upload_to='icons',
        null=True
    )
    icon_url = models.CharField(
        max_length=251,
        null=True
    )
