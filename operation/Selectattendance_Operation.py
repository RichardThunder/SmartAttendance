from models.attendance import Attendance

from db_config import db_init as db


# 用户模块操作类
class Selectattendance_Operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['id', 'CkInTime', 'CkOutTime']

    # 操作1 获取所有用户
    def _selectattendance(self, username):
        user_data = Attendance.query.filter(Attendance.id==username)
        return user_data