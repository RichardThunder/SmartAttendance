# 业务逻辑
# 一系列业务功能

# 导入用户操作类
from operation.user_operation import User_Operation
from operation.account_operation import Account_Operation
from utils.data_process import *

import json


def User_transport():
    # 数据验证
    # 功能具体操作
    # 返回数据
    # 包装数据
    # return 数据

    user_p = User_Operation()
    result_data = user_p._all()

    result = Class_To_Data(result_data, user_p.__fields__)
    return result


def Account_reg(kwargs):
    account_operation = Account_Operation()
    re_data = Account_Operation._reg(kwargs)
    return re_data


def Account_login(username, password):  # use account table
    account_Operation = Account_Operation()
    re_data = account_Operation._login(username)

    # re_data = json.loads(re_data)

    if re_data:
        re_data = Class_To_Data(re_data, account_Operation.__field__, 1)
    result = {
        'code': 0,
        'message': "",
        'userid': "",
        'Identity': ""
    }
    print(re_data)
    # print("user.api,,line46")
    if re_data:
        if re_data.get('pwd') == str(password):
            result['code'] = 0
            result['message'] = "登录成功"
            result['userid'] = re_data.get('aid')
            result['Identity']=re_data.get('Identity')
        else:
            result['code'] = -1
            result['message'] = "密码错误"
            result['userid'] = re_data.get('aid')

    else:
        result['code'] = -1
        result['message'] = "账户不存在"
    return result

def select_api(username):
    #查询历史打卡记录
    user_p = Select_Operation()
    result_data = user_p._select(username)

    result = Class_To_Data(result_data, user_p.__fields__)
    return result

def Worker_contact(kwargs):
    account_operation = Add_Operation()
    re_data = Add_Operation._add(kwargs)
    return re_data


def select_id_api(userid):
    user_p = select_id_operation()
    result_data = user_p._select_id(userid)

    result = Class_To_Data(result_data, user_p.__fields__)
    return result

def select_name_api(username):
    user_p = select_name_operation()
    result_data = user_p._select_name(username)

    result = Class_To_Data(result_data, user_p.__fields__)
    return result

def select_gender_api(usergender):
    user_p = select_gender_operation()
    result_data = user_p._select_gender(usergender)

    result = Class_To_Data(result_data, user_p.__fields__)
    return result

def select_department_api(userdepartment):
    user_p = select_department_operation()
    result_data = user_p._select_department(userdepartment)

    result = Class_To_Data(result_data, user_p.__fields__)
    return result

def select_contact_api(usercontact):
    user_p = select_contact_operation()
    result_data = user_p._select_contact(usercontact)

    result = Class_To_Data(result_data, user_p.__fields__)
    return result