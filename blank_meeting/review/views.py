from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Review
from .forms import CreateReview
from django.views.generic.edit import FormView
# Create your views here.


def Create(request):
    ## 소개팅 게시글 생성
    if request.method == "GET":
        form = CreateReview()
    ## 소개팅 게시글 업로드 요청 
    elif request.method == "POST":
        form = CreateReview(request.POST, request.FILES, initial={'publisher':request.user})

        if form.is_valid():
            obj = form.save(commit=False)
            obj.publisher = request.user
            obj.save()
            return HttpResponse("Review 등록완료")

    ctx = {
        'form' : form,
    }
    return render(request, 'create.html', ctx)
