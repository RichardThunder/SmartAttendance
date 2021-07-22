from models.attendance import Attendance
from db_config import db_init as db


class Add_attendence():
    # 映射account表
    def __init__(self):
        self.__field__ = ['fid', 'FacePath']

        # 操作1 获取所有用户

    def path_insert(iid, iCkInTime, iCkOutTime):
        us = Attendance(id=iid, CkInTime=iCkInTime, CkOutTime=iCkOutTime)
        db.session.add(us)
        db.session.commit()
