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
 
    //Employee一覧取得メソッド
    getEmployee(): Promise<Employee[]> {
        return this.http.get(this.url,{ headers: this.headers }).toPromise()
        .then((response: Response) => response.json().data as Employee[])
        .catch(this.handleError);
    }
    //Employee詳細取得メソッド
    getEmployee(e_id: string): Promise<Employee> {
        const url: string = `${this.url}/${id}`;
        return this.http.get(url,{ headers: this.headers }).toPromise()
        .then((response: Response) => response.json().data as Employee)
        .catch(this.handleError);
    }
    //Employee更新メソッド
    update(employee: Employee): Promise<Employee> {
        const url: string = `${this.url}/${employee.e_id}`;
        return this.http
        .put(url, JSON.stringify(user), { headers: this.headers }).toPromise()
        .then(() => employee)
        .catch(this.handleError);
    }
    //Employee追加メソッド
    create(e_name: string): Promise<Employee> {
        return this.http
        .post(this.url, JSON.stringify({ e_name: e_name }), { headers: this.headers }).toPromise()
        .then((response: Response) => response.json().data)
        .catch(this.handleError);
    }
    //Employee削除メソッド
    delete(e_id: string): Promise<void> {
        const url = `${this.url}/${id}`;
        return this.http.delete(url, { headers: this.headers }).toPromise()
        .then(() => null)
        .catch(this.handleError);
    }
    //エラーハンドリングメソッド
    private handleError(error: any): Promise<any> {
        console.error('Error occured : ', error);
        return Promise.reject(error.message || error);
    }
}