import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Review } from 'src/app/Modelo/Review';
import { ReviewsService } from 'src/app/services/reviews.service';
import {Location} from '@angular/common'
import { MoviesService } from 'src/app/services/movies.service';

@Component({
  selector: 'app-listar',
  templateUrl: './listar.component.html',
  styleUrls: ['./listar.component.css']
})
export class ListarComponent implements OnInit{

  resenas!: Review[];
  movieId!: string;
  movie!: any;

 
  constructor(
    private service:ReviewsService, 
    private route:ActivatedRoute,
    private router:Router,
    private location:Location,
    private movieService: MoviesService){}

  ngOnInit(){
    this.route.params.subscribe(params => {
      this.movieId = params['movieId'];
    });

        this.service.getReviews(this.movieId).subscribe(data => {
        this.resenas = data;
      })

      {
        this.route.params.subscribe((params:any) => {
          this.movieService.buscarPeliculaPorId(params.movieId).subscribe(response => {
            this.movie = response;
          })
        })
      } 
    }

    Regresar():void{
      this.location.back();
    }

    Nuevo(movieId:String){
      this.router.navigate(["add", movieId]);
    }

    Editar(resena:Review):void{
    localStorage.setItem("id",resena.id.toString());
    this.router.navigate(["edit"]);
    }

    Eliminar(id: number){
      if (confirm('¿Estás seguro de eliminar este elemento?\nID=' + id.toString())) {
        this.service.Eliminar(id);
      }
    }
  
}
