import { Component, OnInit } from '@angular/core';
import { User } from '../user';
import {EnrollmentService} from '../enrollment.service';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  userModel = new User('Rob','rob@gmail.com',7555784325,'123rob');
  
  constructor(private _enrollmentService:EnrollmentService) { }
  ngOnInit() {
    this._enrollmentService.enroll(this.userModel)
    .subscribe(
      data => console.log('Success!',data),
      error => console.error('Eror!',error)
    )
  }

  
  onSubmit(){
    
    }

    
  }

