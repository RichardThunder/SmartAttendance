from handler.user import user
from flask import  Flask
#from handler.picture import picture

#数据库配置
from db_config import app
# app = Flask(__name__)

# 解决跨域
from flask_cors import CORS
CORS(app, supports_credentials=True)

#注册蓝图1 user
app.register_blueprint(user,url_prefix="/user")

app.register_blueprint(picture,url_prefix="/picture")

#default路由配置
@app.route('/')
def index():
    return 'Please visit user/login'

if __name__=='__main__':
    app.run(host="0.0.0.0",port='5000',debug=True)