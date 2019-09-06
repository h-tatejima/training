#index.py
#coding=UTF-8

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask, render_template, request
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
    join_date = Column(String(100))
    company_email = Column(String(100))
    e_id = Column(Integer, primary_key=True)
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
        self.join_date,\
        self.company_email,\
        self.e_id,\
        self.image)
 
 
# テーブルの作成
# テーブルがない場合 CREATE TABLE 文が実行される
Base.metadata.create_all(engine)  # 作成した engine を引数にすること


app = Flask(__name__)


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
    return render_template('/bootstrap/insert.html')
    
@app.route('/add',methods=["post"])
def  add():
    #pdb.set_trace()
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
    join_date=join_date,\
    company_email=company_email,\
    e_id=e_id,\
    image=image))
    session.commit()
    return index()
    
@app.route('/<int:id>/detail', methods=["get"])
def detail(id):
    employee = session.query(Employee).get(id)
    return render_template('/bootstrap/detail.html', employee=employee)
    
@app.route('/<int:id>/delete', methods=["get"])
def delete(id):
    employee = session.query(Employee).get(id)
    session.delete(employee)
    session.commit()
    return index()
    
@app.route('/<int:id>/update', methods=["get"])
def update(id):
    employee = session.query(Employee).get(id)
    return render_template('bootstrap/insert.html', employee=employee)
    
@app.route('/<int:id>/update_employee', methods=["post"])
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