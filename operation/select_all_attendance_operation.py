# 导入数据模型类
from models.attendance import Attendance


from db_config import db_init as db


# 用户模块操作类
class select_all_attendance_operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['recordNum', 'id', 'CkInTime', 'CkOutTime']

    # 操作1 获取所有用户
    def _select_all_attendance(self):
        user_data = Attendance.query.all()
        return user_data