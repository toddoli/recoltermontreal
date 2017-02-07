#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='rediriger_vers')
def espaceperso(request):
    return render_to_response('espaceperso/espaceperso.html')

