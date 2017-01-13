#-*- coding: utf-8 -*-

from django.contrib import admin
from .models import Questionnairequantitatif, Organisme

class NomOrdreAdmin(admin.ModelAdmin):
    list_display   = ('name', 'order')
    ordering       = ('order',)
    search_fields  = ('name',)

class QualitatifAdmin(admin.ModelAdmin):
    list_filter    = ('nom_organisme','poids_total','nombre_varietes','nombre_personnes_toute_activite','nombre_educateurs','nombre_heures_activite','nombre_jardiniers','nombre_heures_jardins','nombre_benevoles','nombre_heures_benevoles','ca_total','ca_agriculture_urbaine','nombre_paniers','prix_panier','semis','ca_semis','nombre_semis_rustiques','nombre_ruches','poids_miel','poids_composte','poids_pluie','nombre_heures_enfant','nombre_heures_aines','nombre_sujets',)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)



admin.site.register(Questionnairequantitatif)
admin.site.register(Organisme,NomOrdreAdmin)