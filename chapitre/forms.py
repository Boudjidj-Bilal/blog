from django import forms
from django.forms import ModelForm
from .models import Chapitre, Commentairechapitre

class CommentairechapitreForm(ModelForm):
    #pseudo = forms.cherField(label='Pseudo')
    class Meta:
       model = Commentairechapitre #représente le model de commentaire chapitre
       fields = ('comment', 'pseudo') #représente les champs de commentaire chapitre à saisir uniquement par l'utilisateur 

class ChapitreForm(ModelForm):
    class Meta:
       model = Chapitre #représente le model de Chapitre
       fields = ('name', 'description', 'slug') #représente les champs de chapitre à saisir uniquement par l'utilisateur 
