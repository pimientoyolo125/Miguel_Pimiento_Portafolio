import { Component, OnInit } from '@angular/core';
import { MoviesService } from 'src/app/services/movies.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-movies-list',
  templateUrl: './movies-list.component.html',
  styleUrls: ['./movies-list.component.css']
})
export class MoviesListComponent implements OnInit {

  movies!: any[];
  constructor(
    private moviesService: MoviesService,
    private activatedRoute: ActivatedRoute) { }  

  ngOnInit(): void { 
    this.activatedRoute.queryParams.subscribe((params: any) => {
      this.moviesService.buscarPeliculas(params.q).subscribe(response => {
        this.movies = response;
      });
    });
   
  }
}

