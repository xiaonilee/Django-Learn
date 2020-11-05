from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("双击666")

def hehe(request):
    return HttpResponse("你真是个小天才，这么快就学会了！")

def haha(request):
    return HttpResponse("<h1>睡觉的站起来！</h1>")

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')