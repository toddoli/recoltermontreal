__author__ = 'Chloe'
#-*- coding: utf-8 -*-
from django import forms

# Create your models here.
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

