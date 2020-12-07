from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def login(request):
    return render(request, 'home/login.html')

def signup(request):
    return render(request, 'home/signup.html')

def signupfull(request):
    return render(request, 'home/signupfull.html')
