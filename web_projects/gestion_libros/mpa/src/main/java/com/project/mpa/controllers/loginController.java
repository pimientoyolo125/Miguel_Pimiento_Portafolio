package com.project.mpa.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.project.mpa.entitys.Usuario;
import com.project.mpa.services.UsuarioService;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;


@Controller
public class loginController {

    private UsuarioService usuarioService;

    @Autowired
    public loginController(UsuarioService usuarioService) {
        this.usuarioService = usuarioService;
    }

    @PostMapping("/ingresar")
    public String Login(@RequestParam("correo") String correo, @RequestParam("contrasena") String contrasena,
     Model model, HttpServletRequest request) {
        Usuario usuario = usuarioService.logueo(correo, contrasena);

        if (usuario != null) {

            HttpSession session = request.getSession();
            session.setAttribute("usuario", usuario);

            return "redirect:/listaLibros";
        } else {
            model.addAttribute("condicion", true);
            return "ingresar";
        } 
    }
}
