import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { environment } from "environments/environment";
import { Observable } from "rxjs";

@Injectable({
  providedIn: "root",
})
export abstract class RestService<T> {
  protected url: string = environment.baseUrl;

  constructor(protected http: HttpClient) {}

  getAll(): Observable<T[]> {
    return this.http.get<T[]>(this.url);
  }

  getOne(id: number): Observable<T> {
    return this.http.get<T>(`${this.url}${id}`);
  }

  create(obj: T): Observable<T> {
    return this.http.post<T>(this.url, obj);
  }

  update(id: number, obj: T): Observable<T> {
    return this.http.put<T>(`${this.url}${id}`, obj);
  }

  delete(id: number): Observable<T> {
    return this.http.delete<T>(`${this.url}${id}`);
  }
}
