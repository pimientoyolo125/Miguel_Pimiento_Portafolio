
console.log("se cargoo el json");

function eliminarLibro(id) {
    console.log(id)
    if (confirm('¿Estás seguro de eliminar este libro?')) {
        fetch(`/eliminarLibro/${id}`, {
            method: 'DELETE',
        })
        .then(response => {
            if (response.ok) {
                alert("Libro eliminado con exito")
                // Hacer algo si la eliminación fue exitosa
                // Por ejemplo, recargar la página o actualizar la tabla
                window.location.reload();
            } else {
                // Manejar el caso si hubo un error al eliminar
                console.error('Error al eliminar el libro');
            }
        })
        .catch(error => {
            console.error('Error en la solicitud:', error);
        });
    }
}

function editarLibro(id) {
    console.log(id)
        fetch(`/editarLibro/${id}`, {
            method: 'GET',
        })
        
}
