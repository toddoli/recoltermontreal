#-*- coding: utf-8 -*-
from django.conf.urls import include, url
from authentification import views

urlpatterns = [
    url(r'^connexion/$', views.connexion, name='connexion'),
    url(r'^index/$', views.index, name='index'),
    url(r'^resultats/$', views.resultats, name='resultats'),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
    url(r'^accounts/$', include('registration.backends.hmac.urls')),
    url(r'^register/$', include('django.contrib.auth.urls')),
    url(r'^creercompte/$', views.creercompte),
]

