from django.db import models
from useraccount.models import User

# Create your models here.

from tokenize import PseudoExtras
from django.utils.text import slugify
from django.db import models

# from useraccount.models import User


# Create your models here.
class TraitementImage(models.Model):
    image = models.ImageField(default='', blank=True, upload_to='images')
    intensite = models.IntegerField()

    # user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) #un chapitre appartient à un seul manga

    def __str__(self):
        return self
