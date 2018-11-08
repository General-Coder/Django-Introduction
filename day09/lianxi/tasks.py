from io import BytesIO

import oss2
from celery import  task
from .my_until import get_unique_str


@task
def upload_ali_oss(fileName,file_name):
    endpoint = 'http://oss-cn-shanghai.aliyuncs.com'
    access_key_id = 'LTAIYRooVAgBYAyx'
    access_key_secret = 'xieuygrcdHaJFm34Qe9iz5ok3cTP3Y'
    bucket_name = 'zdbuck'
        # 生成一个认证对象
    auth = oss2.Auth(access_key_id, access_key_secret)
    buf = BytesIO()
    bucket = oss2.Bucket(auth, endpoint, bucket_name)
    for i in fileName.chunks():
        buf.write(i)
    buf.seek(0)
    bucket.put_object(file_name, buf.getvalue())
    print('执行成功')

