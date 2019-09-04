#models.py
#coding=UTF-8

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask, render_template
  
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name
 
 
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