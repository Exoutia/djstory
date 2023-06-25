from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("accounts-home")

def login(request):
    return HttpResponse("login")

def register(request):
    return HttpResponse("signup")

def logout(request):
    return HttpResponse("logout")