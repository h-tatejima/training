import { Injectable } from '@angular/core';
import { Employee } from '../models/employee';
import { Observable, of } from 'rxjs/index';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {
  employee = [
      new Employee('名前', 'e_name_kana', 'e_name_en', 'postal_code', 'address', 'phone_number', 'email', 'sex', 'birthday', 'final_education', 'final_education2', '入社年月日', 'company_email', '1', 'image', 'branch_id', 'department_id'),
      new Employee('名前', 'e_name_kana', 'e_name_en', 'postal_code', 'address', 'phone_number', 'email', 'sex', 'birthday', 'final_education', 'final_education2', '入社年月日', 'company_email', '2', 'image', 'branch_id', 'department_id')
      ];

  constructor() { }
  
  list(): Observable<Employee[]> {
    return of(this.employee);
  }
  
  get(id: string): Observable<Employee> {
    return of(this.employee[id]);
  }
}
