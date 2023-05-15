from django.shortcuts import render

# Create your views here.

from email.mime import image
# from subprocess import CREATE_NEW_CONSOLE
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
from useraccount.models import User

from traitementImage.fonctions import *

from traitementImage.models import TraitementImage
from traitementImage.forms import TraitementImageForm
from django.core.files.storage import FileSystemStorage

from urllib.parse import quote_plus, unquote_plus


@login_required
def traitementImage(request): 
    if request.method == 'POST':
        form = TraitementImageForm(request.POST, request.FILES) #récupère tout les champs du formulair remplis par l'utilisateur
        if form.is_valid():
            formValue = form.save(commit=False) # récupère le contenus du formulaire (user,comment)
            image = formValue.image
            intensite = formValue.intensite
            fs = FileSystemStorage()
            filename = fs.save("traitementImages/" + image.name, image)
            uploaded_file_url = fs.url(filename)

            blackAndWhiteImage = convertBlackAndWhiteImage(uploaded_file_url,intensite)

            uploaded_file_url = quote_plus(blackAndWhiteImage)
            return redirect('imageprocessing:renduImage',uploaded_file_url)
        else:
            form = TraitementImageForm()
            return render(request, 'traitementImage/traitementImage.html', {'form': form}) # paramètre image traité) rediriger vers la page renduImage
    else: #SINON effectue la suite:
        form = TraitementImageForm() #envoyer le formulair vide pour être saisis par l'utilisateur
    return render(request, 'traitementImage/traitementImage.html', {'form': form}) # paramètre image traité) rediriger vers la page renduImage


@login_required
def renduImage(request, uploaded_file_url=str):
    uploaded_file_url = unquote_plus(uploaded_file_url)
    return render(request, 'traitementImage/renduImage.html',{'uploaded_file_urlhtml':uploaded_file_url })


# 'uploaded_file_urlhtml':uploaded_file_url