from django.shortcuts import render

from manga.models import Manga

# Create your views here.

def profil(request,id):
  mangalist = Manga.objects.filter(user_id=id)  #recupère les mangas defini par l'id
  return render(request, 'useraccount/profil.html', {'mangahtml': mangalist })