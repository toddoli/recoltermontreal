#-*- coding: utf-8 -*-
from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User

class Categorie(models.Model):
    name = models.CharField(max_length=1000)
    order = models.CharField(max_length=1)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Profil(models.Model):
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    nom_organisme = models.TextField(blank=True)
    nom_referent = models.TextField(blank=True)
    courriel = models.EmailField(blank=True)
    adresse = models.TextField(blank=True)
    mandat = models.TextField(blank=True)
    objetif = models.TextField(blank=True)
    personnes_impliquees = models.IntegerField(blank=True)
    personnes_employees = models.IntegerField(blank=True)
    personnes_moins_de_25 = models.IntegerField(blank=True)
    categories = models.ManyToManyField(Categorie, verbose_name="8. Quelles sont les catégories d’activités mises sur pied par votre organisme?",default='Sélectionnez')
    retombees = models.TextField(blank=True)
    superficie = models.IntegerField(default='0')
    adresse_jardin = models.TextField(blank=True)
    city = models.CharField(max_length=255, default='Montreal')
    location = PlainLocationField(based_fields=['city'], zoom=7, default='45.5016889,-73.56725599999999')