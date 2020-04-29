import { Component, OnInit } from '@angular/core';



@Component({
  selector: 'app-first-page',
  templateUrl: './first-page.component.html',
  styleUrls: ['./first-page.component.css']
})
export class FirstPageComponent implements OnInit {
  imageUrl: String="/assets/img/insertImage.png";
  fileToUpload:File=null;

  

  constructor() {
    
   }

  ngOnInit() {
    
  }

  onSubmit(){
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


