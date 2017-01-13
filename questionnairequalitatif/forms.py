#-*- coding: utf-8 -*-
from django import forms
from .models import QuestionnaireQualitatif


class QualitatifForm(forms.ModelForm):
    class Meta:
        model = QuestionnaireQualitatif
        fields = '__all__'


