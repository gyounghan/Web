from django.urls import path

from . import views

urlpatterns = [
    path('post/search', views.search, name='search'),
]
