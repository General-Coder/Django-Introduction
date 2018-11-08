from django.http import HttpResponse
from django.shortcuts import render
import  time
from  .tasks import  *
# Create your views here.


def  test_task(req):
    # my_task.delay()
    result = res_task.delay(4)
    print(dir(result))
    print(result.task_id)
    return  HttpResponse('ok')


def  stus_view(req):
    return  render(req,'app09/stu.html')