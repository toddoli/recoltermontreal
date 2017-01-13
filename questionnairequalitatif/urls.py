#-*- coding: utf-8 -*-

__author__ = 'Chloe'
from django.conf.urls import url
from questionnairequalitatif import views

urlpatterns = [
    url(r'^questionnairequalitatif/$', views.questionnaire, name='questionnairequalitatif'),
]