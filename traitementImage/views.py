from django.shortcuts import render

# Create your views here.

from email.mime import image
# from subprocess import CREATE_NEW_CONSOLE
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
from useraccount.models import User

from traitementImage import fonctions

from traitementImage.models import TraitementImage
from traitementImage.forms import TraitementImageForm


@login_required
def traitementImage(request): 
    if request.method == 'POST':
        form = TraitementImageForm(request.POST) #récupère tout les champs du formulair remplis par l'utilisateur
        # if form.is_valid():
            # image = TraitementImageForm(request.POST['image'])
            # intensite = TraitementImageForm(request.POST['intensite'])
        return redirect('traitementImage:renduImage')
    else: #SINON effectue la suite:
        form = TraitementImageForm() #envoyer le formulair vide pour être saisis par l'utilisateur
    return render(request, 'traitementImage/traitementImage.html', {'form': form}) # paramètre image traité) rediriger vers la page renduImage


@login_required
def renduImage(request):
    return render(request, 'traitementImage/renduImage.html')



