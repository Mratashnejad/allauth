from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    form = UserCreationForm()
    return render(request, "accounts/signup.html", {'form': form})
