from django.conf.urls import url,include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^add_home$',add_home),
    url(r'^home$',get_home_by_humen),
    url(r'^humen$',get_human_by_home),
    url(r'^students$',get_stu_by_grade),
    url(r'^grade$',get_grade_by_student),
    url(r'^phone$',get_phone_by_xinpian),
    url(r'^u$',get_u_by_phone),
]
