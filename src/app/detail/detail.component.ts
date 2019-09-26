import { Component, OnInit } from '@angular/core';
import { Employee } from '../shared/models/employee';
import { EmployeeService } from '../shared/services/employee.service';
import { ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent implements OnInit {
  employee: Employee;

  constructor(
    private route: ActivatedRoute,
    private employeeService: EmployeeService,
  ) { }

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      this.employeeService.detail(params['id']).subscribe((employee: Employee) => {
        this.employee = employee;
      });
    });
  }

}
