from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from chapitre.models import Chapitre

from .models import Manga

# Create your views here.
def manga(request):
    mangaliste = Manga.objects.all()
    return render(request, 'manga/manga.html', {'mangahtml': mangaliste })

def bidon(request):
    #mangaliste = Manga.objects.all()
    return render(request, 'manga/bidon.html')

def mangadetail(request, slug=None):
    manga = get_object_or_404(Manga, slug=slug)  #recupère le manga specifique defini dans slug
    chapitre = Chapitre.objects.filter(manga=manga.id) #recupere les chapitres du manga specifique defini par son  id

    return render(request, 'manga/mangadetail.html', {'chapitreshtml': chapitre,'mangadetailhtml': manga})

