from django.contrib import admin

# Register your models here.
from myapp1.models import  Flower, Voiture, Chaise, Profile
admin.site.register(Flower)
admin.site.register(Voiture)
admin.site.register(Chaise)
admin.site.register(Profile)
