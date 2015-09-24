from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse("Hello, you're at the polls index. IP: " + ip)

def appcheck(request):
    return HttpResponse("ok")
