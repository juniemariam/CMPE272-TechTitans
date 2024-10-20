import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Cars } from './cars';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  API_URL = 'http://localhost/api';

  constructor(private http: HttpClient) { }

  public getCars(): Observable<Cars[]> {
    return this.http.get<Cars[]>(`${this.API_URL}/cars/`);
  }

  public postCarDetails(new_car_deatil: Cars) {
    return this.http.post(`${this.API_URL}/cars/`,new_car_deatil);
  }

  // Update a Car Details.
  public putCarDetails(the_car: Cars) {
    return this.http.put(`${this.API_URL}/cars/${the_car.id}/`,the_car);
  }

  // Delete a Car Details.
  public deleteCarDetails(car_id: number) {
    return this.http.delete(`${this.API_URL}/cars/${car_id}/`);
  }

}
