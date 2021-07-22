from models.company import Company

from db_config import db_init as db


# 用户模块操作类
class select_company_bydepartment_operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['aid', 'companyname', 'department']

    def _select_company_bydepartment(self, department):
        user_data = Company.query.filter(Company.department == department)
        return user_data

