from __future__ import  absolute_import  #必须写在第一行
from .celery import  app as celery_app


import pymysql
pymysql.install_as_MySQLdb()