from django.utils.text import slugify
from django.db import models

from manga.models import Manga

#   model chapitre
class Chapitre(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    slug = models.SlugField(blank=True, default='')
    manga = models.ForeignKey(Manga, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Chapitre, self).save()

#   model commentaire
class Commentairechapitre(models.Model):
    pseudo = models.CharField(max_length=30, default='')
    comment = models.TextField(default='')
    date = models.CharField(max_length=30, default='')
    chapitre = models.ForeignKey(Chapitre,  null=True, on_delete=models.CASCADE)

    def __str__(self):
        #return self.pseudo
        return "%s %s" % ( self.date, self.pseudo)

