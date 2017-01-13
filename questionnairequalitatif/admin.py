#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Quartierdb, QuestionnaireQualitatif, Raison, VilleOrigine, Langue, SourceRevenu, Genre

class NomOrdreAdmin(admin.ModelAdmin):
    list_display   = ('name', 'order')
    ordering       = ('order',)
    search_fields  = ('name',)


class QualitatifAdmin(admin.ModelAdmin):
    list_filter    = ('date','raison','lien','bien_etre','envie_legumes','nouvelle_competence','nouvelle_competence_si_oui','implication','genre','age','enfant_0_a_4','enfant_5_a_8','enfant_8_a_12','enfant_13_a_17','condition_physique_ou_cognitive', 'condition_physique_ou_cognitive_si_oui','situation_familiale','source_revenus','revenu_annuel_familial','langue','quartier','ville_origine','resident_depuis',)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)


admin.site.register(QuestionnaireQualitatif,QualitatifAdmin)
admin.site.register(Raison,NomOrdreAdmin)
admin.site.register(Quartierdb,NomOrdreAdmin)
admin.site.register(VilleOrigine,NomOrdreAdmin)
admin.site.register(Langue,NomOrdreAdmin)
admin.site.register(SourceRevenu,NomOrdreAdmin)
admin.site.register(Genre,NomOrdreAdmin)


