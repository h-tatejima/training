import { Component, OnInit } from '@angular/core';
import { Employee } from '../shared/models/employee';
import { EmployeeService } from '../shared/services/employee.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {
  employee: Employee[] = null;
  
  constructor(
    private employeeService: EmployeeService,
  ) { }

  ngOnInit() {
      this.employeeService.list();
    }
  

}
