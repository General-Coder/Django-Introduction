from django.conf.urls import url,include
from django.contrib import admin
from .views import  *

urlpatterns = [
    url(r'^getidcard$',get_idcard_by_humen),
    url(r'^gethumen$',get_humen_by_idcard),
    url(r'^humen$',get_humen_v1),
    url(r'^del_humen$',delete_humen),
    url(r'^grade$',get_grade_by_stu),
    url(r'^students$',get_stu_by_grade),
    url(r'^author$',get_author_by_book),
    url(r'^book$',get_book_by_author),

]