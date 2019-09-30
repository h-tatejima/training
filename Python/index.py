#index.py
#coding=UTF-8

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, ValidationError
import re
import datetime
import json
import pdb
  
engine = create_engine('mysql+pymysql://testUser:testPassword@localhost/test')

# モデルの作成
 
# まずベースモデルを生成します
Base = declarative_base()
 
 
# 従業員モデルクラス
class Employee(Base):
    __tablename__ = 'employee'
 
    e_name = Column(String(100))
    e_name_kana = Column(String(100))
    e_name_en = Column(String(100))
    postal_code = Column(String(100))
    address = Column(String(100))
    phone_number = Column(String(100))
    email = Column(String(100))
    sex = Column(String(100))
    birthday = Column(String(100))
    final_education = Column(String(100))
    final_education2 = Column(String(100))
    join_date = Column(String(100))
    company_email = Column(String(100))
    e_id = Column(String(100), primary_key=True)
    image = Column(String(100))
    branch_id = Column(String(5))
    department_id = Column(String(5))
     
    def __repr__(self):
        return "<Employee(\
        e_name='%s',\
        e_name_kana='%s',\
        e_name_en='%s',\
        postal_code='%s',\
        address='%s',\
        phone_number='%s',\
        email='%s',\
        sex='%s',\
        birthday='%s',\
        final_education='%s',\
        final_education2='%s',\
        join_date='%s',\
        company_email='%s',\
        e_id='%s',\
        image='%s'\
        branch_id='%s'\
        department_id='%s')>"\
         % (\
        self.e_name,\
        self.e_name_kana,\
        self.e_name_en,\
        self.postal_code,\
        self.address,\
        self.phone_number,\
        self.email,\
        self.sex,\
        self.birthday,\
        self.final_education,\
        self.final_education2,\
        self.join_date,\
        self.company_email,\
        self.e_id,\
        self.image,\
        self.branch,\
        self.department)

# 支店モデルクラス
class Branch(Base):
    __tablename__ = 'branch'
 
    branch_id = Column(String(5), primary_key=True)
    branch_name = Column(String(100))
    
    def __repr__(self):
        return "<Branch(\
        branch_id='%s',\
        branch_name='%s')>"\
         % (\
        self.branch_id,\
        self.branch_name)

# 部署モデルクラス
class Department(Base):
    __tablename__ = 'department'
 
    department_id = Column(String(5), primary_key=True)
    department_name = Column(String(100))
    
    def __repr__(self):
        return "<Department(\
        department_id='%s',\
        department_name='%s')>"\
         % (\
        self.department_id,\
        self.department_name)

# テーブルの作成
# テーブルがない場合 CREATE TABLE 文が実行される
Base.metadata.create_all(engine)  # 作成した engine を引数にすること

#入力チェック
class InsertForm(FlaskForm):
    e_name = StringField('名前')
    e_name_kana = StringField('よみがな')
    e_name_en = StringField('name')
    postal_code = StringField('郵便番号')
    address = StringField('住所')
    phone_number = StringField('電話番号')
    email = StringField('メールアドレス')
    sex = StringField('性別')
    birthday = StringField('生年月日')
    final_education = StringField('最終学歴')
    join_date = StringField('入社年月日')
    company_email = StringField('自社メールアドレス')
    e_id = StringField('従業員ID')
    image = FileField('写真イメージ')
    branch_id = StringField('所属支店')
    department_id = StringField('所属部署')
    
    def validate_e_name(self, e_name):
        if e_name.data == "":
            raise ValidationError("名前を入力して下さい")
            
    def validate_e_name_kana(self, e_name_kana):
        if e_name_kana.data == "":
            raise ValidationError("よみがなを入力して下さい")
            
    def validate_e_name_en(self, e_name_en):
        if e_name_en.data == "":
            raise ValidationError("nameを入力して下さい")
        if not re.match(r'^[a-z ]+$', e_name_en.data):
            raise ValidationError("英字(小文字)で入力して下さい")
            
    def validate_postal_code(self, postal_code):
        if postal_code.data == "":
            raise ValidationError("郵便番号を入力して下さい")
        if not re.match(r'[0-9]{3}-[0-9]{4}', postal_code.data):
            raise ValidationError("000-0000で入力して下さい")
            
    def validate_address(self, address):
        if address.data == "":
            raise ValidationError("住所を入力して下さい")
            
    def validate_phone_number(self, phone_number):
        if phone_number.data == "":
            raise ValidationError("電話番号を入力して下さい")
        if not re.match(r'[0-9]{2}-[0-9]{4}-[0-9]{4}', phone_number.data):
            raise ValidationError("00-0000-0000で入力して下さい")
            
    def validate_email(self, email):
        if email.data != "":
           if not re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email.data):
               raise ValidationError("aaa@aaa.aaaで入力して下さい")
            
    def validate_sex(self, sex):
        if sex.data == "":
            raise ValidationError("性別を入力して下さい")
            
    def validate_birthday(self, birthday):
        if birthday.data == "":
            raise ValidationError("生年月日を入力して下さい")
        if not re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', birthday.data):
            raise ValidationError("yyyy-mm-ddで入力して下さい")
            
    def validate_final_education(self, final_education):
        if final_education.data == "":
            raise ValidationError("最終学歴を入力して下さい")
            
    def validate_join_date(self, join_date):
        join_date_split = join_date.data.split("-")
        join_date_datetime = datetime.datetime(int(join_date_split[0]),int(join_date_split[1]),int(join_date_split[2]))
        join_date_weekday = join_date_datetime.weekday()
        if join_date.data == "":
            raise ValidationError("入社年月日を入力して下さい")
        if not re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', join_date.data):
            raise ValidationError("yyyy-mm-ddで入力して下さい")
        if join_date_weekday != 0:
            raise ValidationError("入社年月日は月曜日を入力して下さい")
            
    def validate_image(self, image):
        if image.data == "":
            raise ValidationError("写真イメージを選択して下さい")
            
    def validate_department_id(self, department_id):
        branch_id = request.form["branch_id"]
        if branch_id == "00001":
            if department_id.data == "00001" or department_id.data == "00005":
                raise ValidationError("東京支店の場合、所属部署はSI事業部、新規商材開発部、受託開発事業部、営業部を選択して下さい")
        elif branch_id == "00002":
            if department_id.data == "00003" or department_id.data == "00004":
                raise ValidationError("東海支店の場合、所属部署は組み込み開発事業部、SI事業部、総務部、営業部を選択して下さい")
        else:
            if department_id.data != "00003":
                raise ValidationError("東北支店の場合、所属部署は受託開発事業部を選択して下さい")
                
#入力チェック(編集画面)
class UpdateForm(FlaskForm):
    e_name = StringField('名前')
    e_name_kana = StringField('よみがな')
    e_name_en = StringField('name')
    postal_code = StringField('郵便番号')
    address = StringField('住所')
    phone_number = StringField('電話番号')
    email = StringField('メールアドレス')
    sex = StringField('性別')
    birthday = StringField('生年月日')
    final_education = StringField('最終学歴')
    join_date = StringField('入社年月日')
    company_email = StringField('自社メールアドレス')
    e_id = StringField('従業員ID')
    image = FileField('写真イメージ')
    branch_id = StringField('所属支店')
    department_id = StringField('所属部署')
    
    def validate_e_name(self, e_name):
        if e_name.data == "":
            raise ValidationError("名前を入力して下さい")
            
    def validate_e_name_kana(self, e_name_kana):
        if e_name_kana.data == "":
            raise ValidationError("よみがなを入力して下さい")
            
    def validate_e_name_en(self, e_name_en):
        if e_name_en.data == "":
            raise ValidationError("nameを入力して下さい")
        if not re.match(r'^[a-z ]+$', e_name_en.data):
            raise ValidationError("英字(小文字)で入力して下さい")
            
    def validate_postal_code(self, postal_code):
        if postal_code.data == "":
            raise ValidationError("郵便番号を入力して下さい")
        if not re.match(r'[0-9]{3}-[0-9]{4}', postal_code.data):
            raise ValidationError("000-0000で入力して下さい")
            
    def validate_address(self, address):
        if address.data == "":
            raise ValidationError("住所を入力して下さい")
            
    def validate_phone_number(self, phone_number):
        if phone_number.data == "":
            raise ValidationError("電話番号を入力して下さい")
        if not re.match(r'[0-9]{2}-[0-9]{4}-[0-9]{4}', phone_number.data):
            raise ValidationError("00-0000-0000で入力して下さい")
            
    def validate_email(self, email):
        if email.data != "":
           if not re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email.data):
               raise ValidationError("aaa@aaa.aaaで入力して下さい")
            
    def validate_sex(self, sex):
        if sex.data == "":
            raise ValidationError("性別を入力して下さい")
            
    def validate_birthday(self, birthday):
        if birthday.data == "":
            raise ValidationError("生年月日を入力して下さい")
        if not re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', birthday.data):
            raise ValidationError("yyyy-mm-ddで入力して下さい")
            
    def validate_final_education(self, final_education):
        if final_education.data == "":
            raise ValidationError("最終学歴を入力して下さい")
            
    def validate_join_date(self, join_date):
        join_date_split = join_date.data.split("-")
        join_date_datetime = datetime.datetime(int(join_date_split[0]),int(join_date_split[1]),int(join_date_split[2]))
        join_date_weekday = join_date_datetime.weekday()
        if join_date.data == "":
            raise ValidationError("入社年月日を入力して下さい")
        if not re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', join_date.data):
            raise ValidationError("yyyy-mm-ddで入力して下さい")
        if join_date_weekday != 0:
            raise ValidationError("入社年月日は月曜日を入力して下さい")
            
    def validate_image(self, image):
        if image.data == "":
            raise ValidationError("写真イメージを選択して下さい")
            
    def validate_department_id(self, department_id):
        branch_id = request.form["branch_id"]
        if branch_id == "00001":
            if department_id.data == "00001" or department_id.data == "00005":
                raise ValidationError("東京支店の場合、所属部署はSI事業部、新規商材開発部、受託開発事業部、営業部を選択して下さい")
        elif branch_id == "00002":
            if department_id.data == "00003" or department_id.data == "00004":
                raise ValidationError("東海支店の場合、所属部署は組み込み開発事業部、SI事業部、総務部、営業部を選択して下さい")
        else:
            if department_id.data != "00003":
                raise ValidationError("東北支店の場合、所属部署は受託開発事業部を選択して下さい")
                
    def validate_company_email(self, company_email):
        branch_id = request.form["branch_id"]
        if branch_id == "00001":
            if not re.match(r'^\w+([-+.]\w+)*@tky.emdes.co.jp', company_email.data):
                raise ValidationError("aaa@tky.emdes.co.jpで入力して下さい")
        elif branch_id == "00002":
            if not re.match(r'^\w+([-+.]\w+)*@ngy.emdes.co.jp', company_email.data):
                raise ValidationError("aaa@ngy.emdes.co.jpで入力して下さい")
        else:
            if not re.match(r'^\w+([-+.]\w+)*@sdi.emdes.co.jp', company_email.data):
                raise ValidationError("aaa@sdi.emdes.co.jpで入力して下さい")
                  
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"
app.config['JSON_AS_ASCII'] = False

# SQLAlchemy はセッションを介してクエリを実行する
Session = sessionmaker(bind=engine)
session = Session()

branch = session.query(Branch).count()
if branch == 0:

    session.add_all([
        Branch(branch_id="00001", branch_name="東京支店"),
        Branch(branch_id="00002", branch_name="東海支店"),
        Branch(branch_id="00003", branch_name="東北支店")
    ])

    session.commit()
    
department = session.query(Department).count()
if department == 0:

    session.add_all([
        Department(department_id="00001", department_name="組み込み開発事業部"),
        Department(department_id="00002", department_name="SI事業部"),
        Department(department_id="00003", department_name="受託開発事業部"),
        Department(department_id="00004", department_name="新規商材開発事業部"),
        Department(department_id="00005", department_name="総務部"),
        Department(department_id="00006", department_name="営業部")
    ])
    
    session.commit()

@app.route('/api/list', methods=["GET"])
def  list():
    emp_list = []
    for emp in session.query(Employee.e_id, Employee.e_name, Employee.join_date):
        emp_list.append({
          'e_id': emp.e_id,
          'e_name': emp.e_name,
          'join_date': emp.join_date
        })
    return jsonify(emp_list)
    
@app.route('/api/insert', methods=["GET"])
def  insert():
    #pdb.set_trace()
    form = InsertForm()
    branch_list = []
    department_list = []
    for branch in session.query(Branch.branch_id, Branch.branch_name):
        branch_list.append({
          'branch_id': branch.branch_id,
          'branch_name': branch.branch_name
        })
    for department in session.query(Department.department_id, Department.department_name):
        department_list.append({
          'department_id': department.department_id,
          'department_name': department.department_name
        })
    return jsonify(branch_list,department_list)
    
@app.route('/api/add', methods=["POST"])
def  add():
      e_name = request.json["e_name"]
      e_name_kana = request.json["e_name_kana"]
      e_name_en = request.json["e_name_en"]
      postal_code = request.json["postal_code"]
      address = request.json["address"]
      phone_number = request.json["phone_number"]
      email = request.json["email"]
      sex = request.json["sex"]
      birthday = request.json["birthday"]
      final_education = request.json["final_education"]
      final_education2 = request.json["final_education2"]
      join_date = request.json["join_date"]
      company_email = request.json["company_email"]
      e_id = request.json["e_id"]
      image = request.json["image"]
      branch_id = request.json["branch_id"]
      department_id = request.json["department_id"]
      
      session.add(Employee(\
      e_name=e_name,\
      e_name_kana=e_name_kana,\
      e_name_en=e_name_en,\
      postal_code=postal_code,\
      address=address,\
      phone_number=phone_number,\
      email=email,\
      sex=sex,\
      birthday=birthday,\
      final_education=final_education,\
      final_education2=final_education2,\
      join_date=join_date,\
      company_email=company_email,\
      e_id=e_id,\
      image=image,\
      branch_id=branch_id,\
      department_id=department_id))
      session.commit()
      return list()
        
      return make_response(jsonify({'res': 'OK'}))
    
@app.route('/api/detail/<id>', methods=["get"])
def detail(id):
    detail = {}
    for emp in session.query(Employee).filter(Employee.e_id==id):
        detail = {
          'e_name': emp.e_name,
          'e_name_kana': emp.e_name_kana,
          'e_name_en': emp.e_name_en,
          'postal_code': emp.postal_code,
          'address': emp.address,
          'phone_number': emp.phone_number,
          'email': emp.email,
          'sex': emp.sex,
          'birthday': emp.birthday,
          'final_education': emp.final_education,
          'final_education2': emp.final_education2,
          'join_date': emp.join_date,
          'company_email': emp.company_email,
          'e_id': emp.e_id,
          'image': emp.image,
          'branch_id': emp.branch_id,
          'department_id': emp.department_id
        }
    return jsonify(detail)
    
@app.route('/delete/<id>', methods=["get"])
def delete(id):
    employee = session.query(Employee).get(id)
    session.delete(employee)
    session.commit()
    return index()
    
@app.route('/update/<id>', methods=["get"])
def update(id):
    employee = session.query(Employee).get(id)
    form = UpdateForm()
    branch = session.query(Branch).all()
    department = session.query(Department).all()
    return render_template("/bootstrap/insert.html", employee=employee, form=form, branch=branch, department=department)
    
@app.route('/api/update/<id>', methods=["post"])
def update_employee(id):
    form = UpdateForm()
    employee = session.query(Employee).get(id)
    employee.e_name = request.json["e_name"]
    employee.e_name_kana = request.json["e_name_kana"]
    employee.e_name_en = request.json["e_name_en"]
    employee.postal_code = request.json["postal_code"]
    employee.address = request.json["address"]
    employee.phone_number = request.json["phone_number"]
    employee.email = request.json["email"]
    employee.sex = request.json["sex"]
    employee.birthday = request.json["birthday"]
    employee.final_education = request.json["final_education"]
    employee.final_education2 = request.json["final_education2"]
    employee.join_date = request.json["join_date"]
    employee.company_email = request.json["company_email"]
    employee.e_id = request.json["e_id"]
    employee.image = request.json["image"]
    employee.branch_id = reqest.json["branch_id"]
    employee.department_id = request.json["department_id"]
    session.add(employee)
    session.commit()
    return make_response(jsonify({'res': 'OK'}))

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)


# セッション・クローズ
# DB処理が不要になったタイミングやスクリプトの最後で実行
session.close()