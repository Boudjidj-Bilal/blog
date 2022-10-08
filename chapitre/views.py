from datetime import datetime
from email.mime import image
# from subprocess import CREATE_NEW_CONSOLE
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
from chapitre.forms import ChapitreEditForm, ChapitreForm, CommentairechapitreForm, ImageschapitreForm
from chapitre.models import ChangementComment, Chapitre, Commentairechapitre, Imageschapitre, Likechapitre, Vuechapitre
from manga.models import Manga
from useraccount.models import User


"""
la fonction "deletecommentaire" permet de suprimer des commentaires dans la base de donnée
"""
@login_required
def deletecommentaire(request, id=None): 
    deletecomment = Commentairechapitre.objects.get(id=id) #récupère le commentaire à suprimer
    userconnected = request.user.username #récupère l'utilisateur connecté
    username = deletecomment.user.username #récupère la personne qui a commenté 
    if username == userconnected: #SI la personne qui est connecté est aussi la personne qui a commenté
        deletecomment.delete() #suprimer le commentaire récupéré 
    return redirect('chapitredetail',deletecomment.chapitre.slug) #rediriger vers la page chapitredetail

@login_required
def deletecommentairejs(request, id=None): 
    deletecomment = Commentairechapitre.objects.get(id=id) #récupère le commentaire à suprimer qui contient l'id spécifique
    userconnected = request.user.username #récupère l'utilisateur connecté
    username = deletecomment.user.username #récupère la personne qui a commenté 
    if username == userconnected: #SI la personne qui est connecté est aussi la personne qui a commenté
        deletecomment.delete() #suprimer le commentaire récupéré 
        return JsonResponse({'deletecomment': True }) #rediriger vers la page chapitredetail
    else:
        return JsonResponse({'deletecomment': False }) #rediriger vers la page chapitredetail

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
            commentaire = form.save(commit=False) # récupère le contenus du formulaire (user,comment)
            commentaire.chapitre = Chapitre.objects.get(id=id) # ajouter le chapitre concerné par le commentaire
            commentaire.user = request.user # ajouter l'utilisateur qui a commenté
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
    userconnected = request.user.username #récupère l'utilisateur connecté
    if (userconnected):
        vueuserchap = Vuechapitre.objects.filter (user=userconnected, chapitre_id=chapitre) #récupère la vue qui correspond a un utilisateur données et un chapitre
        if (not vueuserchap):  #si il n'existe pas   
                    vue = Vuechapitre.objects.create() #créée une vue sans aucun champs remplis
                    vue.user = request.user.username # ajouter l'utilisateur qui a vue
                    vue.chapitre = chapitre # remplir le champ chapitre de la vue 
                    vue.save() #sauvegarder le vue dans la base de donnée
        else:
            pass
    else: 
        pass
    vues = Vuechapitre.objects.filter(chapitre_id=chapitre) #récupère toutes les vues qui correponde au chapitre donnée
    #  récuperer  le  dernier code
    codedb = ChangementComment.objects.filter(chapitre_id=chapitre).last().code
    return render(request, 'chapitre/chapitredetail.html',{'chapitrehtml': chapitre , 'commentshtml': comments , 'likehtml': likes, 'imageshtml': images, 'vueshtml': vues, 'codehtml': codedb }) #renvoie à la page chapitredetail

"""
la fonction "addlike" permet d'ajouter un like dans la base de donnée dans la table like
"""
@login_required
def addlike(request, id=None):
      user = request.user #récupère l'utilisateur connecté 
    #   slug = like.chapitre.slug
      chapitre = get_object_or_404(Chapitre, id=id) #récupérer un chapitre donné par son id que l'on veut liker
      likeexistindb = Likechapitre.objects.filter(user = user.id, chapitre = chapitre.id) #vérifier dans la base de données si il y a au moins une ligne contenent l'user connecté et le chapitre concerné 
      if (likeexistindb.count() == 0): #si il n'y a pas de like alors effectue la suite
        like = Likechapitre.objects.create() #je creer un like sans aucun champs remplis
        like.user = user # remplir le champ user du like
        like.chapitre = chapitre # remplir le champ chapitre du like
        like.save() #sauvegarder le commentaire dans la base de donnée
      else: #sinon il y a deja un like
        likeexistindb.delete() #alors surprime tous les likes concerné par l'user qui a liké un même chapitre
      return redirect('chapitredetail',chapitre.slug) #rediriger vers la page chapitredetail
    

"""
la fonction "addlikeJS" permet d'ajouter un like dans la base de donnée dans la table like
"""
# @login_required
def addlikeJS(request, id=None):
      
      user = request.user #récupère l'utilisateur connecté 
    #   slug = like.chapitre.slug
      chapitre = get_object_or_404(Chapitre, id=id) #récupérer un chapitre donné par son id que l'on veut liker
      likeexistindb = Likechapitre.objects.filter(user = user.id, chapitre = chapitre.id) #vérifier dans la base de données si il y a au moins une ligne contenent l'user connecté et le chapitre concerné 
      if (likeexistindb.count() == 0): #si il n'y a pas de like alors effectue la suite
        like = Likechapitre.objects.create() #je creer un like sans aucun champs remplis
        like.user = user # remplir le champ user du like
        like.chapitre = chapitre # remplir le champ chapitre du like
        like.save() #sauvegarder le like dans la base de donnée
        return JsonResponse({'nombreLike': likeexistindb.count()}) #rediriger vers la page chapitredetail
      else: #sinon si il y a deja un like
        likeexistindb.delete() #alors surprime tous les likes concerné par l'user qui a liké un même chapitre
        return JsonResponse({'nombreLike': 0 }) #rediriger vers la page chapitredetail

"""
la fonction "addchapitre" permet de ajoter un chapitre dans la base de donnée dans la table chapitre
"""
@login_required
def addchapitre(request, id=None): # le id représente le id de manga
    if request.method == 'POST': #SI l'utilisateur ajoute un chapitre alors effectue la suite:
        form = ChapitreForm(request.POST) #récupère tout les champs du formulair remplis par l'utilisateur
        if form.is_valid(): #vérifier si tout les champs remplis par l'utilisateur son valide,
            chapitre = form.save(commit=False) # récupère le contenus du formulaire (user,comment)
            chapitre.manga = Manga.objects.get(id=id) # ajouter le chapitre concerné par le manga
            #manga.user = request.user # ajouter l'utilisateur qui a commenté
            #manga.date = datetime.now().strftime('%H:%M:%S') #ajouter la date du manga
            chapitre.save() #sauvegarder le chapitre dans la base de donnée
            return redirect('pagedetailmanga',chapitre.manga.slug) #rediriger vers la page chapitre d'un utilisateur
    else: #SINON effectue la suite:
        form = ChapitreForm() #envoyer le formulair vide pour être saisis par l'utilisateur
    return render(request, 'chapitre/formulaireaddchapitre.html', {'form': form}) #renvoie à la page formulaireaddmanga

@login_required
def addimagechapitre(request, id=None):
    if request.method == 'POST': #SI l'utilisateur ajoute une image alors effectue la suite:
        form = ImageschapitreForm(request.POST, request.FILES) #récupère tout les champs du formulair remplis par l'utilisateur
        if form.is_valid(): #vérifier si tout les champs remplis par l'utilisateur son valide
            imagename = form.save(commit=False) # récupère le contenus du formulaire (user,comment)
            imagename.chapitre = Chapitre.objects.get(id=id) # ajouter l'image concerné par le chapitre
            imagename.save() #sauvegarder l'image dans la base de donnée
            return redirect('chapitredetail',imagename.chapitre.slug) #rediriger vers la page chapitre d'un utilisateur
    else: #SINON effectue la suite:
        form = ImageschapitreForm() #envoyer le formulair vide pour être saisis par l'utilisateur
        return render(request, 'chapitre/formulaireaddimage.html', {'form': form}) #renvoie à la page formulaireadd

@login_required
def editchapitre(request, id=None): #le id est celui du chapitre
    chapitre = Chapitre.objects.get(id=id)
    if request.method == 'POST': #SI l'utilisateur ajoute un chapitre alors effectue la suite:
        form = ChapitreEditForm(request.POST, request.FILES, instance=chapitre) #récupère tout les champs du formulair remplis par l'utilisateur
        if form.is_valid(): #vérifier si tout les champs remplis par l'utilisateur son valide
            chapitrenew = form.save(commit=False) # récupère le contenus du formulaire (name,description)
            chapitrenew.save() #sauvegarder le chapitre dans la base de donnée
            return redirect('pagedetailmanga', chapitrenew.manga.slug) #rediriger vers la page detailmanga d'un utilisateur
    else: #SINON effectue la suite:
        form = ChapitreEditForm(instance=chapitre) #envoyer le formulair vide pour être saisis par l'utilisateur
    return render(request, 'chapitre/formulaireeditchapitre.html', {'form': form}) #renvoie à la page formulaireeditchapitre




def changecomments(request, chapitreid, derniercode):
    codedb = ''
    try:
       codedb = ChangementComment.objects.filter(chapitre_id=chapitreid).last().code
    finally:
        pass

    print("code data base : "+codedb+" dernier code : "+derniercode)

    if codedb == derniercode:

        return JsonResponse(
            {
                'changement': False 
            }
        )  #rediriger vers la page chapitredetail
    else: 
        commentaires = Commentairechapitre.objects.filter(chapitre=chapitreid) #récupère tous les commentaires d'un seul chapitre spécifique
        # récuperer l'utilisateur username
        utilisateurs = User.objects.all()

        userconnected = request.user.username

        userSerializes = serializers.serialize('json', utilisateurs)

        commentsSerializes = serializers.serialize('json', commentaires)
        return JsonResponse(
            {
                'changement': True,
                'derniercode':codedb,
                'comments': commentsSerializes,
                'users': userSerializes,
                'userconnected': userconnected,
            } 
        )
