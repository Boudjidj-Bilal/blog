from email.mime import image
from itertools import count
from django.utils.text import slugify
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import random
import string

from manga.models import Manga
from useraccount.models import User


#   model chapitre
class Chapitre(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    slug = models.SlugField(blank=True, default='')
    manga = models.ForeignKey(Manga, null=True, on_delete=models.CASCADE) #un chapitre appartient à un seul manga

    def __str__(self):
        return "%s %s %s" % ( self.name, self.slug, self.manga.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.manga.name + "-" + self.name)
        super(Chapitre, self).save()

#   model commentaire
class Commentairechapitre(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comment = models.TextField(default='')
    date = models.CharField(max_length=30, default='')
    chapitre = models.ForeignKey(Chapitre,  null=True, on_delete=models.CASCADE)

    def __str__(self):
        #return self.pseudo
        return "%s %s" % ( self.date, self.user.username)

class Likechapitre(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    chapitre = models.ForeignKey(Chapitre, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % ( self.user.username, self.chapitre)

class Imageschapitre(models.Model):
    chapitre = models.ForeignKey(Chapitre, null=True, on_delete=models.CASCADE)
    imagename = models.ImageField(default='', blank=True, upload_to='images')
    order = models.IntegerField(blank=True, null=False, default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return "%s %s %s %s" % ( self.id, self.imagename, self.chapitre, self.order)

class Vuechapitre(models.Model):
    user = models.CharField(max_length=30, default='')
    chapitre = models.ForeignKey(Chapitre, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % ( self.user, self.chapitre)

class ChangementComment(models.Model):  # cette table possède une seul ligne: date du dernier changement des commentaires
    code = models.CharField(max_length=30, default='')
    chapitre = models.OneToOneField(Chapitre, null=True, on_delete=models.CASCADE)

    def __str__(self):
        #return self.pseudo
        return "%s %s %s" % ( self.code,self.chapitre.name,self.chapitre.manga.name)


"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
@receiver([post_save, post_delete], sender=Commentairechapitre)
def deleteOldCodeCreateNewCodeForCommentChanges(sender,instance, **kwargs):
    changecomments = ChangementComment.objects.filter(chapitre_id=instance.chapitre.id) #récupère la liste des changements de tout les commentaires d'un seul chapitre
    changecomments.delete() # suprime toute la liste des changements récupérer précedement
    changecomment = ChangementComment.objects.create() #je creer une ligne sans aucun champs remplis
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(20)) #créer un code aléatoire sur 20 caractère
    changecomment.code = result_str # remplir le champ code par le code de 20 caractère
    changecomment.chapitre = instance.chapitre
    changecomment.save() #sauvegarder le like dans la base de donnée



"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
@receiver([post_save], sender=Chapitre)
def creatNewChangeCommentForNewchapitre(sender,instance, **kwargs):
    changecomments = ChangementComment.objects.filter(chapitre_id=instance.id) #récupère la liste des changements de tout les commentaires d'un seul chapitre
    if changecomments:
        pass
    else:
        changecomment = ChangementComment.objects.create() #je creer une ligne sans aucun champs remplis
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(20)) #créer un code aléatoire sur 20 caractère
        changecomment.code = result_str # remplir le champ code par le code de 20 caractère
        changecomment.chapitre = instance
        changecomment.save() #sauvegarder le chapitre dans la base de donnée


@receiver([post_delete], sender=Chapitre)
def DeleteChangeCommentForDeletechapitre(sender,instance, **kwargs):
    deletecode = ChangementComment.objects.filter(chapitre_id=instance.id)
    deletecode.delete()
