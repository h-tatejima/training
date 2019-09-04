#index.py
#coding=UTF-8

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask, render_template
  
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


@app.route('/index')
def  index2():
    return render_template('/bootstrap/index.html')
    
@app.route('/insert')
def  insert():
    return render_template('/bootstrap/insert.html')

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)

# SQLAlchemy はセッションを介してクエリを実行する
Session = sessionmaker(bind=engine)
session = Session()

# セッション・クローズ
# DB処理が不要になったタイミングやスクリプトの最後で実行
session.close()