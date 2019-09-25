#index.py
#coding=UTF-8

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask, render_template, request
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
    employee = session.query(Employee).all()
    return jsonify({'employee' : employee})
    
@app.route('/insert')
def  insert():
    #pdb.set_trace()
    form = InsertForm()
    branch = session.query(Branch).all()
    department = session.query(Department).all()
    return render_template('/bootstrap/insert.html', form=form, branch=branch, department=department)
    
@app.route('/add',methods=["post"])
def  add():
    form = InsertForm()
    if form.validate_on_submit():
        e_name = request.form["e_name"]
        e_name_kana = request.form["e_name_kana"]
        e_name_en = request.form["e_name_en"]
        postal_code = request.form["postal_code"]
        address = request.form["address"]
        phone_number = request.form["phone_number"]
        email = request.form["email"]
        sex = request.form["sex"]
        birthday = request.form["birthday"]
        final_education = request.form["final_education"]
        final_education2 = request.form["final_education2"]
        join_date = request.form["join_date"]
        image = request.form["image"]
        branch_id = request.form["branch_id"]
        department_id = request.form["department_id"]
        
        name = e_name_en.split()
        name_first = name[0]
        name_family = name[1]
        name_head = name_first[0]
        
        for emp_name in session.query(Employee).filter(Employee.e_name_en.like("%" + name_first + "%")):
             db_name = emp_name.e_name_en
             db_name_split = db_name.split()
             db_name_first = db_name_split[0]
             if db_name_first == name_first:
                 name_family = name_family[0]
                 name_head = name_first
                 break
                 
        else:
            name_list = list()
            for emp_family in session.query(Employee).filter(Employee.e_name_en.like("%" + name_family + "%")):
                 db_name = emp_family.e_name_en
                 db_name_split = db_name.split()
                 db_name_first = db_name_split[0]
                 db_name_len = len(db_name_first)
                 in_name_len = len(name_first)
                 if db_name_len > in_name_len:
                     name_len = in_name_len
                 else:
                     name_len = db_name_len
                     
                 for i in range(name_len):
                      if db_name_first[i] == name_first[i]:
                          name_head = name_first[:i+2]
                      else:
                          break
                      
                 name_list.append(name_head)
             
            name_list_len = len(name_list)
            if name_list_len != 0:
                name_list_max = max(name_list, key=len)
                name_head = name_list_max
        
        if branch_id == "00001":
            branch_head = "tky"
        elif branch_id == "00002":
            branch_head = "ngy"
        else:
            branch_head = "sdi"
            
        company_email = name_head + "-" + name_family + "@" + branch_head + ".emdes.co.jp"
        
        db_employee_id = list()
        for emp in session.query(Employee):
            db_employee_id.append(emp.e_id[6:13])
            
        db_employee_id_len = len(db_employee_id)
        if db_employee_id_len != 0:
            db_e_id_max = max(db_employee_id)
            e_id_num = int(db_e_id_max) + 1
            e_id = "emd" + branch_head + str(e_id_num).rjust(7,"0")
        else:
            e_id = "emd" + branch_head + "0000000"
        
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
        return index()
        
    branch = session.query(Branch).all()
    department = session.query(Department).all()
    return render_template("/bootstrap/insert.html", form=form, branch=branch, department=department)
    
@app.route('/detail/<id>', methods=["get"])
def detail(id):
    employee = session.query(Employee).get(id)
    return render_template('/bootstrap/detail.html', employee=employee)
    
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
    
@app.route('/update_employee/<id>', methods=["post"])
def update_employee(id):
    form = UpdateForm()
    employee = session.query(Employee).get(id)
    employee.e_name = request.form["e_name"]
    employee.e_name_kana = request.form["e_name_kana"]
    employee.e_name_en = request.form["e_name_en"]
    employee.postal_code = request.form["postal_code"]
    employee.address = request.form["address"]
    employee.phone_number = request.form["phone_number"]
    employee.email = request.form["email"]
    employee.sex = request.form["sex"]
    employee.birthday = request.form["birthday"]
    employee.final_education = request.form["final_education"]
    employee.final_education2 = request.form["final_education2"]
    employee.join_date = request.form["join_date"]
    employee.company_email = request.form["company_email"]
    employee.image = request.form["image"]
    if form.validate_on_submit():
        session.add(employee)
        session.commit()
        return index()
    branch = session.query(Branch).all()
    department = session.query(Department).all()
    return render_template("/bootstrap/insert.html", employee=employee, form=form, branch=branch, department=department)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)


# セッション・クローズ
# DB処理が不要になったタイミングやスクリプトの最後で実行
session.close()