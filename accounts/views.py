from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/index.html')

def login(request):
    return HttpResponse("login")

def register(request):
    return HttpResponse("register") 

def logout(request):
    return HttpResponse("logout")