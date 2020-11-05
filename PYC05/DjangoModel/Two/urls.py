from django.conf.urls import url

from . import views

urlpatterns = [
    url('getuser/', views.get_user),
    url('getusers', views.get_users),
    url('getorders/', views.get_orders),
    url('getgrades/', views.get_grades),
    url('getcustomer/', views.get_customer),
    url('getcompany/', views.get_company),
    url('getanimals/', views.get_animals),
]