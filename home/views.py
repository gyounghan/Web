from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CreateUserForm
from .forms import PhotoUploadForm

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


def PhotoUploadView(request):
    ## 게시글 작성 페이지
    if request.method == "GET":
        form = PhotoUploadForm()
    ## 게시글 업로드 요청
    elif request.method == "POST":
        form = PhotoUploadForm(request.POST, request.FILES)

        if form.is_valid() : 
            obj = form.save() ##form 유효성 검사 후 db에 저장

    ctx = {
        'form':form,
    }
    return render(request, 'upload.html', ctx)


