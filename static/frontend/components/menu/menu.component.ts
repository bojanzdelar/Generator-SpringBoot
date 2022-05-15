import { Component } from '@angular/core';
import { LoginService } from '@services/login.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css'],
})
export class MenuComponent {
  constructor(public loginService: LoginService) {}
}
