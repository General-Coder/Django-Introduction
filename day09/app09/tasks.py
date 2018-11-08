from celery import  task
import  time


@task
def  my_task():
    print('执行前')
    time.sleep(5)
    print('执行后')


@task
def res_task(n):
    print(n)
    #也可以通过缓存保存结果
    return  {'data':n}


@task
def  write_task():
    print('我是定时任务')