from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)


class Grade(models.Model):
    g_name = models.CharField(max_length=16)


class School(models.Model):
    s_name = models.CharField(max_length=16)


class Book(models.Model):
    b_name = models.CharField(max_length=32)