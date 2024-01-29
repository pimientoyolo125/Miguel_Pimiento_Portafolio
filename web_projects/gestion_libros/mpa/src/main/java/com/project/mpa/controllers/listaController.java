package com.project.mpa.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.project.mpa.entitys.Libro;
import com.project.mpa.entitys.Usuario;
import com.project.mpa.services.UsuarioService;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;

@Controller
public class listaController{
    
    private UsuarioService usuarioService;

    @Autowired
    public listaController(UsuarioService usuarioService) {
        this.usuarioService = usuarioService;
    }

    private Usuario usuario;

    @GetMapping("/listaLibros")
    public String listaLibros(Model model, HttpServletRequest request) {

        HttpSession session = request.getSession();
        usuario = (Usuario) session.getAttribute("usuario");

        usuario = usuarioService.usuarioPorId(usuario.getId());

        List<Libro> libros = usuario.getLibros();

        model.addAttribute("libros", libros);

        return "listaLibros"; 
    }

    @GetMapping("/addyLibros")
    public String anadirLibros(Model model, HttpServletRequest request) {

        HttpSession session2 = request.getSession();
        session2.setAttribute("usuario", usuario);

        return "redirect:/addLibros";

    }

    

}
