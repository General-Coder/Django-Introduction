from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^play$',play,name='play'),
    url(r'^myjson$',json_test,name='json_test'),
    url(r'^response$',test_res,name='test_res'),
    url(r'^login$',mylogin,name='login'),
    url(r'^index$',index,name='index'),
    url(r'^logout$',mylogout,name='logout'),

]
