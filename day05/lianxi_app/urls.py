from django.conf.urls import url,include
from django.contrib import admin
from .views import *
urlpatterns = [
    url(r'^$',No_ne),
    url(r'^json$',my_json),
    url(r'^res$',test_res),
    url(r'^index$',index,name='index'),
    url(r'^login$',login,name='login'),
    url(r'^logout$',logout,name='logout'),
]