import { Component, OnInit } from '@angular/core';
import {FormGroup, FormBuilder, Validators} from '@angular/forms';
import { HttpClient} from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  signUpForm:FormGroup;
  invalidLogin:boolean=false;
  constructor(private formBuilder:FormBuilder,private router:Router,private http:HttpClient) { 
    
  }

  ngOnInit() {
    this.signUpForm=this.formBuilder.group({
      inputUserName4: ['',Validators.compose([Validators.required])],
      inputPassword4:['', Validators.required] ,
      inputAddress:['', Validators.required] ,
      inputAddress2:['', Validators.required] ,
      inputCity:['', Validators.required] ,
      inputZip:['', Validators.required] 
    });

}
onSubmit(){
  console.log(this.signUpForm.value);
  if(this.signUpForm.invalid){
    return;
  }

  const signInData = {
    userNameData:this.signUpForm.controls.inputUserName4.value,
    passwordData:this.signUpForm.controls.inputPassword4.value,
    addressData:this.signUpForm.controls.inputAddress.value,
    addressData2:this.signUpForm.controls.inputAddress2.value,
    cityData:this.signUpForm.controls.inputCity.value,
    zipData:this.signUpForm.controls.inputZip.value
  }

  
}
}
