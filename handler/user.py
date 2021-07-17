from flask import Blueprint, request, Response, jsonify, json
from api.user_api import *

user = Blueprint('user', __name__)


@user.route("/login", methods=["POST"])
def login():
    data = json.loads(request.data)
    print(data)
    username = data.get("username")
    password = data.get("password")
    print(username)
    print(password)
    result = User_login(username, password)
    return jsonify(result)


@user.route("/transport", methods=["GET"])
def transport():
    # 调用user_api功能方法返回需要的数据
    data = User_transport()
    return data
