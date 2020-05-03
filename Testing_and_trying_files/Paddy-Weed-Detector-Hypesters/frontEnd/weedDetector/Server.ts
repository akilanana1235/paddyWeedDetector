import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable ({
    providedIn : 'root'
})
export class uploadImage {
    DJANGO_SERVER: string = "http://127.0.0.1:4200";
    constructor(private http: HttpClient) {}


}
