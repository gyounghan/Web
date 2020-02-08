from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello") 


def indexView(request):
    return render(request, 'home/index.html',{})
 
#class indexView(TemplateView):
#    template_name = 'home/index.html'
