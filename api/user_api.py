# 业务逻辑
# 一系列业务功能

# 导入用户操作类
from operation.user_operation import User_Operation
from operation.account_operation import Account_Operation
from utils.data_process import *


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
    re_data = Account_Operation._login(kwargs)
    return re_data



def Account_login(username, password):  #use account table
    account_Operation =Account_Operation()
    re_data = account_Operation._login(username)

    if re_data:
        re_data = Class_To_Data(re_data, Account_Operation.__field__, 1)
    print(re_data)

    result = {
        'code': 0,
        'message': "",
        'userid': ""
    }

    if re_data:
        if re_data.get('password') == password:
            result['code'] = 0
            result['message'] = "登录成功"
            result['userid'] = re_data.get('id')
        else:
            result['code'] = -1
            result['message'] = "密码错误"
    else:
        result['code'] = -1
        result['message'] = "账户不存在"
    return result
