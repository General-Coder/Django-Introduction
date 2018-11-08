from django.db import models

# Create your models here.


#一对一
#定义身份证类
class IdCard(models.Model):
    num = models.CharField(
        max_length=20,
        verbose_name="身份证编号"
    )
    addr = models.CharField(
        max_length=20,
        default='千锋派出所'
    )
    class Meta:
        verbose_name = "身份证类"


#定义人类
class Person(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="人名"
    )
    #确定一对一关系
    idcard = models.OneToOneField(
        IdCard,
        on_delete=models.PROTECT
    )
    def __str__(self):
        return  self.name



#一对多
#定义班级类
class Grade(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="班级名"
    )
    def __str__(self):
        return self.name

#定义学生类
class Students(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="学生名"
    )
    grade = models.ForeignKey(
        Grade
    )
    def __str__(self):
        return self.name



#多对多关系
#定义作者类
class Author(models.Model):
    name = models.CharField(
        max_length=30
    )
    def __str__(self):
        return  self.name

#定义书类
class Book(models.Model):
    name = models.CharField(
        max_length=30
    )
    author = models.ManyToManyField(
        Author
    )
    def __str__(self):
        return self.name


#抽象继承
class HumenBase(models.Model):
    name = models.CharField(
        max_length=20
    )
    age = models.IntegerField()
    sex = models.CharField(
        max_length=10
    )
    class Meta:
        abstract = True

class Teacher(HumenBase):
    t_no = models.CharField(
        max_length=30
    )

class XZ(HumenBase):
    hobby = models.CharField(
        max_length=30
    )

class Animal(models.Model):
    name = models.CharField(
        max_length=30
    )
    color = models.CharField(
        max_length=30
    )
    gender = models.CharField(
        max_length=30
    )
    age = models.IntegerField()
    class Meta:
        abstract=False

class Dog(Animal):
    size = models.CharField(
        max_length=20
    )

class Cat(Animal):
    type = models.CharField(
        max_length=20
    )