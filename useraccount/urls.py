from useraccount import views
from django.urls import path

urlpatterns = [
    path('<int:id>/',views.profil,name='pageprofil'),
]