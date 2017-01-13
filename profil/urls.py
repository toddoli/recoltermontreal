#-*- coding: utf-8 -*-

__author__ = 'Chloe'
from django.conf.urls import url
from profil import views

urlpatterns = [
    url(r'^profil/$', views.profil, name='profil'),
]