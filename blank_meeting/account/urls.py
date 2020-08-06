from django.urls import path

from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('logout/', views.signout, name='signout'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
]
