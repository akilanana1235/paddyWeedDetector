import { NgModule } from '@angular/core';
import {MatButtonModule, MatGridListModule} from '@angular/material';

const Materials=[
  MatButtonModule,
  MatGridListModule
];

@NgModule({
  
  imports: [
    Materials
  ],
  exports: [
    Materials
  ]
})
export class MaterialModule { }
