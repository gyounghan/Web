
from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('signup/', views.signupView.as_view(), name='signup'),
    path('upload/', views.PhotoUploadView, name='photoupload'),
    path('photos/', views.PhotoListView, name='photolist'),
]
