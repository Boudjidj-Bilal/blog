var deleteBtns = document.getElementsByClassName("delete");

for (var i = 0; i < deleteBtns.length; i++) //à chaque boutton
{  
  deleteBtns[i].addEventListener("click", function() { // ajoute un événement clique
        var divPrincipalImage = this.parentNode.parentNode.parentNode; // récupère toute la div de l'image avec les boutton en remontant deux fois au parent pour aller a la div-contenair
        var precedentDivPrincipalImage = divPrincipalImage.previousElementSibling; //
        if (precedentDivPrincipalImage) 
        {
            divPrincipalImage.parentNode.insertBefore(divPrincipalImage, precedentDivPrincipalImage);
            annuler.style.display = "block"; 
            // update_order();
        }
    });
}