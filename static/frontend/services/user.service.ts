import { Injectable } from '@angular/core';
import { RestService } from './rest.service';
import { User } from '@models/user';

@Injectable({
  providedIn: 'root',
})
export class UserService extends RestService<User> {
  protected override url: string = `${this.url}/user/`;
}
