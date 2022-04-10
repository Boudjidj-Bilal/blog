from datetime import datetime
from email.mime import image
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
from chapitre.forms import CommentairechapitreForm
from chapitre.models import Chapitre, Commentairechapitre, Imageschapitre, Likechapitre, Vuechapitre


"""
la fonction "deletecommentaire" permet de suprimer des commentaires dans la base de donnée
"""
@login_required
def deletecommentaire(request, id=None): 
    deletecomment = Commentairechapitre.objects.get(id=id) #récupère le commentaire à suprimer
    userconnected = request.user.username #récupère l'utilisateur connecté
    user = deletecomment.pseudo #récupère la personne qui a commenté 
    if user == userconnected: #SI la personne qui est connecté est aussi la personne qui a commenté
        deletecomment.delete() #suprimer le commentaire récupéré 
    return redirect('chapitredetail',deletecomment.chapitre.slug) #rediriger vers la page chapitredetail

"""
la fonction "addcomentaire" permet d'ajouter un commentaire dans la base de donnée pour un chapitre
page html 'chapitre/commentaire.html'
"""
@login_required
def addcommentaire(request, id=None):
    #chapitre = get_object_or_404(Chapitre, id=id)
    #comments = Commentairechapitre.objects.filter(manga=manga.id)
    if request.method == 'POST': #SI l'utilisateur ajoute un commentaire alors effectue la suite:
        form = CommentairechapitreForm(request.POST) #récupère tout les champs du formulair remplis par l'utilisateur
        if form.is_valid(): #vérifier si tout les champs remplis par l'utilisateur son valide,
            commentaire = form.save(commit=False) # récupère le contenus du formulaire (pseudo,comment)
            commentaire.chapitre = Chapitre.objects.get(id=id) # ajouter le chapitre concerné par le commentaire
            commentaire.pseudo = request.user.username # ajouter l'utilisateur qui a commenté
            commentaire.date = datetime.now().strftime('%H:%M:%S') #ajouter la date du commentaire
            commentaire.save() #sauvegarder le commentaire dans la base de donnée
            return redirect('chapitredetail',commentaire.chapitre.slug) #rediriger vers la page chapitredetail
    else: #SINON effectue la suite:
        form = CommentairechapitreForm() #envoyer le formulair vide pour être saisis par l'utilisateur
    return render(request, 'chapitre/commentaire.html', {'form': form}) #renvoie à la page commentaire

""" 
la fonction "chapitredetail" permet d'afficher le contenus (détailler) du chapitre
"""
def chapitredetail(request, slug=None):
    chapitre = get_object_or_404(Chapitre, slug=slug) #récupère un chapitre donné par son slug
    comments = Commentairechapitre.objects.filter (chapitre_id = chapitre.id) #récupère tous les commentaires appartenant a un chapitre donné par son id
    likes = Likechapitre.objects.filter (chapitre_id = chapitre.id) #récupère tous les likes appartenant a un chapitre donné par son id 
    images = Imageschapitre.objects.filter (chapitre_id = chapitre.id) #récupère toutes les images appartenant a un chapitre donné par son id
    vue = Vuechapitre.objects.create() #créée une vue sans aucun champs remplis
    vue.pseudo = request.user.username # ajouter l'utilisateur qui a vue
    vue.chapitre = chapitre # remplir le champ chapitre de la vue 
    vue.save() #sauvegarder le vue dans la base de donnée
    vues = Vuechapitre.objects.all() #récupère toutes les vues
    return render(request, 'chapitre/chapitredetail.html',{'chapitrehtml': chapitre , 'commentshtml': comments , 'likehtml': likes, 'imageshtml': images, 'vueshtml': vues}) #renvoie à la page chapitredetail

"""
la donction "addlike" permet d'ajouter un like dans la base de donnée pour un chapitre
"""
@login_required
def addlike(request, id=None):
    chapitre = get_object_or_404(Chapitre, id=id) #récupérer un chapitre donné par son id
    like = Likechapitre.objects.create() #je creer un like sans aucun champs remplis
    like.pseudo = "bilal" # remplir le champ pseudo du like
    like.chapitre = chapitre # remplir le champ chapitre du like
    like.save() #sauvegarder le commentaire dans la base de donnée
    return redirect('chapitredetail',like.chapitre.slug) #rediriger vers la page chapitredetail

