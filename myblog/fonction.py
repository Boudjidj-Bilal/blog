import os
import schedule
import time
import subprocess

# import datetime
# from myblog.settings import *
#  variabiliser le chemin  ====> "media/traitementImage" 


TRAITEMENTIMG = os.path.join(os.curdir,"media/traitementImages/")
                             
def delete_old_images():
    print("suprime les images ")
    
    now = time.time() # l'heure actuelle
    # cutoff = now - (24 * 60 * 60) 
    cutoff = now - (300) # l'heure actuelle - 300 secondes donc 5minute 
    print (TRAITEMENTIMG + " delete_old") 
    for filename in os.listdir(TRAITEMENTIMG): #fait une boucle sur tout les fichier du répertoire traitementImages
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".pdf"): # si le fichier est en format jpg, png, ou pdf
            path = os.path.join(TRAITEMENTIMG, filename) # os.path.join() permet de joindre le repertoire et le fichier en une seule url pour former le chemin du fichier image
            if os.path.getmtime(path) < cutoff: # os.path.getmtime() permet de récupérer ma variable sous forme de temps, si la date du fichier sélectionner est inférieur à la date actuelle moins 5minute 
                os.remove(path) # suprime l'image sélectionné 
                print(f"{filename} supprimé")



# schedule.every(5).minutes.do(delete_old_images)  # se lance toute les 5minutes
schedule.every(1).minutes.do(delete_old_images)  

while True:
    # print (TRAITEMENTIMG + " while")
    schedule.run_pending()
    time.sleep(1)

