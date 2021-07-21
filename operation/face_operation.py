from models.face import Face
from db_config import db_init as db


class Face_Operation():
    # 映射account表
    def __init__(self):
        self.__field__ = ['fid', 'FacePath']

        # 操作1 获取所有用户

    def path_insert(iid, ipath):
        us = Face(fid=iid, FacePath=ipath)
        db.session.add(us)
        db.session.commit()
        print(iid, ipath)
