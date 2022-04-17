from tokenize import PseudoExtras
from django.utils.text import slugify
from django.db import models

from useraccount.models import User


# Create your models here.
class Manga(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    slug = models.SlugField(blank=True, default='')
    image = models.ImageField(default='', blank=True, upload_to='images')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) #un chapitre appartient à un seul manga

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Manga, self).save()

