from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime

from myapp1.models import Chaise, Flower

# Create your views here.
def maison(request): 
    return render(request, 'myapp1/maison.html')

def profilbilal(request):
    return render(request, 'myapp1/profil.html')

def naruto(request):
    return render(request, 'myapp1/naruto.html')

def onepiece(request):
    return render(request, 'myapp1/onepiece.html')

def index(request):
    return render(request, 'myapp1/index.html')

def index2(request):
    return render(request, 'myapp1/index2.html')

def flowers(request):
    flowers = Flower.objects.all()
    return render(request, 'myapp1/flowers.html', {'flowershtml': flowers })

def chaise(request):
    chaises = Chaise.objects.all()
    return render(request, 'myapp1/chaise.html', {'chaiseshtml': chaises })


