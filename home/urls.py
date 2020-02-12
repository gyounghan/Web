
from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('signup/', views.signupView.as_view(), name='signup'),
]
