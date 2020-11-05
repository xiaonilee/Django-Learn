from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from .models import Student


def hello(request):
    return HttpResponse("Hello")


def index(request):
    # render的本质也是HttpResponse,将模版和context数据渲染成字符串
    # return render(request, 'index.html')
    temp =loader.get_template('index.html')
    content = temp.render()
    return HttpResponse(content)


def get_students(request):

    students = Student.objects.all()


    student_dict = {
        "hobby": "learning",
        "time": "20years"
    }

    code = "<h2>gogogo</h2>"

    data = {
        "students": students,
        "student_dict": student_dict,
        "count": 10,
        "code": code
    }


    return render(request, 'student_list.html', context=data)


def temp(request):
    return render(request, 'home.html', context={"title": "home"})


def home(request):
    return render(request, 'home_mine.html')