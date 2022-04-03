from datetime import datetime
from email.mime import image
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from chapitre.forms import CommentairechapitreForm
from chapitre.models import Chapitre, Commentairechapitre, Imageschapitre, Likechapitre, Vuechapitre

def deletecommentaire(request, id=None):
    deletecomment = Commentairechapitre.objects.get(id=id)
    deletecomment.delete()
    return redirect('/' ) #rediriger vers la page principal

def addcommentaire(request, id=None):
    #chapitre = get_object_or_404(Chapitre, id=id)
    #comments = Commentairechapitre.objects.filter(manga=manga.id)
    if request.method == 'POST':
        form = CommentairechapitreForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False) # récupère le contenus du formulaire (pseudo,comment)
            commentaire.chapitre = Chapitre.objects.get(id=id) # ajouter le chapitre concerné par le commentaire
            commentaire.date = datetime.now().strftime('%H:%M:%S') #ajouter la date du commentaire
            commentaire.save() #sauvegarder le commentaire dans la base de donnée
            return redirect('/' ) #rediriger vers la page principal
    else:
        form = CommentairechapitreForm()
    return render(request, 'manga/commentaire.html', {'form': form})


def chapitredetail(request, slug=None):
    chapitre = get_object_or_404(Chapitre, slug=slug)
    comments = Commentairechapitre.objects.filter (chapitre_id = chapitre.id) 
    likes = Likechapitre.objects.filter (chapitre_id = chapitre.id) 
    images = Imageschapitre.objects.filter (chapitre_id = chapitre.id)
    vue = Vuechapitre.objects.create() 
    vue.pseudo = "bilal" # remplir le champ pseudo
    vue.chapitre = chapitre # remplir le champ chapitre
    vue.save() #sauvegarder le commentaire dans la base de donnée
    return render(request, 'chapitre/chapitredetail.html',{'chapitrehtml': chapitre , 'commentshtml': comments , 'likehtml': likes, 'imageshtml': images})

def addlike(request, id=None):
    chapitre = get_object_or_404(Chapitre, id=id)
    like = Likechapitre.objects.create() #je creer un objet likechapitre
    like.pseudo = "bilal" # remplir le champ pseudo
    like.chapitre = chapitre # remplir le champ chapitre
    like.save() #sauvegarder le commentaire dans la base de donnée
    return redirect('/' ) #rediriger vers la page principal
