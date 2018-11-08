from django.conf.urls import url
from .views import  *

urlpatterns = [
    url(r'^test_task$',test_task),
    url(r'^stu$',stus_view),
]
