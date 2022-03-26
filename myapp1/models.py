from tokenize import PseudoExtras
from django.utils.text import slugify
from django.db import models

# Create your models here.
class Flower(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    
    def __str__(self):
        return self.title

class Chaise(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title

class Voiture(models.Model):
    title = models.CharField(max_length=255, default='')

class Profile(models.Model):
    name = models.CharField(max_length=255, default='')
    age = models.IntegerField()
    
class Manga(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    slug = models.SlugField(blank=True, default='')
    


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Manga, self).save()

class Commentairechapitre(models.Model):
    pseudo = models.CharField(max_length=30, default='')
    comment = models.TextField(default='')
    date = models.CharField(max_length=30, default='')
    manga = models.ForeignKey(Manga,  null=True, on_delete=models.CASCADE)

    def __str__(self):
        #return self.pseudo
        return "%s %s %s" % ( self.date, self.pseudo, self.manga.name)
