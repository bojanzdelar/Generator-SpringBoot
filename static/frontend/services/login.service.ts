import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Token } from '@models/token';
import { User } from '@models/user';
import { environment } from 'environments/environment';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  private url: string = `${environment.baseUrl}/login/`;

  token: any;
  user: any;

  public redirectUrl: string | undefined;

  constructor(private http: HttpClient, private router: Router) {
    this.token = localStorage.getItem('token');
    if (this.token) {
      this.user = JSON.parse(atob(this.token.split('.')[1]));
    }
  }

  login(user: User) {
    this.http.post<Token>(this.url, user).subscribe((token: Token) => {
      this.token = token.token;
      this.user = JSON.parse(atob(this.token.split('.')[1]));
      localStorage.setItem('token', token.token);
      if (this.redirectUrl) {
        this.router.navigate([this.redirectUrl]);
        this.redirectUrl = undefined;
      } else {
        this.router.navigate(['/']);
      }
    });
  }

  logout() {
    this.token = null;
    this.user = null;
    localStorage.removeItem('token');
    this.router.navigate(['/']);
  }

  validateRoles(roles: any, method = 'any') {
    if (!this.token || !['any', 'all'].includes(method)) return false;

    if (method == 'any')
      return roles.some((role: any) => this.user.roles.includes(role));

    if (method == 'all')
      return roles.every((role: any) => this.user.roles.includes(role));
  }
}
