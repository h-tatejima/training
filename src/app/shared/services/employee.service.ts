import { Injectable } from '@angular/core';
import { Employee } from '../models/employee';
import { Observable, of } from 'rxjs/index';
import { HttpClient, HttpHeaders } from '@angular/common/http';

const http_options = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {
  employee = [];

  constructor(
    private client: HttpClient,
  ) { }
  
  list(): Observable<Employee[]> {
    return of(this.employee);
  }
  
  get(id: string): Observable<Employee> {
    return of(this.employee[id]);
  }
}
