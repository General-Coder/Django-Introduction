from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register$',register,name='register'),
    url(r'^login$',my_login,name='login'),
    url(r'^middle$',middle,name='middle'),
    url(r'^cartoon$',cortoon,name='cartoon'),
    url(r'^upload$',upload,name='upload'),
    url(r'^index',index,name='index'),
]
