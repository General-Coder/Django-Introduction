from django.conf.urls import  url
from .views import *

urlpatterns = [
    url(r'^upload$',upload_file,name='upload'),
    url(r'^upload_oss$',upload_oss,name='upload_oss')
]
