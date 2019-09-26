import { Injectable } from '@angular/core';
import { Employee } from '../models/employee';
import { Observable, of } from 'rxjs/index';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';

const http_options = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

  constructor(
    private client: HttpClient,
    private router: Router,
  ) { }
  
  list() {
      return this.client.get('/api/list')
  }
  
  add() {
      this.client.post('/api/add',http_options).subscribe((result) => {
      switch (result['res']) {
        case 'OK':
          this.router.navigate(['/list']);
          break;
        case 'NG':
      }
    });
  }
  
  detail(id: string) {
      return this.client.get('/api/detail/'+id)
  }
}
