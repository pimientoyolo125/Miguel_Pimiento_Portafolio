var nombre = document.getElementById("nombre");
var apellido = document.getElementById("apellido");
var correo = document.getElementById("correo");
var contrasena = document.getElementById("contrasena");
var cf_contrasena = document.getElementById("cf_contrasena");
var registrar = document.getElementById("registrar");
var fecha = document.getElementById("input_date");

validacion = {
    nombre: /^[a-zA-Z\s]{1,25}$/,
    apellido: /^[a-zA-Z\s]{1,25}$/,
    contrasena: /^.{15,20}$/, // 
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
}

function ocultar(elementos) {
    for (i = 0; i < elementos.length; i++) {
        elementos[i].style.display = "none";
    }
}

registrar.addEventListener("click", function() {
    let alertas = document.querySelectorAll(".alerta");
    ocultar(alertas);

    var bandera = true;

    if (!validacion.nombre.test(nombre.value)) {
        if (nombre.value.length > 25) {
            alertas[0].style.display = "block";
        } else {
            alertas[1].style.display = "block";
        }
        bandera = false;
    }

    if (!validacion.apellido.test(apellido.value)) {
        if (apellido.value.length > 25) {
            alertas[2].style.display = "block";
        } else {
            alertas[3].style.display = "block";
        }
        bandera = false;
    }

    if(input_date.value == ""){
        alertas[4].style.display = "block";
        document.getElementById("age").style.display = "none";
        bandera = false;
    }else if((new Date(input_date.value)) > new Date()){
        alertas[5].style.display = "block";
        document.getElementById("age").style.display = "none";
        bandera = false;
    }

    if (!validacion.correo.test(correo.value)) {
        alertas[6].style.display = "block";
        bandera = false;
    }

    if (!validacion.contrasena.test(contrasena.value)) {
        alertas[7].style.display = "block";
        bandera = false;
    } else if (contrasena.value != cf_contrasena.value) {
        alertas[8].style.display = "block";
        alertas[9].style.display = "block";
        bandera = false;
    }

    if (checkbox_enfermedades.checked) {

        if (entrada_enfermedades.value == "Elegir") {
            alertas[9].style.display = "block"
            bandera = false;
        }
    }

    if (bandera) {
        alert("Formulario Enviado")
    }
})