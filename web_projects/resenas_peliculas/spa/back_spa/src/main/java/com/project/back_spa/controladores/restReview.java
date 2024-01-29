package com.project.back_spa.controladores;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.project.back_spa.modelos.Review;
import com.project.back_spa.servicios.serviceReview;

@CrossOrigin(origins ="http://localhost:4200", maxAge = 3600)

@RestController
@RequestMapping("/review")
public class restReview {
    
    @Autowired
    private serviceReview servicioReview;

    @GetMapping("/pelicula/{id}")
    public ResponseEntity<List<Review>> findByPelicula(@PathVariable("id") String pelicula){
        return ResponseEntity.ok(servicioReview.findAllbyPelicula(pelicula));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Review> getReviewById(@PathVariable("id") Long id){
        return ResponseEntity.ok(servicioReview.findById(id));
    }

    @DeleteMapping("/{id}")
    public void deleteReviewById(@PathVariable("id") Long id){
        servicioReview.deleteById(id);
    }

    @PostMapping
    public ResponseEntity<Review> createReview(@RequestBody Review review){
        return ResponseEntity.ok(servicioReview.create(review));
    }

    @PutMapping
    public ResponseEntity<Review> updateReview(@RequestBody Review review){
        return ResponseEntity.ok(servicioReview.update(review));
    }
}
