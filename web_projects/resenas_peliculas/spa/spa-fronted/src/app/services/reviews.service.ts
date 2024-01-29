import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Review } from '../Modelo/Review';

@Injectable({
  providedIn: 'root'
})
export class ReviewsService {

  constructor(private http:HttpClient) { }

  Url='http://localhost:8080/review/pelicula/';
  Url2='http://localhost:8080/review';

  getReviews(movieId: String){
    return this.http.get<Review[]>(this.Url + movieId);
  }
  
  createReview(review:Review){
    return this.http.post<Review>(this.Url2, review);
  }

  getResenaId(id:number){
    return this.http.get<Review>(this.Url2+ "/" + id);
  }

  updateResena(review:Review){
    return this.http.put<Review>(this.Url2,review)
  }

  Eliminar(id: number){
    this.http.delete(this.Url2 + "/" + id).subscribe(() => {
      location.reload();
    });
  }
}
