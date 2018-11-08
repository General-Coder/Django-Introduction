from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import MyUser

class MyBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = MyUser.objects.get(Q(username=username) |
                                      Q(phone=username) |
                                      Q(email=username))

            if user.check_password(password) and user.is_active == True:
                return user
        except Exception as e:
            return None