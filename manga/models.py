from tokenize import PseudoExtras
from django.utils.text import slugify
from django.db import models

# Create your models here.
class Manga(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    slug = models.SlugField(blank=True, default='')
    

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Manga, self).save()
