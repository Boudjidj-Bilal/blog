from email.mime import image
from itertools import count
from django.utils.text import slugify
from django.db import models

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
    imagename = models.ImageField(default='', blank=True, upload_to='images')
    chapitre = models.ForeignKey(Chapitre, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % ( self.imagename, self.chapitre)

class Vuechapitre(models.Model):
    user = models.CharField(max_length=30, default='')
    chapitre = models.ForeignKey(Chapitre, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % ( self.user.username, self.chapitre)