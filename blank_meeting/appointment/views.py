from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import CreateAppointment, SearchForm, CreateNotification
from .models import Appointment
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.db.models import Q
# Create your views here.

def Home(request):

    appointment = Appointment.objects.all()
    # appointment = Appointment.objects.all()
    return render(request, 'index.html', {'blogs' : appointment})


def Create(request):
    ## 소개팅 게시글 생성
    if request.method == "GET":
        form = CreateAppointment()
    ## 소개팅 게시글 업로드 요청 
    elif request.method == "POST":
        form = CreateAppointment(request.POST, request.FILES, initial={'publisher':request.user})

        if form.is_valid():
            obj = form.save(commit=False)
            obj.publisher = request.user
            obj.save()
            return HttpResponse("Appointment 등록완료")

    ctx = {
        'form' : form,
    }
    return render(request, 'create.html', ctx)


#def List(request):

## 특정 게시물 상세조회
# pk : 모델 마다 자동으로 생성해준 ID 번호, primary key
def Detail(request, pk):
    appointment=get_object_or_404(Appointment, pk=pk)
    return render(request, 'detail2.html', {'appointment': appointment})


## 특정 게시물 삭제
def Delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return HttpResponse("Appointment 삭제 완료") 


## 특정 게시물에 만남 신청
def Apply(request, pk):
    appointment=get_object_or_404(Appointment, pk=pk)

    ## 게시물 작성자/만남신청자 한테 알림 메시지 보내는 로직 필요
    if request.method == "POST":
        print("여기는 들어오니?")
        appointment = get_object_or_404(Appointment, pk=pk)

        form = CreateNotification(request.POST, request.FILES)
        print(form.is_valid())

        if form.is_valid():
            print("valid가 안되나")
            obj = form.save(commit=False)
            obj.sender = request.user
            obj.receiver = appointment.publisher
            obj.message = request.POST['message']
            obj.appointment = appointment
            obj.save()
            return HttpResponse("만남신청완료")

    return render(request, 'detail2.html', {'appointment': appointment})


def SearchFormView(request):
    # post method로 값이 전달 됬을 경우
    word = request.POST.get('q', " ")
    # 검색어
    if word:
        appointment = Appointment.objects.filter(Q(title__icontains=word) | Q(content__icontains=word)).distinct()
        # appointment = Appointment.objects.all()
        return render(request, 'index.html', {'blogs': appointment, 'q': word})

    else:
        return render(request, 'index.html')

    # post_list = Appointment.objects.filter( Q(title__icontains=word) | Q(content__icontains=word)).distinct()
    # # Q 객체를 사용해서 검색한다.
    # # title,context 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사
    # #중복을 제거한다.
    # context = {}
    # context['object_list'] = post_list
    # # 검색된 결과를 컨텍스트 변수에 담는다.
    # context['search_word']= word
    # 검색어를 컨텍스트 변수에 담는다.

    # return context


def RemoveFormView():
    appointment = Appointment.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == appointment.password:
            appointment.delete()
            return redirect('/')

    return render(request, 'remove.html', {'feed': article})
