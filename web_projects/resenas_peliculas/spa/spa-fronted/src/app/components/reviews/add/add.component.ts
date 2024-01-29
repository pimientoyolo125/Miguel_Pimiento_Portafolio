import { Component, OnInit } from '@angular/core';
import {Location} from '@angular/common'
import { ReviewsService } from 'src/app/services/reviews.service';
import { Review } from 'src/app/Modelo/Review';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent implements OnInit{
  
  movieId!: string;
  review:Review = new Review();
  constructor(
    private location:Location,
    private route:ActivatedRoute,
    private router:Router,
    private service:ReviewsService) { }
    
  ngOnInit(){
    this.route.params.subscribe(params => {
      this.movieId = params['movieId'];
    });
  }

  Guardar(){
    this.review.pelicula = this.movieId;
    this.service.createReview(this.review).subscribe({
      next: data =>{
      console.log(data);
      alert("Se agrego con Éxito...!!!")
      this.location.back();
      }
    });
  }

  guardarSubmit(){
    this.Guardar();
  }

  Regresar(){
    this.location.back();
  }
}
