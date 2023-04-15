let humberger = document.querySelector('#humberger'); //récupère la balise qui contient le id humberger et affecte le a la variable humberger
let taillemobile = 600;  // récupère la taille de l'écrant (largeur) du mobile et affecte le a la variable taillemobile


humberger.addEventListener("click", myFunction); // créer un éléments click sur la variable humberger et lorsque qu'il click execute myfonction


let affiche = false;  //créer une variable (faux) qui s'appelle affiche pour que sur telephone au démarrage le menu ne s'affiche pas par defaut

function myFunction(event) { 
    let tailleEcran = document.body.clientWidth; // taille de l'écrant courant
    console.log('document.body.clientWidth'+ document.body.clientWidth); //affiche la taille de l'écrant sur console log
    if (tailleEcran < taillemobile ) { // si la taille courante est inférieur à la taille maximal du mobile
        event.preventDefault() //enlève le comportement par défaut

        // var element = document.getElementById("");
        let menu = document.querySelector('#menu'); //récupère la balise qui contient le id menu et affecte le a la variable menu
        if (affiche === true)   { //si il clique sur le humberger et que le menu est visible
            menu.classList.remove("actif"); // alors suprime la class actif qui contient display=flex
            menu.classList.add("inactif"); // et ajoute la class inactif qui contient display=none        
            affiche = false; // donc n'affiche pas le menu
            if (event.target.className === 'elementmenu') { //récupère la class elementmenu  
                console.log(this.getAttribute("href")); //affiche le liens href sur le console log
                let liensElementMenu = this.getAttribute("href"); //récupère le liens de elementmenu et affecte le a la variable liensElementMenu
                window.location.href = liensElementMenu //va sur le liens récupérer avant

            }            
            // console.log(event.currentTarget.id);
        }
        else { //sinon
            menu.classList.add("actif"); // sinon ajoute la class actif
            menu.classList.remove("inactif"); //et suprime la class inactif
            affiche = true; //donc affiche le menu
    
        }
    }
    
  }


  let elementmenus = document.querySelectorAll('.elementmenu'); //récupère toute les balise possédant la classe elementmenu et affecte le a la variable elementmenus

  elementmenus.forEach(elementmenu => { //fait une boucle


    elementmenu.addEventListener("click", myFunction); // crér un evennement clique sur chacune de ses balise et applique myfonction sur l'évenement clique
  });

