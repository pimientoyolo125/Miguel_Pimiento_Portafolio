package com.project.mpa.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.project.mpa.dao.UsuarioDao;
import com.project.mpa.entitys.Usuario;

@Service
public class UsuarioService {
    @Autowired
    private UsuarioDao usuarioDao;

    public UsuarioService(UsuarioDao usuarioDao) {
        this.usuarioDao = usuarioDao;
    }

    public Usuario usuarioPorId(Long id){
        
        Optional<Usuario> opUsuario = usuarioDao.findById(id);
        return opUsuario.get();
    }

    public Usuario logueo(String correo, String contrasena) {
        Usuario usuario = usuarioDao.logueo(correo, contrasena);
        return usuario;
    }

    public List<Usuario> registro(String correo, String nombreUsuario) {
        List<Usuario> usuarios = usuarioDao.registro(correo, nombreUsuario);
        return usuarios;
    }

    public Iterable<Usuario> getAllUsuarios() {
        return usuarioDao.findAll();
    }

    public Usuario addUsuario(String nombre, String apellido, String correo,
            String telefono, String nombreUsuario, String contrasena) {
        Usuario nuevoUsuario = new Usuario();

        nuevoUsuario.setNombre(nombre);
        nuevoUsuario.setApellido(apellido);
        nuevoUsuario.setTelefono(telefono);
        nuevoUsuario.setCorreo(correo);
        nuevoUsuario.setNombreUsuario(nombreUsuario);
        nuevoUsuario.setContrasena(contrasena);

        return usuarioDao.save(nuevoUsuario);
    }
}
