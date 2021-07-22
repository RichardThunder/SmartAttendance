# 导入数据模型类
from models.worker import Worker


from db_config import db_init as db


# 用户模块操作类
class User_Operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['id', 'name', 'gender', 'department', 'contact', 'company']

    # 操作1 获取所有用户
    def _all(self):
        user_data = Worker.query.all()
        return user_data

