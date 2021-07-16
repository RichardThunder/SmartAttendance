#业务逻辑
#一系列业务功能

#导入用户操作类
from Back.operation.user_operation import User_Operation

from Back.utils.data_process import *

def User_transport():
    #数据验证
    #功能具体操作
    #返回数据
    #包装数据
    #return 数据

    user_p = User_Operation()
    result_data = user_p._all()

    result =  Class_To_Data(result_data,user_p.__fields__)
    return result
  