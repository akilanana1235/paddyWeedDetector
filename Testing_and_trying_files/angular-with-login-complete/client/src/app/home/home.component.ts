import { Component } from '@angular/core';

@Component({
  templateUrl: './home.component.html'
})
export class HomeComponent {
  imageUrl: String="/assets/img/insertImage.png";
  fileToUpload:File=null;

  
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
