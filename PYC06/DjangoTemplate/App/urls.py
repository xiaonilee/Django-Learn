from django.conf.urls import url

from . import views

urlpatterns = [
    url('hello/', views.hello),
    url('index/', views.index),
    url('getstudents/', views.get_students),
    url('temp/', views.temp),
    url('home/', views.home)
]