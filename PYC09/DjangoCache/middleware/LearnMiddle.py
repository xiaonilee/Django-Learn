import random
import time

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):
    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))

        ip = request.META.get('REMOTE_ADDR')

#实现权重控制案例：
        # if request.path == '/app/getphone/':
        #     if ip == '127.0.0.1':
        #         if random.randrange(100) > 20:
        #             return HttpResponse('Congratulate, you got the phone!')
        #
        # if request.path == '/app/getticket/':
        #     if ip.startwith('10.0.22.7'):
        #         return HttpResponse('You are too late!')
        #
        # if request.path == '/app/search/':
        #     result = cache.get(ip)
        #     if result:
        #         return HttpResponse('Search Too Frequently, Please WAIT FOR Another 10 Second')
        #     cache.set(ip, ip, timeout=10)

#实现频率反爬控制案例：
        # black_list = cache.get('black', [])
        #
        # if ip in black_list:
        #     return HttpResponse('BLACK LIST')
        #
        # requests = cache.get(ip, [])
        #
        # while requests and time.time() - requests[-1] > 60:
        #     requests.pop()
        #
        # requests.insert(0, time.time())
        # cache.set(ip, requests, timeout=60)
        #
        # if len(requests) > 30:
        #     black_list.append(ip)
        #     cache.set('black', black_list, timeout=60*60*24)
        #     return HttpResponse('No chance Now, You can go back to try tomorrow')
        #
        # if len(requests) > 10:
        #     return HttpResponse('Too frequently, please hold on!')
        pass

#
    def process_exception(self, request, exception):
        print(request, exception)
        return redirect(reverse('app:index'))
