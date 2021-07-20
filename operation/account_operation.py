# 导入数据模型类
from models.worker import Worker
from models.account import Account
from db_config import db_init as db


class Account_Operation():
    # 映射account表
    def __init__(self):
        self.__field__ = ['aid', 'pwd', 'Identity']

        # 操作1 获取所有用户

    def _all(self):
        # 数据库模型类：调用查询方法
        account_data = Account.query.all()
        return account_data

    def _login(self, username):
        account_data = Account.query.filter_by(aid=username).first()
        print(account_data)
        return account_data

    def _reg(kwargs):
        # 数据模型类 创建对象
        me = Account(**kwargs)
        # 使用数据库链接对接 在对应表添加一条数据记录

        db.session.add(me)
        db.session.commit()
        data = {'code': 0, 'message': 'success'}

        return data
