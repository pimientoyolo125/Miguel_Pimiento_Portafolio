let tabla;

window.addEventListener("load",function(){
    cargarTabla();
});

function cargarTabla(){

    const objeto_ajax = new XMLHttpRequest();

    objeto_ajax.open("GET", "https://jsonplaceholder.typicode.com/users", true);

    objeto_ajax.send();

    objeto_ajax.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            
            llenarTabla(JSON.parse(this.responseText));
            /* tabla = $("#tabla_usuarios").DataTable(); */
            tabla = new DataTable('#tabla_usuarios', {
                language: {
                    url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json',
                },
            });
        }
    }
}

function llenarTabla(jason_datos){
    let datos_tabla = document.getElementById("datos_tabla")

    datos_tabla.innerHTML = '';

    for(let dato of jason_datos){
        datos_tabla.innerHTML += `
            <tr>
                <td>${dato.id}</td>
                <td>${dato.name}</td>
                <td>${dato.username}</td>
                <td>${dato.email}</td>
                <td>${dato.phone}</td>
            </tr>`;
    }
}


/* const initDataTable = async() => {
    if (tabla_iniciada) {
        tabla.destroy();
    }

    await listUsers();

    tabla = $("#tabla_usuarios").DataTable();

    tabla_iniciada = true;
};

const listUsers = async() => {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/users");
        const users = await response.json();

        let content = ``;
        users.forEach((user, index) => {
            content += `
                <tr>
                    <th>${index + 1}</th>
                    <th>${user.name}</th>
                    <th>${user.email}</th>
                    <th>${user.address.city}</th>
                    <th>${user.company.name}</th>
                </tr>`;
        });
        datos_tabla.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async() => {
    await initDataTable();
}); */