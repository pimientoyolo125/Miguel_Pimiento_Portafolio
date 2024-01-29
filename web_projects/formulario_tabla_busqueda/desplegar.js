var desplegar = document.getElementById("despliegue_enfermedades");
var checkbox_enfermedades = document.getElementById("enfermedades");

var bandera = false;

checkbox_enfermedades.addEventListener("click", function() {
    if(this.checked){
        desplegar.style.display = "block";
    }else {
        desplegar.style.display = "none";
    }
})