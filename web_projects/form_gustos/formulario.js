var editando = false;

function guardar_gusto(){
    var body_tabla = document.getElementById("body_tabla_gustos");
    var gusto = document.getElementById("input_gustos").value;

    document.getElementById("input_gustos").value = "";

    fila = '<tr><td>' + gusto + '</td>' +
    '<td> 0 </td>' + 
    '<td>' + 
    '<a class="editar" onclick="editar(this)">Editar</a>' +
    '</td></tr>';

    body_tabla.innerHTML += fila;
    
}

function editar(casilla){
    if(!editando){
        editando = true;

        document.getElementById("div_botones").style.display = "block";

        var fila = (casilla.parentNode).parentNode;

        var gusto = fila.getElementsByTagName("td")[0].textContent;
        var porcentaje = fila.getElementsByTagName("td")[1].textContent;

        colocar_inputs = '<td> <input class="input" type="text" id="edit_gusto" value="' + gusto + '"></td>' +
        '<td>  <input class="input" type="text" id="edit_porcentaje" value="' + porcentaje + '"></td>' + 
        '<td>' + 
        'En edicion' +
        '</td>';

        fila.innerHTML = colocar_inputs;
        
    }else{
        alert("Solo se puede editar una línea. Recargue la página para poder editar otra");
    }
}

function aceptar() {
    var nombre = document.getElementById("nombre").value;
    var email = document.getElementById("email").value;
    var telefono = document.getElementById("telefono").value;
    var gusto = document.getElementById("edit_gusto").value;
    var porcentaje = document.getElementById("edit_porcentaje").value;
  
    var url = 'resultado.html?' +
                'nombre=' + encodeURIComponent(nombre) +
                '&email=' + encodeURIComponent(email) +
                '&telefono=' + encodeURIComponent(telefono) + 
                '&gusto=' + encodeURIComponent(gusto) + 
                '&porc=' + encodeURIComponent(porcentaje);
    
    window.location.href = url;
  }