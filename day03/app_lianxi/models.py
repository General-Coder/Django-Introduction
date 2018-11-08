from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="家"
    )
    class Meta:
        db_table = "zd_home"

    @classmethod
    def create_home(cls,name):
        ho = cls(name = name)
        return  ho

    class HomeManage(models.Manager):
        def create_home(self,name):
            ho = Home.objects.create(name = name)
            return ho
    objects = models.Manager()
    homeObj = HomeManage()




class Humen(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='人名'
    )
    jia = models.OneToOneField(
        Home,
        max_length=20,
        verbose_name="人的家",

    )
    class Meta:
        db_table = "zd_humen"

class Grade(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="班级名字"
    )
    def  __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="学生姓名"
    )
    grade = models.ForeignKey(
        Grade,
        max_length=20,
        verbose_name="学生的班级"
    )
    def __str__(self):
        return  self.name

class Xinpian(models.Model):
    name = models.CharField(
        max_length=20
    )
    def __str__(self):
        return  self.name
    class Meta:
        db_table="zd_xinpian"

class Phone(models.Model):
    name = models.CharField(
        max_length=20
    )
    u = models.ManyToManyField(
        Xinpian,
        max_length=20
    )
    def __str__(self):
        return  self.name
    class Meta:
        db_table = "zd_phone"