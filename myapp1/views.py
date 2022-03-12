from django.shortcuts import get_object_or_404, render

from myapp1.models import Chaise, Flower, Manga

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

def manga(request):
    mangaliste = Manga.objects.all()
    return render(request, 'myapp1/manga.html', {'mangahtml': mangaliste })

def mangadetail(request, slug=None):
    manga = get_object_or_404(Manga, slug=slug)
    return render(request, 'myapp1/mangadetail.html', {'mangadetailhtml': manga })