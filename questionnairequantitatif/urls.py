#-*- coding: utf-8 -*-
from django.conf.urls import url
from questionnairequantitatif import views

urlpatterns = [
    url(r'^questionnairequantitatif/$', views.questionnaire, name='questionnairequantitatif'),
]


