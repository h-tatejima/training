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
  
  list() {
    this.client.get('/api/list').subscribe((results: EmpList) => {
      for(let index in results.idList) {
        this.itemService.empInfoList[index] = {
          id: results.idList[index]
          , name: results.nameList[index]
          , date: results.dateList[index]
        };
      }
    });
  }
  
  get(id: string): Observable<Employee> {
    return of(this.employee[id]);
  }
}
