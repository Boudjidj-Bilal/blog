from django.urls import path 
from chapitre import views


urlpatterns = [
    path('chap/<slug:slug>/',views.chapitredetail,name='chapitredetail'),
    path('chap/addcomment/<int:id>/',views.addcommentaire,name='addcomments'),
    path('chap/deletecomment/<int:id>/',views.deletecommentaire,name='deletecomments'),
    path('chap/addlike/<int:id>/',views.addlike,name='addlike'),
]