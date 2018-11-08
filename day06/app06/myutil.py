import uuid
import hashlib
import random

def get_unique_str():
    #得到一个uuid的字符串
    uuid_str = str(uuid.uuid4()).encode('utf8')
    #实例化md5
    md5 = hashlib.md5()
    #进行加密
    md5.update(uuid_str)
    #返回32位的十六进制数据
    return md5.hexdigest()

def get_random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)