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
        image='%s')>"\
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
        self.image)
 
 
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
    
    def validate_e_name(self, e_name):
        if e_name.data == "":
            raise ValidationError("名前を入力して下さい")
            
    def validate_e_name_kana(self, e_name_kana):
        if e_name_kana.data == "":
            raise ValidationError("よみがなを入力して下さい")
            
    def validate_e_name_en(self, e_name_en):
        if e_name_en.data == "":
            raise ValidationError("nameを入力して下さい")
        if not (e_name_en.data.isalpha() and e_name_en.data.islower()):
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
        if join_date.data == "":
            raise ValidationError("入社年月日を入力して下さい")
        if not re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', join_date.data):
            raise ValidationError("yyyy-mm-ddで入力して下さい")
            
    def validate_company_email(self, company_email):
        if company_email.data == "":
            raise ValidationError("自社メールアドレスを入力して下さい")
        if not re.match(r'^\w+([-+.]\w+)*@emdes.co.jp', company_email.data):
            raise ValidationError("aaa@emdes.co.jpで入力して下さい")
            
    def validate_e_id(self, e_id):
        if e_id.data == "":
            raise ValidationError("従業員IDを入力して下さい")
        if not re.match(r'emd[0-9]{10}', e_id.data):
            raise ValidationError("emd0000000000で入力して下さい")
            
    def validate_image(self, image):
        if image.data == "":
            raise ValidationError("写真イメージを選択して下さい")

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

# SQLAlchemy はセッションを介してクエリを実行する
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/index')
def  index():
    employee = session.query(Employee).all()
    return render_template('/bootstrap/index.html', employee=employee)
    
@app.route('/insert')
def  insert():
    #pdb.set_trace()
    form = InsertForm()
    message = "message"
    return render_template('/bootstrap/insert.html', form=form)
    
@app.route('/add',methods=["post"])
def  add():
    #pdb.set_trace()
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
        company_email = request.form["company_email"]
        e_id = request.form["e_id"]
        image = request.form["image"]
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
        image=image))
        session.commit()
        return index()
        
    return render_template("/bootstrap/insert.html", form=form)
    
@app.route('/<id>/detail', methods=["get"])
def detail(id):
    employee = session.query(Employee).get(id)
    return render_template('/bootstrap/detail.html', employee=employee)
    
@app.route('/<id>/delete', methods=["get"])
def delete(id):
    employee = session.query(Employee).get(id)
    session.delete(employee)
    session.commit()
    return index()
    
@app.route('/<id>/update', methods=["get"])
def update(id):
    employee = session.query(Employee).get(id)
    return render_template('bootstrap/insert.html', employee=employee)
    
@app.route('/<id>/update_employee', methods=["post"])
def update_employee(id):
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
    employee.e_id = request.form["e_id"]
    employee.image = request.form["image"]
    session.add(employee)
    session.commit()
    return index()

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)


# セッション・クローズ
# DB処理が不要になったタイミングやスクリプトの最後で実行
session.close()