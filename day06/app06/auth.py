from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import MyUser


class MyBackend1(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        #查找用户
        try:
            user = MyUser.objects.get(username=username)
        except Exception:
            try:
                user = MyUser.objects.get(phone=username)
            except Exception:
                return None

        #密码认证
        if user.check_password(password):
            return user
        else:
            return None


class MyBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = MyUser.objects.get(Q(username=username) |
                                      Q(phone=username) |
                                      Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None