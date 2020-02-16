from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import auth
# Create your views here.
def hello(request):
    
    return render(request, 'home.html')


def signup(request):
    
    if request.method == "POST":
    
        form = UserForm(request.POST)
    
        if form.is_valid():
    
            new_user = User.objects.create_user(**form.cleaned_data)

            login(request, new_user)

            return redirect('home')
    
        else:
    
            return HttpResponse('사용자명이 이미 존재합니다.')
    
    else:
    
        form = UserForm()
    
        return render(request, 'signup.html', {'form': form})


def signin(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(username = username, password = password)
       
        if user is not None :

            login(request, user)

            return redirect('home')

        else:

            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:

        form = LoginForm()
        
        return render(request, 'signin.html', {'form': form})

def logout(request):

    auth.logout(request)

    return redirect('home')