package com.project.back_spa.servicios;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.project.back_spa.modelos.Review;
import com.project.back_spa.repositorios.repoReview;

@Service
public class serviceReview{
    
    @Autowired
    private repoReview repo;

    public List<Review> findAllbyPelicula(String pelicula){
        return repo.findByPelicula(pelicula);
    }

    public Review findById(Long id){
        Optional<Review> opReview = repo.findById(id);
        return opReview.get();
    }

    public void deleteById(Long id){
        repo.deleteById(id);
    }

    public Review create(Review review){
        return repo.save(review);
    }

    public Review update(Review review){
        return repo.save(review);
    }
}
