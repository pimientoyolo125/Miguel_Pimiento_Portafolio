import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MoviesDetailsComponent } from './movie-details.component';

describe('MovieDetailsComponent', () => {
  let component: MoviesDetailsComponent;
  let fixture: ComponentFixture<MoviesDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MoviesDetailsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MoviesDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
