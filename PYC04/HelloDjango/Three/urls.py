from django.conf.urls import url

from . import views

urlpatterns = [
    url('index/', views.index),
    url('getgrade/', views.get_grade),
    url('getstudents', views.get_students),
]