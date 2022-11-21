# coding:utf-8
from django.urls import path
from post import views

urlpatterns = [
    path('', views.IndexView.as_view()),
]
