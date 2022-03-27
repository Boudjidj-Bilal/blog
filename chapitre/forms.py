from django import forms
from django.forms import ModelForm
from .models import Commentairechapitre

class CommentairechapitreForm(ModelForm):
    #pseudo = forms.cherField(label='Pseudo')
    class Meta:
       model = Commentairechapitre
       fields = ('comment', 'pseudo')
