from models.worker import Worker

from db_config import db_init as db


# 用户模块操作类
class select_company_operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['id', 'name', 'gender', 'department', 'contact', 'company']

    def _select_company(self, usercompany):
        user_data = Worker.query.filter(Worker.company == usercompany)
        print(user_data)
        return user_data