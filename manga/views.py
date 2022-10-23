from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from chapitre.models import Chapitre
from manga.forms import MangaEditForm, MangaForm

from .models import Manga

from django.contrib.auth.decorators import login_required

"""
la fonction "manga" permet d'afficher la liste de tous les mangas
"""
def manga(request):
    mangaliste = Manga.objects.all() #récupère tous la liste des mangas
    return render(request, 'manga/manga.html', {'mangalistehtml': mangaliste }) #crée la page de la liste des mangas

"""
la fonction "mangadetail" permet d'afficher le manga données avec les chapitres qui lui appartient
"""
def mangadetail(request, slug=None):
    manga = get_object_or_404(Manga, slug=slug)  #recupère le manga specifique defini dans slug
    chapitre = Chapitre.objects.filter(manga=manga.id) #recupere les chapitres du manga specifique defini par son id

    return render(request, 'manga/mangadetail.html', {'chapitreshtml': chapitre,'mangadetailhtml': manga}) #crée la page contenat le manga spécifique avec tous ces chapitres 

@login_required
def addmanga(request):
    if request.method == 'POST': #SI l'utilisateur ajoute un manga alors effectue la suite:
        form = MangaForm(request.POST, request.FILES) #récupère tout les champs du formulair remplis par l'utilisateur
        if form.is_valid(): #vérifier si tout les champs remplis par l'utilisateur son valide,
            manga = form.save(commit=False) # récupère le contenus du formulaire (pseudo,comment)
            manga.user = request.user # ajouter l'utilisateur qui a commenté
            #manga.date = datetime.now().strftime('%H:%M:%S') #ajouter la date du manga
            manga.save() #sauvegarder le manga dans la base de donnée
            return redirect('pageprofil',request.user.id) #rediriger vers la page profil.html d'un utilisateur
    else: #SINON effectue la suite:
        form = MangaForm() #envoyer le formulair vide pour être saisis par l'utilisateur
    return render(request, 'manga/formulaireaddmanga.html', {'form': form}) #renvoie à la page formulaireaddmanga

@login_required
def editmanga(request, id=None): #le id est celui du manga
    manga = Manga.objects.get(id=id)
    if request.method == 'POST': #SI l'utilisateur ajoute un manga alors effectue la suite:
        form = MangaEditForm(request.POST, request.FILES, instance=manga) #récupère tout les champs du formulair remplis par l'utilisateur
        if form.is_valid(): #vérifier si tout les champs remplis par l'utilisateur son valide
            manganew = form.save(commit=False) # récupère le contenus du formulaire (pseudo,comment)
            manganew.save() #sauvegarder le manga dans la base de donnée
            return redirect('pageprofil',request.user.id) #rediriger vers la page profil.html d'un utilisateur
    else: #SINON effectue la suite:
        form = MangaEditForm(instance=manga) #envoyer le formulair vide pour être saisis par l'utilisateur
    return render(request, 'manga/formulaireaddmanga.html', {'form': form}) #renvoie à la page formulaireaddmanga

@login_required
def deletemanga(request, id=None): #le id est celui du manga
    manga = Manga.objects.get(id=id)
    manga.delete()
    return redirect('pageprofil',request.user.id) #rediriger vers la page profil.html d'un utilisateur


@login_required
def deletechapitre(request, id=None): #le id est celui du chapitre
    chapitre = Chapitre.objects.get(id=id)
    chapitre.delete()
    return redirect('chapitre/formulaireeditchapitre.html',request.user.id) #rediriger vers la page profil.html d'un utilisateur
