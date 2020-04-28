import { Component, OnInit } from '@angular/core';
import {FormGroup, FormBuilder, Validators} from '@angular/forms';
import { Router } from '@angular/router';


@Component({
  selector: 'app-first-page',
  templateUrl: './first-page.component.html',
  styleUrls: ['./first-page.component.css']
})
export class FirstPageComponent implements OnInit {
  imageUrl: String="/assets/img/insertImage.png";
  fileToUpload:File=null;

  signUpForm:FormGroup;
  invalidLogin:boolean=false;

  constructor(private formBuilder:FormBuilder,private router:Router) {
    
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

  handleFileInput(file: FileList){
    this.fileToUpload=file.item(0);

    //preview of the image
    var reader=new FileReader();
    reader.onload=(event:any)=> {
      this.imageUrl=event.target.result;
    }
    reader.readAsDataURL(this.fileToUpload);
  }

  isShown: boolean = false ; // hidden by default


toggleShow() {

this.isShown = ! this.isShown;

}


}


