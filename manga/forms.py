from django.forms import ModelForm

from manga.models import Manga

class MangaForm(ModelForm):
    #pseudo = forms.cherField(label='Pseudo')
    class Meta:
       model = Manga #représente le model de Manga 
       fields = ('name', 'description', 'image') #représente les champs à saisir dans le formulaire

class MangaEditForm(ModelForm):
    #pseudo = forms.cherField(label='Pseudo')
    class Meta:
       model = Manga #représente le model de Manga 
       fields = ('description', 'image') #représente les champs à saisir dans le formulaire

