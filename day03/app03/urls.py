from django.conf.urls import url,include
from .views import  *

urlpatterns = [
    url(r'^getdata$',get_data),
    url(r'^qdata$',get_data_by_q),
    url(r'^fdata$',get_data_by_f),
    url(r'^lianxi$',exercise),
    url(r'^del_humen$',delete_humen),
    url(r'^update_humen$',updata_humen),
]