from django.contrib.auth.models import User,AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

from login_app.models import MyUser





# Create your models here.
class ZdUser(MyUser):
    pass

User = get_user_model()