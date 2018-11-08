from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^index$',index,name='index'),
    url(r'^show_info$',show_info,name='show_info'),
    url(r'^new_index$',new_index,name='new_index'),
    url(r'^new_show_info/(\d+)$',new_show_info,name='new_show_info'),
    url(r'^show_info1/(?P<num>\d+)$',show_info1,name='show_info1'),
    url(r'^demos1/(\d+)$',demos1,name='demo1'),

]