package com.project.mpa.controllers;


import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import com.project.mpa.entitys.Usuario;
import com.project.mpa.services.UsuarioService;

@Controller
public class usuarioController {

    private final UsuarioService usuarioService;

    @Autowired
    public usuarioController(UsuarioService usuarioService) {
        this.usuarioService = usuarioService;
    }

    @GetMapping("/usuarios")
    public String mostrarUsuarios(Model model) {

        Iterable<Usuario> Iusuarios = usuarioService.getAllUsuarios();

        List<Usuario> usuarios = new ArrayList<>();
        Iusuarios.forEach(usuarios::add);

        model.addAttribute("usuarios", usuarios);
        return "usuarios"; 
    }

}