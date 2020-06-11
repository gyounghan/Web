from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateAppointment
from .models import Appointment

# Create your views here.


def Create(request):
    ## 소개팅 게시글 생성
    if request.method == "GET":
        form = CreateAppointment()
    ## 소개팅 게시글 업로드 요청 
    elif request.method == "POST":
        form = CreateAppointment(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponse("Appointment 등록완료")

    ctx = {
        'form' : form,
    }
    return render(request, 'create.html', ctx)
