import { Component, OnInit  } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiService } from '../api.service';
import { Cars } from '../cars';
import { CommonModule } from '@angular/common';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

@Component({
  selector: 'app-car-list',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, FormsModule],
  templateUrl: './car-list.component.html',
  styleUrl: './car-list.component.css'
})
export class CarListComponent implements OnInit {
  cars$!: Observable<Cars[]>;
  car_details_form!: FormGroup;

  constructor(private apiService: ApiService, private form_builder: FormBuilder) { }

  ngOnInit() {
    this.getCars();

    this.car_details_form = this.form_builder.group({
      car_title: '',
      description: ''
    });

    // Set validators for fields.
    this.car_details_form.controls["car_title"].setValidators([Validators.required]);
    this.car_details_form.controls["description"].setValidators([Validators.required]);
  }

  public getCars() {
    this.cars$ = this.apiService.getCars();
  }

  onSubmit() {
    // Create the Task.
    this.apiService.postCarDetails(this.car_details_form.value)
      .subscribe(
        (response) => {
          console.log(response);
          this.getCars();
        }
      )
  }

  deleteCarDetails(car_id: number) {
    this.apiService.deleteCarDetails(car_id)
      .subscribe(
        (response) => {
          console.log(response);
          this.getCars();
        }
      )
  }

  updateCarDetails(car: Cars) {
    this.apiService.putCarDetails(car)
      .subscribe(
        (response) => {
          console.log(response);
          this.getCars();
        }
      )
  }

}
