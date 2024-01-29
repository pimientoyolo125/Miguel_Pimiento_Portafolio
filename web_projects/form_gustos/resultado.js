const url = new URL(window.location.href);
var nombre = url.searchParams.get('nombre');
var email = url.searchParams.get("email");
var telefono = url.searchParams.get("telefono");
var gusto = url.searchParams.get("gusto");
var porcentaje = url.searchParams.get("porc");

document.getElementById("th_content").innerHTML += " " + nombre + "<br>Ficha";
document.getElementById("email").innerHTML = email;
document.getElementById("telefono").innerHTML = telefono;
document.getElementById("gusto").innerHTML = gusto;
document.getElementById("porcentaje").innerHTML = porcentaje;
