from flask import Blueprint

from api.user_api import *

user = Blueprint('user',__name__)




@user.route("/transport")
def transport():
    #调用user_api功能方法返回需要的数据
    data = User_transport()
    return data