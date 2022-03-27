import datetime
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from chapitre.forms import CommentairechapitreForm
from chapitre.models import Chapitre


def addcommentaire(request,id=None):
    #manga = get_object_or_404(Manga, slug=slug)
    #comments = Commentairechapitre.objects.filter(manga=manga.id)
    if request.method == 'POST':
        form = CommentairechapitreForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            #commentaire.manga = Manga.objects.get(id=id)
            #slug = Manga.objects.get(id=id).slug
            commentaire.date = datetime.now().strftime('%H:%M:%S')  
            commentaire.save()
            return redirect('/' )
    else:
        form = CommentairechapitreForm()
    return render(request, 'manga/commentaire.html', {'form': form})


def chapitredetail(request, slug=None):
    chapitre = get_object_or_404(Chapitre, slug=slug)
    return render(request, 'chapitre/chapitredetail.html',{'chapitrehtml': chapitre})