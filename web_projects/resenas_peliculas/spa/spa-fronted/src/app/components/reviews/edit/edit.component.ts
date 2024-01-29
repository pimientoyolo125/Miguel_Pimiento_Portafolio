import { Component, OnInit } from '@angular/core';
import {Location} from '@angular/common'
import { Router } from '@angular/router';
import { ReviewsService } from 'src/app/services/reviews.service';
import { Review } from 'src/app/Modelo/Review';

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.css']
})
export class EditComponent implements OnInit{

    review: Review=new Review();
    constructor(
    private location:Location,
    private service:ReviewsService){}

  ngOnInit(){
   this.Editar();
  }

  Editar() {
    let id = localStorage.getItem("id");
    if (id !== null) {
        this.service.getResenaId(+id) // Convierte la cadena a número usando el operador unario '+'
            .subscribe(data => {
              console.log(data);
                this.review = data;
            });
    } else {
        console.error('El ID almacenado en localStorage es nulo.');
    }
  }

  Actualizar(){
    this.service.updateResena(this.review)
    .subscribe(data=>{
      this.review=data;
      alert("Se actualizo con Exito...!!!");
      this.location.back();
    })
  }

  Regresar(){
    this.location.back();
  }
}
