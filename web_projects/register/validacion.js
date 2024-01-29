const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    nombres: /^[a-zA-Z\s]{2,25}$/, // Letras y espacios, pueden llevar acentos.
    apellidos: /^[a-zA-ZÀ-ÿ\s]{2,25}$/, // Letras y espacios, pueden llevar acentos.
    direccion: /^(cll|cra|av|anv|trans)[a-zA-Z0-9\s\_\-]{1,16}$/,
    usuario: /^[a-zA-Z0-9\-\_]{10,20}$/, // Letras, numeros, guion y guion_bajo
    password: /^.{15,20}$/, // 
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    celular: /^[0-9]{10,10}$/,
}

const campos = {
    nombres: false,
    apellidos: false,
    direccion: false,
    usuario: false,
    password: false,
    correo: false,
    celular: false,
    confirmarps: false,
}


const validarformulario = (e) => {
    switch (e.target.name) {
        case "nombres":
            validar(expresiones.nombres, e.target, 'nombres');
            break;
        case "apellidos":
            validar(expresiones.apellidos, e.target, 'apellidos');
            break;
        case "direccion":
            validar(expresiones.direccion, e.target, 'direccion');
            break;
        case "usuario":
            validar(expresiones.usuario, e.target, 'usuario');
            break;
        case "correo":
            validar(expresiones.correo, e.target, 'correo');
            break;
        case "celular":
            validar(expresiones.celular, e.target, 'celular');
            break;
        case "contraseñas":
            validar(expresiones.password, e.target, 'contraseñas');
            validarPassword();
            break;
        case "confirmarps":
            validarPassword();
            break;
    }
}

const validar = (exp, input, id) => {
    if (exp.test(input.value)) {
        document.getElementById(`${id}Correcto`).classList.remove('porDefecto');
        document.getElementById(`${id}Error`).classList.remove('activarMensaje');
        document.getElementById(`${id}Error`).classList.add('porDefecto');
        document.getElementById(`${id}Correcto`).classList.add('activarMensajeCorrecto');
        campos[id] = true;
    } else {
        document.getElementById(`${id}Error`).classList.remove('porDefecto');
        document.getElementById(`${id}Correcto`).classList.remove('activarMensajeCorrecto');
        document.getElementById(`${id}Correcto`).classList.add('porDefecto');
        document.getElementById(`${id}Error`).classList.add('activarMensaje');
        campos[id] = false;
    }
}

const validarPassword = () => {
    const inputPassword = document.getElementById('contraseñas')
    const inputPassword2 = document.getElementById('confirmarps')
    if (inputPassword.value !== inputPassword2.value || inputPassword2.value == '') {
        document.getElementById('confirmarpsError').classList.add('activarMensaje');
        document.getElementById('confirmarpsError').classList.remove('porDefecto');
        document.getElementById('confirmarpsCorrecto').classList.add('porDefecto');
        document.getElementById('confirmarpsCorrecto').classList.remove('activarMensajeCorrecto');
        campos['contraseñas'] = false;
    } else {
        document.getElementById('confirmarpsError').classList.remove('activarMensaje');
        document.getElementById('confirmarpsError').classList.add('porDefecto');
        document.getElementById('confirmarpsCorrecto').classList.remove('porDefecto');
        document.getElementById('confirmarpsCorrecto').classList.add('activarMensajeCorrecto');
        campos['contraseñas'] = true;
    }

}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarformulario);
    input.addEventListener('blur', validarformulario);
})