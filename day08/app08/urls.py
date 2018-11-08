from django.conf.urls import url
from .views import *
from . import my_util

urlpatterns = [
    url('^test_email$',test_mail),
    url('^send_html$',send_html),
    url('^send_file$',file_email),
    url('^send_many_email$',send_many_msg),
    url('^register$',send_verify_mail),
    url('^verify/(.*)',verify),
    url('^test$',test),
    url('^cz$',cz_api),

]