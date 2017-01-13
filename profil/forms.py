#-*- coding: utf-8 -*-

from django import forms
from .models import Profil

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = '__all__'

