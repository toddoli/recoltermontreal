#-*- coding: utf-8 -*-

from django import forms
from .models import Profil

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ("nom_referent", "courriel", "adresse", "mandat", "objectif", "personnes_impliquees", "personnes_employees", "personnes_moins_de_25", "categories", "retombees", "superficie", "adresse_jardin", "city")










