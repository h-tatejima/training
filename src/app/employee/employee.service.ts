import { Injectable } from '@angular/core';
import { Employee } from './employee';
import { Observable } from 'rxjs/Observable';
import { Headers, Http, Response } from '@angular/http';
import 'rxjs/add/operator/toPromise';
 
@Injectable()
export class EmployeeService {
 
    private url = 'employee';
    private headers: Headers = new Headers({
        'Content-Type': 'application/json',
    });
 
    constructor(private http: Http) { }
 
    //Employee�ꗗ�擾���\�b�h
    getEmployee(): Promise<Employee[]> {
        return this.http.get(this.url,{ headers: this.headers }).toPromise()
        .then((response: Response) => response.json().data as Employee[])
        .catch(this.handleError);
    }
    //Employee�ڍ׎擾���\�b�h
    getEmployee(e_id: string): Promise<Employee> {
        const url: string = `${this.url}/${id}`;
        return this.http.get(url,{ headers: this.headers }).toPromise()
        .then((response: Response) => response.json().data as Employee)
        .catch(this.handleError);
    }
    //Employee�X�V���\�b�h
    update(employee: Employee): Promise<Employee> {
        const url: string = `${this.url}/${employee.e_id}`;
        return this.http
        .put(url, JSON.stringify(user), { headers: this.headers }).toPromise()
        .then(() => employee)
        .catch(this.handleError);
    }
    //Employee�ǉ����\�b�h
    create(e_name: string): Promise<Employee> {
        return this.http
        .post(this.url, JSON.stringify({ e_name: e_name }), { headers: this.headers }).toPromise()
        .then((response: Response) => response.json().data)
        .catch(this.handleError);
    }
    //Employee�폜���\�b�h
    delete(e_id: string): Promise<void> {
        const url = `${this.url}/${id}`;
        return this.http.delete(url, { headers: this.headers }).toPromise()
        .then(() => null)
        .catch(this.handleError);
    }
    //�G���[�n���h�����O���\�b�h
    private handleError(error: any): Promise<any> {
        console.error('Error occured : ', error);
        return Promise.reject(error.message || error);
    }
}