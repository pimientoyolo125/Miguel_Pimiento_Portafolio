var titulo = document.getElementById("Nombre_libro");
var autor = document.getElementById("autor_libro");
var cantidad = document.getElementById("cantidad");
var precio = document.getElementById("precio_libro");
var anadir = document.getElementById("btnAddBook");



validacion = {
    titulo: /^.{1,100}$/,
    autor: /^.{1,50}$/,
    cantidad: /^[0-9]{1,6}$/,
    precio: /^\d+(\.\d{1,2})?$/,
}

function ocultar(elementos) {
    for (i = 0; i < elementos.length; i++) {
        elementos[i].style.display = "none";
    }
}

anadir.addEventListener("click", function() {
    let alertas = document.querySelectorAll(".control .porDefecto");
    ocultar(alertas);

    var bandera = true;

    if (!validacion.titulo.test(titulo.value.trim())) {
        if (titulo.value.trim().length > 100) {
            alertas[0].style.display = "block";
        } else if(titulo.value.trim().length == 0){
            alertas[1].style.display = "block";
        }
        bandera = false;
    }

    if (!validacion.autor.test(autor.value.trim())) {
        if (autor.value.trim().length > 50) {
            alertas[2].style.display = "block";
        } else if(autor.value.trim().length == 0){
            alertas[3].style.display = "block";
        }
        bandera = false;
    }


    if (!validacion.cantidad.test(cantidad.value.trim())) {
        if (cantidad.value.trim().length == 0) {
            alertas[5].style.display = "block";
        }else{
            alertas[4].style.display = "block"
        }
        bandera = false;
    }
    if (!validacion.precio.test(precio.value.trim())) {
        alertas[6].style.display = "block"
        bandera = false;
    }else if(precio.value.trim().length == 0){
        alertas[7].style.display = "block"
        bandera = false;
    }

    if (bandera) {
        document.getElementById("anadir_formulario").submit();
    }
})