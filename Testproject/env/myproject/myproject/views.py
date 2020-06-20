from django.http import HttpResponse
from django.shortcuts import render
from . import class_car

def homepage(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('about')



