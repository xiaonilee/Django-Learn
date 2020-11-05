from django.db import models

# Create your models here.
class User(models.Model):
    objects = None
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)


class Order(models.Model):
    objects = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.objects = None

    o_num = models.CharField(max_length=16, unique=True)
    o_time = models.DateTimeField(auto_now_add=True)


class Grade(models.Model):
    objects = None
    g_name = models.CharField(max_length=16)


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


class Customer(models.Model):
    objects = None
    c_name = models.CharField(max_length=16)
    c_cost = models.IntegerField(default=10)


class Company(models.Model):
    objects = None
    c_name = models.CharField(max_length=16)
    c_girl_num = models.IntegerField(default=5)
    c_boy_num = models.IntegerField(default=3)


class AnimalManager(models.Manager):
    def get_queryset(self):
        return super(AnimalManager, self).get_queryset().filter(is_delete=False)

    def create_animal(self, a_name="Chicken"):
        a = self.model()
        a.a_name = a_name

class Animal(models.Model):
    objects = None
    a_name = models.CharField(max_length=16)
    is_delete = models.BooleanField(default=False)

    a_m = AnimalManager()