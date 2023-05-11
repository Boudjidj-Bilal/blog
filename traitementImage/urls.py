from django.urls import path 
from traitementImage import views

app_name = "traitementImage"

urlpatterns = [
    path('traitementImage/',views.traitementImage,name='traitementImage'), 
    path('renduImage/',views.renduImage,name='renduImage'), 

]