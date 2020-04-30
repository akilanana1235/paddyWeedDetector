import {Routes,RouterModule} from '@angular/router';
import { FirstPageComponent } from './first-page/first-page.component';
import { SignupComponent } from './signup/signup.component';

const routes: Routes=[
    {
        path:"first-page" , component:FirstPageComponent
    },
    {
        path:"signup" , component:SignupComponent
    }
]

export const routing=RouterModule.forRoot(routes);