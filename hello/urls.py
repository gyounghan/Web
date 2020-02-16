from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello',views.hello, name='home' ),
    path('signup',views.signup),
    path('signin',views.signin, name='login'),
    path('logout',views.logout, name='logout'),
]