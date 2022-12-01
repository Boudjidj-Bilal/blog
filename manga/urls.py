from os import name
from django.contrib import admin
from django.urls import path 

from manga import views
app_name = "manga"


urlpatterns = [
    path('',views.manga,name='pagemanga'),
    path('manga/add/',views.addmanga,name='addmanga'),
    path('manga/edit/<int:id>/',views.editmanga,name='editmanga'),
    path('manga/delete/<int:id>/',views.deletemanga,name='deletemanga'),
    path('manga/<slug:slug>/',views.mangadetail,name='pagedetailmanga'),
]