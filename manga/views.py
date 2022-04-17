from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from chapitre.models import Chapitre

from .models import Manga

"""
la fonction "manga" permet d'afficher la liste de tous les mangas
"""
def manga(request):
    mangaliste = Manga.objects.all() #récupère tous la liste des mangas
    return render(request, 'manga/manga.html', {'mangahtml': mangaliste }) #crée la page de la liste des mangas

"""
la fonction "mangadetail" permet d'afficher le manga données avec les chapitres qui lui appartient
"""
def mangadetail(request, slug=None):
    manga = get_object_or_404(Manga, slug=slug)  #recupère le manga specifique defini dans slug
    chapitre = Chapitre.objects.filter(manga=manga.id) #recupere les chapitres du manga specifique defini par son id

    return render(request, 'manga/mangadetail.html', {'chapitreshtml': chapitre,'mangadetailhtml': manga}) #crée la page contenat le manga spécifique avec tous ces chapitres 



