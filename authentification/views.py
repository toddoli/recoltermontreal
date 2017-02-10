#-*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response
from .forms import ConnexionForm, UserCreateForm
from django.contrib.auth import logout
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.views import login
from questionnairequantitatif.models import Questionnairequantitatif
from profil.models import Profil
from django.contrib.auth.models import User
import sys



from django.db.models import Avg





def resultats(request):
    return render_to_response('resultats.html')


def connexion(request):
    error = False

    if request.method == "POST":
        form3 = ConnexionForm(request.POST)
        if form3.is_valid():
            username = form3.cleaned_data["username"]
            password = form3.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user) # nous connectons l'utilisateur
                return redirect('/espaceperso')
            else: # sinon une erreur sera affichée
                error = True
    else:
        form3 = ConnexionForm()

    return render(request, 'connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def index(request):
    data = Questionnairequantitatif.objects.all()
    poids_total_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('poids_total'))['poids_total__avg'])
    nombre_varietes_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_varietes'))['nombre_varietes__avg'])
    nombre_personnes_toute_activite_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_personnes_toute_activite'))['nombre_personnes_toute_activite__avg'])
    nombre_educateurs_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_educateurs'))['nombre_educateurs__avg'])
    nombre_heures_activite_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_heures_activite'))['nombre_heures_activite__avg'])
    nombre_jardiniers_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_jardiniers'))['nombre_jardiniers__avg'])
    nombre_heures_jardins_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_heures_jardins'))['nombre_heures_jardins__avg'])
    nombre_benevoles_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_benevoles'))['nombre_benevoles__avg'])
    nombre_heures_benevoles_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_heures_benevoles'))['nombre_heures_benevoles__avg'])
    ca_total_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('ca_total'))['ca_total__avg'])
    ca_agriculture_urbaine_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('ca_agriculture_urbaine'))['ca_agriculture_urbaine__avg'])
    nombre_paniers_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_paniers'))['nombre_paniers__avg'])
    prix_panier_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('prix_panier'))['prix_panier__avg'])
    semis_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('semis'))['semis__avg'])
    ca_semis_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('ca_semis'))['ca_semis__avg'])
    nombre_semis_rustiques_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_semis_rustiques'))['nombre_semis_rustiques__avg'])
    nombre_ruches_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_ruches'))['nombre_ruches__avg'])
    poids_miel_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('poids_miel'))['poids_miel__avg'])
    poids_composte_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('poids_composte'))['poids_composte__avg'])
    poids_pluie_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('poids_pluie'))['poids_pluie__avg'])
    nombre_heures_enfant_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_heures_enfant'))['nombre_heures_enfant__avg'])
    nombre_heures_aines_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_heures_aines'))['nombre_heures_aines__avg'])
    nombre_sujets_avg = str(Questionnairequantitatif.objects.all().aggregate(Avg('nombre_sujets'))['nombre_sujets__avg'])
    current_user_avg=str(Profil.objects.all().aggregate(Avg('current_user'))['current_user__avg'])
    nom_referent_avg=str(Profil.objects.all().aggregate(Avg('nom_referent'))['nom_referent__avg'])
    courriel_avg=str(Profil.objects.all().aggregate(Avg('courriel'))['courriel__avg'])
    adresse_avg=str(Profil.objects.all().aggregate(Avg('adresse'))['adresse__avg'])
    mandat_avg=str(Profil.objects.all().aggregate(Avg('mandat'))['mandat__avg'])
    objectif_avg=str(Profil.objects.all().aggregate(Avg('objectif'))['objectif__avg'])
    personnes_impliquees_avg=str(Profil.objects.all().aggregate(Avg('personnes_impliquees'))['personnes_impliquees__avg'])
    personnes_employees_avg=str(Profil.objects.all().aggregate(Avg('personnes_employees'))['personnes_employees__avg'])
    personnes_moins_de_25_avg=str(Profil.objects.all().aggregate(Avg('personnes_moins_de_25'))['personnes_moins_de_25__avg'])
    categories_avg=str(Profil.objects.all().aggregate(Avg('categories'))['categories__avg'])
    retombees_avg=str(Profil.objects.all().aggregate(Avg('retombees'))['retombees__avg'])
    superficie_avg=str(Profil.objects.all().aggregate(Avg('superficie'))['superficie__avg'])
    adresse_jardin_avg=str(Profil.objects.all().aggregate(Avg('adresse_jardin'))['adresse_jardin__avg'])
    city_avg=str(Profil.objects.all().aggregate(Avg('city'))['city__avg'])

    return render_to_response('index.html', {'data': data, 'poids_total_avg': poids_total_avg, 'nombre_varietes_avg' : nombre_varietes_avg, 'nombre_personnes_toute_activite_avg' : nombre_personnes_toute_activite_avg, 'nombre_educateurs_avg' : nombre_educateurs_avg, 'nombre_heures_activite_avg' : nombre_heures_activite_avg, 'nombre_jardiniers_avg' : nombre_jardiniers_avg, 'nombre_heures_jardins_avg' : nombre_heures_jardins_avg, 'nombre_benevoles_avg' : nombre_benevoles_avg, 'nombre_heures_benevoles_avg' : nombre_heures_benevoles_avg, 'ca_total_avg' : ca_total_avg, 'ca_agriculture_urbaine_avg' : ca_agriculture_urbaine_avg, 'nombre_paniers_avg' : nombre_paniers_avg, 'prix_panier_avg' : prix_panier_avg, 'semis_avg' : semis_avg, 'ca_semis_avg' : ca_semis_avg, 'nombre_semis_rustiques_avg' : nombre_semis_rustiques_avg, 'nombre_ruches_avg' : nombre_ruches_avg, 'poids_miel_avg' : poids_miel_avg, 'poids_composte_avg' : poids_composte_avg, 'poids_pluie_avg' : poids_pluie_avg, 'nombre_heures_enfant_avg' : nombre_heures_enfant_avg, 'nombre_heures_aines_avg' : nombre_heures_aines_avg, 'nombre_sujets_avg' : nombre_sujets_avg,'current_user_avg' : current_user_avg, 'nom_referent_avg' : nom_referent_avg, 'courriel_avg' : courriel_avg, 'adresse_avg' : adresse_avg, 'mandat_avg' : mandat_avg, 'objectif_avg' : objectif_avg, 'personnes_impliquees_avg' : personnes_impliquees_avg, 'personnes_employees_avg' : personnes_employees_avg, 'personnes_moins_de_25_avg' : personnes_moins_de_25_avg, 'categories_avg' : categories_avg, 'retombees_avg' : retombees_avg, 'superficie_avg' : superficie_avg, 'adresse_jardin_avg' : adresse_jardin_avg, 'city_avg' : city_avg,})



def creercompte(request):
    logged = False
    error = False
    success = False
    form5 = ""
    if request.user.is_authenticated():
        logged = True
    else:
        if request.method == "POST":
            form5 = UserCreateForm(request.POST)
            if form5.is_valid():
                form5.save()
                username = form5.cleaned_data["username"]
                password = form5.cleaned_data["password1"]
                user2 = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
                if user2:
                    success = True
                else:
                    error = True
        else:
                form5 = UserCreateForm()
    return render(request, 'registration/registration_form.html', {'form5': form5, 'logged': logged, 'success': success, 'error': error})


