from flask import Blueprint,request,Response,jsonify


from Back.api.user_api import *

user = Blueprint('user',__name__)




@user.route("/transports")
def transport():
    #调用user_api功能方法返回需要的数据
    data = User_transport()
    return data