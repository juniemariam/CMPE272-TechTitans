import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
// import { CarListComponent } from './car-list/car-list.component';  // Import CarListComponent

@NgModule({
  declarations: [
    AppComponent,
    // CarListComponent  // Declare CarListComponent here
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
