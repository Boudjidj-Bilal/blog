from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Chapitre, Commentairechapitre, Imageschapitre

class CommentairechapitreForm(ModelForm):
    #pseudo = forms.cherField(label='Pseudo')
    class Meta:
       model = Commentairechapitre #représente le model de commentaire chapitre
       fields = ('comment',) #représente les champs de commentaire chapitre à saisir uniquement par l'utilisateur 

class ChapitreForm(ModelForm):
    class Meta:
       model = Chapitre #représente le model de Chapitre
       fields = ('name', 'description') #représente les champs de chapitre à saisir uniquement par l'utilisateur 

class ImageschapitreForm(ModelForm):
    class Meta:
        model = Imageschapitre #représente le model de Imageschapitre
        fields = ('imagename',) #représente le champ de Imageschapitre à saisir uniquement par l'utilisateur

class ChapitreEditForm(ModelForm):
    class Meta:
       model = Chapitre #représente le model de Chapitre 
       fields = ('description', 'name') #représente les champs à saisir dans le formulaire