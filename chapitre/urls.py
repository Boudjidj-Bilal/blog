import imp
from django.urls import path 
from chapitre import views


urlpatterns = [
    path('chap/<slug:slug>/',views.chapitredetail,name='chapitredetail'),
]