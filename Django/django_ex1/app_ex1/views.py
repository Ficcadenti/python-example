from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(reguest):
    return HttpResponse('<h1>Prima App Djengo</h1>')

def zafferano1(request):
    return HttpResponse('<h1>Zafferano 1</h1>')

def zafferano2(request):
    return HttpResponse('<h1>Zafferano 2</h1>')

def zafferano3(request):
    return HttpResponse('<h1>Zafferano 3</h1>')

