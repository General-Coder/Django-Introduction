from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^data$',page_num,name='page'),
    url(r'^cache$',my_cache,name='cache'),
]