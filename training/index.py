#index.py
#coding=UTF-8

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask
  
engine = create_engine('mysql+pymysql://testUser:testPassword@localhost/test')

# モデルの作成
 
# まずベースモデルを生成します
Base = declarative_base()
 
 
# 従業員モデルクラス
class Employee(Base):
    __tablename__ = 'employee'
 
    e_name = Cloumn(String)
    e_name_kana = Cloumn(String)
    e_name_en = Cloumn(String)
    postal_code = Cloumn(String)
    address = Cloumn(String)
    phone_number = Cloumn(String)
    email = Cloumn(String)
    sex = Cloumn(String)
    birthday = Cloumn(String)
    final_education = Cloumn(String)
    join_date = Cloumn(String)
    company_email = Cloumn(String)
    e_id = Cloumn(Integer, primary_key=True)
    image = Cloumn(String)
     
    def __repr__(self):
        return "<Employee(
        e_name='%s',
        e_name_kana='%s',
        e_name_en='%s',
        postal_code='%s',
        address='%s',
        phone_number='%s',
        email='%s',
        sex='%s',
        birthday='%s',
        final_education='%s',
        join_date='%s',
        company_email='%s',
        e_id='%s',
        image='%s')>"
         % (
        self.e_name,
        self.e_name_kana,
        self.e_name_en,
        self.postal_code,
        self.address,
        self.phone_number,
        self.email,
        self.sex,
        self.birthday,
        self.final_education,
        self.join_date,
        self.company_email,
        self.e_id,
        self.image)
 
 
# テーブルの作成
# テーブルがない場合 CREATE TABLE 文が実行される
Base.metadata.create_all(engine)  # 作成した engine を引数にすること

# SQLAlchemy はセッションを介してクエリを実行する
Session = sessionmaker(bind=engine)
session = Session()

# 1レコードの追加
session.add(Student(id=1, name='Suzuki', score=70))
 
# コミット（データ追加を実行）
session.commit()

# セッション・クローズ
# DB処理が不要になったタイミングやスクリプトの最後で実行
session.close()