from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('hehe/', views.hehe),
    path('haha/', views.haha),
    path('index/', views.index),
    path('home/', views.home),
]