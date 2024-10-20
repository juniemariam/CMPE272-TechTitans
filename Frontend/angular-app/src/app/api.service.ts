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
}
