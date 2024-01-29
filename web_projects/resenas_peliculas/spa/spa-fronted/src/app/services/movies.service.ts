import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MoviesService {

  private urlBase = 'https://movies-app1.p.rapidapi.com/api';
  private headers = {
    'X-RapidAPI-Key': '6f2ba8dafbmsh61710dd0798d23ep18276ejsnb047db196768',
    'X-RapidAPI-Host': 'movies-app1.p.rapidapi.com'
  }
  constructor(private http: HttpClient) { }

  buscarPeliculas(titulo: string): Observable<any> {
    
    return this.http.get(this.urlBase + '/movies',
    {headers: this.headers, params: {query: titulo}})
    .pipe(map((resp: any) => resp.results))
  }

  buscarPeliculaPorId(movieId: string): Observable<any>{
    return this.http.get(this.urlBase + '/movie' + '/' + movieId,
    {
      headers: this.headers
    })
    .pipe(map((resp: any) => resp.result))
  }

  
}
