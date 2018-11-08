from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^test_mail',test_email),
    url(r'^html_mail',mail_html),
    url(r'^image_mail',image_mail),
    url(r'^send_many_mail',send_many_mail),
    url(r'^register$',register),
    url(r'^previry/(.*)',previry),

]