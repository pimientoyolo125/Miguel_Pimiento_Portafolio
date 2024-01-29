package com.project.mpa.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.project.mpa.entitys.Libro;
import com.project.mpa.entitys.Usuario;
import com.project.mpa.services.LibroService;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;

@Controller
public class anadirController {

    private Usuario usuario;

    private LibroService libroService;

    @Autowired
    public anadirController(LibroService libroService) {
        this.libroService = libroService;
    }

    @GetMapping("/addLibros")
    public String anadirLibros(Model model, HttpServletRequest request) {

        HttpSession session = request.getSession();
        usuario = (Usuario) session.getAttribute("usuario");

        return "anadirLibro"; 
    }
    

    @PostMapping("/adiLibro")
    public String adi(@RequestParam("Nombre_libro") String Nombre_libro, @RequestParam("autor_libro") String autor_libro,
            @RequestParam("cantidad") String cantidad, @RequestParam("precio_libro") String precio_libro,
            Model model) {

        Long longCantidad = Long.parseLong(cantidad);
        Double doublePrecio = Double.parseDouble(precio_libro);

        libroService.addLibro(Nombre_libro, autor_libro, longCantidad, doublePrecio, usuario);
        
        model.addAttribute("condicion", true);
        return "anadirLibro";
        
    }


    @PostMapping("/ediLibro")
    public String edi(@RequestParam("id") String id, @RequestParam("Nombre_libro") String Nombre_libro, @RequestParam("autor_libro") String autor_libro,
            @RequestParam("cantidad") String cantidad, @RequestParam("precio_libro") String precio_libro,
            Model model, HttpServletRequest request) {

        Long longId = Long.parseLong(id);        
        Long longCantidad = Long.parseLong(cantidad);
        Double doublePrecio = Double.parseDouble(precio_libro);

        Libro libro = libroService.obtenerLibroId(longId);

        HttpSession session = request.getSession();
        session.setAttribute("usuario", libro.getUsuario());

        libroService.actualizaLibro(longId,Nombre_libro, autor_libro, longCantidad, doublePrecio, libro.getUsuario());
        
        return "redirect:/redireccionarLista";
        
    }

    @GetMapping("/redireccionarLista")
    public String redirect(Model model, HttpServletRequest request) {

        HttpSession session = request.getSession();

        if(usuario == null){
            usuario = (Usuario) session.getAttribute("usuario");
        }

        session.setAttribute("usuario", usuario);

        return "redirect:/listaLibros";

    }

}
