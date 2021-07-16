from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:root@127.0.0.1:3306/smartattendance"

db_init=SQLAlchemy(app)