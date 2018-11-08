from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class MyUser(AbstractUser):
    phone =models.CharField(
       max_length=30,
       verbose_name='手机号码'
    )
    class Meta(AbstractUser.Meta):
        db_table='User'
        # abstract=True

User = get_user_model()