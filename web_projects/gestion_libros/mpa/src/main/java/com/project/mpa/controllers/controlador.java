package com.project.mpa.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping()
public class controlador {

    /* @Autowired
    private UsuarioService usuarioService; */

    @GetMapping("/")
    public String redirigir(){
        return "redirect:/ingresar";
    }
    
    @GetMapping("/ingresar")
    public String ingreso(){
        return "ingresar";
    }

    @GetMapping("/registro")
    public String registro(){
        return "registro";
    }


}
