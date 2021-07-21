from flask import Blueprint, request, Response, jsonify, json
from api.user_api import *
import os
from operation.face_operation import *
from pathlib import Path


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
# 密码错误
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
    identity = data.get("Identity")
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
# http://127.0.0.1:5000/user/reg
# 请求实例:
# {
#     "username":3,
#     "password":12345,
#     "Identity":"0"
# }
# 注意检查空值,值的类型


@user.route('/select', methods=['POST'])
def select():
    data = json.loads(request.get_data(as_text=True))
    # data.get("属性名")
    username = data.get("username")
    print(username)
    data = select_api(username)
    return data
######################
# {
#     "username": 1
# }
###################
# [
#     {
#         "CkInTime": "Fri, 16 Jul 2021 10:12:29 GMT",
#         "CkOutTime": "Sat, 17 Jul 2021 10:12:32 GMT",
#         "id": 1,
#         "recordNum": 1
#     }
# ]
#

@user.route('/add', methods=['POST'])
def add():
    data = json.loads(request.get_data(as_text=True))
    # data.get("属性名")
    id = data.get("id")
    name = data.get("name")
    gender = data.get("gender")
    department = data.get("department")
    contact = data.get("contact")
    print("id")
    print("name")
    print("gender")
    print("department")
    print("contact")
    worker = {
        'id': id,
        'name': name,
        'gender': gender,
        'department': department,
        'contact': contact

    }
    result = Worker_contact(worker)
    return jsonify(result)
########################
# {
#     "id":3,
#     "name":"gxx",
#     "gender":"fm",
#     "department":"ccp",
#     "contact":"gxx"
# }
#########################
# {
#     "code": 0,
#     "message": "success"
# }


@user.route('/select_id', methods=["GET"])
def select_id():
    data = json.loads(request.get_data(as_text=True))
    # data.get("属性名")
    userid = data.get("userid")
    print(userid)
    data = select_id_api(userid)
    return data
#######################
# {
#     "userid":1
# }
# #######################
# [
#     {
#         "contact": "2079265227",
#         "department": "A",
#         "gender": "M",
#         "id": 1,
#         "name": "richard"
#     }
# ]


@user.route('/select_name', methods=["GET"])
def select_name():
    data = json.loads(request.get_data(as_text=True))
    # data.get("属性名")
    username = data.get("username")
    print(username)
    data = select_name_api(username)
    return data
########################
# {
#     "username":"gxx"
# }
######################
# [
#     {
#         "contact": "gxx",
#         "department": "ccp",
#         "gender": "fm",
#         "id": 2,
#         "name": "gxx"
#     }
# ]


@user.route('/select_gender', methods=["GET"])
def select_gender():
    data = json.loads(request.get_data(as_text=True))
    # data.get("属性名")
    usergender = data.get("usergender")
    print(usergender)
    data = select_gender_api(usergender)
    return data
#####################
# {
#     "usergender":"M"
# }
####################
# [
#     {
#         "contact": "2079265227",
#         "department": "A",
#         "gender": "M",
#         "id": 1,
#         "name": "richard"
#     }
# ]

@user.route('/select_department', methods=["GET"])
def select_department():
    data = json.loads(request.get_data(as_text=True))
    # data.get("属性名")
    userdepartment = data.get("userdepartment")
    print(userdepartment)
    data = select_department_api(userdepartment)
    return data
#########################
# {
#     "userdepartment":"ccp"
# }
#########################
# [
#     {
#         "contact": "gxx",
#         "department": "ccp",
#         "gender": "fm",
#         "id": 2,
#         "name": "gxx"
#     }
# ]

@user.route('/select_contact', methods=["GET"])
def select_contact():
    data = json.loads(request.get_data(as_text=True))
    # data.get("属性名")
    usercontact = data.get("usercontact")
    print(usercontact)
    data = select_contact_api(usercontact)
    return data
#####################
# {
#     "usercontact":"gxx"
# }
#####################
# [
#     {
#         "contact": "gxx",
#         "department": "ccp",
#         "gender": "fm",
#         "id": 2,
#         "name": "gxx"
#     }
# ]


@user.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        #base_path = os.path.dirname(__file__)
        #filepath = os.path.join(os.path.split(base_path)[0], 'static', f.filename.split('_')[0])
        filepath = os.path.join('.\static', f.filename.split('_')[0])
        if not os.path.exists(filepath):
            os.makedirs(filepath)
            Face_Operation.path_insert(int(f.filename.split('_')[0]), filepath)
        all_files = os.listdir(filepath)
        num = 0
        for each_file in all_files:
            num = num + 1
        str_path = str(num) + '.' + f.filename.split('.')[1]
        upload_path = os.path.join(filepath, Path(str_path))
        f.save(upload_path)
        return jsonify("1")
    return jsonify("0")

####################




######################






@user.route('/change_worker', methods = ["POST"])
def change_worker():
    data = json.loads(request.get_data(as_text=True))
    # data.get("属性名")
    id = data.get("id")
    name = data.get("name")
    gender = data.get("gender")
    department = data.get("department")
    contact = data.get("contact")
    print("id")
    print("name")
    print("gender")
    print("department")
    print("contact")
    worker = {
        'id': id,
        'name': name,
        'gender': gender,
        'department': department,
        'contact': contact

    }
    result = change(worker, id)
    return result
#################
# {
#     "id":5,
#     "name":"gxx",
#     "gender":"m",
#     "department":"A",
#     "contact":"huxixi"
# }
#
# {
#     "code": 0,
#     "message": "success"
# }
#################