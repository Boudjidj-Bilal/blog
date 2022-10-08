let mydomorigin = window.location.origin; 

// gestion de addlike

//portabilité de variable: une variable global est accessible partout dans le programe elle est mise à l'exterieur des fonction 
// une variable a l'intérieur d'une fonction est local à la fonction uniquement, elle ne seras pas accessible en dehors de cette fonction
// une variable à l'intérieur d'un boucle est local uniqquement à la boucle, elle ne seras pas accessible en dehors de cette boucle

let like = document.querySelector('#like'); //récupère la balise qui contient le id like et affecte le a la variable like

let nombreDeLike = document.querySelector('#nombreDeLike'); //récupère la balise qui contient le id nombreDeLike et affecte le a la variable nombreDeLike


like.addEventListener("click", myFunction); // créer un événnement click sur la variable like et lorsque qu'il click execute myfonction
 


function myFunction(event) {

    let chapitreId = nombreDeLike.dataset.chapitreid 
     console.log('ok je vais lancer ajax'); // affiche un message dans la console log du browser
    let url = mydomorigin + '/chapitre/chap/addlikeJS/' + chapitreId + '/' //récupère l'url
    $.ajax({  // ajax permet d'envoyer des requêtes CRUD au serveur
        url: url, // interroge cette url
        type: "GET", // 
        dataType: "json", // type clé valeurs exemple nom:Boudjidj ; prénom:Bilal de format à envoyer
        success: (reponse) => { // si il envoie une réponse positive alors effectue la suite, le reponse contient les données que me répons le serveur
            console.log('réponse succés django');
            console.log(reponse) // affiche toutes les données
            nombreDeLike.textContent= reponse.nombreLike // parmis toute les données récupéré, récupère seulement le nombre de like et affecte le au texte de la balise qui contient l'id nombreDeLike     j'ai compris le commentaire
        },
        error: (error) => { // sinon éxecute
           console.log('réponse erreur django');
        }
      });
}

// gestion de la supression des commentaires

let btnDeleteComments = document.querySelectorAll('.btnDeleteCommente'); //récupère la balise qui contient le id  et affecte le a la variable btndeletecomments


btnDeleteComments.forEach(btnDeleteComment => { //fait une boucle


btnDeleteComment.addEventListener("click", FunctionDeleteComment); // crér un evennement clique sur chacune de ses balise et applique myfonction sur l'évenement clique
});

function FunctionDeleteComment(event) {
    let commentaireId = this.dataset.commentid; // récupère (dans la balise en cours) tout les attribus commencent par data- de l'éléments en cours (commentid) exemple: data-commentid
    console.log(commentaireId); // affiche le commentaireId qui se trouve dans le html dans la console log du browser 
    let url = mydomorigin + '/chapitre/chap/deletecommentJS/' + commentaireId + '/' //récupère l'url de deletecommentJS
    $.ajax({  // ajax permet d'envoyer des requêtes CRUD au serveur
      url: url, // interroge l'url deletecommentJS
      type: "GET", // 
      dataType: "json", // type clé valeurs exemple nom:Boudjidj ; prénom:Bilal de format à envoyer
      success: (reponse) => { // si il envoie une réponse positive alors effectue la suite, le data contient toutes les données que me répons le serveur
          console.log('réponse succés django');
          console.log(reponse) // affiche toutes les données
          let deletecomment = reponse.deletecomment // parmis les données récupère seulement deletecomment qui contient soit true ou false
          console.log(deletecomment) // affiche toutes les données
          if (deletecomment === true ) { // si la réponse donnée est vrai alors effectue la suite 
            let baliseCommentaireId = '#comment-'+ commentaireId // créer une variable baliseCommentaireId et affecte le nom de l'id
            let baliseCommentaire = document.querySelector(baliseCommentaireId) // créer une variable baliseCommentaire et affecte lui la balise qui contient le commentaireId
            baliseCommentaire.remove() // suprime la balise qui contient l'id commentaireId

          }
        
      },
      error: (error) => { // sinon éxecute
         console.log('réponse erreur django');
      }
    });
}

let changecomments = document.querySelector('#changecomment');

//changecomments.addEventListener("click", FunctionChangeComments); // crér un evennement clique sur chacune de ses balise et applique myfonction sur l'évenement clique

let initialisation = true

let url = ''
let channgement = false
function FunctionChangeComments(event){

 
  let  chapitreId = changecomments.dataset.chapitreid // data-

  if ( initialisation === true) // si  la page se charge pour la première fois 
  {
      let dernierCode  = changecomments.dataset.derniercode // data- 
      initialisation = false; // la page n'est pas charger pour la première fois

       url = mydomorigin + '/chapitre/chap/changecomments/' + chapitreId + '/' + dernierCode + '/'
       console.log('initialisation: true url: ' +  url)
  }
  else {
       console.log('dans le else initialisation : false')
  }
  
// let changecomment = this.dataset.changecomments;

  $.ajax({  // ajax permet d'envoyer des requêtes CRUD au serveur
    url: url, // interroge l'url 
    type: "GET", // 
    dataType: "json", // type clé valeurs exemple nom:Boudjidj ; prénom:Bilal de format à envoyer
    success: (reponse) => { // si il envoie une réponse positive alors effectue la suite, le data contient toutes les données que me répons le serveur
    changement = reponse.changement // parmis les données récupère seulement codedb qui contient soit true ou false
    if (changement === true){ // si il y a des changements efectue la suite
       
          
       let codeRecuperer = reponse.derniercode ;  // récupère le dernier code et mets le dans la variable codeRecup
       // recuprer le code puis changer url
       url = mydomorigin + '/chapitre/chap/changecomments/' + chapitreId +   '/'  +  codeRecuperer + '/' 
       // changement == false; // il n'y a pas de changements 
    
       comments = document.querySelectorAll('.classcomments'); //récupère toutes les balises contenants la classcomments
   
       comments.forEach(comment => { //fait une boucle
          comment.remove(); //suprime les commentaire un par un
          // comment.getAttribute();
       });


       commentsDeserialize = JSON.parse( reponse.comments) //récupère tout les commentaires et deserialise les
       usersDeserialize = JSON.parse( reponse.users) //récupère tout les users et deserialise les
       var today = new Date();
       console.log(today.toString());
       console.log('il y a des changements ' + reponse);
       console.log('changement vrai: code: ' + codeRecuperer + 'initilisation: false' + ' url: ' + url , commentsDeserialize)  //  affiche le code recuperer 
       console.log('utilisateurDeserialize: '+usersDeserialize)
       commentsDeserialize.forEach(
        comment =>{ 
            let contenaircommentairs = document.querySelector('#contenaircommentairs');
            var newDivComment = document.createElement("div");
            let userid = comment.fields.user
             let usernamecomment = ""
            usersDeserialize.forEach( user => {
                    if (user.pk === userid){
                      usernamecomment = user.fields.username
                    }
            })
            
            var newuser = document.createElement("h3");
            newuser.innerHTML = usernamecomment
            var newbuttondelete = document.createElement("button");
            newbuttondelete.innerHTML = "delete comment"
            var newdate = document.createElement("h5");
            newdate.innerHTML = comment.fields.date
            var newcomment = document.createElement("span");
            newcomment.innerHTML = comment.fields.comment
            newDivComment.appendChild(newuser);
            newDivComment.appendChild(newdate);
            newDivComment.appendChild(newcomment);
            contenaircommentairs.appendChild(newDivComment);
            // recupere balise contenaircommentairs  == 
            // tu  luis ajoute les commenaitres grace  à innerhtml
            // attention il y a plusieurs commentaires
            console.log(comment)
            console.log(comment.fields.comment + ' ' + comment.fields.chapitre)

            newbuttondelete.addonclick = FunctionDeleteComment;
            
            let userconnected = reponse.userconnected;
            if (userconnected === usernamecomment){
                newDivComment.appendChild(newbuttondelete);
            }
        }
       );
   

    }
    else {
      console.log("il n'y a pas de changements")
      //initialisation == true;
    }
  }
  });
}




setInterval(FunctionChangeComments ,15000); // actualise toutes les 5 secondes la page