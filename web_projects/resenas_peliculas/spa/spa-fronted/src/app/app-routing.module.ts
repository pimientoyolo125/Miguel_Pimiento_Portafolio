import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { MoviesListComponent } from './components/movies/movies-list/movies-list.component';
import { MoviesDetailsComponent } from './components/movies/movie-details/movie-details.component';
import { ListarComponent } from './components/reviews/listar/listar.component';
import { AddComponent } from './components/reviews/add/add.component';
import { EditComponent } from './components/reviews/edit/edit.component';

const routes: Routes = [
 
  {
    path:'home',
    component: HomeComponent
  },
  {
    path:'movies',
    component: MoviesListComponent
  },
  {
    path:'movie/:movieId',
    component: MoviesDetailsComponent
  },
  {
   path:'listar/:movieId',
  component: ListarComponent
  },
  {
   path:'add/:movieId',
    component: AddComponent
  },
  {
    path:'edit',
    component: EditComponent
  },
  {
    path:'**',
    pathMatch:'full',
    redirectTo:'home'
  }
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
