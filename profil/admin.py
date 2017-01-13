#-*- coding: utf-8 -*-

from django.contrib import admin
from .models import Categorie, Profil


class NomOrdreAdmin(admin.ModelAdmin):
    list_display   = ('name', 'order')
    ordering       = ('order',)
    search_fields  = ('name',)

admin.site.register(Categorie,NomOrdreAdmin)
admin.site.register(Profil)