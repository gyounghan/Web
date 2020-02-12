from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CreateUserForm
# Create your views here.


def index(request):
    return HttpResponse("Hello") 


def indexView(request):
    return render(request, 'home/index.html',{})
 
#class indexView(TemplateView):
#    template_name = 'home/index.html'


class signupView(CreateView):
    template_name = 'registration/signup.html'
    form_class =  CreateUserForm
    success_url = reverse_lazy('index')
