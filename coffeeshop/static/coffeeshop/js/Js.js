function validacion(){
  var a=document.getElementById('tb1').value;
  var b=document.getElementById('tb2').value;
  if (a=='admin' && b=='123') {

    parent.location="Prb.html";
    return false;
  } 
  else{
    alert("Usuario y/o Contraseña incorrecta");
    return false;
  }
}


function validacion2(){
  var a=document.getElementById('tb1').value;
  var b=document.getElementById('tb2').value;
  if (a=='travel' && b=='engine') {

    parent.location="Pr2b.html";
    return false;
  } 
  else{
    alert("Usuario y/o Contraseña incorrecta");
    return false;
  }
}


function loginA() {

        document.getElementById("Log1").innerHTML = "";
        document.getElementById("Log2").innerHTML = "";
        document.getElementById("body").style='overflow-y: visible';
        document.getElementById("f2").style = "z-index: 1;";
        document.getElementById("f4").style = "z-index: 1;";
  
}


function textbox1a(){

  document.getElementById('tb1').style= '';

}


function textbox2a(){

  document.getElementById('tb2').style= '';

}



function textbox1(){
     
        var gt1=for1.tbt1.value; 

        if (gt1=="admin" || gt1=="123") 
        {
          document.getElementById('tb1').style= 'background: linear-gradient(to right, rgba(25,25,25,1) 90%, green 10%);';
        }
        else
        {
          if (gt1=="") {
          document.getElementById('tb1').style= 'background: linear-gradient(to right, rgba(25,25,25,1) 90%, rgb(0, 95, 129) 10%);';
          }
          else
          {
          document.getElementById('tb1').style= 'background: linear-gradient(to right, rgba(25,25,25,1) 90%, red 10%);';  
          } 
        }

      } 

      function textbox2(){
     
        var gt2=for1.tbt2.value; 

        if (gt2=="admin" || gt2=="123") 
        {
          document.getElementById('tb2').style= 'background: linear-gradient(to right, rgba(25,25,25,1) 90%, green 10%);';
        }
        else
        {
          if (gt2=="") {
          document.getElementById('tb2').style= 'background: linear-gradient(to right, rgba(25,25,25,1) 90%, rgb(0, 95, 129) 10%);';
          }
          else
          {
          document.getElementById('tb2').style= 'background: linear-gradient(to right, rgba(25,25,25,1) 90%, red 10%);';  
          } 
        }

        
      }

    
window.onscroll = function() {myFunction()};

function myFunction() {
    
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        document.getElementById("f2").className = "change";
    } else {
        document.getElementById("f2").className = "";
    }

}

function busqueda () {

            var search = document.getElementById("tb"),
  op = document.getElementsByTagName("span"),
  forEach = Array.prototype.forEach;


search.addEventListener("keyup", function(e) {
  var choice = this.value;

  forEach.call(op, function(f) {
    if (f.innerHTML.toLowerCase().search(choice.toLowerCase()) == -1)
      f.parentNode.style.display = "none";
    else
      f.parentNode.style.display = "block";
  });
}, false);

        }
