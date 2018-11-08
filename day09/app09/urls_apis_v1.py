from django.conf.urls  import   url
from  .apis_v1 import  *

urlpatterns = [
    url(r'^stu$',StuAPI.as_view()),
    url(r'^test$',TestAPI.as_view()),
]