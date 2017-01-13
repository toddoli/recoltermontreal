#-*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response
from .forms import ConnexionForm
from django.contrib.auth import logout
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login


def resultats(request):
    return render_to_response('resultats.html')

def index(request):
    return render_to_response('index.html')

def connexion(request):
    error = False

    if request.method == "POST":
        form3 = ConnexionForm(request.POST)
        if form3.is_valid():
            username = form3.cleaned_data["username"]
            password = form3.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form3 = ConnexionForm()

    return render(request, 'connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


def dire_bonjour(request):
    if request.user.is_authenticated():
        return HttpResponse("Salut, {0} !".format(request.user.username))
    return HttpResponse("Salut, anonyme.")



@login_required
def ma_vue(request):
    return HttpResponse("Salut, mec.")
