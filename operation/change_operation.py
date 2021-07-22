# 导入数据模型类
from models.worker import Worker
from db_config import db_init as db


class Change_Operation():
    def __init__(self):
        self.__fields__ = ['id', 'name', 'gender', 'department', 'contact', 'company']


    def _change(worker, id):
        # 数据模型类 创建对象
        user_data = Worker.query.filter(Worker.id == id).first()
        db.session.delete(user_data)
        db.session.commit()
        me = Worker(**worker)
        # 使用数据库链接对接 在对应表添加一条数据记录
        db.session.add(me)
        db.session.commit()
        data = {'code': 0, 'message': 'success'}
        return data