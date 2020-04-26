import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  cover: File;

  constructor(private http: HttpClient) {}

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
}
