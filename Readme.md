## HOME 화면
0) /home : hello ~ 문구 출력 페이지


1) 모든 호스트 접속 허가  
[PRJ_HOME]/settings.py 수정  
ALLOWED_HOST = ['*']  
  
2) HOME 앱 생성  
$ python manage.py startapp [APP_NAME]
  

## 로그인/로그아웃
0) /accounts/login : 로그인 화면   


1) django 기본 auth 기능 가져오기  
[PRJ_HOME]/urls.py 수정  

urlpatterns = [  
  url(r'^accounts/', include('django.contrib.auth.urls')),  
]  


2) auth 기능 가져오면 자동으로 설정되는 url들  
^login/$ [name='login']  
^logout/$ [name='logout']  
^password_change/$ [name='password_change']  
^password_change/done/$ [name='password_change_done']  
^password_reset/$ [name='password_reset']  
^password_reset/done/$ [name='password_reset_done']  
^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']  
^reset/done/$ [name='password_reset_complete']  

3) auth 기능 사용시, view 함수 작성 필요 없음, template만 작성하면 됨.  -> login 화면 템플릿 작성하기   

- 템플릿경로 (변경불가) : registration/login.html  
- 로그인 완료 시 redirection url 설정 -> settings.py 변경 필요  
LOGIN_REDIRECT_URL = '/경로이름/' 추가  


4) 로그인 테스트 계정 생성하기  
$ python manage.py shell  
- from django.contrib.auth.models import User  
- user = User.objects.create_user('chiken1', 'chiken1@out.org', 'pass5678')  
- user = User.objects.create_user(username = 'test1', email = 'na@na.com', password = '1234')  
- User.objects.all() # 전체 User 리스트 확인  

## 회원가입
0) /home/signup : 회원가입 화면   

1) forms.py 생성  
회원 가입 form 작성  

2) reverse_lazy('[URL_NAME]')  
회원 가입 성공 시 redirection할 url의 name을 넣어줘야 함  


## 사진 업로드
0) /admin : admin 페이지 UI로 사진 업로드 가능

1) settings.py 에 MEDIA_URL, MEDIA_ROOT 설정
MEDIA_URL = '/picutres/' -> 사진 파일 업로드 URL
MEDIA_ROOT = os.path.join(BASE_DIR, 'pictures') -> 실제 사진을 저장할 디렉토리

2) project의 urls.py 에 MEDIA_URL 반영
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

3) models.py 작성  
Photo Model 만듦

3') admin.py 에 모델 추가  
admin.site.register(Photo)

4) migration
$ python manage.py makemigrations
$ python manage.py migrate


## 게시글 업로드
0) /home/upload : 게시글 입력 받고 업로드 가능  

1) views.py 수정  
request가 GET 일때; 게시글 form 입력 받기.   
request가 POST 일 때; 게시글 form 유효성 검사 후 업로드. 


## 게시글 목록
0) /home/photos : DB에 저장된 게시글 목록 출력  
1) views.py 수정   
Photo.objects.all() 함수로 DB에 있는 Photo 모델 다 불러옴.   
ctx로 template HTML에 전달    
2) HTML 작성   
{% 코드구문 %} 넣으면 HTMl안에서 코드 실행  
ctx로 넘겨준 변수명을 HTML에서 사용가능  


## 댓글
0) /home/photos : 게시글 목록 출력에 댓글 칼럼 추가함.   
1) models.py 수정   
Comment 모델 -> ForeginKey로 Photo 모델과 1:N 관계형 모델 만듦  
2) HTML 작성   
{% comment in photo.comments.all %} 로 photo객체와 관계된 N개 comment 루프 돔.
