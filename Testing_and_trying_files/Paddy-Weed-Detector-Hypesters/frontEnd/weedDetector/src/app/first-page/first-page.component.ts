import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {Server} from './Server';

@Component({
  selector: 'app-root',
  templateUrl: './first-page.component.html',
  styleUrls: ['./first-page.component.css']
})
export class FirstPageComponent implements OnInit {



  DJANGO_SERVER = 'http://127.0.0.1:4200'
  form: FormGroup;
  response;
  imageUrl: String="/assets/img/insertImage.png";
  fileToUpload:File=null;

  constructor(private formgroup: FormGroup, private httpClient: HttpClient ) { }

  ngOnInit() {
    this.uploadForm = this.formBuilder.group ({
      firstPage: ['']
    });
  }
  onSubmit(imageUrl){
    const formData = new FormData();
    console.log("on submit "+ this.imageUrl);
    formData.append('key', imageUrl.value);
    this.http.get('http://localhost:4200/api?='+ this.imageUrl,{ responseType: 'text' } ).subscribe(
      (response) => console.log(response),
      (error) => console.log(error)
    )
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


}
