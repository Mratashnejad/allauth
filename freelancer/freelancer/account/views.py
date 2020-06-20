from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def account(request):
    return render(request, 'AccountPage.html')
def signup(request):
    return render(request, 'SignupPage.html')
def login(request):
    return render(request, 'LoginPage.html')