#-*- coding: utf-8 -*-
from .models import Questionnairequantitatif
from django import forms


class QuantitativeForm(forms.ModelForm):

    class Meta:
        model = Questionnairequantitatif
        fields = ("poids_total","nombre_varietes","nombre_personnes_toute_activite","nombre_educateurs","nombre_heures_activite","nombre_jardiniers","nombre_heures_jardins","nombre_benevoles","nombre_heures_benevoles","ca_total","ca_agriculture_urbaine","nombre_paniers","prix_panier","semis","ca_semis","nombre_semis_rustiques","nombre_ruches","poids_miel","poids_composte","poids_pluie","nombre_heures_enfant","nombre_heures_aines","nombre_sujets",)

