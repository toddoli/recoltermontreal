#-*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import QuantitativeForm
from django.contrib.auth.decorators import login_required
from questionnairequantitatif.models import Questionnairequantitatif


@login_required(redirect_field_name='rediriger_vers')




def questionnairequantitatif_list(request):
    form = Questionnairequantitatif.objects.all().filter(current_user=request.user)
    return render(request, 'questionnairequantitatif/voirquestionnaires.html', locals())


def questionnairequantitatif_new(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.


    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if request.POST:
        form = QuantitativeForm(request.data)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.current_user = request.user
            obj.save()
            # Ici nous pouvons traiter les données du formulaire
            # Nous pourrions ici envoyer l'e-mail grâce aux données
            # que nous venons de récupérer
            envoi = True


    return render(request, 'questionnairequantitatif/questionnaire.html',   locals())


def questionnairequantitatif_read(request, id=None):

    form_existant = Questionnairequantitatif.objects.all().filter(id=id)
    form = QuantitativeForm(form_existant)

    return render(request, 'questionnairequantitatif/questionnaires.html', locals())

def questionnairequantitatif_edit(request, id=None):



    return render(request, 'questionnairequantitatif/questionnaires.html', locals())