export class Employee {
  e_name: string;
  e_name_kana: string;
  e_name_en: string;
  postal_code: string;
  address: string;
  phone_number: string;
  email: string;
  sex: string;
  birthday: string;
  final_education: string;
  final_education2: string;
  join_date: string;
  company_email: string;
  e_id: string;
  image: string;
  branch_id: number;
  department_id: string;

  constructor(e_name, e_name_kana, e_name_en, postal_code, address, phone_number, email, sex, birthday, final_education, final_education2, join_date, company_email, e_id, image, branch_id, department_id) {
    this.e_name = e_name;
    this.e_name_kana = e_name_kana;
    this.e_name_en = e_name_en;
    this.postal_code = postal_code;
    this.address = address;
    this.phone_number = phone_number;
    this.email = email;
    this.sex = sex;
    this.birthday = birthday;
    this.final_education = final_education;
    this.final_education2 = final_education2;
    this.join_date = join_date;
    this.company_email = company_email;
    this.e_id = e_id;
    this.image = image;
    this.branch_id = branch_id;
    this.department_id = department_id;
  }
}
