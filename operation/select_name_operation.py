from models.worker import Worker

from db_config import db_init as db


# 用户模块操作类
class select_name_operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['id', 'name', 'gender', 'department', 'contact', 'company']

    def _select_name(self, username):
        user_data = Worker.query.filter(Worker.name == username)
        return user_data