from os import name
from django.contrib import admin
from django.urls import path 

from myapp1 import views

urlpatterns = [
    path('maison/',views.maison,name='pagemaison'),
    path('profilbilal/',views.profilbilal,name='pageprofil'),
    path('naruto/',views.naruto,name='pagenaruto'),
    path('onepiece/',views.onepiece,name='pageonepiece'), 
    path('index',views.index,name='pageindex'),
    path('index2/',views.index2,name='pageindex2'),
    path('flowers/',views.flowers,name='pageflowers'),
    path('chaise/',views.chaise,name='pagechaise'),
    path('',views.manga,name='pagemanga'),
    path('manga/<slug:slug>/',views.mangadetail,name='pagedetailmanga'),
    path('manga/commentaire/<int:id>/',views.mangadetailcommentaire,name='pagedetailmangacommentaire'),
]
