import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Student


def index(request):
    return HttpResponse('Two index')

def add_student(request):
    student = Student()
    student.s_name = 'Jerry%d' % random.randrange(100)
    student.save()
    return HttpResponse('Add Success %s' % student.s_name)


def get_students(request):
    students = Student.objects.all()
    for student in students:
        print(student.s_name)

    #return HttpResponse('Student List')

    context = {
        "hobby": "Play Games",
        "eat": "bread",
        "students": students
    }
    return render(request, 'student_list.html', context=context)


def update_student(request):
    student = Student.objects.get(pk=2)
    student.s_name = 'Jack'
    student.save()
    return HttpResponse("Student Update Success")


def delete_student(request):
    student = Student.objects.get(pk=5)
    student.delete()
    return HttpResponse("Student Delete Success")