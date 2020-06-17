from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import CreateAppointment, SearchForm
from .models import Appointment
from django.views.generic.edit import FormView
# Create your views here.


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

<<<<<<< HEAD

#def List(request):



## 특정 게시물 상세조회
# pk : 모델 마다 자동으로 생성해준 ID 번호, primary key
def Detail(request, pk):
    appointment=get_object_or_404(Appointment, pk=pk)
    return render(request, 'detail.html', {'appointment': appointment})


## 특정 게시물 삭제
def Delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return HttpResponse("Appointment 삭제 완료") 


## 특정 게시물에 만남 신청
def Apply(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    ## 게시물 작성자/만남신청자 한테 알림 메시지 보내는 로직 필요
    return HttpResponse("만남신청완료")
=======
class SearchFormView():
    form_class = SearchForm 
    template_name = 'search.html' 
    
    def form_valid(self, form): 
        # post method로 값이 전달 됬을 경우 
        word = '%s' %self.request.POST['word'] 
        # 검색어 
        post_list = Appointment.objects.filter( Q(title__icontains=word) | Q(content__icontains=word) 
        # Q 객체를 사용해서 검색한다. 
        # title,context 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사 
        ).distinct() #중복을 제거한다. 
        context = {}
        context['object_list'] = post_list 
        # 검색된 결과를 컨텍스트 변수에 담는다. 
        context['search_word']= word 
        # 검색어를 컨텍스트 변수에 담는다. 
        
        return context
>>>>>>> 6211a2863860b3f13821417ef125371e82f5765b
