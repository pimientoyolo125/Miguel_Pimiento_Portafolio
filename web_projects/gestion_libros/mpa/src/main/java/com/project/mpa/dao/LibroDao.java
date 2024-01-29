package com.project.mpa.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.project.mpa.entitys.Libro;

@Repository
public interface LibroDao extends JpaRepository<Libro, Long>{
    

    @Modifying
    @Query("DELETE FROM Libro l WHERE l.id = :id")
    void eliminarLibroPorId(@Param("id") Long id);
}
