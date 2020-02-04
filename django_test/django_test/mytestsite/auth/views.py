from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
#from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


def index(request):
    return HttpResponse('auth home')

def createUser(request):
    return HttpResponse('signup page')

   
class createUser(CreateView):
    template_name = 'signup/signup.html'
    from_class = CreateUserForm
#    success_url = reverse_lazy('create_user_done')

class createUserDone(TemplateView):
    template_name = 'signup/signup_done.html' 

# Create your views here.
