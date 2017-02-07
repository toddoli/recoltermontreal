#-*- coding: utf-8 -*-
from django.db import models
from .forms import ProfilForm
from django.shortcuts import render
from .models import Profil
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='rediriger_vers')
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
        obj = form2.save(commit=False)
        obj.current_user = request.user
        obj.save()
        # Ici nous pouvons traiter les données du formulaire
        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    return render(request, 'profil/profil.html', locals())

def resultats(request):
    personnes=Profil.objects.all().aggregate(Avg('personnes_impliquees'))
    return render(request,'profil/Resultats.html',  {'Resultats personnes': personnes} )
