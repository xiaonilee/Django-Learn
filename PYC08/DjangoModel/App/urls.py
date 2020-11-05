from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
]