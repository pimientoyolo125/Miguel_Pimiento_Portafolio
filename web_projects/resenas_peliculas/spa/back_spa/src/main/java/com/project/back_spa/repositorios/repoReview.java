package com.project.back_spa.repositorios;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.project.back_spa.modelos.Review;

@Repository
public interface repoReview extends JpaRepository<Review, Long>{

    @Query("SELECT r FROM Review r WHERE r.pelicula = :pelicula")
    List<Review> findByPelicula(@Param("pelicula") String pelicula);
}
