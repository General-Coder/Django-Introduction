from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="人名"
    )
    content = models.CharField(
        max_length=100,
        verbose_name='介绍'
    )
    isDelete = models.BooleanField(
        default=False
    )
    class Meta:
        db_table = "Person"
