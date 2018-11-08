from django.conf.urls import url,include
from django.contrib import admin
from .views import *
urlpatterns = [
    url(r'^index$',index,name='index'),
    url(r'^mylogin$',mylogin,name='login'),
    url(r'^register$',register,name='register'),
    url(r'^forget_pwd$',forget_pwd,name='forget_pwd'),
    url(r'^forget$',forget,name='forget'),
    url(r'^mylogout$',mylogout,name='logout'),
    url(r'^reset$',reset,name='reset'),
]