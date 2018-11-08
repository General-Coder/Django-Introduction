from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index$',index,name='index'),
    url(r'^register$',register,name='register'),
    url(r'^verify/(.*)',verify,name='verify'),
    url(r'^verify_num$',verify_num,name='verify_num'),
    url(r'^login$',my_login,name='login'),
    url(r'^logout$',my_logout,name='logout'),
    url(r'^img', get_confirm_code, name='img'),
    url(r'^reset$', reset_pwd, name='reset'),
]
