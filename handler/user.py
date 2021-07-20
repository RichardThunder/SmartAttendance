from flask import Blueprint, request, Response, jsonify, json
from api.user_api import *
import os
from operation.face_operation import *
user = Blueprint('user', __name__)




@user.route("/transport", methods=["GET"])
def transport():
    # 调用user_api功能方法返回需要的数据
    data = User_transport()
    return data


@user.route("/login", methods=["POST"])
def login():
    data = json.loads(request.get_data(as_text=True))
    print(data)
    username = data.get("username")
    password = data.get("password")
    print(username)
    print(password)
    result = Account_login(username, password)
    return jsonify(result)
#########Login################
# http://127.0.0.1:5000/user/login
# 示例
# {
#     "username":1,
#     "password":1234
# }
# 返回值 登录成功
# {
#     "code": 0,
#     "message": "登录成功",
#     "userid": 1
#     "Identity":0
# }
# 账户不存在
# {
#     "code": -1,
#     "message": "账户不存在",
#     "userid": ""
# }
#密码错误
# {
#     "code": -1,
#     "message": "密码错误",
#     "userid": 1
# }


@user.route('/reg', methods=['POST'])
def user_reg():
    # request.data ===json.loads===对象
    data = json.loads(request.get_data(as_text=True))
    # data.get("属性名")
    username = data.get("username")
    password = data.get("password")
    identity=data.get("Identity")
    # print(username)
    # print(password)

    # 形成对象形式 插入数据库
    user = {
        'aid': username,
        'pwd': password,
        'Identity': identity
    }
    result = Account_reg(user)
    return jsonify(result)
#########______reg注册_________##########
# http POST 方法
#http://127.0.0.1:5000/user/reg
# 请求实例:
# {
#     "username":3,
#     "password":12345,
#     "Identity":"0"
# }
# 注意检查空值,值的类型





@user.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(os.path.split(basepath)[0], 'static', f.filename.split('_')[0])
        if not os.path.exists(filepath):
            os.makedirs(filepath)
            Face_Operation.path_insert(f.filename.split('_')[0], filepath)
        all_files = os.listdir(filepath)
        num = 0
        for each_file in all_files:
            num = num + 1
        upload_path = os.path.join(filepath, str(num) + f.filename.split('.')[1])
        f.save(upload_path)
        return "succeed"
    return "fail"
