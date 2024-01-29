import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { HomeComponent } from './components/home/home.component';
import { FormsModule } from '@angular/forms';
import { MoviesListComponent } from './components/movies/movies-list/movies-list.component';
import { MoviesDetailsComponent } from './components/movies/movie-details/movie-details.component';
import { HttpClientModule } from '@angular/common/http';
import { ListarComponent } from './components/reviews/listar/listar.component';
import { EditComponent } from './components/reviews/edit/edit.component';
import { AddComponent } from './components/reviews/add/add.component';
import {ReviewsService} from '../app/services/reviews.service';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeComponent,
    MoviesListComponent,
    MoviesDetailsComponent,
    ListarComponent,
    EditComponent,
    AddComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule // <-- import the FormsModule before binding with [(ngModel)]
  ],
  providers: [ReviewsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
