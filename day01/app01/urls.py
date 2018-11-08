from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^humen/$',views.get_humen),
    url(r'^index/$',views.index),
    url(r'^hello/$',views.hello),
    url(r'^mygod/$',views.hehe),
    url(r'^women/$',views.search_women),
]