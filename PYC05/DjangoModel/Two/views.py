from django.db.models import Max, Avg, F, Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import User, Order, Grade, Customer, Company, Animal


def get_user(request):
    username = 'Sunck'
    password = '120'

    users = User.objects.filter(u_name=username)
    print(users.count())

    if users.count(): # users.exist()也可以
        user = users.first()
        if user.u_password == password:
            print("获取用户信息成功")
        else:
            print("密码错误")
    else:
        print("用户名不存在")

    return HttpResponse("获取成功")


def get_users(request):

    users = User.objects.all()[1:3]

    context = {
        'users': users
    }

    return render(request, 'user_list.html', context=context)


def get_orders(request):

    orders = Order.objects.filter(o_time__year=2020)
    for order in orders:
        print(order.o_num)

    return HttpResponse("获取订单成功")


def get_grades(request):

    grades = Grade.objects.filter(student__s_name='Jack')

    for grade in grades:
        print(grade.g_name)

    return HttpResponse("查询成功")


def get_customer(request):
    result = Customer.objects.aggregate(Avg("c_cost"))
    print(result)

    return HttpResponse("获取花费成功")


def get_company(request):
    #companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num'))
    #companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num')-15)
    #companies = Company.objects.filter(c_boy_num__gt=1).filter(c_girl_num__gt=5)

    companies = Company.objects.filter(Q(c_boy_num__gt=5) | Q(c_girl_num__gt=10))
    for company in companies:
        print(company.c_name)

    return HttpResponse("获取公司成功")


def get_animals(request):
    animals = Animal.a_m.all()
    for animal in animals:
        print(animal.a_name)

    #Animal.objects.create_animal()

    return HttpResponse("动物获取成功")