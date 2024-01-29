package com.project.mpa.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.project.mpa.entitys.Usuario;
import com.project.mpa.services.UsuarioService;

@Controller
public class registerController {
    private UsuarioService usuarioService;

    @Autowired
    public registerController(UsuarioService usuarioService) {
        this.usuarioService = usuarioService;
    }

    @PostMapping("/registro")
    public String Login(@RequestParam("nombre") String nombre, @RequestParam("apellido") String apellido,
            @RequestParam("correo") String correo, @RequestParam("telefono") String telefono, 
            @RequestParam("nombreUsuario") String nombreUsuario, @RequestParam("contrasena") String contrasena,
            @RequestParam("confirmarContrasena") String confirmarContrasena, Model model) {

        List<Usuario> usuarios = usuarioService.registro(correo, nombreUsuario);
         
        if (usuarios.isEmpty()) {
            usuarioService.addUsuario(nombre, apellido, correo, telefono, nombreUsuario, contrasena);
            model.addAttribute("condicion", true);
            return "registro";
        } else {
            model.addAttribute("condicion", false);
            return "registro";
        }
        
    }
}
