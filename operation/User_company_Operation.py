# 导入数据模型类
from models.company import Company


from db_config import db_init as db


# 用户模块操作类
class User_company_Operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['aid', 'companyname', 'department']

    # 操作1 获取所有用户
    def _all_company(self):
        user_data = Company.query.all()
        return user_data
