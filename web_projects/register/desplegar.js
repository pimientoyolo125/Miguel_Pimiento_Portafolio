var gustos = document.getElementById('gustos');
var formGustos = document.getElementById('formGustos');

document.getElementById("formGustos").style.display = "none";

var bool = false;

gustos.addEventListener('click', function(){
    if(bool !== false){
        gustos.checked = !gustos.checked;
        formGustos.style.display = "none";
        bool = false;
    }else{
        bool = true;
        formGustos.style.display = "block";
    }
  });
