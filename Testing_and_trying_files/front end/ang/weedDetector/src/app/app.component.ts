import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import {User} from './user';
import {EnrollmentService} from './enrollment.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'weedDetector';
  showModal: boolean;
  registerForm: FormGroup;
  submitted = false;
  constructor(private formBuilder: FormBuilder,private _enrollmentService:EnrollmentService) { }

  //userModel=new User('Rob', '1234',7635489061,'Baker st,London');

  
  ngOnInit() {
    
}



}
