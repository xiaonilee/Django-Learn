from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('index/', views.index),
    url('addstudent/', views.add_student),
    url('getstudents/', views.get_students),
    url('updatestudent', views.update_student),
    url('deletestudent', views.delete_student),
]