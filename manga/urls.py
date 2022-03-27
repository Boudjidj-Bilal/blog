from os import name
from django.contrib import admin
from django.urls import path 

from manga import views

urlpatterns = [
    path('',views.manga,name='pagemanga'),
    path('manga/<slug:slug>/',views.mangadetail,name='pagedetailmanga'),
    path('manga/bidon/',views.bidon,name='bidon'),
]