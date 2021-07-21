# 导入数据模型类
from models.worker import Worker
from db_config import db_init as db


class Add_Operation():

    def _add(kwargs):
        # 数据模型类 创建对象
        me = Worker(**kwargs)
        # 使用数据库链接对接 在对应表添加一条数据记录
        db.session.add(me)
        db.session.commit()
        data = {'code': 0, 'message': 'success'}
        return data