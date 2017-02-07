#-*- coding: utf-8 -*-
from django.conf.urls import url
from espaceperso import views


urlpatterns = [
    url(r'^espaceperso/', views.espaceperso, name='espaceperso'),

]


