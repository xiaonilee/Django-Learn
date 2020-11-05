import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Person


def add_persons(request):

    for i in range(15):
        person = Person()
        flag = random.randrange(100)
        person.p_name = 'Tom%d' % i
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()

    return HttpResponse("批量创建成功")


def get_persons(request):
    #persons = Person.objects.filter(p_age__gt=48).filter(p_age__lt=80)
    # persons = Person.objects.exclude(p_age__lt=48).filter(p_age__lt=80)
    #
    # persons_two = persons.filter(p_age__in=[61, 66])
    # print(type(persons))

    persons = Person.objects.all().order_by("p_age")
    persons_values = persons.values()
    print(type(persons_values))
    print(persons_values)

    for persons_value in persons_values:
        print(persons_value)

    context = {
        #'persons': persons
        #'persons': persons_two
        'persons': persons
    }

    return render(request, 'person_list.html', context=context)

def add_person(request):

    #person = Person.objects.create(p_name="Sunck", p_age=15, p_sex=True)
    # 是"",而非null, None,不能重写__init__ 可以通过其他手段，实现属性自定义赋值
    #person = Person(p_age=28)

    person = Person.create('Jack')
    person.save()
    return HttpResponse("创建成功")


def get_person(request):

    # person = Person.objects.get(p_age=66)
    # print(person)
    person = Person.objects.all().first()
    print(person.p_name)

    person_one = Person.objects.all().last()
    print(person_one.p_name)

    return HttpResponse('获取成功')