from useraccount import views
from django.urls import path

app_name = "profil"

urlpatterns = [
    path('<int:id>/',views.profil,name='pageprofil'),
]