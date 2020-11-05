from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Grade
from .models import Student


def students(request, g_id):
    student_list = Student.objects.filter(s_grade_id=g_id)
    return render(request, 'grade_student_list.html', context=locals())


def student(request, s_id):
    print(s_id)
    print(type(s_id))

    return HttpResponse("Got a student")


def grades(request):
    grade_list = Grade.objects.all()
    return render(request, 'grade_list.html', context=locals())


def get_time(request, hour, minute, second):
    return HttpResponse("Time %s: %s: %s" %(hour, minute, second))


def get_date(request, year, month, day):
    return HttpResponse("Date %s-%s-%s" %(year, month, day))


def learn(request):
    return HttpResponse("Love Learning")


def have_request(request):

    print(request.path)

    print(request.method)

    print(request.GET)

    hobby = request.GET.get('hobby')
    print(hobby)

    hobbies = request.GET.getlist('hobby')
    print(hobbies)

    print(request.POST)
    # print(request.META)
    #
    # for key in request.META:
    #     print(key, request.META.get(key))

    print("Remote IP", request.META.get("REMOTE_ARRD"))

    return HttpResponse("Request Success")


def create_student(request):
    return render(request, 'student.html')


def do_create_student(request):

    print(request.method)
    username = request.POST.get('username')

    return HttpResponse(username)