import { Component, OnInit  } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiService } from '../api.service';
import { Cars } from '../cars';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-car-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './car-list.component.html',
  styleUrl: './car-list.component.css'
})
export class CarListComponent implements OnInit {
  cars$!: Observable<Cars[]>;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getTasks();
  }

  public getTasks() {
    this.cars$ = this.apiService.getCars();
  }

}
