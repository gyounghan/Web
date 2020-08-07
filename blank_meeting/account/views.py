from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate


# SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
#    return HttpResponse("Hello, world, You're at the account index.")
    return render(request, 'account/index.html')

# 로그인 함수
@csrf_exempt
def signin(request):
    if request.method == 'POST':
        try :
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.get(username=username)
            if user.check_password(password):
                if user.is_active == False:
                    return render(request, 'account/signin.html')
                login(request, user)
                print("password : " + password + " " + "user.password : "+ str(user.password))
                print("user.is_active : " + str(user.is_active))
                return redirect('index')
            else:
                return render(request, 'account/signin_fail.html') 
        except:
            return render(request, 'account/signin_fail.html') 

    return render(request, 'account/signin.html') 


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            user = Account.objects.create(userid=request.POST['username'], password = request.POST['password1'], email_address = request.POST['email'])
            user.is_active = False
            user.save()
            
            user = User.objects.create_user(username=request.POST['username'], password = request.POST['password1'])
            user.is_active = False
            user.save()
            
            current_site = get_current_site(request)
            message = render_to_string('account/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "계정 활성화 확인 이메일"
            mail_to = request.POST['email']
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            return redirect('index')

    return render(request, 'account/signup.html')

# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("index")
    else:
        return redirect("index")
    return 
# Create your views here.

def signout(request):
    logout(request)
    return redirect('signin')