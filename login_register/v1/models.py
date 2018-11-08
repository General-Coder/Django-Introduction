from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.


class MyUser(AbstractUser):
    phone = models.CharField(
        max_length=20,
        verbose_name='手机号',
        unique=True
    )
    is_active = models.BooleanField(
        default=False
    )
    email = models.CharField(
        unique=True,
        max_length=50
    )