var nuevaHojaDeEstilo = document.createElement("style");
document.head.appendChild(nuevaHojaDeEstilo);

// los elementos padre donde poner los sliders
var elementoPadre1 = document.querySelector(".inputDiv.i1");
var elementoPadre2 = document.querySelector(".inputDiv.i2");
var inputsRy = [];

function Input(id) {
    //<input type="range" value="35" min="0" max="100" autocomplete="off" step="1">
    this.att = {};
    this.att.type = "range";
    this.att.id = id;
    this.att.value = 0;
    this.att.min = 0;
    this.att.max = 100000;
    this.att.autocomplete = "off";
    this.att.step = "1";
    this.color = {};
    this.color.a = "#fcb045"; // la parte "baja" del slider
    this.color.b = "#833ab4"; // la parte "alta" del slider
    this.input;
    this.output;
    this.interval = this.att.max - this.att.min;

    this.crear = function(elementoPadre) {
        this.input = document.createElement("input");
        this.output = document.createElement("div");
        this.output.innerHTML = this.att.value;
        this.output.setAttribute("class", "output");
        for (var name in this.att) {
            if (this.att.hasOwnProperty(name)) {
                this.input.setAttribute(name, this.att[name]);
            }
        }
        elementoPadre.appendChild(this.input);
        elementoPadre.appendChild(this.output);

        this.CSSstyle()
    }
    this.actualizar = function() {
        this.output.innerHTML = this.input.value;
        this.att.value = this.input.value;
        this.CSSstyle();
    }
    this.CSSstyle = function() {
        // calcula la posición del thumb en porcentajes
        this.porcentaje = ((this.att.value - this.att.min) / this.interval) * 100;
        // establece las nuevas reglas CSS
        this.style = "#" + this.att.id + "::-webkit-slider-runnable-track{ background-image:-webkit-linear-gradient(left, " + this.color.a + " " + this.porcentaje + "%, " + this.color.b + " " + this.porcentaje + "%)}\n";
        this.style += "#" + this.att.id + "::-moz-range-track{ background-image:-moz-linear-gradient(left, " + this.color.a + " " + this.porcentaje + "%, " + this.color.b + " " + this.porcentaje + "%)}\n";
    }
}

function actualizarCSS() {
    // una cadena de texto donde guardar los estilos
    var HojaCSS = "";
    for (var i = 0; i < inputsRy.length; i++) {
        HojaCSS += inputsRy[i].style;
    }

    nuevaHojaDeEstilo.textContent = HojaCSS;
}

// setup
var i = new Input("itr1");
i.crear(elementoPadre1);
inputsRy.push(i);

var i2 = new Input("itr2");
i2.att.value = 0;
i2.att.min = 0;
i2.att.max = 100000;
i2.crear(elementoPadre2);
inputsRy.push(i2);

actualizarCSS();

for (var n = 0; n < inputsRy.length; n++) {

    (function(n) {
        inputsRy[n].input.addEventListener("input", function() {
            inputsRy[n].actualizar();
            actualizarCSS();
        }, false)
    }(n));
}