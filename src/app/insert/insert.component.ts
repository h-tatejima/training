import { Component, OnInit } from '@angular/core';
import { Branch } from '../shared/models/branch';
import { Department } from '../shared/models/department';
import { BranchService } from '../shared/services/branch.service';
import { Employee } from '../shared/models/employee';
import { EmployeeService } from '../shared/services/employee.service';


@Component({
  selector: 'app-insert',
  templateUrl: './insert.component.html',
  styleUrls: ['./insert.component.css']
})
export class InsertComponent implements OnInit {
  branch: Branch[]
  department: Department[]

  constructor(
    private branchService: BranchService,
    private employeeService: EmployeeService,
  ) { }

  ngOnInit() {
      this.branchService.list().subscribe((branch: Branch) => {
        this.branch = branch[0];
        this.department = branch[1];
      });
  }
  
  onSubmit() {
      this.employeeService.add()
  }

}
