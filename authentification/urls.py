__author__ = 'Chloe'
from django.conf.urls import include, url
from authentification import views


urlpatterns = [
    url(r'^connexion/$', views.connexion, name='connexion'),
    url(r'^index/', views.index, name='index'),
    url(r'^resultats/', views.resultats, name='resultats'),
    url(r'^deconnexion/', views.deconnexion, name='deconnexion'),
    url(r'^bonjour/', views.dire_bonjour, name='bonjour'),
    url(r'^acces/', views.ma_vue, name='acces'),
]


