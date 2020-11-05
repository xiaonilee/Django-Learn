from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import UserModel


def index(request):
    return render(request, 'index.html')


def upload_file(request):
    if request.method == "GET":
        return render(request, 'upload.html')
    elif request.method == "POST":
        icon = request.FILES.get('icon')

        print(type(icon))

        with open('/Users/xiaonili/PycharmProjects/PythonCloudSys2/PYC08/ModelToSQL/static/img/icon2.png', 'wb') as save_file:
            for part in icon.chunks():
                save_file.write(part)
                save_file.flush()

        return HttpResponse('Files Uploaded')


def image_field(request):
    if request.method == "GET":
        return render(request, 'image_field.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        icon = request.FILES.get('icon')
        user = UserModel()
        user.u_name = username
        user.u_icon = icon
        user.save()

        return HttpResponse('Uploaded %d' % user.id)


def mine(request):
    username = request.GET.get('username')
    user = UserModel.objects.get(u_name=username)
    print('/static/upload/'+user.u_icon.url)

    data = {
        'username': username,
        'icon_url': '/static/upload/'+user.u_icon.url,
    }
    return render(request, 'mine.html', context=data)