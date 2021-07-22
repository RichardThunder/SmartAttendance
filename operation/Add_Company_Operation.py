from models.company import Company
from db_config import db_init as db


class Add_Company_Operation():

    def _add_company(kwargs):
        # 数据模型类 创建对象
        me = Company(**kwargs)
        # 使用数据库链接对接 在对应表添加一条数据记录
        db.session.add(me)
        db.session.commit()
        data = {'code': 0, 'message': 'success'}
        return data