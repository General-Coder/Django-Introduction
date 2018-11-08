import os
from django.http import HttpResponse
from .my_until import get_unique_str
from django.conf import settings
from django.shortcuts import render
from .tasks import  upload_ali_oss

# Create your views here.

def upload_file(req):
    if req.method == "GET":
        return render(req,'lianxi/file.html')
    else:
        uuid_str = get_unique_str()
        name = req.POST.get('name')
        file = req.FILES.get('file')
        fileName = uuid_str + '.' + file.name.split(".")[-1]
        filePath = os.path.join(settings.MEDIA_ROOT,fileName )
        with open(filePath,'wb') as f:
            for i in file.readlines():
                f.write(i)
        return  HttpResponse('上传成功')


def upload_oss(req):
    if req.method=='GET':
        return render(req,'lianxi/file.html')
    else:
        uuid_str = get_unique_str()
        file = req.FILES.get('file')
        file_name = uuid_str + '.' + file.name.split('.')[-1]
        upload_ali_oss.delay(file,file_name)
        return HttpResponse('文件上传成功' )


