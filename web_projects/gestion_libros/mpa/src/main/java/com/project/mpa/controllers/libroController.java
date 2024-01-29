package com.project.mpa.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.project.mpa.entitys.Libro;
import com.project.mpa.services.LibroService;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;



@Controller
public class libroController {
    private LibroService libroService;

    @Autowired
    public libroController(LibroService libroService){
        this.libroService = libroService;
    }

    @DeleteMapping("/eliminarLibro/{id}")
    public ResponseEntity<Void> eliminarLibro(@PathVariable Long id){
        Libro libro = libroService.obtenerLibroId(id);
        libroService.deleteLibro(libro);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/editarLibro/{id}")
    public String actualizarLibro(@PathVariable Long id, Model model, HttpServletRequest request){
        Libro libro = libroService.obtenerLibroId(id);

        HttpSession session = request.getSession();
        session.setAttribute("usuario", libro.getUsuario());

        model.addAttribute("libro", libro);
        return "actualizarLibro";
    }
}
