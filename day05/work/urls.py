from django.conf.urls import url
from .views import *


urlpatterns = [
   url(r"^login$",login,name='login'),
   url(r"^index$",index,name='index'),
   url(r"^register$",register,name='register'),
]
