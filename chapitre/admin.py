from django.contrib import admin

from chapitre.models import Commentairechapitre, Chapitre, Likechapitre, Imageschapitre, Vuechapitre

# Register your models here.
admin.site.register(Commentairechapitre)
admin.site.register(Chapitre)
admin.site.register(Likechapitre)
admin.site.register(Imageschapitre)
admin.site.register(Vuechapitre)