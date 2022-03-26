from django.contrib import admin

# Register your models here.
from myapp1.models import Commentairechapitre, Flower, Voiture, Chaise, Profile, Manga
admin.site.register(Flower)
admin.site.register(Voiture)
admin.site.register(Chaise)
admin.site.register(Profile)
admin.site.register(Manga)
admin.site.register(Commentairechapitre)
