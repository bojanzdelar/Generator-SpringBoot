import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { LoginService } from '@services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  form: FormGroup = new FormGroup({
    username: new FormControl(null, Validators.required),
    password: new FormControl(null, Validators.required),
  });

  constructor(private loginService: LoginService) {}

  ngOnInit(): void {}

  login() {
    if (!this.form.valid) {
      window.alert('Username and password must be entered!');
      return;
    }

    this.loginService.login(this.form.value);
  }
}
