var nombre = document.getElementById("nombre");
var apellido = document.getElementById("apellido");
var correo = document.getElementById("correo");
var contrasena = document.getElementById("contrasena");
var cf_contrasena = document.getElementById("confirmarContrasena");
var registrar = document.getElementById("registrar");
var usuario = document.getElementById("nombreUsuario");
var telefono = document.getElementById("telefono");


validacion = {
    nombre: /^[a-zA-Z\s]{1,50}$/,
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,50}$/,
    usuario: /^[a-zA-Z0-9\-\_]{8,50}$/,
    contrasena: /^.{8,100}$/,
    correo: /^[a-zA-Z0-9_.+-]{1,100}@[a-zA-Z0-9-]{1,100}\.[a-zA-Z0-9-.]{1,100}$/,/* /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/, */
    telefono: /^[0-9]{10,10}$/,
}

function ocultar(elementos) {
    for (i = 0; i < elementos.length; i++) {
        elementos[i].style.display = "none";
    }
}

registrar.addEventListener("click", function() {
    let alertas = document.querySelectorAll(".control .porDefecto");
    ocultar(alertas);

    var bandera = true;

    if (!validacion.nombre.test(nombre.value)) {
        if (nombre.value.length > 50) {
            alertas[0].style.display = "block";
        } else {
            alertas[1].style.display = "block";
        }
        bandera = false;
    }

    if (!validacion.apellido.test(apellido.value)) {
        if (apellido.value.length > 50) {
            alertas[2].style.display = "block";
        } else {
            alertas[3].style.display = "block";
        }
        bandera = false;
    }

    if (!validacion.correo.test(correo.value)) {
        alertas[4].style.display = "block";
        bandera = false;
    }

    if (!validacion.telefono.test(telefono.value)) {
        if (telefono.value.length > 10 || telefono.value.length == 0) {
            alertas[5].style.display = "block";
        }
        bandera = false;
    }
    if (!validacion.usuario.test(usuario.value)) {
        if (usuario.value.length > 50) {
            alertas[6].style.display = "block";
        } else {
            alertas[7].style.display = "block";
        }
        bandera = false;
    }

    if (!validacion.contrasena.test(contrasena.value)) {
        alertas[8].style.display = "block";
        bandera = false;
    } else if (contrasena.value != cf_contrasena.value) {
        alertas[9].style.display = "block";
        alertas[10].style.display = "block";
        bandera = false;
    }

    if (bandera) {
        document.getElementById("formulario_reg").submit();
    }
})