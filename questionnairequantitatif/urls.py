#-*- coding: utf-8 -*-
from django.conf.urls import url
from questionnairequantitatif import views

urlpatterns = [
    url(r'^questionnairequantitatif/$', views.questionnaire, name='questionnairequantitatif'),
    url(r'^questionnairequantitatif/(?P<id>[0-9]+)$', views.questionnaire, name='questionnairequantitatif'),
    url(r'^voirquestionnairequantitatif/$', views.afficherquestionnaire, name='voirquestionnairequantitatif'),

]


