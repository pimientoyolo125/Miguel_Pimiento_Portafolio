var input_date = document.getElementById("input_date");
var p_edad = document.getElementById("age");

input_date.addEventListener("change", function() {

    var cumple = new Date(this.value);

    var hoy = new Date();

    p_edad.style.display = "block";

    if(cumple > hoy){
        p_edad.textContent = "No es posible calcular la edad";
    }else{

        var edad = hoy.getFullYear() - cumple.getFullYear();

        if (hoy.getMonth() < cumple.getMonth() || (hoy.getMonth() == cumple.getMonth() && hoy.getDate() < cumple.getDate())) {
            edad--;
        }

        p_edad.textContent = "La edad es: " + edad;
    }
});