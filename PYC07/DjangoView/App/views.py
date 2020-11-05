import random

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def hello(request):

    response = HttpResponse()
    # response.content = "keep doing"
    # response.status_code = 404

    response.write("remove buffer")
    response.flush()

    return response


def get_ticket(request):

    # if random.randrange(10) > 2:
    #     return HttpResponseRedirect('/app/hello/')
    # return HttpResponse("Congraduate, you got the ticket")

    url = reverse('app:hello')
    print(url)
    # return HttpResponseRedirect(url)
    return redirect(url)


def get_info(request):

    data = {
        "status": 200,
        "msg": "ok",
    }
    return JsonResponse(data=data)


def set_cookie(request):

    response = HttpResponse("Set cookies")
    response.set_cookie('username', 'Rock')

    return response


def get_cookie(request):

    username = request.COOKIES.get("username")
    return HttpResponse(username)


def login(request):
    return render(request, 'login.html')


def do_login(request):

    uname = request.POST.get('uname')

    # response = HttpResponse('登陆成功')
    response = HttpResponseRedirect(reverse('app:mine'))

    # response.set_cookie('uname', uname, max_age=60)
    response.set_signed_cookie('content', uname, 'Rose')
    return response


def mine(request):

    # uname = request.COOKIES.get('content')

    try:
        uname = request.get_signed_cookie('content', salt='Rose')
        if uname:
            # return HttpResponse(uname)
            return render(request, 'mine.html', context={"uname": uname})
    except Exception as e:
        print("获取失败")
    return redirect(reverse('app:login'))


def logout(request):

    response = redirect(reverse('app:login'))
    response.delete_cookie('content')

    return response