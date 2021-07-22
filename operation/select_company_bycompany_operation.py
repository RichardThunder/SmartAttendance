
from models.company import Company

from db_config import db_init as db


# 用户模块操作类
class select_company_bycompany_operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['aid', 'companyname', 'department']

    def _select_company_bycompany(self, company):
        user_data = Company.query.filter(Company.companyname == company)
        return user_data