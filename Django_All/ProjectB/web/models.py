from django.db import models


# Create your models here.
class Student(models.Model):  # 创建一个Test数据表 主表
    Name = models.CharField(max_length=10)  # 数据表中的字段，最大字符限制为10
    Chinese = models.CharField(max_length=10)
    Math = models.CharField(max_length=10)
    English = models.CharField(max_length=10)
    Chemistry = models.CharField(max_length=10)
    Biology = models.CharField(max_length=10)
    Physics = models.CharField(max_length=10)
    All_score = models.CharField(max_length=10)

    class Meta:
        db_table = 'web_student'


class User_Table(models.Model):  # 子表
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                          verbose_name='ID')  # 创建主键，自增长、设置主键、无序列号设置、详细名称为ID
    Username = models.CharField(max_length=15)  # 用户名，最大字符限制为十五
    Password = models.CharField(max_length=20)  # 密码，最大字符限制为二十

    class Meta:
        db_table = "user"
