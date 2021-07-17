#数据库的配置<必须使用app配置
# > ip 3306 数据库名字 root账户和密码

from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123qweASD@182.92.179.151:3306/demo"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/smartattendance"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/smartattendance"
db_init = SQLAlchemy(app)