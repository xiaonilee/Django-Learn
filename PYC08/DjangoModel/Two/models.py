from django.db import models

# Create your models here.
class Person(models.Model):
    objects = None
    p_name = models.CharField(max_length=16)
    p_sex = models.BooleanField(default=False)


class IDCard(models.Model):
    objects = None
    id_num = models.CharField(max_length=18, unique=True)
    id_person = models.OneToOneField(Person, on_delete=models.SET_NULL, null=True, blank=True)


class Customer(models.Model):
    objects = None
    c_name = models.CharField(max_length=16)


class Goods(models.Model):
    objects = None
    g_name = models.CharField(max_length=16)
    g_customer = models.ManyToManyField(Customer)


class Animal(models.Model):
    a_name = models.CharField(max_length=16)
    class Meta:
        abstract = True

class Cat(Animal):
    c_eat = models.CharField(max_length=32)


class Dog(Animal):
    d_legs = models.IntegerField(default=4)
