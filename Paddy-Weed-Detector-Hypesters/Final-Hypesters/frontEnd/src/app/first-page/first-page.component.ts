import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';



@Component({
  selector: 'app-first-page',
  templateUrl: './first-page.component.html',
  styleUrls: ['./first-page.component.css']
})

export class FirstPageComponent  {
  imageUrl: String="/assets/img/insertImage.png";
  // fileToUpload:File=null;

  cover: File;

  constructor(private http: HttpClient) { }

  onImageChanged(event: any) {
    this.cover = event.target.files[0];
  }

  newBook() {
    const uploadData = new FormData();
    uploadData.append('cover', this.cover);
    console.log("uploadData" + this.cover);
    this.http.post('http://127.0.0.1:8000/books/', uploadData).subscribe(

      (data) => console.log(data),
      (error) => console.log(error)
    );
  }


  // handleFileInput(file: FileList){
  //   this.fileToUpload=file.item(0);

  //   //preview of the image
  //   var reader=new FileReader();
  //   reader.onload=(event:any)=> {
  //     this.imageUrl=event.target.result;
  //   }
  //   reader.readAsDataURL(this.fileToUpload);
  // }

  // isShown: boolean = false ; // hidden by default


// toggleShow() {

// this.isShown = ! this.isShown;

// }

}


