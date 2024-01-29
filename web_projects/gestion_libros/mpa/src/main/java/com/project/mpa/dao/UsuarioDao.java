package com.project.mpa.dao;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.project.mpa.entitys.Usuario;

@Repository
public interface UsuarioDao extends JpaRepository<Usuario, Long>{

    @Query("SELECT u FROM Usuario u WHERE u.correo = :correo AND u.contrasena = :contrasena")
    Usuario logueo(@Param("correo") String correo, @Param("contrasena") String contrasena);

    @Query("SELECT u FROM Usuario u WHERE u.correo = :correo OR u.nombreUsuario = :nombreUsuario")
    List<Usuario> registro(@Param("correo") String correo, @Param("nombreUsuario") String nombreUsuario);
}
