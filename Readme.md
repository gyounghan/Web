## HOME 화면

1) 모든 호스트 접속 허가
[PRJ_HOME]/settings.py 수정 
ALLOWED_HOST = ['*']

2) HOME 앱 생성
$ python manage.py startapp [APP_NAME]


## 로그인/로그아웃

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
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('chiken1', 'chiken1@out.org', 'pass5678')
>>> user = User.objects.create_user(username = 'test1', email = 'na@na.com', password = '1234')
>>> User.objects.all() # 전체 User 리스트 확인


