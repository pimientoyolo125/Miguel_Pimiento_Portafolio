## Proyecto de gestion de libros por usuario (con Spring Boot + PostgresSQL). 

Esta pagina web es un gestos simple de libros, posee con un formulario
para que en caso de tener una cuenta existente el usuario pueda ingresar,
con validacion de campo y varias alertas para saber que sucede al momento 
de intento de sesion.

Por otro lado, si el usuario nu cuenta con una contraseña este puede ir a
otra pagina para que este pueda crear su usuario. Posee varios validadores para 
saber si el usuario esta existente o se estan ingresando valores no validos, una vez
validado el sistema le indica al usuario si fue o no exitoso el registro.

Una vez ingresado a la pagina principal del sistema, el usuario puede hacer la
gestion de sus libros, se muestra una tabla con informacion de cada libro, el cual
puede tanto eliminar como editar cada uno. De ser nesesario existe la opcion para que
se ingrese un libro nuevo

Este proyecto esta realizado con el framework Spring Boot, el cual se conecta con una 
base de datos en la nube de PosgresSQl, usando el servicion de ElephanSQL
