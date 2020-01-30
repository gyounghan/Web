from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *

# Create your views here.
def hello(request):
    
    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'POST' :
       
        user_id = request.POST['username']

        password = request.POST['password']


        new_User = User_Info(UserId = user_id, Password = password)

        new_User.save()

    else :
        
        signup_form = UserCreationForm()
    
    return render(request, 'signup.html')


    