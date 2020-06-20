from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('about')
