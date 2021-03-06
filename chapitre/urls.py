from django.urls import path 
from chapitre import views


urlpatterns = [

    path('chap/addcomment/<int:id>/',views.addcommentaire,name='addcomments'), #id correpond à l'id du chapitre
    path('chap/deletecomment/<int:id>/',views.deletecommentaire,name='deletecomments'), #id correpond à l'id du chapitre
    path('chap/addlike/<int:id>/',views.addlike,name='addlike'),  #id correpond à l'id du chapitre
    path('chap/addchapitre/<int:id>/',views.addchapitre,name='addchapitres'),  #id correpond à l'id du manga
    path('chap/addimage/<int:id>/',views.addimagechapitre,name='addimage'),  #id correpond à l'id de chapitre
    path('chap/edit/<int:id>/',views.editchapitre,name='editchapitre'), #id correspond à l'id de chapitre
    path('chap/<slug:slug>/',views.chapitredetail,name='chapitredetail'),
]