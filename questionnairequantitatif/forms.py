#-*- coding: utf-8 -*-
from .models import Questionnairequantitatif
from django import forms


class QuantitativeForm(forms.ModelForm):
    class Meta:
        model = Questionnairequantitatif
        fields = '__all__'

