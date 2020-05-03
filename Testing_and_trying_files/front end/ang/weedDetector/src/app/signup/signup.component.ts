import { Component, OnInit } from '@angular/core';
import { User } from '../user';
import {EnrollmentService} from '../enrollment.service';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  submitted=false;

  userModel = new User('Rob','rob@gmail.com',7555784325,'rob123');
  
  constructor(private _enrollmentService:EnrollmentService) { }
  ngOnInit() { 
  }

  
  onSubmit(){
    this.submitted=true;
    this._enrollmentService.enroll(this.userModel)
    .subscribe(
      data => console.log('Success!',data),
      error => console.error('Eror!',error)
    )
    }
  }

