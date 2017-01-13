#-*- coding: utf-8 -*-
from django.db import models
from .forms import ProfilForm
from django.shortcuts import render



def profil(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form2 = ProfilForm(request.POST or None)
    # form2 = AuthorForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form2.is_valid():
        # Ici nous pouvons traiter les données du formulaire

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True
        form2.save()
    return render(request, 'profil/profil.html', locals())


