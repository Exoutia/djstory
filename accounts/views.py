from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'accounts/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request, 'accounts/index.html')
            else:
                return render(request, 'login.hmtl', {'form': form, 'messages': ['Username or password is wrong']})
        else:
            return render(request, 'login.hmtl', {'form': form})
            
        

def register(request):
    return HttpResponse("register") 

def logout(request):
    return HttpResponse("logout")