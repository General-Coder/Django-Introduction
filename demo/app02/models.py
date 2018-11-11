
from django.db import models

class ap3(models.Model):
    app2_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    data = models.DateField()

class ap4(models.Model):
    app2 = models.CharField(max_length=50)
    sex1 = models.CharField(max_length=50)
    data1 = models.DateField()
    class Meta:
        db_table = 'mytable'

