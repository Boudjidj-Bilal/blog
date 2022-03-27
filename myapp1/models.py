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
    
