from django.urls import path 
from traitementImage import views

app_name = "imageprocessing"

urlpatterns = [
    path('traitementImage/',views.traitementImage,name='traitementImage'), 
    path('renduImage/<str:uploaded_file_url>',views.renduImage,name='renduImage'), 

]