from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('create/', views.Create, name='create'),
    path('<int:pk>/', views.Detail, name='detail'), #특정 게시물 자세히보기
    path('<int:pk>/delete/', views.Delete, name='delete'), #특정 게시물 삭제
    path('<int:pk>/apply/', views.Apply, name='apply'), #특정 게시물에 만남신청
    path('post/search', views.SearchFormView, name='SearchFormView'),
    path('ppst/remove', views.RemoveFormView, name='RemoveFormView'),

]
