from models.attendance import Attendance

from db_config import db_init as db


# 用户模块操作类
class select_attendance_date_operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['recordNum', 'id', 'CkInTime', 'CkOutTime']

    def _select_attendance_date(self, start_date, end_date):
        user_data = db.session.query(Attendance).filter(Attendance.CkInTime.between(start_date , end_date )).all()
        return user_data
