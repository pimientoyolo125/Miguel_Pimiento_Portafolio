package com.project.mpa.services;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.project.mpa.dao.LibroDao;
import com.project.mpa.entitys.Libro;
import com.project.mpa.entitys.Usuario;

@Service
public class LibroService {
    
    
    private LibroDao libroDao;

    @Autowired
    public LibroService (LibroDao libroDao) {
        this.libroDao = libroDao;
    }

    public Libro addLibro(String titulo, String autor, Long cantidad, Double precio, Usuario usuario){
        Libro newLibro = new Libro();
        newLibro.setAutor(autor);
        newLibro.setCantidad(cantidad);
        newLibro.setPrecio(precio);
        newLibro.setTitulo(titulo);
        newLibro.setUsuario(usuario);

        libroDao.save(newLibro);
        return newLibro;
    }

    public Libro actualizaLibro(Long id, String titulo, String autor, Long cantidad, Double precio, Usuario usuario){
        Libro newLibro = new Libro();
        newLibro.setId(id);
        newLibro.setAutor(autor);
        newLibro.setCantidad(cantidad);
        newLibro.setPrecio(precio);
        newLibro.setTitulo(titulo);
        newLibro.setUsuario(usuario);

        libroDao.save(newLibro);
        return newLibro;
    }

    @Transactional
    public void deleteLibro(Libro libro){
        libroDao.eliminarLibroPorId(libro.getId());
    }
    
    public Libro obtenerLibroId(Long id){
        Optional<Libro> libroOp = libroDao.findById(id);
        Libro libro = libroOp.get();
        return libro;
    }

}
