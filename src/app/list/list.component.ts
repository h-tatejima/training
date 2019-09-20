import { Component, OnInit } from '@angular/core';
import { Employee } from './employee';
import { EmployeeService } from './employee.service';
import { Http, HttpModule } from '@angular/http';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {
  employee: Employee[]
  
  constructor(
    private employeeService: EmployeeService
  ) { }

  ngOnInit() {
    this.getEmployee()
  }
  
  getEmployee(): void {
    this.employeeService.getEmployee().then((employee: Employee[]) => this.employee = employee);
  }

}
