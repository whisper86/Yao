from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from ProjectB.web.models import Student, User_Table
from ProjectB.web import models


# Create your views here.

def student_list(request):
    student_queryset = models.Student.objects.all()
    return render(request, "student.html", {"student_queryset": student_queryset})


def register_success(request):
    return render(request, "register_success.html")


def register_view(request):
    if request.method == "POST":  # 判断请求为POST请求则是提交表单
        user = Student()  # 创建一个apply实例
        id = request.POST.get("id")
        name = request.POST.get("Name")  # 获取提交表单中的name值，赋值给变量name
        chinese = request.POST.get("Chinese")  # 获取提交表单中的clas值，赋值给clas
        math = request.POST.get("Math")
        english = request.POST.get("English")
        chemistry = request.POST.get("Chemistry")
        biology = request.POST.get("Biology")
        physics = request.POST.get("Physics")
        all_score = request.POST.get("All_score")
        user.id = id
        user.Name = name  # 给实例赋值
        user.Chinese = chinese
        user.Math = math
        user.English = english
        user.Chemistry = chemistry
        user.Biology = biology
        user.Physics = physics
        user.All_score = all_score
        user.save()  # 保存实例，把数据存到数据库
        return render(request, 'register_success.html')  # 数据保存之后，从register网页跳转到成功的页面
    else:
        return render(request, 'register.html')  # 没有数据的时候，跳转到register网页


def sign_up(request):
    if request.method == "POST":
        User = User_Table()  # 创建实例化对象
        name = request.POST.get("Username")  # 获取提交表单中的name值，赋值给变量name
        password = request.POST.get("Password")  # 获取提交表单中的clas值，赋值给clas

        User.Username = name  # 给实例赋值
        User.Password = password
        User.save()
        return render(request, 'register_success.html')
    else:
        return render(request, "sign_up.html")


# 类视图---登录模板
class Student_Login(View):
    def get(self, request):
        return render(request, "Login.html")

    def post(self, request):
        Username = request.POST.get("username")
        Password = request.POST.get("password")

        # 登录失败时需要提示是用户名不存在还是密码错误
        try:  # 存放可能出现异常的代码 查询数据多个条件时默认是并且的关系
            user = User_Table.objects.get(Username=Username)
            # 当输入的用户名在数据库里查询不到，说明try里面的代码存在异常
            # 执行万能异常里面的语句
        except Exception as e:  # 捕获异常将异常存到e里
            print(e)
            return HttpResponse(f"用户名不存在{e}")

        # 如果用户名对，就判断密码有没有输入正确
        if Password != user.Password:
            return HttpResponse("用户名和密码不匹配")

        return redirect('/student_list')
