from django.http import HttpResponse
from django.shortcuts import render



def home_page(request):
    return render(request, 'index.html')
def about_Page(request):
    return render(request, 'about.html')
def contact_Page(request):
    return render (request , 'contact.html')
def blackjack_page(request):
    return render(request, 'blackjack.html')
def roulette_page(request):
    return render(request, 'roulette.html')
def poker_page(request):
    return render(request,'poker.html')
    
