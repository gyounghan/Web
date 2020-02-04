from django.urls import path 
from .import views


urlpatterns = [
    path('', views.createUser.as_view(), name='signup'),
]
