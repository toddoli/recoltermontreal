#-*- coding: utf-8 -*-
from django.conf.urls import url
from questionnairequantitatif import views

urlpatterns = [
    url(r'^questionnairequantitatif/new/$', views.questionnairequantitatif_new, name='questionnairequantitatif_new'),
    url(r'^questionnairequantitatif/(?P<id>\d+)/edit/$', views.questionnairequantitatif_edit, name='questionnairequantitatif_edit'),
    url(r'^questionnairequantitatif/liste/$', views.questionnairequantitatif_list, name='questionnairequantitatif_list'),
    url(r'^questionnairequantitatif/(?P<id>\d+)/lire/$', views.questionnairequantitatif_read, name='questionnairequantitatif_read'),
    url(r'^questionnairequantitatif/$', views.questionnairequantitatif_new, name='questionnairequantitatif_new'),



]


