from django.urls import path

from . import views

urlpatterns = [
    path('post/search', views.SearchFormView, name='SearchFormView'),
]
