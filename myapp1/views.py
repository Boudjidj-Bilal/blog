from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from myapp1.forms import CommentairechapitreForm
from datetime import datetime

from myapp1.models import Chaise, Commentairechapitre, Flower, Manga

# Create your views here.
def maison(request): 
    return render(request, 'myapp1/maison.html')

def profilbilal(request):
    return render(request, 'myapp1/profil.html')

def naruto(request):
    return render(request, 'myapp1/naruto.html')

def onepiece(request):
    return render(request, 'myapp1/onepiece.html')

def index(request):
    return render(request, 'myapp1/index.html')

def index2(request):
    return render(request, 'myapp1/index2.html')

def flowers(request):
    flowers = Flower.objects.all()
    return render(request, 'myapp1/flowers.html', {'flowershtml': flowers })

def chaise(request):
    chaises = Chaise.objects.all()
    return render(request, 'myapp1/chaise.html', {'chaiseshtml': chaises })

def manga(request):
    mangaliste = Manga.objects.all()
    return render(request, 'myapp1/manga.html', {'mangahtml': mangaliste })

def mangadetail(request, slug=None):
    manga = get_object_or_404(Manga, slug=slug)
    comments = Commentairechapitre.objects.filter(manga=manga.id)
    return render(request, 'myapp1/mangadetail.html', {'mangadetailhtml': manga, 'commentairechapitrehtml': comments })

def mangadetailcommentaire(request,id=None):
    #manga = get_object_or_404(Manga, slug=slug)
    #comments = Commentairechapitre.objects.filter(manga=manga.id)
    if request.method == 'POST':
        form = CommentairechapitreForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.manga = Manga.objects.get(id=id)
            #slug = Manga.objects.get(id=id).slug
            commentaire.date = datetime.now().strftime('%H:%M:%S')  
            commentaire.save()
            return redirect('/' )
    else:
        form = CommentairechapitreForm()
    return render(request, 'myapp1/commentaire.html', {'form': form})

